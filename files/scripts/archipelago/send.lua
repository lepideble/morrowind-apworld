local I = require('openmw.interfaces')
local types = require('openmw.types')
local world = require('openmw.world')

local function startsWith(str, prefix)
    return str:sub(1, #prefix) == prefix
end

local function stripPrefix(str, prefix)
    if startsWith(str, prefix) then
        return str:sub(#prefix + 1)
    end

    return nil
end

local function checkInventory()
    for _, player in pairs(world.players) do
        for _, item in pairs(types.Actor.inventory(player):getAll()) do
            if startsWith(item.recordId, 'ap_') then
                local locationId = tonumber(stripPrefix(item.recordId, 'ap_'))

                if locationId ~= nil then
                    I.Archipelago.sendLocation(player, locationId)
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
