import bpy

# ADD list ->
# 
#### Mesh Objects
# 
# add_arch_object_ot_operator
# add_pipe_line_object_x_ot_operator
# add_pipe_line_object_y_ot_operator
# add_pipe_line_object_z_ot_operator
# 
#### Spline Objects
# 
# add_basic_spline_y_ot_operator
# add_pipe_spline_y_ot_operator
# 
# 

class ADD_OT_Solid_Plane_Object(bpy.types.Operator):
	bl_idname = 'wm.add_ot_solid_plane_object'
	bl_label = 'Decimate Panel'
	bl_description = 'Add Solid Plane.'
	bl_options = {'REGISTER', 'UNDO'}

	# check_solidify: bpy.props.BoolProperty(
	# name="Solidify",
	# description="Check if inset should be individual faces or single.",
	# default=True
	# )

	# check_bevel: bpy.props.BoolProperty(
	# name="Bevel",
	# description="Check if bevel should be added.",
	# default=False
	# )

	check_cursor_align: bpy.props.BoolProperty(
	name="Align To Cursor",
	description="Align to cursor location.",
	default=False
	)

	check_mod_triangulate: bpy.props.BoolProperty(
	name="Triangulate",
	description="Triangulate.",
	default=False
	)

	check_mod_weightednormals: bpy.props.BoolProperty(
	name="Weighted Normals",
	description="Weighted normals.",
	default=False
	)

	solid_thickness: bpy.props.FloatProperty(
	name="Solid Thickness",
	description="Solid thickness.",
	default=0.2,
	soft_min=0.0,
	soft_max=5.0,
	)

	solid_offset: bpy.props.FloatProperty(
	name="Solid Offset",
	description="Solid depth offset.",
	default=1.0,
	soft_min=-1.0,
	soft_max=1.0,
	)

	bevel_width: bpy.props.FloatProperty(
	name="Bevel Width",
	description="Bevel width.",
	default=0.03,
	min=0.001,
	soft_max=1.0,
	)

	bevel_segments: bpy.props.IntProperty(
	name="Bevel Segments",
	description="Bevel segments.",
	default=0,
	min=0,
	soft_max=5,
	)

	subdivision_level: bpy.props.IntProperty(
	name="Subdivision Level",
	description="Subdivision level.",
	default=0,
	min=0,
	soft_max=5,
	)

	def execute(self, context):

		axis_mode = context.scene.axis_mod
		mod_mirror = context.scene.mod_mirror
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

		bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(0, 0, 0))

		if self.check_cursor_align == True:
			bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

		obj = bpy.context.active_object

		if self.solid_thickness > 0:
			bpy.ops.object.modifier_add(type='SOLIDIFY')
			bpy.context.object.modifiers["Solidify"].offset = self.solid_offset
			bpy.context.object.modifiers["Solidify"].thickness = self.solid_thickness
			bpy.context.object.modifiers["Solidify"].use_even_offset = True
			bpy.context.object.modifiers["Solidify"].use_quality_normals = True
			bpy.context.object.modifiers["Solidify"].show_on_cage = True
			bpy.context.object.modifiers["Solidify"].show_expanded = False
		
			if mod_mirror == True:
				bpy.context.object.modifiers["Solidify"].use_rim_only = True
			else:
				bpy.context.object.modifiers["Solidify"].use_rim_only = False

		if mod_mirror == True:
			bpy.ops.object.modifier_add(type='MIRROR')
			bpy.context.object.modifiers["Mirror"].use_axis[0] = False

			if axis_mode == "X":
				bpy.context.object.modifiers["Mirror"].use_axis[0] = True
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[0] = True
			elif axis_mode == "Y":
				bpy.context.object.modifiers["Mirror"].use_axis[1] = True
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[1] = True
			elif axis_mode == "Z":
				bpy.context.object.modifiers["Mirror"].use_axis[2] = True
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[2] = True
			
			bpy.context.object.modifiers["Mirror"].use_clip = True
			bpy.context.object.modifiers["Mirror"].show_expanded = False


		if self.bevel_segments > 0:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = self.bevel_segments
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].width = self.bevel_width
			bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if self.subdivision_level > 0:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = self.subdivision_level
			bpy.context.object.modifiers["Subdivision"].show_expanded = False
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
		
		if self.check_mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
			bpy.context.object.modifiers["Triangulate"].show_expanded = False
		
		bpy.context.object.data.use_auto_smooth = True
		bpy.context.object.data.auto_smooth_angle = 0.785398
		bpy.ops.object.shade_smooth()

		if self.check_mod_weightednormals == True:
			bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
			bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
			bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
			bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
			bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
		
		return {'FINISHED'}
		return {'FINISHED'}

class ADD_OT_Solid_Circle_Object(bpy.types.Operator):
	bl_idname = 'wm.add_ot_solid_circle_object'
	bl_label = 'Decimate Panel'
	bl_description = 'Add Solid Circle.'
	bl_options = {'REGISTER', 'UNDO'}

	check_cursor_align: bpy.props.BoolProperty(
	name="Align To Cursor",
	description="Align to cursor location.",
	default=False
	)

	check_mod_mirror: bpy.props.BoolProperty(
	name="Mirror",
	description="Add mirror modifier.",
	default=False
	)

	check_mod_triangulate: bpy.props.BoolProperty(
	name="Triangulate",
	description="Triangulate.",
	default=False
	)

	check_mod_weightednormals: bpy.props.BoolProperty(
	name="Weighted Normals",
	description="Weighted normals.",
	default=False
	)

	solid_type: bpy.props.EnumProperty(
	name="Solid Type",
	description="Defines the solid fill type.",
	items=(
		('Solid', 'Solid', 'Solid',0),
		('Hollow', 'Hollow', 'Hollow',1),
		),
	default='Solid'
	)

	mirror_axis: bpy.props.EnumProperty(
	name="Mirror Axis",
	description="Defines the mirror axis",
	items=(
		('X', 'X', 'X',0),
		('Y', 'Y', 'Y',1),
		('Z', 'Z', 'Z',2)
		),
	default='X'
	)

	center_width: bpy.props.FloatProperty(
	name="Center Width",
	description="Center width.",
	default=0.3,
	min=0,
	soft_max=1.0,
	)

	solid_thickness: bpy.props.FloatProperty(
	name="Solid Thickness",
	description="Solid thickness.",
	default=0.2,
	soft_min=0.0,
	soft_max=5.0,
	)

	solid_offset: bpy.props.FloatProperty(
	name="Solid Offset",
	description="Solid depth offset.",
	default=1.0,
	soft_min=-1.0,
	soft_max=1.0,
	)

	bevel_width: bpy.props.FloatProperty(
	name="Bevel Width",
	description="Bevel width.",
	default=0.03,
	min=0.001,
	soft_max=1.0,
	)

	bevel_segments: bpy.props.IntProperty(
	name="Bevel Segments",
	description="Bevel segments.",
	default=0,
	min=0,
	soft_max=5,
	)

	subdivision_level: bpy.props.IntProperty(
	name="Subdivision Level",
	description="Subdivision level.",
	default=0,
	min=0,
	soft_max=5,
	)

	circle_verts: bpy.props.IntProperty(
	name="Vert Count",
	description="Circle vert amount.",
	default=12,
	min=3,
	soft_max=32,
	)

	def execute(self, context):

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

		# bpy.ops.mesh.primitive_circle_add(vertices=16, radius=1, enter_editmode=True, location=(0, 0, 0))
		bpy.ops.mesh.primitive_circle_add(vertices=self.circle_verts, radius=1, fill_type='NGON', enter_editmode=True, location=(0, 0, 0))

		bpy.ops.mesh.edge_face_add()

		if self.center_width > 0 and self.center_width < 1:
			bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=False, use_edge_rail=False, thickness=self.center_width, depth=0, use_outset=False, use_select_inset=False, use_individual=False, use_interpolate=True)
			if self.center_width < 1:
				bpy.ops.mesh.delete(type='FACE')

		bpy.ops.object.editmode_toggle()

		if self.solid_thickness > 0:
			bpy.ops.object.modifier_add(type='SOLIDIFY')
			bpy.context.object.modifiers["Solidify"].offset = self.solid_offset
			bpy.context.object.modifiers["Solidify"].use_even_offset = True
			bpy.context.object.modifiers["Solidify"].use_quality_normals = True
			bpy.context.object.modifiers["Solidify"].thickness = self.solid_thickness
			bpy.context.object.modifiers["Solidify"].show_on_cage = True
			bpy.context.object.modifiers["Solidify"].show_expanded = False

			if self.solid_type == 'Hollow':
				bpy.context.object.modifiers["Solidify"].use_rim_only = True
			else:
				bpy.context.object.modifiers["Solidify"].use_rim_only = False

		if self.check_mod_mirror == True:
			bpy.ops.object.modifier_add(type='MIRROR')
			if self.mirror_axis == 'X':
				bpy.context.object.modifiers["Mirror"].use_axis[0] = True
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[0] = True
			else:
				bpy.context.object.modifiers["Mirror"].use_axis[0] = False
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[0] = False
			if self.mirror_axis == 'Y':
				bpy.context.object.modifiers["Mirror"].use_axis[1] = True
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[1] = True
			else:
				bpy.context.object.modifiers["Mirror"].use_axis[1] = False
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[1] = False
			if self.mirror_axis == 'Z':
				bpy.context.object.modifiers["Mirror"].use_axis[2] = True
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[2] = True
			else:
				bpy.context.object.modifiers["Mirror"].use_axis[2] = False
				bpy.context.object.modifiers["Mirror"].use_bisect_axis[2] = False
			bpy.context.object.modifiers["Mirror"].use_clip = True
			bpy.context.object.modifiers["Mirror"].show_expanded = False

		if self.bevel_segments > 0:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = self.bevel_segments
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].width = self.bevel_width
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if self.subdivision_level > 0:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = self.subdivision_level
			bpy.context.object.modifiers["Subdivision"].render_levels = self.subdivision_level
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
			bpy.context.object.modifiers["Subdivision"].show_expanded = False

		if self.check_mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
			bpy.context.object.modifiers["Triangulate"].show_expanded = False
		
		bpy.context.object.data.use_auto_smooth = True
		bpy.context.object.data.auto_smooth_angle = 0.785398
		bpy.ops.object.shade_smooth()

		if self.check_mod_weightednormals == True:
			bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
			bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
			bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
			bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
			bpy.context.object.modifiers["Weighted Normal"].show_expanded = False

		return {'FINISHED'}
		return {'FINISHED'}

class ADD_OT_Arch_Object_X(bpy.types.Operator):
	bl_idname = 'wm.add_ot_arch_object_x'
	bl_label = 'Add Arch X Axis'
	bl_description = 'Add Arch.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		solid_offset = 1
		solid_thickness = 0.20
		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_mirror = context.scene.mod_mirror
		mod_bevel = context.scene.mod_bevel
		bevel_segments = 3
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

		# bpy.ops.object.editmode_toggle()

		bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=True, location=(0, 0, 0))
		bpy.ops.transform.resize(value=(0.1, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.translate(value=(-1.1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.rotate(value=1.5708, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.translate(value=(1.1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.translate(value=(0, 1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)

		bpy.ops.object.modifier_add(type='SCREW')
		bpy.context.object.modifiers["Screw"].axis = 'X'
		bpy.context.object.modifiers["Screw"].angle = 3.14159
		bpy.context.object.modifiers["Screw"].use_normal_calculate = True
		bpy.context.object.modifiers["Screw"].use_normal_calculate = False
		# bpy.context.object.modifiers["Screw"].use_merge_vertices = True
		bpy.context.object.modifiers["Screw"].steps = 12
		bpy.context.object.modifiers["Screw"].show_expanded = False

		if mod_bevel == True:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = bevel_segments
			bpy.context.object.modifiers["Bevel"].width = 0.026
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if mod_subsurf == True:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = subsurf_vlevel
			bpy.context.object.modifiers["Subdivision"].render_levels = subsurf_rlevel
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
			bpy.context.object.modifiers["Subdivision"].show_expanded = False

		if mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].show_expanded = False
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False

		bpy.context.object.data.use_auto_smooth = True
		bpy.context.object.data.auto_smooth_angle = 0.785398
		bpy.ops.object.shade_smooth()

		if mod_weightednormals == True:
			bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
			bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
			bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
			bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
			bpy.context.object.modifiers["Weighted Normal"].show_expanded = False

		return {'FINISHED'}
		return {'FINISHED'}

class ADD_OT_Arch_Object_Y(bpy.types.Operator):
	bl_idname = 'wm.add_ot_arch_object_y'
	bl_label = 'Decimate Panel'
	bl_description = 'Add Arch.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		solid_offset = 1
		solid_thickness = 0.20
		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_mirror = context.scene.mod_mirror
		mod_bevel = context.scene.mod_bevel
		bevel_segments = 3
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

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

		if mod_bevel == True:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = bevel_segments
			bpy.context.object.modifiers["Bevel"].width = 0.026
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if mod_subsurf == True:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = subsurf_vlevel
			bpy.context.object.modifiers["Subdivision"].render_levels = subsurf_rlevel
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
			bpy.context.object.modifiers["Subdivision"].show_expanded = False

		if mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].show_expanded = False
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
		
		bpy.context.object.data.use_auto_smooth = True
		bpy.context.object.data.auto_smooth_angle = 0.785398
		bpy.ops.object.shade_smooth()

		if mod_weightednormals == True:
			bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
			bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
			bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
			bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
			bpy.context.object.modifiers["Weighted Normal"].show_expanded = False

		return {'FINISHED'}
		return {'FINISHED'}

class ADD_OT_Arch_Object_Z(bpy.types.Operator):
	bl_idname = 'wm.add_ot_arch_object_z'
	bl_label = 'Decimate Panel'
	bl_description = 'Add Arch.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		solid_offset = 1
		solid_thickness = 0.20
		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_mirror = context.scene.mod_mirror
		mod_bevel = context.scene.mod_bevel
		bevel_segments = 3
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

		bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=True, location=(0, 0, 0))
		bpy.ops.transform.resize(value=(0.1, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.translate(value=(-1.1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.object.editmode_toggle()

		bpy.ops.object.modifier_add(type='SCREW')
		bpy.context.object.modifiers["Screw"].axis = 'Z'
		bpy.context.object.modifiers["Screw"].angle = 3.14159
		bpy.context.object.modifiers["Screw"].use_normal_calculate = True
		bpy.context.object.modifiers["Screw"].use_normal_calculate = False
		bpy.context.object.modifiers["Screw"].use_merge_vertices = True
		bpy.context.object.modifiers["Screw"].steps = 12
		bpy.context.object.modifiers["Screw"].show_expanded = False

		if mod_bevel == True:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = bevel_segments
			bpy.context.object.modifiers["Bevel"].width = 0.026
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if mod_subsurf == True:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = subsurf_vlevel
			bpy.context.object.modifiers["Subdivision"].render_levels = subsurf_rlevel
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
			bpy.context.object.modifiers["Subdivision"].show_expanded = False

		if mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].show_expanded = False
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False

		bpy.context.object.data.use_auto_smooth = True
		bpy.context.object.data.auto_smooth_angle = 0.785398
		bpy.ops.object.shade_smooth()

		if mod_weightednormals == True:
			bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
			bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
			bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
			bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
			bpy.context.object.modifiers["Weighted Normal"].show_expanded = False

		return {'FINISHED'}
		return {'FINISHED'}

class ADD_OT_Pipe_Line_Object_Y(bpy.types.Operator):
	bl_idname = 'wm.add_ot_pipe_line_object_y'
	bl_label = 'Decimate Panel'
	bl_description = 'Add Spiral Line.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		solid_offset = 1
		solid_thickness = 0.20
		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_mirror = context.scene.mod_mirror
		mod_bevel = context.scene.mod_bevel
		bevel_segments = 3
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

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

		if mod_solid == True:
			bpy.ops.object.modifier_add(type='SOLIDIFY')
			bpy.context.object.modifiers["Solidify"].offset = solid_offset
			bpy.context.object.modifiers["Solidify"].thickness = solid_thickness
			bpy.context.object.modifiers["Solidify"].use_quality_normals = True
			bpy.context.object.modifiers["Solidify"].use_even_offset = True
			bpy.context.object.modifiers["Solidify"].show_expanded = False
			bpy.context.object.modifiers["Solidify"].show_in_editmode = True

		if mod_bevel == True:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = bevel_segments
			bpy.context.object.modifiers["Bevel"].width = 0.016
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if mod_subsurf == True:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = subsurf_vlevel
			bpy.context.object.modifiers["Subdivision"].render_levels = subsurf_rlevel
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
			bpy.context.object.modifiers["Subdivision"].show_expanded = False
		
		if mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
			bpy.context.object.modifiers["Triangulate"].show_expanded = False

		bpy.context.object.data.use_auto_smooth = True
		bpy.context.object.data.auto_smooth_angle = 0.785398
		bpy.ops.object.shade_smooth()

		if mod_weightednormals == True:
			bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
			bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
			bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
			bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
			bpy.context.object.modifiers["Weighted Normal"].show_expanded = False

		return {'FINISHED'}
		return {'FINISHED'}

class ADD_OT_Pipe_Line_Object_Z(bpy.types.Operator):
	bl_idname = 'wm.add_ot_pipe_line_object_z'
	bl_label = 'Decimate Panel'
	bl_description = 'Add Spiral Line.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		solid_offset = 1
		solid_thickness = 0.20
		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_mirror = context.scene.mod_mirror
		mod_bevel = context.scene.mod_bevel
		bevel_segments = 3
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

		bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(0, 0, 0))
		bpy.ops.object.editmode_toggle()
		bpy.ops.transform.resize(value=(1, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.mesh.remove_doubles()
		bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.translate(value=(-1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.object.editmode_toggle()
		bpy.ops.object.modifier_add(type='SCREW')
		bpy.context.object.modifiers["Screw"].axis = 'Z'
		bpy.context.object.modifiers["Screw"].use_normal_calculate = True
		bpy.context.object.modifiers["Screw"].use_merge_vertices = True
		bpy.context.object.modifiers["Screw"].steps = 12
		bpy.context.object.modifiers["Screw"].show_in_editmode = True
		bpy.context.object.modifiers["Screw"].show_expanded = False

		if mod_solid == True:
			bpy.ops.object.modifier_add(type='SOLIDIFY')
			bpy.context.object.modifiers["Solidify"].offset = solid_offset
			bpy.context.object.modifiers["Solidify"].thickness = solid_thickness
			bpy.context.object.modifiers["Solidify"].use_quality_normals = True
			bpy.context.object.modifiers["Solidify"].use_even_offset = True
			bpy.context.object.modifiers["Solidify"].show_expanded = False
			bpy.context.object.modifiers["Solidify"].show_in_editmode = True

		if mod_bevel == True:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = bevel_segments
			bpy.context.object.modifiers["Bevel"].width = 0.016
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if mod_subsurf == True:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = subsurf_vlevel
			bpy.context.object.modifiers["Subdivision"].render_levels = subsurf_rlevel
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
			bpy.context.object.modifiers["Subdivision"].show_expanded = False

		if mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
			bpy.context.object.modifiers["Triangulate"].show_expanded = False

		bpy.context.object.data.use_auto_smooth = True
		bpy.context.object.data.auto_smooth_angle = 0.785398
		bpy.ops.object.shade_smooth()

		if mod_weightednormals == True:
			bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
			bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
			bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
			bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
			bpy.context.object.modifiers["Weighted Normal"].show_expanded = False

		return {'FINISHED'}
		return {'FINISHED'}

#### Spline Objects ###################################################################

#### X Axis ############################
#### Y Axis ############################
#### Z Axis ############################

class ADD_OT_Basic_Spline_Y(bpy.types.Operator):
	bl_idname = 'wm.add_ot_basic_spline_y'
	bl_label = 'Decimate Panel'
	bl_description = 'Add Spline.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		solid_offset = 1
		solid_thickness = 0.20
		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_mirror = context.scene.mod_mirror
		mod_bevel = context.scene.mod_bevel
		bevel_segments = 3
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

		bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=True, location=(0, 0, 0))
		bpy.ops.transform.resize(value=(0, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=3.7975, use_proportional_connected=False, use_proportional_projected=False)
		bpy.ops.mesh.remove_doubles()
		bpy.ops.object.editmode_toggle()
		bpy.ops.object.convert(target='CURVE')
		bpy.context.object.data.bevel_depth = 1

		if mod_solid == True:
			bpy.ops.object.modifier_add(type='SOLIDIFY')
			bpy.context.object.modifiers["Solidify"].thickness = solid_thickness
			bpy.context.object.modifiers["Solidify"].offset = solid_offset
			bpy.context.object.modifiers["Solidify"].use_even_offset = True
			bpy.context.object.modifiers["Solidify"].use_quality_normals = False
			bpy.context.object.modifiers["Solidify"].show_expanded = False

		if mod_bevel == True:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = bevel_segments
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].width = 0.025
			bpy.context.object.modifiers["Bevel"].angle_limit = 1.48353
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if mod_subsurf == True:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = subsurf_vlevel
			bpy.context.object.modifiers["Subdivision"].render_levels = subsurf_rlevel
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
			bpy.context.object.modifiers["Subdivision"].show_expanded = False

		if mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].show_expanded = False
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False

		bpy.ops.object.shade_smooth()

		return {'FINISHED'}
		return {'FINISHED'}

class ADD_OT_Pipe_Spline_Y(bpy.types.Operator):
	bl_idname = 'wm.add_ot_pipe_spline_y'
	bl_label = 'Decimate Panel'
	bl_description = 'Add Solidified Spline.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		solid_offset = 1
		solid_thickness = 0.20
		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_mirror = context.scene.mod_mirror
		mod_bevel = context.scene.mod_bevel
		bevel_segments = 3
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

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

		if mod_solid == True:
			bpy.ops.object.modifier_add(type='SOLIDIFY')
			bpy.context.object.modifiers["Solidify"].thickness = solid_thickness
			bpy.context.object.modifiers["Solidify"].offset = solid_offset
			bpy.context.object.modifiers["Solidify"].use_even_offset = True
			bpy.context.object.modifiers["Solidify"].use_quality_normals = False
			bpy.context.object.modifiers["Solidify"].show_expanded = False

		bpy.ops.object.modifier_add(type='SMOOTH')
		bpy.context.object.modifiers["Smooth.001"].show_viewport = True
		bpy.context.object.modifiers["Smooth.001"].show_expanded = False
		bpy.context.object.modifiers["Smooth.001"].show_in_editmode = True

		if mod_bevel == True:
			bpy.ops.object.modifier_add(type='BEVEL')
			bpy.context.object.modifiers["Bevel"].segments = bevel_segments
			bpy.context.object.modifiers["Bevel"].show_in_editmode = False
			bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
			bpy.context.object.modifiers["Bevel"].width = 0.025
			bpy.context.object.modifiers["Bevel"].angle_limit = 1.48353
			bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
			bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
			bpy.context.object.modifiers["Bevel"].show_expanded = False

		if mod_subsurf == True:
			bpy.ops.object.modifier_add(type='SUBSURF')
			bpy.context.object.modifiers["Subdivision"].levels = subsurf_vlevel
			bpy.context.object.modifiers["Subdivision"].render_levels = subsurf_rlevel
			bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
			bpy.context.object.modifiers["Subdivision"].show_expanded = False

		if mod_triangulate == True:
			bpy.ops.object.modifier_add(type='TRIANGULATE')
			bpy.context.object.modifiers["Triangulate"].quad_method = 'FIXED'
			bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
			bpy.context.object.modifiers["Triangulate"].show_expanded = False
			bpy.context.object.modifiers["Triangulate"].show_in_editmode = False

		bpy.ops.object.shade_smooth()

		return {'FINISHED'}
		return {'FINISHED'}

#### Z Axis ###################


class ADD_OT_Spline_Follow_Y(bpy.types.Operator):
	bl_idname = 'wm.add_ot_spline_folow_y'
	bl_label = 'Add Spline Follow Y'
	bl_description = 'Add cube following spline path.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		solid_offset = 1
		solid_thickness = 0.20
		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_mirror = context.scene.mod_mirror
		mod_bevel = context.scene.mod_bevel
		bevel_segments = 3
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		obj = bpy.context.active_object

		if obj != None:
			bpy.ops.object.mode_set(mode="OBJECT")

		obj = bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))
		curve = bpy.ops.curve.primitive_nurbs_path_add(enter_editmode=False, location=(0, 0, 0))

		for nr, obj in enumerate(bpy.context.selected_objects):

			#types = obj.type

			bpy.context.view_layer.objects.active = obj
			obj.select_set(state=True)
				
			#obj.active_selection = True
			#curve.active_selection = True
			obj.parent_set(type='PATH_CONST')
			bpy.context.view_layer.objects.active = obj
			obj.constraints["AutoPath"].use_curve_follow = True
			obj.constraints["AutoPath"].use_curve_radius = True
			obj.constraints["AutoPath"].use_fixed_location = True
		
		return {'FINISHED'}
		return {'FINISHED'}



class ADD_OT_TestCube(bpy.types.Operator):
	"""Subdivided Cube Test"""
	bl_idname = 'wm.add_ot_sub_cube'
	bl_label = 'Subdivided Cube Test'
	bl_description = 'Add a custom cube.'
	bl_options = {'REGISTER', 'UNDO'}

	size: bpy.props.FloatProperty(
	name="Scale",
	description="Cube scale.",
	default=1,
	min=0.01,
	soft_max=10.0
	)

	cuts: bpy.props.IntProperty(
	name="Loop Cuts",
	description="Subdivision loops.",
	default=1,
	min=0,
	soft_max=5,
	)

	smoothness: bpy.props.FloatProperty(
	name="Subdivision Smoothness",
	description="Smoothes subdivision loop cuts.",
	default=0.0,
	soft_min=0.0,
	soft_max=1.0,
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def execute(self, context):
		bpy.ops.mesh.primitive_cube_add(size=self.size, calc_uvs=True, enter_editmode=True, align='WORLD', location=(0, 0, 0))
		if self.cuts > 0:
			bpy.ops.mesh.subdivide(number_cuts=self.cuts, smoothness=self.smoothness)
		return {'FINISHED'}
