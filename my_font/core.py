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

    def register_urls(self):
        """Rejestruje tymczasowy URL do debugowania fontu."""

        from django.urls import path
        from django.templatetags.static import static
        from django.http import JsonResponse

        def debug_font_url(request):
            font_url = static('plugins/myfont/icons/boxicons.ttf')
            # DEBUG: zapisz do pliku w kontenerze
            try:
                with open("/tmp/myfont_url.txt", "w") as f:
                    f.write(font_url)
            except Exception as e:
                with open("/tmp/myfont_url.txt", "w") as f:
                    f.write(f"ERROR: {e}")
            return JsonResponse({"font_url": font_url})

        # Zwracamy listę URL-i **wewnątrz metody**
        return [path("debug-font/", debug_font_url)]
