bl_info = {
    "name": "FFXV Utilities",
    "blender": (2, 79, 0),
    "category": "Object"
}

from ffxv_blender.cleanup.register import (register_cleanup, unregister_cleanup)
from ffxv_blender.animation.register import (register_animation, unregister_animation)
from ffxv_blender.weight.register import (register_weight, unregister_weight)

def register():
    register_cleanup()
    register_animation()
    register_weight()

def unregister():
    unregister_weight()
    unregister_animation()
    unregister_cleanup()