import bpy

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
	soft_max=1.0
	)

	inset_depth: bpy.props.FloatProperty(
	name="Inset Depth",
	description="Margin between UV islands.",
	default=0.03,
	soft_min=-1.0,
	soft_max=1.0,
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def execute(self, context):

		if self.check_inset_individual == True:
			if self.check_inset_depth == False and self.check_inset_thickness == True:
				#bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=True, use_edge_rail=False, thickness=check_inset_thickness, depth=inset_depth, use_outset=False, use_select_inset=False, use_individual=check_inset_individual)
				bpy.ops.mesh.inset(thickness=self.inset_thickness, depth=0.00, use_individual=self.check_inset_individual)

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
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def execute(self, context):

		if self.cuts > 0:
			bpy.ops.mesh.subdivide(number_cuts=self.cuts, smoothness=self.smoothness, fractal_along_normal=0.0)

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
	soft_max=1.0
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
	)

	inset_thickness_center: bpy.props.FloatProperty(
	name="Inset Thickness Center",
	description="Center thickness.",
	default=0.25,
	soft_min=0.0,
	soft_max=0.99,
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
	)

	inset_center_depth: bpy.props.FloatProperty(
	name="Inset Center Depth",
	description="Inset center depth.",
	default=-0.15,
	soft_min=-1.0,
	soft_max=1.0,
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

	def execute(self, context):
		bpy.ops.mesh.inset(thickness=self.inset_thickness_edge, depth=0, use_individual=self.check_inset_individual)
		bpy.ops.mesh.inset(thickness=self.inset_thickness_center, depth=0)
		#bpy.ops.mesh.subdivide(quadcorner='INNERVERT') 'STRAIGHT_CUT' 'FAN' 'PATH'
		bpy.ops.mesh.subdivide(number_cuts=self.cuts, quadcorner='INNERVERT')
		bpy.ops.mesh.looptools_circle(custom_radius=False, fit='best', flatten=True, influence=100, lock_x=False, lock_y=False, lock_z=False, radius=1, regular=True)
		bpy.ops.mesh.dissolve_limited()
		if self.check_circle_depth:
			bpy.ops.mesh.inset(thickness=self.inset_circle_thickness, depth=self.inset_center_depth)
		else:
			bpy.ops.mesh.inset(thickness=self.inset_circle_thickness, depth=0)
		if self.check_remove_center:
			bpy.ops.mesh.delete(type='FACE')


		return {'FINISHED'}
		return {'FINISHED'}


# bpy.ops.mesh.subdivide(number_cuts=1, ngon=False, quadcorner='FAN')




#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":9, "mesh_select_mode_init":(False, False, True)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":False, "use_accurate":False})
