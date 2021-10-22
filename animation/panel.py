import bpy
from bpy.types import (Panel)
from .remove_translation_x import RemoveTranslationXOperator
from .remove_translation_y import RemoveTranslationYOperator
from .remove_translation_z import RemoveTranslationZOperator

if bpy.app.version < (2, 80, 0):
    region = "TOOLS"
else:
    region = "UI"

class AnimationPanel(Panel):
    bl_idname = "ffxv_animation"
    bl_label = "Animation"
    bl_category = "FFXV"
    bl_space_type = 'VIEW_3D'
    bl_region_type = region

    def draw(self, context):
        layout = self.layout
        layout.label(text="Remove translation:")
        row = layout.row(align=True)
        row.operator(RemoveTranslationXOperator.bl_idname)
        sub = row.row(align=True)
        sub.operator(RemoveTranslationYOperator.bl_idname)
        sub.operator(RemoveTranslationZOperator.bl_idname)