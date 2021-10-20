from .panel import AnimationPanel
from .remove_translation_x import RemoveTranslationXOperator
from .remove_translation_y import RemoveTranslationYOperator
from .remove_translation_z import RemoveTranslationZOperator

from bpy.utils import (register_class, unregister_class)

def register_animation():
    register_class(AnimationPanel)
    register_class(RemoveTranslationXOperator)
    register_class(RemoveTranslationYOperator)
    register_class(RemoveTranslationZOperator)

def unregister_animation():
    unregister_class(RemoveTranslationZOperator)
    unregister_class(RemoveTranslationYOperator)
    unregister_class(RemoveTranslationXOperator)
    unregister_class(AnimationPanel)