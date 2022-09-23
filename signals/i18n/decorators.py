"""
Decorators used to provide internationalization
"""
from django.contrib.admin import site, ModelAdmin, TabularInline

from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.admin import TranslationAdmin

from .hooks import model_translation_hooks


class translate():
    """Add localization to a model
    Usage:
        >>> from django.db import models
        >>> from signals.i18n.decorators import translate
        >>> 
        >>> @translate('title', admin=True)
        >>> class Person(models.Model):
        >>>     name = models.CharField(max_length=255)
        >>>     title = models.CharField(max_length=255)

        The ``title`` field will now support multiple languages as defined in
        ``LANGUAGES``.

        The optional attribute admin=True will automatically add the model to
        Django's built-in administration interface.
    """

    def __init__(self, fields, admin=False):
        self.fields = fields
        self.admin = admin
        self.cls = None

    def __call__(self, cls):
        def register_model():
            translator.register(cls, type(
                'f"{cls.__name__}TranslationOptions"', (TranslationOptions,), {'fields': self.fields}))
            if self.admin:
                site.register(
                    cls, type('f"{cls.__name__}TranslatedAdmin"', (TranslationAdmin,), {}))
        model_translation_hooks.append(register_model)
        return cls


class add_admin():
    """
    Add site to administration interface

    @todo - this should not be in this module
    """

    def __init__(self, inlines=None, admin_options=None):
        self.ao = admin_options
        self.inlines = inlines

    def __call__(self, cls):
        def register_model():
            opts = self.ao or {}
            opts["inlines"] = []
            if self.inlines is not None:
                for model in self.inlines:
                    opts["inlines"].append(type('f"{cls.__name__}_{model}InlineAdmin"',
                                                (TabularInline,), {'model': model}))
            site.register(
                cls, type('f"{cls.__name__}Admin"', (ModelAdmin,), opts))
        model_translation_hooks.append(register_model)
        return cls
