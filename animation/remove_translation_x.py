from .remove_translation import remove_translation
import bpy

class RemoveTranslationXOperator(bpy.types.Operator):
    bl_idname = "ffxv_animation.remove_translation_x"
    bl_label = "X"
    bl_description = "Removes X axis translation from the active action to prevent the model running away when playing animations"

    @classmethod
    def poll(cls, context):
        object = context.active_object
        return object is not None and object.animation_data is not None and object.animation_data.action is not None

    def execute(self, context):
        remove_translation(context, 0)
        return {'FINISHED'}