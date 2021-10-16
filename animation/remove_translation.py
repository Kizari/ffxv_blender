import bpy

def remove_translation(context, axis):
    animation = context.active_object.animation_data.action
    fcurve = animation.fcurves.find("location", axis)

    for keyframe in fcurve.keyframe_points:
        keyframe.co[1] = 0