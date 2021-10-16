from .panel import WeightPanel
from .smooth_seams import SmoothSeamsOperator

from bpy.utils import (register_class, unregister_class)

def register_weight():
    register_class(WeightPanel)
    register_class(SmoothSeamsOperator)

def unregister_weight():
    unregister_class(SmoothSeamsOperator)
    unregister_class(WeightPanel)