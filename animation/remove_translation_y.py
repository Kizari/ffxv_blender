from .remove_translation import remove_translation
import bpy

class RemoveTranslationYOperator(bpy.types.Operator):
    bl_idname = "ffxv_animation.remove_translation_y"
    bl_label = "Y"
    bl_description = "Removes Y axis translation from the active action to prevent the model running away when playing animations"

    @classmethod
    def poll(cls, context):
        object = context.active_object
        return object is not None and object.animation_data is not None and object.animation_data.action is not None

    def execute(self, context):
        remove_translation(context, 1)
        return {'FINISHED'}