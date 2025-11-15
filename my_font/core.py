def register_urls(self):
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

    return [path("debug-font/", debug_font_url)]
