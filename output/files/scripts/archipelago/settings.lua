local async = require('openmw.async')
local I = require('openmw.interfaces')
local storage = require('openmw.storage')
local ui = require('openmw.ui')

local serverGroup = 'SettingsServer'

I.Settings.registerPage {
    key = 'ArchipelagoPage',
    l10n = 'Archipelago',
    name = 'Archipelago',
    description = 'Archipelago Settings',
}

I.Settings.registerGroup {
    key = serverGroup,
    page = 'ArchipelagoPage',
    l10n = 'Archipelago',
    name = 'Server',
    description = 'Archipelago server connection options',
    permanentStorage = false,
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

local server = storage.playerSection(serverGroup)

local function handleConnect()
    local connect = server:get('connect')

    I.Settings.updateRendererArgument(serverGroup, 'address', { disabled = connect })
    I.Settings.updateRendererArgument(serverGroup, 'slot', { disabled = connect })
    I.Settings.updateRendererArgument(serverGroup, 'password', { disabled = connect })

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