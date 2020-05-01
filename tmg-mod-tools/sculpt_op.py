import bpy


##################### Update Sculpt View Distance #############################
def sculpt_spacingDistance_changed(self, context):
	sculpt_spacingDistance = context.scene.sculpt_spacingDistance

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		if obj.type == 'MESH':
			bpy.context.scene.tool_settings.unified_paint_settings.use_locked_size = sculpt_spacingDistance
			bpy.data.brushes["SculptDraw"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Draw Sharp"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Clay"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Clay Strips"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Clay Thumb"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Layer"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Inflate/Deflate"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Blob"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Crease"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Smooth"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Flatten/Contrast"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Fill/Deepen"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Scrape/Peaks"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Pinch/Magnify"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Grab"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Elastic Deform"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Snake Hook"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Thumb"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Pose"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Nudge"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Rotate"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Simplify"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Multi-plane Scrape"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Slide Relax"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Cloth"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Simplify"].use_scene_spacing = sculpt_spacingDistance
			bpy.data.brushes["Mask"].use_scene_spacing = sculpt_spacingDistance

##################### Update Sculpt Face Sets #############################
def sculpt_faceSets_changed(self, context):
	sculpt_faceSets = context.scene.sculpt_faceSets

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		if obj.type == 'MESH':

			bpy.data.brushes["SculptDraw"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Draw Sharp"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Clay"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Clay Strips"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Clay Thumb"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Layer"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Inflate/Deflate"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Blob"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Crease"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Smooth"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Flatten/Contrast"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Fill/Deepen"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Scrape/Peaks"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Pinch/Magnify"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Grab"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Elastic Deform"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Snake Hook"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Thumb"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Pose"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Nudge"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Rotate"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Simplify"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Multi-plane Scrape"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Slide Relax"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Cloth"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Simplify"].use_automasking_face_sets = sculpt_faceSets
			bpy.data.brushes["Mask"].use_automasking_face_sets = sculpt_faceSets

##################### Update Sculpt Referance View Transparency #############################
def sculpt_referanceTransparency_changed(self, context):
	sculpt_referanceTransparency = context.scene.sculpt_referanceTransparency

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		types = obj.type

		if types == "EMPTY":
			if obj.use_empty_image_alpha == False:
				obj.use_empty_image_alpha = True
			obj.color[3] = sculpt_referanceTransparency


##################### Update Sculpt Referance Position #############################
def sculpt_referancePosition_changed(self, context):
	sculpt_referancePositionX = context.scene.sculpt_referancePositionX
	sculpt_referancePositionY = context.scene.sculpt_referancePositionY

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		types = obj.type

		if types == "EMPTY":
			obj.empty_image_offset[0] = sculpt_referancePositionX
			obj.empty_image_offset[1] = sculpt_referancePositionY


##################### Update Sculpt Referance Size #############################
def sculpt_referanceSize_changed(self, context):
	sculpt_referanceSize = context.scene.sculpt_referanceSize

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		types = obj.type

		if types == "EMPTY":
			obj.empty_display_size = sculpt_referanceSize


# obj.empty_display_size = 14.92

class Sculpt_Shape_Keys_Panel(bpy.types.Panel):
	bl_idname = 'SCULPT_PT_shape_keys_panel'
	bl_category = 'Edit'
	bl_label = 'TMG Shape Keys Panel'
	bl_context = "sculpt_mode"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_EEVEE', 'BLENDER_WORKBENCH'}

	@classmethod
	def poll(cls, context):
		engine = context.engine
		obj = context.object
		return (obj and obj.type in {'MESH', 'LATTICE', 'CURVE', 'SURFACE'} and (engine in cls.COMPAT_ENGINES))

	def draw(self, context):
		layout = self.layout

		ob = context.object
		key = ob.data.shape_keys
		kb = ob.active_shape_key

		props = self.layout.separator()
			# props = self.layout.label(text='TMG Objects')
		props = self.layout.operator('mesh.sculpt_ot_shape_key_set',
									text = 'Add Layer',
									icon = 'MESH_CUBE')
		props.mode = 0

		if bpy.context.active_object.active_shape_key_index > 0:

			props = self.layout.separator()
				# props = self.layout.label(text='TMG Objects')
			props = self.layout.operator('mesh.sculpt_ot_shape_key_set',
										text = 'Selected Layer',
										icon = 'MESH_CUBE')
			props.mode = 1

			props = self.layout.separator()
				# props = self.layout.label(text='TMG Objects')
			props = self.layout.operator('mesh.sculpt_ot_shape_key_set',
										text = 'All Timeline Frame',
										icon = 'MESH_CUBE')
			props.mode = 2

			props = self.layout.separator()
				# props = self.layout.label(text='TMG Objects')
			props = self.layout.operator('mesh.sculpt_ot_shape_key_set',
										text = 'Apply All Layers',
										icon = 'MESH_CUBE')
			props.mode = 3

			props = self.layout.separator()
				# props = self.layout.label(text='TMG Objects')
			props = self.layout.operator('mesh.sculpt_ot_shape_key_set',
										text = 'Solo Layer Toggle',
										icon = 'MESH_CUBE')
			props.mode = 4
			props.check_layer_mute = True

		enable_edit = ob.mode != 'EDIT'
		enable_edit_value = False

		if ob.show_only_shape_key is False:
			if enable_edit or (ob.type == 'MESH' and ob.use_shape_key_edit_mode):
				enable_edit_value = True

		row = layout.row()

		rows = 3
		if kb:
			rows = 5

		row.template_list("MESH_UL_shape_keys", "", key, "key_blocks", ob, "active_shape_key_index", rows=rows)

		col = row.column(align=True)

		col.operator("object.shape_key_add", icon='ADD', text="").from_mix = False
		col.operator("object.shape_key_remove", icon='REMOVE', text="").all = False

		col.separator()

		col.menu("MESH_MT_shape_key_context_menu", icon='DOWNARROW_HLT', text="")

		if kb:
			col.separator()

			sub = col.column(align=True)
			sub.operator("object.shape_key_move", icon='TRIA_UP', text="").type = 'UP'
			sub.operator("object.shape_key_move", icon='TRIA_DOWN', text="").type = 'DOWN'

			split = layout.split(factor=0.4)
			row = split.row()
			row.enabled = enable_edit
			row.prop(key, "use_relative")

			row = split.row()
			row.alignment = 'RIGHT'

			sub = row.row(align=True)
			sub.label()  # XXX, for alignment only
			subsub = sub.row(align=True)
			subsub.active = enable_edit_value
			subsub.prop(ob, "show_only_shape_key", text="")
			sub.prop(ob, "use_shape_key_edit_mode", text="")

			sub = row.row()
			if key.use_relative:
				sub.operator("object.shape_key_clear", icon='X', text="")
			else:
				sub.operator("object.shape_key_retime", icon='RECOVER_LAST', text="")

			layout.use_property_split = True
			if key.use_relative:
				if ob.active_shape_key_index != 0:
					row = layout.row()
					row.active = enable_edit_value
					row.prop(kb, "value")

					col = layout.column()
					sub.active = enable_edit_value
					sub = col.column(align=True)
					sub.prop(kb, "slider_min", text="Range Min")
					sub.prop(kb, "slider_max", text="Max")

					col.prop_search(kb, "vertex_group", ob, "vertex_groups", text="Vertex Group")
					col.prop_search(kb, "relative_key", key, "key_blocks", text="Relative To")

			else:
				layout.prop(kb, "interpolation")
				row = layout.column()
				row.active = enable_edit_value
				row.prop(key, "eval_time")





class Sculpt_OT_Shape_Key_Set(bpy.types.Operator):
	"""Sculpt Shape Key Set"""
	bl_idname = 'mesh.sculpt_ot_shape_key_set'
	bl_label = 'Add Shape Key'
	bl_description = 'Add Shape Keys for use in sculpt mode.'
	bl_options = {'REGISTER', 'UNDO'}

	check_layer_mute: bpy.props.BoolProperty(
	name="Solo Layer",
	description="Hides all other shape layers.",
	default=False
	)

	# size: bpy.props.FloatProperty(
	# name="Scale",
	# description="Cylinder scale.",
	# default=1,
	# min=0.01,
	# soft_max=10.0,
	# unit='LENGTH',
	# )

	# depth: bpy.props.FloatProperty(
	# name="Depth",
	# description="Cylinder depth.",
	# default=1,
	# min=0.01,
	# soft_max=10.0,
	# unit='LENGTH',
	# )

	mode: bpy.props.IntProperty(
	name="Mode",
	description="Adjust what mode to use when adding shape keys.",
	default=0,
	min=0,
	soft_max=4,
	)

	# cuts: bpy.props.IntProperty(
	# name="Face Subdivisions",
	# description="Subdivision loops.",
	# default=1,
	# min=0,
	# soft_max=10,
	# )

	# smoothness: bpy.props.FloatProperty(
	# name="To Sphere",
	# description="Smoothes subdivision loop cuts.",
	# default=0.0,
	# soft_min=0.0,
	# soft_max=1.0,
	# unit='LENGTH',
	# # step=.5,
	# )

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D'

	def invoke(self, context, event):
		# self.size = 0.5
		# self.depth = 1
		# self.vert_cuts = 8
		# self.cuts = 0
		# self.smoothness = 0
		return self.execute(context)

	def execute(self, context):

		mode = 0
		ob = bpy.context.active_object
		keys = 0

		if self.check_layer_mute == False:

			## Create shape layers
			if self.mode == 0: 
				bpy.ops.object.shape_key_add(from_mix=False)
			current_frame = bpy.context.active_object.active_shape_key_index
			keys = ob.data.shape_keys.key_blocks.keys()

			if self.mode == 0: 
				for shape in ob.data.shape_keys.key_blocks:
					if (current_frame==0):
						shape.name = 'Base Shape'
						shape.keyframe_insert("value",frame=0)
					elif (shape.name==ob.active_shape_key.name):
						shape.name = "Layer " + str(current_frame)
						shape.value=1.0
						shape.keyframe_insert("value",frame=ob.active_shape_key_index)
						bpy.data.scenes['Scene'].frame_current = ob.active_shape_key_index
			
			## Set active shape layer value 
			elif self.mode == 1:
				for shape in ob.data.shape_keys.key_blocks:
					if (shape.name==ob.active_shape_key.name):
						shape.keyframe_insert("value",frame=bpy.data.scenes['Scene'].frame_current)
						bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

			## Set all shape layer's value on current frame
			elif self.mode == 2:
				for shape in ob.data.shape_keys.key_blocks:
					shape.keyframe_insert("value",frame=bpy.data.scenes['Scene'].frame_current)
					bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

			## Apply all layers to shape
			elif self.mode == 3:
				for shape in ob.data.shape_keys.key_blocks:
					shape.keyframe_insert("value",frame=bpy.data.scenes['Scene'].frame_current)
					bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

				bpy.ops.object.shape_key_add(from_mix=True)
		
		## Mute all other layers
		else:
			current_frame = bpy.context.active_object.active_shape_key_index
			keys = ob.data.shape_keys.key_blocks.keys()
			for shape in ob.data.shape_keys.key_blocks:
				if (shape.name is not ob.active_shape_key.name):
					shape.mute = self.check_layer_mute
				elif (shape.name==ob.active_shape_key.name):
					shape.key_blocks[ob.active_shape_key.name].mute = False

		return {'FINISHED'}









# mode = 2
# ob = bpy.context.active_object
# keys = 0

# ## Create shape layers
# if mode == 0: 
#     bpy.ops.object.shape_key_add(from_mix=False)
# current_frame = bpy.context.active_object.active_shape_key_index
# keys = ob.data.shape_keys.key_blocks.keys()

# if mode == 0: 
#     for shape in ob.data.shape_keys.key_blocks:
#         if (current_frame==0):
#             shape.name = 'Base Shape'
#             shape.keyframe_insert("value",frame=0)
#         elif (shape.name==ob.active_shape_key.name):
#             shape.name = "Layer " + str(current_frame)
#             shape.value=1.0
#             shape.keyframe_insert("value",frame=ob.active_shape_key_index)
#             bpy.data.scenes['Scene'].frame_current = ob.active_shape_key_index
		
#         #shape.keyframe_insert("value",frame=ob.data.shape_keys.key_blocks.find(shape.name))
#         #bpy.context.scene.frame_set(ob.data.shape_keys.key_blocks.find(shape.name))
#         #bpy.context.scene.frame_current = ob.data.shape_keys.key_blocks.find(shape.name)
#         #print("Active: " + str(ob.data.shape_keys.key_blocks.find(shape.name)))
	   
# ## Set active shape layer value 
# if mode == 1:
#     for shape in ob.data.shape_keys.key_blocks:
#         if (shape.name==ob.active_shape_key.name):
#             #shape.keyframe_insert("value",frame=ob.active_shape_key_index)
#             shape.keyframe_insert("value",frame=bpy.data.scenes['Scene'].frame_current)
#             #bpy.data.scenes['Scene'].frame_current = ob.active_shape_key_index
#             bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

# ## Set all shape layer's value on current frame
# if mode == 2:
#     for shape in ob.data.shape_keys.key_blocks:
#         shape.keyframe_insert("value",frame=bpy.data.scenes['Scene'].frame_current)
#         bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

# print(ob.active_shape_key_index)
# print('frame: ' + str(bpy.data.scenes['Scene'].frame_current))