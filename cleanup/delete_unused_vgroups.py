import bpy

class DeleteUnusedVGroupsOperator(bpy.types.Operator):
    bl_idname = "ffxv_cleanup.delete_unused_vgroups"
    bl_label = "Unused Vert. Groups"
    bl_description = "Deletes all vertex groups that are not weighted to any vertices in the active mesh"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        mesh = context.active_object

        groups = {i: False for i, k in enumerate(mesh.vertex_groups)}

        for vertex in mesh.data.vertices:
            for group in vertex.groups:
                if group.weight > 0:
                    groups[group.group] = True

        for index, used in sorted(groups.items(), reverse=True):
            if not used:
                mesh.vertex_groups.remove(mesh.vertex_groups[index])

        return {'FINISHED'}