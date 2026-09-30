local async = require('openmw.async')
local I = require('openmw.interfaces')
local storage = require('openmw.storage')
local ui = require('openmw.ui')

local pageName = 'SettingsArchipelagoPage'
local groupName = 'SettingsArchipelagoServer'

I.Settings.registerPage {
    key = pageName,
    l10n = 'Archipelago',
    name = 'Archipelago',
    description = 'Archipelago Settings',
}

I.Settings.registerGroup {
    key = groupName,
    page = pageName,
    l10n = 'Archipelago',
    name = 'Server',
    description = 'Archipelago server connection options',
    permanentStorage = true,
    settings = {
        {
            key = 'address',
            default = '',
            renderer = 'textLine',
            name = 'Address',
            description = 'Server address and port. Example: archipelago.gg:xxxxx',
        },
        {
            key = 'slot',
            default = '',
            renderer = 'textLine',
            name = 'Slot',
            description = 'Name of the slot to connect',
        },
        {
            key = 'password',
            default = '',
            renderer = 'textLine',
            name = 'Password',
            description = 'Server password, leave empty for no password',
        },
        {
            key = 'connect',
            default = false,
            renderer = 'checkbox',
            argument = {
                trueLabel = 'Disconnect',
                falseLabel = 'Connect',
            },
            name = 'Connect',
        },
    },
}

local server = storage.playerSection(groupName)

server:set('connect', false)

local function handleConnect()
    local connect = server:get('connect')

    I.Settings.updateRendererArgument(groupName, 'address', { disabled = connect })
    I.Settings.updateRendererArgument(groupName, 'slot', { disabled = connect })
    I.Settings.updateRendererArgument(groupName, 'password', { disabled = connect })

    if I.Archipelago.isConnected() ~= connect then
        if connect then
            I.Archipelago.connect(server:get('address'), server:get('slot'), server:get('password'))
        else
            I.Archipelago.disconnect()
        end
    end
end

server:subscribe(async:callback(handleConnect))

return {}
