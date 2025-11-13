from django.templatetags.static import static

from common.icons import IconPack
from plugin.base.icons.mixins import IconPackMixin
from plugin.plugin import InvenTreePlugin


PLUGIN_VERSION = "0.0.1"



class myfont(IconPackMixin, InvenTreePlugin):

    """myfont - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "my font"
    NAME = "myfont"
    SLUG = "my-font"
    DESCRIPTION = "A short d"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "Filip Hajduk"
    WEBSITE = "https://github.com/Mistrzu4/my-font"
    LICENSE = "MIT"

    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'

    # Render custom UI elements to the plugin settings page
    ADMIN_SOURCE = "Settings.js:renderPluginSettings"
    
    
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }
    
    
    
    
    
    

    # User interface elements (from UserInterfaceMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/ui/
    
    # Custom UI panels
    
    def icon_packs(self):
        """Return a list of custom icon packs."""
        return [
            IconPack(
                name='My Custom Icons',
                prefix='my',
                fonts={
                    'truetype': static('plugins/my-custom-plugin/icons/boxicons.ttf'),
                },
                icons={
                    'my-icon': {
                        'name': 'My Icon',
                        'category': '',
                        'tags': ['my', 'icon'],
                        'variants': {'default': 'bx-message-circle-heart'}
                    }
                },
            )
        ]
