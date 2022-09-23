
__author__ = "Luc Belliveau <luc.belliveau@phac.aspc.gc.ca>"
model_translation_hooks = []


def process_translate_decorators():
    """
    Process the registered hooks.

    This should occur after the models are loaded by Django, for example from
    the AppConfig's ready function.
    """
    for hook in model_translation_hooks:
        hook()

    model_translation_hooks.clear()
