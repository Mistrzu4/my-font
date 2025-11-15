from django.templatetags.static import static
from django.http import JsonResponse
from django.urls import path
from common.icons import IconPack
from plugin.base.icons.mixins import IconPackMixin
from plugin.plugin import InvenTreePlugin

PLUGIN_VERSION = "0.0.1"

class myfont(IconPackMixin, InvenTreePlugin):
    TITLE = "my font"
    NAME = "myfont"
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

    def register_urls(self):
        def debug_font_url(request):
            font_url = static('plugins/myfont/icons/boxicons.ttf')
            return JsonResponse({"font_url": font_url})

        return [
            path("debug-font/", debug_font_url),
        ]

    def icon_packs(self):
        return [
            IconPack(
                name='My Custom Icons',
                prefix='my',
                fonts={
                    'truetype': static('plugins/myfont/icons/boxicons.ttf'),
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
