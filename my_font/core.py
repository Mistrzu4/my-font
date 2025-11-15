from django.templatetags.static import static
from django.http import JsonResponse
from django.urls import path
from common.icons import IconPack
from plugin.base.icons.mixins import IconPackMixin
from plugin.plugin import InvenTreePlugin

PLUGIN_VERSION = "0.0.1"

class myfont(IconPackMixin, InvenTreePlugin):
    TITLE = "my font"
    NAME = "my-font"
    SLUG = "my-font"
    VERSION = PLUGIN_VERSION

    AUTHOR = "Filip Hajduk"
    WEBSITE = "https://github.com/Mistrzu4/my-font"
    LICENSE = "MIT"

    SETTINGS = {
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }

    # 🔹 Ta metoda jest wymagana przez IconPackMixin
    def icon_packs(self):
        font_url = static('plugins/my-font/icons/boxicons.ttf')
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
                }
            )
        ]

    # 🔹 Debugowy endpoint
    def register_urls(self):
        def debug_font_url(request):
            font_url = static('plugins/my-font/icons/boxicons.ttf')
            try:
                with open("/tmp/myfont_url.txt", "w") as f:
                    f.write(font_url)
            except Exception as e:
                with open("/tmp/myfont_url.txt", "w") as f:
                    f.write(f"ERROR: {e}")
            return JsonResponse({"font_url": font_url})

        return [path("debug-font/", debug_font_url)]
