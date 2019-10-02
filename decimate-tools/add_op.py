import bpy
	
#### Object Mode ###################################################################

class ADD_Arch_Object_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.add_arch_object_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Arch.'

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=True, location=(0, 0, 0))
        bpy.ops.transform.resize(value=(0.1, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.translate(value=(-1.1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='SCREW')
        bpy.context.object.modifiers["Screw"].axis = 'Y'
        bpy.context.object.modifiers["Screw"].angle = 3.14159
        bpy.context.object.modifiers["Screw"].use_normal_calculate = True
        bpy.context.object.modifiers["Screw"].use_normal_calculate = False
        bpy.context.object.modifiers["Screw"].use_merge_vertices = True
        bpy.context.object.modifiers["Screw"].steps = 12
        bpy.context.object.modifiers["Screw"].show_expanded = False
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].width = 0.026
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
        bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
        bpy.context.object.modifiers["Bevel"].show_in_editmode = False
        bpy.context.object.modifiers["Bevel"].show_expanded = False
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        bpy.ops.object.shade_smooth()
        return {'FINISHED'}
        return {'FINISHED'}

class ADD_Pipe_Line_Object_Y_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.add_pipe_line_object_y_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spiral Line.'

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=True, location=(0, 0, 0))
        bpy.ops.transform.resize(value=(0, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.translate(value=(1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='SCREW')
        bpy.context.object.modifiers["Screw"].axis = 'Y'
        bpy.context.object.modifiers["Screw"].use_normal_calculate = True
        bpy.context.object.modifiers["Screw"].use_merge_vertices = True
        bpy.context.object.modifiers["Screw"].steps = 12
        bpy.context.object.modifiers["Screw"].show_in_editmode = True
        bpy.context.object.modifiers["Screw"].show_expanded = False
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].offset = -1
        bpy.context.object.modifiers["Solidify"].thickness = 0.1
        bpy.context.object.modifiers["Solidify"].use_quality_normals = True
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].show_expanded = False
        bpy.context.object.modifiers["Solidify"].show_in_editmode = True
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].width = 0.016
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
        bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
        bpy.context.object.modifiers["Bevel"].show_in_editmode = False
        bpy.context.object.modifiers["Bevel"].show_expanded = False
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
        bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
        bpy.context.object.modifiers["Weighted Normal"].weight = 45
        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        return {'FINISHED'}
        return {'FINISHED'}

class ADD_Pipe_Line_Object_Z_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.add_pipe_line_object_z_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spiral Line.'

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(enter_editmode=True, location=(0, 0, 0))
        bpy.ops.transform.resize(value=(0, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.mesh.remove_doubles()
        bpy.ops.transform.translate(value=(1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='SCREW')
        bpy.context.object.modifiers["Screw"].axis = 'Z'
        bpy.context.object.modifiers["Screw"].use_normal_calculate = True
        bpy.context.object.modifiers["Screw"].use_merge_vertices = True
        bpy.context.object.modifiers["Screw"].steps = 12
        bpy.context.object.modifiers["Screw"].show_in_editmode = True
        bpy.context.object.modifiers["Screw"].show_expanded = False
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].offset = -1
        bpy.context.object.modifiers["Solidify"].thickness = 0.1
        bpy.context.object.modifiers["Solidify"].use_quality_normals = True
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].show_expanded = False
        bpy.context.object.modifiers["Solidify"].show_in_editmode = True
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].width = 0.016
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
        bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
        bpy.context.object.modifiers["Bevel"].show_in_editmode = False
        bpy.context.object.modifiers["Bevel"].show_expanded = False
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
        bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
        bpy.context.object.modifiers["Weighted Normal"].weight = 45
        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        return {'FINISHED'}
        return {'FINISHED'}

#### Spline Objects ###################################################################

class ADD_Basic_Spline_Y_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.add_basic_spline_y_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spline.'

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=True, location=(0, 0, 0))
        bpy.ops.transform.resize(value=(0, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.convert(target='CURVE')
        bpy.context.object.data.bevel_depth = 1
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.ops.object.shade_smooth()
        return {'FINISHED'}
        return {'FINISHED'}

class ADD_Pipe_Spline_Y_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.add_pipe_spline_y_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Solidified Spline.'

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=True, location=(0, 0, 0))
        bpy.ops.transform.resize(value=(0, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.mesh.remove_doubles()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.convert(target='CURVE')
        bpy.context.object.data.bevel_depth = 1
        bpy.ops.object.modifier_add(type='SMOOTH')
        bpy.context.object.modifiers["Smooth"].iterations = 3
        bpy.context.object.modifiers["Smooth"].show_viewport = True
        bpy.context.object.modifiers["Smooth"].show_expanded = False
        bpy.context.object.modifiers["Smooth"].show_in_editmode = True
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = -0.1
        bpy.context.object.modifiers["Solidify"].offset = 0
        bpy.context.object.modifiers["Solidify"].use_even_offset = True
        bpy.context.object.modifiers["Solidify"].use_quality_normals = False
        bpy.context.object.modifiers["Solidify"].show_expanded = False
        bpy.ops.object.modifier_add(type='SMOOTH')
        bpy.context.object.modifiers["Smooth"].show_viewport = True
        bpy.context.object.modifiers["Smooth"].show_expanded = False
        bpy.context.object.modifiers["Smooth"].show_in_editmode = True
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].segments = 3
        bpy.context.object.modifiers["Bevel"].show_in_editmode = False
        bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
        bpy.context.object.modifiers["Bevel"].width = 0.025
        bpy.context.object.modifiers["Bevel"].angle_limit = 1.48353
        bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
        bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
        bpy.context.object.modifiers["Bevel"].show_expanded = False
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        bpy.context.object.modifiers["Subdivision"].show_expanded = False
        bpy.ops.object.modifier_add(type='TRIANGULATE')
        bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.ops.object.shade_smooth()
        return {'FINISHED'}
        return {'FINISHED'}

