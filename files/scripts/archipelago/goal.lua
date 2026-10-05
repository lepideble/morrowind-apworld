local I = require('openmw.interfaces')

local onQuestUpdate = function(questId, stage)
    if questId == 'c3_destroydagoth' and stage == 50 then
        I.Archipelago.setGoalCompleted()
    end
end

return {
    engineHandlers = {
        onQuestUpdate = onQuestUpdate,
    },
}
