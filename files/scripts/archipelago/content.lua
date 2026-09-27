local content = require('openmw.content')

local locations = require('scripts/archipelago/data/locations')

function onContentFilesLoaded()
    for locationId, locationItem in pairs(locations) do
         content.miscs.records['ap_' .. locationId].name = locationItem
    end
end

return {
    engineHandlers = {
        onContentFilesLoaded = onContentFilesLoaded,
    },
}
