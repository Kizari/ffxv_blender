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
            for group in mesh.vertex_groups:
                if group.name in bonesToKeep:
                    continue
                for vertex in mesh.data.vertices:
                    done = False
                    for subgroup in vertex.groups:
                        if subgroup.group == group.index and subgroup.weight > 0:
                            bonesToKeep.append(group.name)
                            done = True
                            break
                    if done:
                        break

        current_mode = context.object.mode
        bpy.ops.object.mode_set(mode='EDIT')

        for bone in armature.data.edit_bones:
            if bone.name not in bonesToKeep:
                armature.data.edit_bones.remove(bone)
                
        bpy.ops.object.mode_set(mode=current_mode)

        return {'FINISHED'}