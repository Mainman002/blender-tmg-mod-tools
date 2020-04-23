import bpy
import bmesh

class TOOL_OT_Knurl_Face_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_knurl_face_edit'
	bl_label = 'Tool Knurl Face'
	bl_description = 'Knurls selected face / faces.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	check_flatten_edge: bpy.props.BoolProperty(
	name="Flatten Edge",
	description="flatten the Knurled edges.",
	default=False
	)

	check_inset_individual: bpy.props.BoolProperty(
	name="Inset Individual",
	description="Checks if individual faces are seperate or unified.",
	default=False
	)

	check_vert_bevel: bpy.props.BoolProperty(
	name="Bevel Verts",
	description="Bevel intersecting verts.",
	default=True
	)

	check_knurl_unsubdived: bpy.props.BoolProperty(
	name="Knurl Un-subdivide",
	description="Unsubdivides mesh to rotate the knurls.",
	default=True
	)

	inset_edge_thickness: bpy.props.FloatProperty(
	name="Inset Edge Thickness",
	description="Adjust outer Inset Thickness.",
	default=0.08,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	inset_center_thickness: bpy.props.FloatProperty(
	name="Inset Center Thickness",
	description="Adjust inside Inset Thickness.",
	default=0.08,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	inset_depth: bpy.props.FloatProperty(
	name="Inset Depth",
	description="Adjust inside Inset Depth.",
	default=0.0,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	poke_depth: bpy.props.FloatProperty(
	name="Vert Depth",
	description="Adjust Vert depth.",
	default=0.2,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	point_bevel: bpy.props.FloatProperty(
	name="Vert Bevel",
	description="Bevel verts.",
	default=0.0,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	point_profile: bpy.props.FloatProperty(
	name="Vert Bevel Profile",
	description="Bevel Verts profile curve.",
	default=0.0,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)


	median_bevel: bpy.props.FloatProperty(
	name="Edge Bevel",
	description="Bevel intersecting edges.",
	default=0.0,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	point_segments: bpy.props.IntProperty(
	name="Vert Subdivisions",
	description="Subdivision Vert loops.",
	default=2,
	min=0,
	soft_max=20,
	)

	median_segments: bpy.props.IntProperty(
	name="Edge Subdivisions",
	description="Subdivision Edge loops.",
	default=3,
	min=0,
	soft_max=20,
	)

	cuts: bpy.props.IntProperty(
	name="Face Subdivisions",
	description="Subdivision Face loops.",
	default=3,
	min=0,
	soft_max=20,
	)

	bridge_cuts: bpy.props.IntProperty(
	name="Bridge Loop Cuts",
	description="Subdivision loops for bridge cuts. !!Warning!! use only if you have a solid object selected, else the bridge operator will throw out an error message",
	default=0,
	min=0,
	soft_max=20,
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def invoke(self, context, event):
		self.cuts = 3
		self.bridge_cuts = 0
		self.point_segments = 2
		return self.execute(context)

	def execute(self, context):
		if self.inset_edge_thickness > 0:
			bpy.ops.mesh.inset(thickness=self.inset_edge_thickness, depth=0, use_individual=self.check_inset_individual)

		if self.inset_center_thickness > 0:
			bpy.ops.mesh.inset(thickness=self.inset_center_thickness, depth=self.inset_depth)

		if self.bridge_cuts > 0:
			bpy.ops.mesh.bridge_edge_loops(type='CLOSED', use_merge=False, number_cuts=self.bridge_cuts)

		if self.median_bevel > 0:
			bpy.ops.mesh.bevel(offset=self.median_bevel, offset_pct=0, segments=self.median_segments, vertex_only=True)

		if self.cuts > 0:
			bpy.ops.mesh.subdivide(number_cuts=self.cuts)

		if self.check_knurl_unsubdived == True:
			bpy.ops.mesh.unsubdivide(iterations=1)

		bpy.ops.mesh.poke(offset=self.poke_depth)

		if self.point_bevel > 0:
			bpy.ops.mesh.bevel(offset=self.point_bevel, offset_pct=0, segments=self.point_segments, profile=self.point_profile, vertex_only=self.check_vert_bevel, miter_outer='SHARP')

		if self.check_flatten_edge:
			bpy.ops.mesh.select_all(action='INVERT')

			bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
			bpy.ops.mesh.region_to_loop()
			bpy.ops.mesh.select_interior_faces()

			bpy.ops.mesh.loop_multi_select(ring=True)
			bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
			bpy.ops.mesh.quads_convert_to_tris(quad_method='SHORTEST_DIAGONAL')

			# bpy.ops.mesh.select_all(action='INVERT')
			bpy.ops.mesh.select_all(action='DESELECT')


		return {'FINISHED'}
		return {'FINISHED'}

class TOOL_OT_Inset_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_inset_edit'
	bl_label = 'Tool Inset Edit'
	bl_description = 'Inset faces.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	check_inset_individual: bpy.props.BoolProperty(
	name="Individual",
	description="Margin between UV islands.",
	default=False
	)

	check_inset_thickness: bpy.props.BoolProperty(
	name="Thickness",
	description="Margin between UV islands.",
	default=True
	)

	check_inset_depth: bpy.props.BoolProperty(
	name="Depth",
	description="Margin between UV islands.",
	default=False
	)

	inset_thickness: bpy.props.FloatProperty(
	name="Inset Thickness",
	description="Margin between UV islands.",
	default=0.05,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	inset_depth: bpy.props.FloatProperty(
	name="Inset Depth",
	description="Margin between UV islands.",
	default=0.03,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def execute(self, context):

		for obj in (bpy.context.selected_objects):
			if (obj.type == "MESH"):
				if self.inset_thickness > 0:
					nthick = (obj.dimensions.x * self.inset_thickness)
					print(nthick)
					# bpy.data.objects['object_name'].dimensions.y
					# bpy.data.objects['object_name'].dimensions.z


		if self.check_inset_individual == True:
			if self.check_inset_depth == False and self.check_inset_thickness == True:
				#bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=True, use_edge_rail=False, thickness=check_inset_thickness, depth=inset_depth, use_outset=False, use_select_inset=False, use_individual=check_inset_individual)
				bpy.ops.mesh.inset(thickness=nthick, depth=0.00, use_individual=self.check_inset_individual)

			elif self.check_inset_depth == True and self.check_inset_thickness == False:
				bpy.ops.mesh.inset(thickness=0.00, depth=self.inset_depth, use_individual=self.check_inset_individual)
			
			elif self.check_inset_depth == True and self.check_inset_thickness == True:
				bpy.ops.mesh.inset(thickness=self.inset_thickness, depth=self.inset_depth, use_individual=self.check_inset_individual)

		else:
			if self.check_inset_depth == False and self.check_inset_thickness == True:
				#bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=True, use_edge_rail=False, thickness=check_inset_thickness, depth=inset_depth, use_outset=False, use_select_inset=False, use_individual=check_inset_individual)
				bpy.ops.mesh.inset(thickness=self.inset_thickness, depth=0.00)

			elif self.check_inset_depth == True and self.check_inset_thickness == False:
				bpy.ops.mesh.inset(thickness=0.00, depth=self.inset_depth)

			elif self.check_inset_depth == True and self.check_inset_thickness == True:
				bpy.ops.mesh.inset(thickness=self.inset_thickness, depth=self.inset_depth)

		return {'FINISHED'}
		return {'FINISHED'}


class TOOL_OT_Bevel_Edge_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_bevel_edge_edit'
	bl_label = 'Tool Bevel Edge Edit'
	bl_description = 'Bevel selected edges.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	check_edge_ngon: bpy.props.BoolProperty(
	name="Edge Ngons",
	description="Connects circle verts to the corner verts.",
	default=True
	)

	check_vertex_only: bpy.props.BoolProperty(
	name="Vertex Only",
	description="Bevel verts only.",
	default=False
	)

	bevel_offset: bpy.props.FloatProperty(
	name="Bevel Offset",
	description="Margin between UV islands.",
	default=0.117745,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	bevel_segments: bpy.props.IntProperty(
	name="Bevel Segments",
	description="Amount of loops to add in between edge loops.",
	default=1,
	min=1,
	soft_max=5,
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
	unit='LENGTH'
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def invoke(self, context, event):
		self.cuts = 0
		self.bevel_segments = 1
		return self.execute(context)

	def execute(self, context):

		if self.cuts > 0:
			bpy.ops.mesh.subdivide(number_cuts=self.cuts, ngon=self.check_edge_ngon, smoothness=self.smoothness, fractal_along_normal=0.0)

		bpy.ops.mesh.bevel(offset=self.bevel_offset, offset_pct=0, segments=self.bevel_segments, vertex_only=self.check_vertex_only)

		return {'FINISHED'}
		return {'FINISHED'}

class TOOL_OT_Remove_Doubles_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_remove_doubles_edit'
	bl_label = 'Tool Remove Doubles Edit'
	bl_description = 'Merge overlapping verts.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	threshold: bpy.props.FloatProperty(
	name="Distance",
	description="Distance between verts to merge.",
	default=0.01,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	def execute(self, context):

		bpy.ops.mesh.remove_doubles(threshold=self.threshold)

		return {'FINISHED'}
		return {'FINISHED'}

class TOOL_OT_Select_Interior_Faces_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_select_interior_faces_edit'
	bl_label = 'Tool Select Interior Faces Edit'
	bl_description = 'Select faces in between selection.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		bpy.ops.mesh.loop_to_region()

		return {'FINISHED'}
		return {'FINISHED'}

class TOOL_OT_Flip_Normals_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_flip_normals_edit'
	bl_label = 'Tool Flip Normals Edit'
	bl_description = 'Flip normals of selection.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		bpy.ops.mesh.flip_normals()

		return {'FINISHED'}
		return {'FINISHED'}


class TOOL_OT_Mesh_Face_To_Circle_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_mesh_face_to_circle_edit'
	bl_label = 'Tool Mesh Face To Circle Edit'
	bl_description = 'Insets face to circle.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	check_edge_ngon: bpy.props.BoolProperty(
	name="Edge Ngons",
	description="Connects circle verts to the corner verts.",
	default=True
	)

	check_remove_center: bpy.props.BoolProperty(
	name="Remove Center",
	description="Removes the center face.",
	default=False
	)

	check_inset_individual: bpy.props.BoolProperty(
	name="Individual",
	description="Check if inset should be individual faces or single.",
	default=False
	)

	inset_thickness_edge: bpy.props.FloatProperty(
	name="Inset Thickness Edge",
	description="Outside thickness.",
	default=0.1,
	soft_min=0.0,
	soft_max=0.99,
	unit='LENGTH'
	)

	inset_thickness_center: bpy.props.FloatProperty(
	name="Inset Thickness Center",
	description="Center thickness.",
	default=0.25,
	soft_min=0.0,
	soft_max=0.99,
	unit='LENGTH'
	)

	check_circle_depth: bpy.props.BoolProperty(
	name="Circle Depth",
	description="Circle depth.",
	default=False,
	)

	inset_circle_thickness: bpy.props.FloatProperty(
	name="Inset Circle Thickness",
	description="Circle thickness.",
	default=0.1,
	soft_min=0.0,
	soft_max=0.99,
	unit='LENGTH'
	)

	inset_center_depth: bpy.props.FloatProperty(
	name="Inset Center Depth",
	description="Inset center depth.",
	default=-0.15,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	cuts: bpy.props.IntProperty(
	name="Loop Cuts",
	description="Subdivision loops.",
	default=3,
	min=1,
	soft_max=5,
	)

	# subdivide_type: bpy.props.EnumProperty(
	# name="Subdivide Type",
	# description="The type of corners to use when subdividing.",
	# items=(
	# 	('INNERVERT', 'INNERVERT', 'INNERVERT',0),
	# 	('STRAIGHT_CUT', 'STRAIGHT_CUT', 'STRAIGHT_CUT',1),
	# 	('FAN', 'FAN', 'FAN',2),
	# 	('PATH', 'PATH', 'PATH',3)
	# 	),
	# default='INNERVERT'
	# )

	def invoke(self, context, event):
		self.cuts = 0
		return self.execute(context)

	def execute(self, context):
		if self.inset_thickness_edge > 0:
			bpy.ops.mesh.inset(thickness=self.inset_thickness_edge, depth=0, use_individual=self.check_inset_individual)
		bpy.ops.mesh.inset(thickness=self.inset_thickness_center, depth=0)
		bpy.ops.mesh.subdivide(number_cuts=self.cuts, ngon=self.check_edge_ngon, quadcorner='INNERVERT')
		bpy.ops.mesh.looptools_circle(custom_radius=False, fit='best', flatten=True, influence=100, lock_x=False, lock_y=False, lock_z=False, radius=1, regular=True)
		if self.check_circle_depth:
			bpy.ops.mesh.inset(thickness=self.inset_circle_thickness, depth=self.inset_center_depth)
		else:
			bpy.ops.mesh.inset(thickness=self.inset_circle_thickness, depth=0)

		bpy.ops.mesh.dissolve_faces()

		if self.check_remove_center:
			bpy.ops.mesh.delete(type='FACE')


		return {'FINISHED'}
		return {'FINISHED'}



class TOOL_OT_Wrinkle_Face_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_wrinkle_face_edit'
	bl_label = 'Tool Wrinkle Face'
	bl_description = 'Wrinkles selected face(s).'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	check_edge_ngon: bpy.props.BoolProperty(
	name="Edge Ngons",
	description="Connects circle verts to the corner verts.",
	default=True
	)

	check_wave_mod: bpy.props.BoolProperty(
	name="Wave modifier",
	description="Adds a wave modifier.",
	default=False
	)

	cuts: bpy.props.IntProperty(
	name="Loop Cuts",
	description="Subdivision loops.",
	default=1,
	min=0,
	soft_max=20,
	)

	smoothing: bpy.props.IntProperty(
	name="Smooth Verts",
	description="Smooth vertex.",
	default=3,
	min=0,
	soft_max=10,
	)

	subdivide_smoothness: bpy.props.FloatProperty(
	name="Subdivision Smoothness",
	description="Smoothes subdivision loop cuts.",
	default=0.0,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	subdivide_fractals: bpy.props.FloatProperty(
	name="Subdivision Fractals",
	description="Subdivision fractal warping.",
	default=0.0,
	soft_min=0.0,
	soft_max=10.0,
	unit='LENGTH'
	)

	warp_angle: bpy.props.FloatProperty(
	name="Warp Angle",
	description="What angle to lean towards when warping.",
	default=0.1,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	offset_angle: bpy.props.FloatProperty(
	name="Warp Offset Angle",
	description="Slide offset for warping the mesh.",
	default=-0.1,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	offset_min: bpy.props.FloatProperty(
	name="Warp Offset Min",
	description="Minimum warp offset.",
	default=0.06,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	offset_max: bpy.props.FloatProperty(
	name="Warp Offset Max",
	description="Maximum warp offset.",
	default=0.2,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	lambda_factor: bpy.props.FloatProperty(
	name="Smooth Factor",
	description="Lambda factor for smoothing vertex.",
	default=5.0,
	soft_min=-0.0,
	soft_max=10.0,
	unit='LENGTH'
	)

	center: bpy.props.FloatVectorProperty(
	name="Center",
	subtype='XYZ',
	default=[0.0, 1.0, 0.0],
	unit='LENGTH'
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def invoke(self, context, event):
		self.cuts = 0
		self.check_wave_mod = False
		return self.execute(context)

	def execute(self, context):

		for obj in (bpy.context.selected_objects):
			if (obj.type == "MESH"):

				if self.cuts > 0:
					# bpy.ops.mesh.subdivide(number_cuts=self.cuts, smoothness=self.subdivide_smoothness, fractal_along_normal=0.0)
					bpy.ops.mesh.subdivide(number_cuts=self.cuts, smoothness=self.subdivide_smoothness, quadcorner='INNERVERT', ngon=self.check_edge_ngon, fractal=self.subdivide_fractals, fractal_along_normal=1, seed=1)

				bpy.ops.transform.vertex_warp(warp_angle=self.warp_angle, offset_angle=self.offset_angle, min=self.offset_min, max=self.offset_max, center=(self.center[0],self.center[1],self.center[2]))

				bpy.ops.mesh.vertices_smooth_laplacian(repeat=self.smoothing, lambda_factor=self.lambda_factor)

				mod = obj.modifiers.get("Ocean")
				if self.check_wave_mod == True:
					if mod is None:
						obj.modifiers.new(name='Ocean', type='OCEAN')
					obj.modifiers["Ocean"].geometry_mode = 'DISPLACE'
					obj.modifiers["Ocean"].size = 0.000999948
					obj.modifiers["Ocean"].wave_alignment = 2.1
					obj.modifiers["Ocean"].choppiness = 0
					obj.modifiers["Ocean"].wave_alignment = 7.97
					obj.modifiers["Ocean"].damping = 0.419192
					obj.modifiers["Ocean"].wave_scale_min = 2.21
					obj.modifiers["Ocean"].wind_velocity = 27.9
					obj.modifiers["Ocean"].use_normals = False
					obj.modifiers["Ocean"].spatial_size = 71
					obj.modifiers["Ocean"].resolution = 4
					obj.modifiers["Ocean"].time = 1.33
					obj.modifiers["Ocean"].random_seed = 3
				else:
					if mod is None:
						pass
					else:
						obj.modifiers.remove(mod)

		return {'FINISHED'}
		return {'FINISHED'}


class TOOL_OT_Edge_Slide_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_edge_slide_edit'
	bl_label = 'Tool Edge Slide'
	bl_description = 'Slides, Rotates, and fixes selected edges.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	check_edge_rotate: bpy.props.BoolProperty(
	name="Edge Rotate",
	description="Connects circle verts to the corner verts.",
	default=True
	)

	remove_doubles_threshold: bpy.props.FloatProperty(
	name="Remove Doubles",
	description="Distance between verts to merge.",
	default=0.01,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	edge_slide: bpy.props.FloatProperty(
	name="Edge Slide",
	description="Smoothes subdivision loop cuts.",
	default=0.0,
	soft_min=-1.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	# center: bpy.props.FloatVectorProperty(
	# name="Center",
	# subtype='XYZ',
	# default=[0.0, 1.0, 0.0],
	# unit='LENGTH'
	# )

	# mirror_axis: bpy.props.EnumProperty(
	# name="Mirror Axis",
	# description="Defines the mirror axis",
	# items=(
	# 	('X', 'X', 'X',0),
	# 	('Y', 'Y', 'Y',1),
	# 	('Z', 'Z', 'Z',2)
	# 	),
	# default='X'
	# )

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def invoke(self, context, event):
		return self.execute(context)

	def execute(self, context):

		for obj in (bpy.context.selected_objects):
			if (obj.type == "MESH"):

				bpy.ops.transform.edge_slide(value=self.edge_slide, use_even=True, flipped=True, mirror=True, correct_uv=True)

				# bpy.ops.transform.rotate(value=-0.766057, orient_axis=self.mirror_axis, orient_type='VIEW', orient_matrix=((self.center[0],0,0), (0, self.center[1], 0), (0, 0, self.center[2])), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

				if self.check_edge_rotate:
					bpy.ops.mesh.edge_rotate(use_ccw=self.check_edge_rotate)

				# if self.remove_doubles_threshold > 0:
				# 	bpy.context.scene.tool_settings.use_mesh_automerge = True
				# 	bpy.context.scene.tool_settings.double_threshold = self.remove_doubles_threshold
				# 	bpy.context.scene.tool_settings.use_mesh_automerge_and_split = True

				if self.remove_doubles_threshold > 0:
					bpy.ops.mesh.select_more(use_face_step=False)
					bpy.ops.mesh.remove_doubles(threshold=self.remove_doubles_threshold)


		return {'FINISHED'}


class TOOL_OT_Slotted_Grate_Edit(bpy.types.Operator):
	bl_idname = 'wm.tool_ot_slotted_grate_edit'
	bl_label = 'Tool Slotted Grate'
	bl_description = 'Turns selected faces into a slotted grate pattern.'
	bl_context = "mesh_edit"
	bl_options = {'REGISTER', 'UNDO'}

	check_vertex_only: bpy.props.BoolProperty(
	name="Vertex Only",
	description="Bevel only vertex.",
	default=True
	)

	bevel_thickness: bpy.props.FloatProperty(
	name="Bevel Thickness",
	description="Adjusts beveled edge thickness.",
	default=0.0,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	inset_thickness: bpy.props.FloatProperty(
	name="Inset Thickness",
	description="Adjusts inset face thickness.",
	default=0.0,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	inset_depth: bpy.props.FloatProperty(
	name="Inset Depth",
	description="Adjusts inset face depth.",
	default=0.0,
	soft_min=0.0,
	soft_max=1.0,
	unit='LENGTH'
	)

	bridge_twist: bpy.props.IntProperty(
	name="Edge Twist",
	description="Twist edge loops.",
	default=0,
	min=0,
	soft_max=60,
	)

	bridge_cuts: bpy.props.IntProperty(
	name="Edge Twist",
	description="Twist edge loops.",
	default=0,
	min=0,
	soft_max=10,
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def invoke(self, context, event):
		return self.execute(context)

	def execute(self, context):

		for obj in (bpy.context.selected_objects):
			if (obj.type == "MESH"):

				# if self.bridge_twist > 0:
				bpy.ops.mesh.bridge_edge_loops(use_merge=False, twist_offset=self.bridge_twist, number_cuts=self.bridge_cuts)
				# else:
				# 	bpy.ops.mesh.bridge_edge_loops(use_merge=False, twist_offset=0, number_cuts=self.bridge_cuts)
				
				bpy.ops.mesh.bevel(offset=self.bevel_thickness, offset_pct=0, vertex_only=self.check_vertex_only)

				bpy.ops.mesh.inset(thickness=self.inset_thickness, depth=self.inset_depth)

		return {'FINISHED'}


# bpy.props.FloatVectorProperty(
# name="", 
# description="", 
# default=(0.0, 0.0, 0.0), 
# min=sys.float_info.min, max=sys.float_info.max, 
# soft_min=sys.float_info.min, soft_max=sys.float_info.max, 
# step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', 
# size=3, update=None, get=None, set=None
# )



# Knurl + scale
# bpy.ops.mesh.inset(thickness=0.229018, depth=0)
# bpy.ops.transform.resize(value=(1, 1, 2.5948), orient_type='LOCAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='LOCAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1.27, use_proportional_connected=False, use_proportional_projected=False)
# bpy.ops.mesh.subdivide(number_cuts=5, quadcorner='INNERVERT')
# bpy.ops.transform.resize(value=(1, 1, 0.163863), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)



# for obj in (bpy.context.selected_objects):
# 	if (obj.type == "MESH"):
		# uniques = context.objects_in_mode_unique_data
		# bms = {}
		# verts = []
		# for obj in uniques:
		# 	me = obj.data
		# 	bms[obj] = bmesh.from_edit_mesh(me)
		# 	for obj in bms:
		# 		verts.extend([obj.matrix_world @ v.co  for v in bms[obj].verts if v.select]) 
		# 		print(verts)




# bpy.ops.transform.edge_slide(value=-0.385636, use_even=False, flipped=False, mirror=True, correct_uv=True)
# bpy.ops.mesh.edge_rotate(use_ccw=False)
# bpy.ops.transform.rotate(value=-0.766057, orient_axis='Z', orient_type='VIEW', orient_matrix=((0.846491, -0.532403, -4.11272e-06), (0.0968547, 0.154001, -0.983312), (-0.523519, -0.832364, -0.181926)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)


# bpy.ops.mesh.bridge_edge_loops(use_merge=False, twist_offset=61, number_cuts=3)
# bpy.ops.mesh.bevel(offset=0.033168, offset_pct=0, vertex_only=False)
# bpy.ops.mesh.inset(thickness=0, depth=0.0337667)