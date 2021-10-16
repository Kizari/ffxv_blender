from .remove_translation import remove_translation
import bpy

class RemoveTranslationZOperator(bpy.types.Operator):
    bl_idname = "ffxv_animation.remove_translation_z"
    bl_label = "Z"
    bl_description = "Removes Z axis translation from the active action to prevent the model running away when playing animations"

    @classmethod
    def poll(cls, context):
        object = context.active_object
        return object is not None and object.animation_data is not None and object.animation_data.action is not None

    def execute(self, context):
        remove_translation(context, 2)
        return {'FINISHED'}