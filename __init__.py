bl_info = {
    "name": "FFXV Utilities",
    "description": "Provides various utility functions to make working with FFXV assets easier.",
    "author": "Kizari",
    "version": (0, 0, 3),
    "blender": (2, 80, 0),
    "location": "3D View > Tools",
    "wiki_url": "https://github.com/Kizari/ffxv_blender",
    "tracker_url": "https://github.com/Kizari/ffxv_blender",
    "category": "Development"
}

# Cleanup
from .cleanup.panel import CleanupPanel
from .cleanup.delete_empties import DeleteEmptiesOperator
from .cleanup.delete_unused_bones import DeleteUnusedBonesOperator
from .cleanup.delete_unused_vgroups import DeleteUnusedVGroupsOperator
from .cleanup.delete_zero_weights import DeleteZeroWeightsOperator

# Weight Tools
from .weight.panel import WeightPanel
from .weight.smooth_seams import SmoothSeamsOperator

# Animation Tools
from .animation.panel import AnimationPanel
from .animation.remove_translation_x import RemoveTranslationXOperator
from .animation.remove_translation_y import RemoveTranslationYOperator
from .animation.remove_translation_z import RemoveTranslationZOperator

classes = (
    CleanupPanel,
    DeleteEmptiesOperator,
    DeleteUnusedBonesOperator,
    DeleteUnusedVGroupsOperator,
    DeleteZeroWeightsOperator,
    WeightPanel,
    SmoothSeamsOperator,
    AnimationPanel,
    RemoveTranslationXOperator,
    RemoveTranslationYOperator,
    RemoveTranslationZOperator
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)    

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
