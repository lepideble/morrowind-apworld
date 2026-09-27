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
local connectionInfos = nil
local received = {}
local receivedIndex = 0

local playerId = nil
local playerInfos = nil

-- Validate that that the save and connection seed match
local function isValid()
    if playerId == nil or playerInfos == nil or connectionInfos == nil then
        return false
    end

    local connectionSeed, connectionSlot = table.unpack(connectionInfos)
    local playerSeed, playerSlot = table.unpack(playerInfos)

    return connectionSeed == playerSeed and connectionSlot == playerSlot
end

local function receive()
    if isValid() and receivedIndex > 0 then
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

        local connectionSeed, connectionSlot = table.unpack(connectionInfos or {})
        if connectionSeed ~= connection:get_seed() or connectionSlot ~= connection:get_slot() then
            connectionInfos = {connection:get_seed(), connection:get_slot()}
            received = {}
            receivedIndex = 0
        end

        core.sendGlobalEvent('ArchipelagoConnection', { playerId = playerId, connectionInfos = connectionInfos })

        ui.showMessage('Connected', { showInDialog = false })
    end

    local function on_slot_refused(reasons)
        if connection == nil then return end
        ui.showMessage('Connection refused: ' .. table.concat(reasons, ', '), { showInDialog = false })
        connection = nil
    end

    local function on_items_received(items)
        for _, item in pairs(items) do
            received[item.index + 1] = { itemId = item.item }
            receivedIndex = item.index + 1
        end

        receive()
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
    connectionSeed = nil
    connectionSlot = nil
    received = {}
    receivedIndex = 0
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
        ArchipelagoPlayer = function(event)
            playerId = event.playerId
            playerInfos = event.playerInfos

            if connectionInfos ~= nil then
                core.sendGlobalEvent('ArchipelagoConnection', { playerId = playerId, connectionInfos = connectionInfos })
            end

            receive()
        end,
        ArchipelagoSend = function(event)
            if event.playerId ~= playerId then return end

            if connection ~= nil and isValid() then
                connection:LocationChecks(event.locationsIds)
            end
        end,
        ArchipelagoGoal = function(event)
            if event.playerId ~= playerId then return end

            if connection ~= nil and isValid() then
                connection:StatusUpdate(APClient.ClientStatus.GOAL)
            end
        end,
    }
}
