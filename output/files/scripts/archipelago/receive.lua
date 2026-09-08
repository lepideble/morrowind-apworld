local types = require('openmw.types')
local world = require('openmw.world')

local items = require('scripts/archipelago/items')

local receive_item = function (event)
    item = world.createObject(unpack(items[event.id]))
    item:moveInto(types.Actor.inventory(event.player))
end

return {
    eventHandlers = {
        ArchipelagoReceive = receive_item,
    },
}