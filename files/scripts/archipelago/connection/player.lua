-- Compagnon script to connection.lua to inform it of the current player's state
local self = require('openmw.self')
local types = require('openmw.types')

local playerSeed = nil
local playerSlot = nil
local foundLocations = {}
local hasReachGoal = false

local sendLocation = function(locationId)
    table.insert(foundLocations, locationId)
    types.Player.sendMenuEvent(self, 'ArchipelagoSend', { locationId = locationId })
end

local setGoalCompleted = function()
    isGoalCompleted = true
    types.Player.sendMenuEvent(self, 'ArchipelagoGoal')
end

return {
    interfaceName = 'Archipelago',
    interface = {
        sendLocation = sendLocation,
        setGoalCompleted = setGoalCompleted,
    },
    engineHandlers = {
        onInit = function ()
            types.Player.sendMenuEvent(self, 'ArchipelagoStart', { playerId = self.object.id })
        end,
        onLoad = function(savedData)
            if savedData and savedData.playerSeed then
                playerSeed = savedData.playerSeed
            end
            if savedData and savedData.playerSlot then
                playerSlot = savedData.playerSlot
            end
            if savedData and savedData.foundLocations then
                foundLocations = savedData.foundLocations
            end
            if savedData and savedData.hasReachGoal then
                hasReachGoal = savedData.hasReachGoal
            end
            types.Player.sendMenuEvent(self, 'ArchipelagoStart', { playerId = self.object.id, playerSeed = playerSeed, playerSlot = playerSlot })
        end,
        onSave = function ()
            return {
                playerSeed = playerSeed,
                playerSlot = playerSlot,
                foundLocations = foundLocations,
                hasReachGoal = hasReachGoal,
            }
        end,
    },
    eventHandler = {
        ArchipelagoSend = function (event)
            sendLocation(event.locationId)
        end,
    },
}
