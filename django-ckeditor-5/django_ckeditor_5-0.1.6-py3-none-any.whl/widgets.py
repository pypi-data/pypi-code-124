from django import forms, get_version
from django.conf import settings
from django.forms.renderers import get_default_renderer
from django.urls import reverse
from django.utils.safestring import mark_safe

if get_version() >= "4.0":
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _
from django.forms.utils import ErrorList

DEFAULT_CONFIG = {
    "toolbar": ["heading", "|", "bold", "italic"],
}


class CKEditor5Widget(forms.Widget):
    template_name = "django_ckeditor_5/widget.html"

    def __init__(self, config_name="default", attrs=None):
        self._config_errors = []
        self.config = DEFAULT_CONFIG.copy()
        try:
            configs = getattr(settings, "CKEDITOR_5_CONFIGS")
            try:
                self.config.update(configs[config_name])
            except (TypeError, KeyError, ValueError) as ex:
                self._config_errors.append(self.format_error(ex))
        except AttributeError as ex:
            self._config_errors.append(self.format_error(ex))

        default_attrs = {"class": "django_ckeditor_5"}
        if attrs:
            default_attrs.update(attrs)
        super(CKEditor5Widget, self).__init__(default_attrs)

    def format_error(self, ex):
        return "{} {}".format(
            _("Check the correct settings.CKEDITOR_5_CONFIGS "), str(ex)
        )

    class Media:
        css = {
            "all": [
                "django_ckeditor_5/dist/styles.css",
            ]
        }
        custom_css = getattr(settings, "CKEDITOR_5_CUSTOM_CSS", None)
        if custom_css:
            css["all"].append(custom_css)
        js = ("django_ckeditor_5/dist/bundle.js",)
        configs = getattr(settings, "CKEDITOR_5_CONFIGS", None)
        for config in configs.keys():
            language = configs[config].get('language')
            if language:
                if isinstance(language, str) and language != "en":
                    js += (f"django_ckeditor_5/dist/translations/{language}.js",)
                elif isinstance(language, dict) and language.get('ui') and language["ui"] != "en":
                    js += (f"django_ckeditor_5/dist/translations/{language['ui']}.js",)

    def render(self, name, value, attrs=None, renderer=None):
        context = super(CKEditor5Widget, self).get_context(name, value, attrs)

        if renderer is None:
            renderer = get_default_renderer()

        context["config"] = self.config
        context["script_id"] = "{}{}".format(attrs["id"], "_script")
        context["upload_url"] = reverse("ck_editor_5_upload_file")
        if self._config_errors:
            context["errors"] = ErrorList(self._config_errors)

        return mark_safe(renderer.render(self.template_name, context))
