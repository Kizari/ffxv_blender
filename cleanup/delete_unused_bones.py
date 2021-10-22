import bpy

class DeleteUnusedBonesOperator(bpy.types.Operator):
    bl_idname = "ffxv_cleanup.delete_unused_bones"
    bl_label = "Unused Bones"
    bl_description = "Deletes all bones in the active armature that do not have any vertices weighted to them"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'ARMATURE'

    def execute(self, context):
        armature = context.active_object

        meshes = []
        for object in bpy.data.objects:
            if object.type == 'MESH' and object.parent == armature:
                meshes.append(object)

        bonesToKeep = []
        bonesToKeep.append("C_Hip")
        
        for mesh in meshes:
            groups = {i: False for i, k in enumerate(mesh.vertex_groups)}

            for vertex in mesh.data.vertices:
                for group in vertex.groups:
                    if group.weight > 0:
                        groups[group.group] = True

            for index, used in sorted(groups.items(), reverse=True):
                if used:
                    bonesToKeep.append(mesh.vertex_groups[index].name)

        current_mode = context.object.mode
        bpy.ops.object.mode_set(mode='EDIT')

        for bone in armature.data.edit_bones:
            if bone.name not in bonesToKeep:
                armature.data.edit_bones.remove(bone)
                
        bpy.ops.object.mode_set(mode=current_mode)

        return {'FINISHED'}