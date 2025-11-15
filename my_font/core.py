from django.templatetags.static import static
from common.icons import IconPack
from plugin.base.icons.mixins import IconPackMixin
from plugin.plugin import InvenTreePlugin
from django.http import JsonResponse
from django.urls import path

PLUGIN_VERSION = "0.0.1"

class myfont(IconPackMixin, InvenTreePlugin):
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

        return [
            IconPack(
                name='My Custom Icons',
                prefix='my',
                fonts={'truetype': font_url},
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

    def register_urls(self):
        """Tymczasowy endpoint debugowy."""
        def debug_font_url(request):
            font_url = static('plugins/myfont/icons/boxicons.ttf')
            return JsonResponse({"font_url": font_url})

        return [
            path("debug-font/", debug
