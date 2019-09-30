import bpy
	
class DEC_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.dec_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Decimate cylinder edges.'

    def execute(self, context):
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.loop_multi_select(ring=False)
        bpy.ops.mesh.dissolve_edges()
        return {'FINISHED'}
        return {'FINISHED'}
