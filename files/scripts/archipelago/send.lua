local world = require('openmw.world')
local types = require('openmw.types')   
local inventory = types.Actor.inventory(player)

local startsWith = function(str, prefix)
    return str:sub(1, #prefix) == prefix
end

local stripPrefix = function(str, prefix)
    if startsWith(str, prefix) then
        return str:sub(#prefix + 1)
    end

    return nil
end

local checkInventory = function ()
    for _, player in ipairs(world.players) do
        for item in types.Actor.inventory(player):getAll() do
            if startsWith(item.recordId, 'ap_') then
                local locationId = toNumber(stripPrefix(item.recordId, 'ap_'))

                if locationId ~= nil then
                    player:sendEvent('ArchipelagoSend', { locationId = locationId })
                    item:remove(1)
                end
            end
        end
    end
end

local time = 0

return {
    engineHandlers = {
        onUpdate = function ()
            if time == 60 then
                checkInventory()
                time = 0
            else
                time = time + 1
            end
        end,
    },
}
