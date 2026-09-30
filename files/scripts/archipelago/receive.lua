local types = require('openmw.types')
local world = require('openmw.world')

local items = require('scripts/archipelago/data/items')

-- index of the last received item
-- this needs to be in the file to ensure it always stays in sync with items actualy sent to the player's inventory
local lastIndexTable = {}

local getPlayer = function (event)
    for _,player in ipairs(world.players) do
        if player.id == event.playerId then
            return player
        end
    end
end

local getName = function (item)
    local name = item.type.record(item).name

    if item.count > 1 then
        name = toString(count) .. ' ' .. name
    end

    return name
end

local receiveItems = function (event)
    local player = getPlayer(event)
    local lastIndex = lastIndexTable[player.id] or 0

    for i=lastIndex+1,event.receivedIndex do
        item = world.createObject(unpack(items[event.received[i].itemId]))
        item:moveInto(types.Actor.inventory(player))

        player:sendEvent('ShowMessage', { message = 'Received ' .. getName(item) })
    end

    lastIndexTable[player.id] = event.receivedIndex
end

return {
    engineHandlers = {
        onSave = function()
            return { lastIndex = lastIndexTable }
        end,
        onLoad = function(savedData)
            if savedData and savedData.lastIndex then
                lastIndexTable = savedData.lastIndex
            end
        end,
    },
    eventHandlers = {
        ArchipelagoReceive = receiveItems,
    },
}
