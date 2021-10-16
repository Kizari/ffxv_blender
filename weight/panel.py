from bpy.types import (Panel)
from .smooth_seams import SmoothSeamsOperator

class WeightPanel(Panel):
    bl_idname = "ffxv_weight"
    bl_label = "Weight Tools"
    bl_category = "FFXV"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout
        layout.operator(SmoothSeamsOperator.bl_idname)