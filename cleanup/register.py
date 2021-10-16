from .panel import CleanupPanel
from .delete_empties import DeleteEmptiesOperator
from .delete_unused_bones import DeleteUnusedBonesOperator
from .delete_unused_vgroups import DeleteUnusedVGroupsOperator
from .delete_zero_weights import DeleteZeroWeightsOperator

from bpy.utils import (register_class, unregister_class)

def register_cleanup():
    register_class(CleanupPanel)
    register_class(DeleteEmptiesOperator)
    register_class(DeleteUnusedBonesOperator)
    register_class(DeleteUnusedVGroupsOperator)
    register_class(DeleteZeroWeightsOperator)

def unregister_cleanup():
    unregister_class(DeleteZeroWeightsOperator)
    unregister_class(DeleteUnusedVGroupsOperator)
    unregister_class(DeleteUnusedBonesOperator)
    unregister_class(DeleteEmptiesOperator)
    unregister_class(CleanupPanel)