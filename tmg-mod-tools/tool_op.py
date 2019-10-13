import bpy

#bpy.ops.object.convert(target='MESH')


class TOOL_Inset_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_inset_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Inset individual faces.'

    def execute(self, context):

        bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=True, use_edge_rail=False, thickness=0.115188, depth=0, use_outset=False, use_select_inset=False, use_individual=True)

        return {'FINISHED'}
        return {'FINISHED'}




