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

    AUTHOR = "Filip Hajduk"
    WEBSITE = "https://github.com/Mistrzu4/my-font"
    LICENSE = "MIT"

    ADMIN_SOURCE = "Settings.js:renderPluginSettings"
    
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }

    def debug_font_url(request):
        font_url = static('plugins/myfont/icons/boxicons.ttf')
        return JsonResponse({"font_url": font_url})

    return [
        path("debug-font/", debug_font_url),
    ]


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
                        'variants': {
                            'default': 'bx-message-circle-heart'  # tylko nazwa ikony z fontu
                        }
                    }
                },
            )
        ]
