local world = require("openmw.world")
local  player = world.players[1]
local types = require("openmw.types")   
local inventory = types.Actor.inventory(player)

Remove = function(min, max)
     for i = min, min + 10 do
       checkinvitem = inventory:find("ap_" .. tostring(i))
       print("ap_" .. i)
          if checkinvitem ~= nil then
            checkinvitem:remove(1)
            player:sendEvent("SendLocation",i)
            
          end
        end
       end


return{
  eventHandlers = {
    Remove = Remove
  }

}
