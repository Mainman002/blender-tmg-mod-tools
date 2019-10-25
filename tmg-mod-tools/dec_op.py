import bpy
	
class DEC_Edge_Random_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.dec_edge_random_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Decimate every other edge.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_edges()
        return {'FINISHED'}
        return {'FINISHED'}

class DEC_Edge_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.dec_edge_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Decimate edge loops.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_edges()
        return {'FINISHED'}
        return {'FINISHED'}


class DEC_Verts_Random_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.dec_verts_random_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Decimate every other vertex loop.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.dissolve_verts()

        return {'FINISHED'}
        return {'FINISHED'}

class DEC_Verts_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.dec_verts_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Decimate vertex loop.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.dissolve_verts()

        return {'FINISHED'}
        return {'FINISHED'}