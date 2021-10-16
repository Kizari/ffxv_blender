from bpy.types import (Panel)
from .delete_unused_bones import DeleteUnusedBonesOperator
from .delete_unused_vgroups import DeleteUnusedVGroupsOperator
from .delete_empties import DeleteEmptiesOperator
from .delete_zero_weights import DeleteZeroWeightsOperator

class CleanupPanel(Panel):
    bl_idname = "ffxv_cleanup"
    bl_label = "Cleanup"
    bl_category = "FFXV"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout
        layout.operator(DeleteEmptiesOperator.bl_idname)
        layout.operator(DeleteUnusedBonesOperator.bl_idname)
        layout.operator(DeleteUnusedVGroupsOperator.bl_idname)
        layout.operator(DeleteZeroWeightsOperator.bl_idname)