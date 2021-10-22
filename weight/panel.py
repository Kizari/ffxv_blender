import bpy
from bpy.types import (Panel)
from .smooth_seams import SmoothSeamsOperator

if bpy.app.version < (2, 80, 0):
    region = "TOOLS"
else:
    region = "UI"

class WeightPanel(Panel):
    bl_idname = "ffxv_weight"
    bl_label = "Weight Tools"
    bl_category = "FFXV"
    bl_space_type = 'VIEW_3D'
    bl_region_type = region

    def draw(self, context):
        layout = self.layout
        layout.operator(SmoothSeamsOperator.bl_idname)