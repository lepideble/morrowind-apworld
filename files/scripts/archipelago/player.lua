local self = require('openmw.self')
local UI = require("openmw.ui")
local util = require('openmw.util')
local core = require('openmw.core')
local async = require('openmw.async')

---@type APClient
local APClient
if requireAp then
    APClient = requireAp()
else
    APClient = require('archipelago').APClient
end

local gameName = 'The Elder Scrolls III: Morrowind'
local itemsHandling = 7 -- binary b111 - we want everything
local messageFormat = APClient.RenderFormat.TEXT
local min = 1
local time = 0


---@type APClient | nil
local connection = nil

--This helps save the received list across instances
Received = Received or {}
local isGoalCompleted = false



Blue = util.color.rgb(0,0,255)

local function showMsg(msg)
    UI.showMessage(tostring(msg), { showInDialog = false })
end

local Address = nil
local Slot = nil
local Pass = nil
local stage = 0


local version = { major = 0, minor = 6, build = 6 }
EnableItems = {}

local errorcount = 0



function add_locations(locations, pos)
  table.insert(locations,pos,value)
end

locations = {}

local function connect(server, slot, password)
    if connection ~= nil then
        connection = nil
        -- collectgarbage("collect")
    end

    local function on_socket_connected()
        print("Connected")
        UI.printToConsole("Connected", Blue)
        
    end

    local function on_socket_error(msg)
        print("Socket error: " .. msg)
        if errorcount == 3 then
          connection = nil
          end
        errorcount = errorcount + 1
    end

    local function on_socket_disconnected()
        print("Socket disconnected")
        UI.printToConsole("Socked disconnected", Blue)
    end

    local function on_room_info()
        if connection == nil then return end
        print("Room info")
        UI.printToConsole("Room info", Blue)
        Version = {major=0, minor=6, build=6}
        connection:ConnectSlot(slot, password, itemsHandling, { "Lua-APClientPP" }, Version)
    end

    local function on_slot_connected(slot_data)
        if connection == nil then return end
        showMsg("Slot connected")
        print(slot_data)
        print("missing locations: " .. table.concat(connection.missing_locations, ", "))
        print("checked locations: " .. table.concat(connection.checked_locations, ", "))
        connection:ConnectUpdate(nil, { "Lua-APClientPP", "DeathLink" })
        connection:LocationChecks({})
        print("Players:")
        local players = connection:get_players()
        for _, player in ipairs(players) do
            print("  " .. tostring(player.slot) .. ": " .. player.name ..
                " playing " .. connection:get_player_game(player.slot))
            UI.printToConsole("  " .. tostring(player.slot) .. ": " .. player.name ..
                " playing " .. connection:get_player_game(player.slot), Blue)
        end
    end

    local function on_slot_refused(reasons)
        showMsg("Slot refused: " .. table.concat(reasons, ", "))
        connection = nil
    end

    local function on_items_received(items)
        for _, item in ipairs(items) do

            local found = false 
            for _, v in pairs(Received) do
              if v == item.item then
                found = true
              end
            end
            if found == false then
              showMsg("Items received :" .. tostring(item.item))
              print(tostring(item.item))
              core.sendGlobalEvent('ArchipelagoReceive', { id = item.item, player = self.object })
              table.insert(Received,item.item)
            end
        end
    end

    local function on_location_info(items)
        print("Locations scouted:")
        for _, item in ipairs(items) do
            print(item.item)
        end
    end

    local function on_location_checked(locations)
        if connection == nil then return end
        print("Locations checked:" .. table.concat(locations, ", "))
        print("Checked locations: " .. table.concat(connection.checked_locations, ", "))
    end

    local function on_data_package_changed(data_package)
        print("Data package changed:")
        print(data_package)
    end

    local function on_print(msg)
        print(msg)
        
    end

    local function on_print_json(msg, extra)
        if connection == nil then return end
        print(connection:render_json(msg, messageFormat))
        UI.printToConsole(connection:render_json(msg, messageFormat), Blue)
        
        for key, value in pairs(extra) do
            -- print("  " .. key .. ": " .. tostring(value))
            -- UI.printToConsole("  " .. key .. ": " .. tostring(value), Blue)
        end
    end

    local function on_bounced(bounce)
        print("Bounced:")
        print(bounce)
    end

    local function on_retrieved(map, keys, extra)
        print("Retrieved:")
        -- since lua tables won't contain nil values, we can use keys array
        -- relevant string.char(97) and string.byte("example")
        for _, key in ipairs(keys) do
            print("  " .. key .. ": " .. tostring(map[key]))
        end
        -- extra will include extra fields from Get
        print("Extra:")
        for key, value in pairs(extra) do
            print("  " .. key .. ": " .. tostring(value))
        end
        -- both keys and extra are optional
    end

    local function on_set_reply(message)
        print("Set Reply:")
        for key, value in pairs(message) do
            print("  " .. key .. ": " .. tostring(value))
            if key == "value" and type(value) == "table" then
                for subkey, subvalue in pairs(value) do
                    print("    " .. subkey .. ": " .. tostring(subvalue))
                end
            end
        end
    end

    local uuid = ""
    connection = APClient(uuid, gameName, server, version);

    connection:set_socket_connected_handler(on_socket_connected)
    connection:set_socket_error_handler(on_socket_error)
    connection:set_socket_disconnected_handler(on_socket_disconnected)
    connection:set_room_info_handler(on_room_info)
    connection:set_slot_connected_handler(on_slot_connected)
    connection:set_slot_refused_handler(on_slot_refused)
    connection:set_items_received_handler(on_items_received)
    connection:set_location_info_handler(on_location_info)
    connection:set_location_checked_handler(on_location_checked)
    connection:set_data_package_changed_handler(on_data_package_changed)
    connection:set_print_handler(on_print)
    connection:set_print_json_handler(on_print_json)
    connection:set_bounced_handler(on_bounced)
    connection:set_retrieved_handler(on_retrieved)
    connection:set_set_reply_handler(on_set_reply)
end

local function disconnect()
    if connection == nil then
        return false
    end
    if connection:get_state() == APClient.State.DISCONNECTED then
        connection = nil
        -- collectgarbage("collect")
        return false
    end
    connection = nil
    -- collectgarbage("collect")
    return true
end

local function isConnected()
    if connection == nil then
        return false
    end
    if connection:get_state() == APClient.State.DISCONNECTED then
        return false
    end
    return true
end

SendLocation = function(location)
  --This is an event received from Global.lua
  connection:LocationChecks({location})
end

local setGoalCompleted = function()
    isGoalCompleted = true

    if isConnected() then
        connection:StatusUpdate(APClient.ClientStatus.GOAL)
    end
end

-- TODO: retry sending goal status on connection if not sent?
-- TODO: add a seed check to prevent accidently release by loading the wrong save?

local onSave = function()
    return {
        received = Received,
        completed = isGoalCompleted,
    }
end

local onLoad = function(data)
    if data and data.received ~= nil then
        Received = data.received
    end
    if data and data.completed ~= nil then
        isGoalCompleted = data.completed
    end
end

return {
    interfaceName = "Archipelago",
    interface = {
        connect = connect,
        disconnect = disconnect,
        isConnected = isConnected,
        setGoalCompleted = setGoalCompleted
    },
    engineHandlers = {
        onSave = onSave,
        onLoad = onLoad,
        onUpdate = function()
            if connection ~= nil then
                connection:poll()
                --Every 120 frames it sends the event Remove to Global.lua.
                --To change the amount of frames simply change time == 60.
                --Min starts at 0 incrementing by 10 every 120 frames right now.
                --Change the min <= 100 to be 10 less than the highest id ap_<item> id that was added to morrowind.
                --For example, if you had ap_115 you would have to change min <= 100 to min <= 105.
                if time == 120 then 
                    time = 0 
                    core.sendGlobalEvent("Remove", min)
                    if min <= 100 then 
                        min = min + 10
                    else 
                        min = 1
                    end               
                else 
                    time = time + 1
                end
            end
        end
    },
    eventHandlers = {
        SendLocation = SendLocation
    },
}
