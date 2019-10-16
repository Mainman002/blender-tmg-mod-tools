import bpy

#bpy.ops.object.convert(target='MESH')


class TOOL_Inset_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_inset_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Inset faces.'

    def execute(self, context):

        bpy.ops.mesh.inset(thickness=0.0722498, depth=0)

        return {'FINISHED'}
        return {'FINISHED'}


class TOOL_Inset_Depth_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_inset_depth_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Inset faces with depth.'

    def execute(self, context):

        bpy.ops.mesh.inset(thickness=0, depth=0.0742538)

        return {'FINISHED'}
        return {'FINISHED'}


class TOOL_Inset_Individual_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_inset_individual_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Inset individual faces.'

    def execute(self, context):

        bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=True, use_edge_rail=False, thickness=0.115188, depth=0, use_outset=False, use_select_inset=False, use_individual=True)

        return {'FINISHED'}
        return {'FINISHED'}


class TOOL_Bevel_Edge_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_bevel_edge_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Bevel selected edges.'

    def execute(self, context):

        bpy.ops.mesh.bevel(offset=0.117745, offset_pct=0, vertex_only=False)

        return {'FINISHED'}
        return {'FINISHED'}



