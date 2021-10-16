import bpy

class DeleteZeroWeightsOperator(bpy.types.Operator):
    bl_idname = "ffxv_cleanup.delete_zero_weights"
    bl_label = "Zero Weights"
    bl_description = "Deletes all zero-weight groups from each vertex in the selected mesh"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        current_mode = context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        mesh = context.active_object
        for vertex in mesh.data.vertices:
            for group in vertex.groups:
                if group.weight == 0:
                    mesh.vertex_groups[group.group].remove([vertex.index])
                    
        bpy.ops.object.mode_set(mode=current_mode)
        return {'FINISHED'}