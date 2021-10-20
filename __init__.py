bl_info = {
    "name": "FFXV Utilities",
    "blender": (2, 8, 0),
    "category": "Object"
}

from .cleanup.register import (register_cleanup, unregister_cleanup)
from .animation.register import (register_animation, unregister_animation)
from .weight.register import (register_weight, unregister_weight)

def register():
    register_cleanup()
    register_animation()
    register_weight()

def unregister():
    unregister_weight()
    unregister_animation()
    unregister_cleanup()