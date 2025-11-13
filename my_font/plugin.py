"""Minimal plugin to add a custom TrueType font."""

from django.templatetags.static import static

from common.icons import IconPack
from plugin.base.icons.mixins import IconPackMixin
from plugin.plugin import InvenTreePlugin


class MyFontPlugin(IconPackMixin, InvenTreePlugin):
    """Plugin to add the 'boxicons' TrueType font."""

    NAME = 'MyFontPlugin'
    SLUG = 'my-font'
    TITLE = 'My Font Plugin'

    VERSION = '0.0.1'

    def icon_packs(self):
        """Return a list of custom icon packs."""
        return [
            IconPack(
                name='Boxicons',
                prefix='box',
                fonts={
                    'truetype': static('my-font/webfonts/boxicons.ttf'),
                },
                icons={
                    'box-icon': {
                        'name': 'Box Icon',
                        'category': '',
                        'tags': ['box', 'icon'],
                        'variants': {'default': 'f000'},
                    }
                },
            )
        ]
