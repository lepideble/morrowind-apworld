local self = require('openmw.self')
local types = require('openmw.types')

local isGoalCompleted = false

local function sendGoalCompleted()
    if isGoalCompleted then
        types.Player.sendMenuEvent(self, 'ArchipelagoGoal', { playerId = self.object.id })
    end
end

return {
    interfaceName = 'Archipelago',
    interface = {
        setGoalCompleted = function()
            isGoalCompleted = true
            sendGoalCompleted()
        end,
    },
    engineHandlers = {
        onLoad = function(savedData)
            if savedData and savedData.isGoalCompleted then
                isGoalCompleted = savedData.isGoalCompleted
            end
        end,
        onSave = function ()
            return { isGoalCompleted = isGoalCompleted }
        end,
    },
    eventHandlers = {
        ArchipelagoConnection = function (event)
            sendGoalCompleted()
        end,
    },
}
