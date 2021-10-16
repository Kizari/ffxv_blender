import bpy

class SmoothSeamsOperator(bpy.types.Operator):
    bl_idname = "ffxv_weight.smooth_seams"
    bl_label = "Smooth Seams"
    bl_description = "SLOW - Averages the weights of vertices that share the exact same location to prevent seam splitting while animating"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        mesh = context.active_object.data
        seamVertices = {}
        groups = []

        current_mode = context.object.mode
        bpy.ops.object.mode_set(mode = 'OBJECT')

        for edge in mesh.edges:
            if edge.use_edge_sharp:
                for vertex in edge.vertices:
                    seamVertices[vertex] = False

        for index in seamVertices:
            if not seamVertices[index]:
                vertex = mesh.vertices[index]
                group = []
                group.append(vertex)
                for matchIndex in seamVertices:
                    if index == matchIndex:
                        continue
                    matchVertex = mesh.vertices[matchIndex]
                    x1 = vertex.undeformed_co[0]
                    y1 = vertex.undeformed_co[1]
                    z1 = vertex.undeformed_co[2]
                    x2 = matchVertex.undeformed_co[0]
                    y2 = matchVertex.undeformed_co[1]
                    z2 = matchVertex.undeformed_co[2]
                    if x1 == x2 and y1 == y2 and z1 == z2:
                        group.append(matchVertex)
                        seamVertices[matchIndex] = True
                if len(group) > 1:
                    groups.append(group)

        for group in groups:
            vertexGroups = {}
            length = len(group)
            for vertex in group:
                for subgroup in vertex.groups:
                    vertexGroups[subgroup.group] += subgroup.weight
            for vertex in group:
                for subgroup in vertex.groups:
                    subgroup.weight = vertexGroups[subgroup.group] / length
                
        bpy.ops.object.mode_set(mode = current_mode)

        return {'FINISHED'}