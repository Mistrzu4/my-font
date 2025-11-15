from django.templatetags.static import static

from common.icons import IconPack
from plugin.base.icons.mixins import IconPackMixin
from plugin.plugin import InvenTreePlugin
from django.http import JsonResponse


PLUGIN_VERSION = "0.0.1"


def debug_icon_packs(request):
    packs = self.icon_packs()
    urls = [pack.fonts['truetype'] for pack in packs]
    return JsonResponse({"fonts": urls})

def urls(self):
    return [path("debug-icon-packs/", debug_icon_packs)]

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
    
    def icon_packs(self):

        font_url = static('plugins/myfont/icons/boxicons.ttf')

        # DEBUG: zapisz URL do pliku w kontenerze
        try:
            with open("/tmp/myfont_url.txt", "w") as f:
                f.write(font_url)
        except Exception as e:
            import traceback
            with open("/tmp/myfont_url.txt", "w") as f:
                f.write(f"ERROR: {e}\n{traceback.format_exc()}")


                
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
