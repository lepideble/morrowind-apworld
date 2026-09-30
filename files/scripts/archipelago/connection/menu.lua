local core = require('openmw.core')
local ui = require('openmw.ui')
local util = require('openmw.util')

---@type APClient
local APClient
if requireAp then
    APClient = requireAp()
else
    APClient = require('archipelago').APClient
end

-- Connection options
local game = 'The Elder Scrolls III: Morrowind'
local items_handling = 7

---@type APClient | nil
local connection = nil
local connectionSeed = nil
local connectionSlot = nil
local received = {}
local receivedIndex = 0

local playerId = nil
local playerSeed = nil
local playerSlot = nil

local function playerValid()
    if playerId == nil then
        return false
    end

    if playerSeed ~= nil and connectionSeed ~= null and playerSeed ~= connectionSeed then
        return false
    end

    if playerSlot ~= nil and connectionSlot ~= null and playerSlot ~= connectionSlot then
        return false
    end

    return true
end

local function addItems()
    if playerValid() and receivedIndex > 0 then
        core.sendGlobalEvent('ArchipelagoReceive', { playerId = playerId, received = received, receivedIndex = receivedIndex })
    end
end

local function connect(host, slot, password)
    if connection ~= nil then
        connection = nil
    end

    local function on_socket_disconnected()
        if connection == nil then return end
        ui.showMessage('Disconnected', { showInDialog = false })
    end

    local function on_room_info()
        if connection == nil then return end
        connection:ConnectSlot(slot, password, items_handling)
    end

    local function on_slot_connected(slot_data)
        if connection == nil then return end

        if connectionSeed ~= connection:get_seed() or connectionSlot ~= connection:get_slot() then
            connectionSeed = connection:get_seed()
            connectionSlot = connection:get_slot()
            received = {}
            receivedIndex = 0
        end

        ui.showMessage('Connected', { showInDialog = false })
    end

    local function on_slot_refused(reasons)
        if connection == nil then return end
        ui.showMessage('Connection refused: ' .. table.concat(reasons, ', '), { showInDialog = false })
        connection = nil
    end

    local function on_items_received(items)
        for _, item in ipairs(items) do
            received[item.index + 1] = { itemId = item.item }
            receivedIndex = item.index + 1
        end

        addItems()
    end

    local function on_print_json(msg, extra)
        if connection == nil then return end
        ui.printToConsole(connection:render_json(msg, APClient.RenderFormat.TEXT), util.color.rgb(0,0,255))
    end

    connection = APClient('', game, host);

    connection:set_socket_disconnected_handler(on_socket_disconnected)
    connection:set_room_info_handler(on_room_info)
    connection:set_slot_connected_handler(on_slot_connected)
    connection:set_slot_refused_handler(on_slot_refused)
    connection:set_items_received_handler(on_items_received)
    connection:set_print_json_handler(on_print_json)
end

local function disconnect()
    connection = nil
end

local function isConnected()
    if connection == nil then
        return false
    end

    return connection:get_state() ~= APClient.State.DISCONNECTED
end

return {
    interfaceName = 'Archipelago',
    interface = {
        connect = connect,
        disconnect = disconnect,
        isConnected = isConnected,
    },
    engineHandlers = {
        onFrame = function()
            if connection ~= nil then
                connection:poll()
            end
        end,
    },
    eventHandlers = {
        ArchipelagoStart = function(event)
            playerId = event.playerId
            playerSeed = event.playerSeed
            playerSlot = event.playerSlot

            addItems()
        end,
        ArchipelagoSend = function(event)
            if connection ~= nil then
                connection:LocationChecks({ event.locationId })
            end
        end,
    }
}
