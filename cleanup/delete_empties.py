import bpy

class DeleteEmptiesOperator(bpy.types.Operator):
    bl_idname = "ffxv_cleanup.delete_empties"
    bl_label = "Empties"
    bl_description = "Deletes all empties in the current scene. Imported FFXV assets usually have many of these"

    def execute(self, context):
        bpy.ops.object.select_all(action = 'DESELECT')

        for object in bpy.data.objects:
            if type(object.data).__name__ == "NoneType":
                if bpy.app.version >= (2, 80, 0):
                    object.select_set(state=True)
                else:
                    object.select = True
                
        bpy.ops.object.delete()
        return {'FINISHED'}