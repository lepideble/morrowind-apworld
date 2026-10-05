local types = require('openmw.types')
local world = require('openmw.world')

local players = {}
local foundLocations = {}

local function getPlayerById(id)
    for _, player in pairs(world.players) do
        if player.id == id then
            return player
        end
    end

    return nil
end

local function sendPlayerInfos(player)
    types.Player.sendMenuEvent(player, 'ArchipelagoPlayer', { playerId = player.id, playerInfos = players[player.id] })
end

local function sendPlayerFoundLocation(player)
    if foundLocations[player.id] then
        types.Player.sendMenuEvent(player, 'ArchipelagoSend', { playerId = player.id, locationsIds = foundLocations[player.id] })
    end
end

return {
    interfaceName = 'Archipelago',
    interface = {
        sendLocation = function (player, locationId)
            foundLocations[player.id] = foundLocations[player.id] or {}

            table.insert(foundLocations[player.id], locationId)

            sendPlayerFoundLocation(player)
        end,
    },
    engineHandlers = {
        onSave = function ()
            return { players = players, foundLocations = foundLocations }
        end,
        onLoad = function (savedData)
            if savedData and savedData.players then
                players = savedData.players
            end
            if savedData and savedData.foundLocations then
                foundLocations = savedData.foundLocations
            end
        end,
        onPlayerAdded = function (player)
            sendPlayerInfos(player)
        end,
    },
    eventHandlers = {
        ArchipelagoConnection = function (event)
            local player = getPlayerById(event.playerId)

            if player == nil then return end

            if players[player.id] == nil then
                players[player.id] = event.connectionInfos

                sendPlayerInfos(player)
            end

            sendPlayerFoundLocation(player)

            player:sendEvent('ArchipelagoConnection', { connectionInfos = connectionInfos })
        end,
    },
}
