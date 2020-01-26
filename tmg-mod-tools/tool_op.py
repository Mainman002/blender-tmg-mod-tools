import bpy

#bpy.ops.object.convert(target='MESH')


#def inset(self, context):
    #inset_thickness = bpy.types.Scene.inset_thickness
    #bpy.ops.mesh.inset(thickness=inset_thickness, depth=0.00, use_individual=False)



class TOOL_Inset_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_inset_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Inset faces.'
    bl_options = {'REGISTER', 'UNDO'}
        

    def execute(self, context):

        check_inset_individual = context.scene.check_inset_individual
        check_inset_thickness = context.scene.check_inset_thickness
        check_inset_depth = context.scene.check_inset_depth

        inset_thickness = context.scene.inset_thickness
        inset_depth = context.scene.inset_depth

        if check_inset_individual == True:
            if check_inset_depth == False and check_inset_thickness == True:
                #bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=True, use_edge_rail=False, thickness=check_inset_thickness, depth=inset_depth, use_outset=False, use_select_inset=False, use_individual=check_inset_individual)
                bpy.ops.mesh.inset(thickness=inset_thickness, depth=0.00, use_individual=check_inset_individual)

            elif check_inset_depth == True and check_inset_thickness == False:
                bpy.ops.mesh.inset(thickness=0.00, depth=inset_depth, use_individual=check_inset_individual)
            
            elif check_inset_depth == True and check_inset_thickness == True:
                bpy.ops.mesh.inset(thickness=inset_thickness, depth=inset_depth, use_individual=check_inset_individual)

        else:
            if check_inset_depth == False and check_inset_thickness == True:
                #bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=True, use_edge_rail=False, thickness=check_inset_thickness, depth=inset_depth, use_outset=False, use_select_inset=False, use_individual=check_inset_individual)
                bpy.ops.mesh.inset(thickness=inset_thickness, depth=0.00)

            elif check_inset_depth == True and check_inset_thickness == False:
                bpy.ops.mesh.inset(thickness=0.00, depth=inset_depth)

            elif check_inset_depth == True and check_inset_thickness == True:
                bpy.ops.mesh.inset(thickness=inset_thickness, depth=inset_depth)

        return {'FINISHED'}
        return {'FINISHED'}


class TOOL_Bevel_Edge_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_bevel_edge_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Bevel selected edges.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.mesh.bevel(offset=0.117745, offset_pct=0, vertex_only=False)

        return {'FINISHED'}
        return {'FINISHED'}

class TOOL_Remove_Doubles_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_remove_doubles_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Merge overlapping verts.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.mesh.remove_doubles(threshold=0.01)

        return {'FINISHED'}
        return {'FINISHED'}

class TOOL_Select_Interior_Faces_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_select_interior_faces_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Select faces in between selection.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.mesh.loop_to_region()

        return {'FINISHED'}
        return {'FINISHED'}

class TOOL_Flip_Normals_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.tool_flip_normals_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Flip normals of selection.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.mesh.flip_normals()

        return {'FINISHED'}
        return {'FINISHED'}



#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":9, "mesh_select_mode_init":(False, False, True)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":False, "use_accurate":False})
