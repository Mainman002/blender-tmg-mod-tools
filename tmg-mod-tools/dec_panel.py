import bpy
from bpy.props import FloatProperty

class DEC_PT_Object_Panel(bpy.types.Panel):
	bl_idname = 'OBJECT_PT_dec_object_panel'
	bl_category = 'Edit'
	bl_label = 'TMG Mod Tools'
	bl_context = "objectmode"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'

	def draw(self, context):

		scene = context.scene
		obj = context.object

		sel_mode = context.tool_settings.mesh_select_mode

		axis_mode = context.scene.axis_mod
		solid_offset = context.scene.solidOffset
		#solid_thickness = context.scene.solid_thickness
		#bevel_width = context.scene.bevel_width
		#bevel_segments = context.scene.bevel_segments
		#angle_limit = context.scene.angle_limit
		#subsurf_vlevel = context.scene.subsurf_vlevel
		#subsurf_rlevel = context.scene.subsurf_rlevel

		check_view = context.scene.check_view
		check_modifiers = context.scene.check_modifiers
		check_modSettings = context.scene.check_modSettings
		check_mods = context.scene.check_mods
		check_adds = context.scene.check_adds
		check_splines = context.scene.check_splines

		modDrop_screw = context.scene.modDrop_screw
		modDrop_solid = context.scene.modDrop_solid
		modDrop_bevel = context.scene.modDrop_bevel
		modDrop_subsurf = context.scene.modDrop_subsurf
		modDrop_triangulate = context.scene.modDrop_triangulate
		modDrop_weightedNormals = context.scene.modDrop_weightedNormals

		mod_solid = context.scene.mod_solid
		mod_bevel = context.scene.mod_bevel
		mod_subsurf = context.scene.mod_subsurf
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		ui_viewMode = context.scene.ui_viewMode
		ui_wireMode = context.scene.ui_wireMode

		layout = self.layout

		#objmesh = obj.data

		layout.use_property_split = True
		layout.use_property_decorate = False  # No animation.

		#### Master Panel Layout Controllers ###############################

		Master_Col = layout.column(align=True)
		Master_Subcol = Master_Col.column()

		#### View Tab Panel Layout Controllers #########################

		View_Col = Master_Col.column(align=True)
		View_Subcol = View_Col.column()
		View_Row = View_Col.row()

		#for nr, ob in enumerate(bpy.context.selected_objects):
			#objmesh = ob.data
			#poly = len(objmesh.polygons)
			#View_Col.label(text="Poly" + str(len(objmesh.polygons)))
		#View_Col.label(text="Poly" + str(obj.triCount))
		#View_Col.prop(scene, "triCount", index=2, text="")

		#### View Tab  ############################################################################################################

		if check_view == False:
			View_Col.prop(scene, "check_view", text="View", icon="RIGHTARROW")
		else:
			View_Col.prop(scene, "check_view", text="View", icon="DOWNARROW_HLT")

			View_Col = Master_Col.column() ###### Box if needed for View Panel #############
			View_Subcol = View_Col.column(align=True)

			View_Col.use_property_split = True
			View_Flow = View_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			#colm = View_Flow.box()

			#View_Col = colm.row()
			#View_Col.label(text="Apply Modifiers")
			#View_Col.operator('wm.mod_apply_object_ot_operator', text='', icon='MODIFIER')

			#colm = View_Flow.box()

			obj = context.object
			if obj is not None:
				colm = View_Flow.box()
				View_Col = colm.row()
				View_Col.label(text="Name")
				View_Col.prop(scene, "objectName", index=2, text="")

				colm = View_Flow.box()

				View_Col = colm.row()
				View_Col.label(text="Display As")
				View_Col.prop(scene, "viewMode", index=2, text="")

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Distraction Free")
			View_Col.operator('wm.ui_distraction_free_ot_operator', text='', icon='RESTRICT_RENDER_OFF')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Wireframe")
			View_Col.operator('wm.ui_wireframe_ot_operator', text='', icon='SHADING_WIRE')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Texel Check")
			View_Col.operator('wm.ui_texel_check_ot_operator', text='', icon='UV_DATA')

		#### Modifiers Tab Panel Layout Controllers #########################

		Modifiers_Col = Master_Col.column(align=True)
		Modifiers_Subcol = Modifiers_Col.column()
		Modifiers_Row = Modifiers_Col.row()

		#### Modifiers Tab  ############################################################################################################

		if check_modifiers == False:
			Modifiers_Col.prop(scene, "check_modifiers", text="Modifiers", icon="RIGHTARROW")
		else:
			Modifiers_Col.prop(scene, "check_modifiers", text="Modifiers", icon="DOWNARROW_HLT")

			Modifiers_Col = Master_Col.box()  ###### Box if needed for Modifiers Panel #############

			if context.view_layer.objects.active:

				Modifiers_Col.use_property_split = True
				Modifiers_Flow2 = Modifiers_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

				Mod_ColM = Modifiers_Flow2.column()
				Mod_ColM.operator('wm.mod_apply_object_ot_operator', text='Apply Modifiers', icon="MODIFIER")

				Mod_ColM = Modifiers_Flow2.column()
				Mod_ColM.operator('wm.mod_object_ot_operator', text='Add Modifiers', icon="PRESET_NEW")

			Modifiers_Col.use_property_split = True
			Modifiers_Flow2 = Modifiers_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

			Mod_ColM = Modifiers_Flow2.column()

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Screw")
			Modifiers_Col.prop(scene, "mod_screw", text="", icon="MOD_SCREW")
			
			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Mirror")
			Modifiers_Col.prop(scene, "mod_mirror", text="", icon="MOD_MIRROR")

			Mod_ColM = Modifiers_Flow2.column()

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Subsurface")
			Modifiers_Col.prop(scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Solidify")
			Modifiers_Col.prop(scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

			Mod_ColM = Modifiers_Flow2.column()

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Bevel")
			Modifiers_Col.prop(scene, "mod_bevel", text="", icon="MOD_BEVEL")

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Triangulate")
			Modifiers_Col.prop(scene, "mod_triangulate", text="", icon="MOD_TRIANGULATE")

			Mod_ColM = Modifiers_Flow2.column()

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Normal Edit")
			Modifiers_Col.prop(scene, "mod_weightednormals", text="", icon="MOD_NORMALEDIT")

			Mod_ColM = Modifiers_Flow2.column()

		#### Modifier Settings Tab Panel Layout Controllers #########################

		ModSettings_Col = Master_Col.column(align=True)
		ModSettings_Subcol = ModSettings_Col.column()
		ModSettings_Row = ModSettings_Col.row()

		#### Modifier Settings Tab  ############################################################################################################

		if check_modSettings == False:
			ModSettings_Col.prop(scene, "check_modSettings", text="Mod Settings", icon="RIGHTARROW")
		else:
			ModSettings_Col.prop(scene, "check_modSettings", text="Mod Settings", icon="DOWNARROW_HLT")

			ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
			ModSettings_Subcol = ModSettings_Col.column(align=True)

			ModSettings_Row = ModSettings_Subcol.row() #angle_limit
			ModSettings_Row.label(text="Global Settings")

			ModSettings_Row = ModSettings_Subcol.box()

			#ModSettings_Row.use_property_split = True
			#ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			#colm = ModSettings_Flow.row()

			#ModSettings_Col = colm.row()
			#ModSettings_Col.label(text="Apply Modifiers")

			#ModSettings_Col = colm.row()
			#ModSettings_Col.operator('wm.mod_apply_object_ot_operator', text='', icon='MODIFIER')

			#colm = ModSettings_Flow.row()

			#ModSettings_Col = colm.row()
			#ModSettings_Col.label(text="Add Modifiers")

			#ModSettings_Col = colm.row()
			#ModSettings_Col.operator('wm.mod_object_ot_operator', text='', icon="PRESET_NEW")

			#ModSettings_Row = ModSettings_Subcol.box()

			ModSettings_Row.use_property_split = True
			ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			colm = ModSettings_Flow.column()

			ModSettings_Col = colm.row()
			ModSettings_Col.label(text="Mod Axis")

			colm = ModSettings_Flow.row()

			ModSettings_Col = colm.row()
			ModSettings_Col.prop(scene, "axis_mod", text="")

			colm = ModSettings_Flow.row()

			ModSettings_Col = colm.row()
			ModSettings_Col.label(text="Angle Limit")

			colm = ModSettings_Flow.column()

			if obj is not None:
				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "angleLimit", index=2, text="")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "solidDropToggle", index=2, text="", icon="MOD_SOLIDIFY")

				ModSettings_Col = colm.row() #angle_limit
				ModSettings_Col.label(text="Solidify")

				if  modDrop_solid == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidToggle", index=2, text="", icon="MOD_SOLIDIFY")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidEToggle", index=2, text="", icon="EDITMODE_HLT")

					ModSettings_Row = ModSettings_Subcol.box()

					ModSettings_Row.use_property_split = True
					ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Offset")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidOffset", index=2, text="", slider=True)

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Thickness")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidThickness", index=2, text="", slider=True)

			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

				ModSettings_Col = colm.row() #angle_limit
				ModSettings_Col.label(text="Solidify")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "subsurfDropToggle", index=2, text="", icon="MOD_SUBSURF")

				ModSettings_Col = colm.row() #angle_limit
				ModSettings_Col.label(text="Subsurf")

				if  modDrop_subsurf == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subsurfToggle", index=2, text="", icon="MOD_SUBSURF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subsurfRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subsurfVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subsurfEToggle", index=2, text="", icon="EDITMODE_HLT")

					ModSettings_Row = ModSettings_Subcol.box()

					ModSettings_Row.use_property_split = True
					ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="View")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subdivisionView", index=2, text="")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Render")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subdivisionRender", index=2, text="")

			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

				ModSettings_Col = colm.row() #angle_limit
				ModSettings_Col.label(text="Subsurf")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "bevelDropToggle", index=2, text="", icon="MOD_BEVEL")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Bevel")

				if modDrop_bevel == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelToggle", index=2, text="", icon="MOD_BEVEL")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelEToggle", index=2, text="", icon="EDITMODE_HLT")

					ModSettings_Row = ModSettings_Subcol.box()

					ModSettings_Row.use_property_split = True
					ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Segments")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelSegments", index=2, text="")

					colm = ModSettings_Flow.column()

					mod = obj.modifiers.get("Bevel")

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Width")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelWidth", index=2, text="", slider=True)

			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_bevel", text="", icon="MOD_BEVEL")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Bevel")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "triangulateDropToggle", index=2, text="", icon="MOD_TRIANGULATE")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Triangulate")

				if modDrop_triangulate == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "triangulateToggle", index=2, text="", icon="MOD_TRIANGULATE")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "triangulateRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "triangulateVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "triangulateEToggle", index=2, text="", icon="EDITMODE_HLT")
			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_triangulate", text="", icon="MOD_TRIANGULATE")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Triangulate")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "weightedNormalsDropToggle", index=2, text="", icon="MOD_NORMALEDIT")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Weighted Normals")

				if modDrop_weightedNormals == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "weightedNormalsToggle", index=2, text="", icon="MOD_NORMALEDIT")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "weightedNormalsRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "weightedNormalsVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "weightedNormalsEToggle", index=2, text="", icon="EDITMODE_HLT")
			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_weightednormals", text="", icon="MOD_TRIANGULATE")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Weighted Normals")

		#### Add Objects Tab Panel Layout Controllers #########################

		AddObjects_Col = Master_Col.column(align=True)
		AddObjects_SubCol = AddObjects_Col.column()
		AddObjects_Row = AddObjects_Col.row()

		#### Add Objects Tab  ############################################################################################################

		if check_adds == False:
			AddObjects_Col.prop(scene, "check_adds", text="Add Objects", icon="RIGHTARROW")
		else:
			AddObjects_Col.prop(scene, "check_adds", text="Add Objects", icon="DOWNARROW_HLT")

			View_Col = Master_Col.column() ###### Box if needed for View Panel #############
			View_Subcol = View_Col.column(align=True)

			View_Col.use_property_split = True
			View_Flow = View_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Subdivided Cube")
			View_Col.operator('mesh.add_ot_subd_cube', text='', icon='MESH_CUBE')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Subdivided Cylinder")
			View_Col.operator('mesh.add_ot_subd_cylinder', text='', icon='MESH_CYLINDER')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Plane")
			View_Col.operator('wm.add_ot_solid_plane_object', text='', icon='MESH_PLANE')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Circle")
			View_Col.operator('wm.add_ot_solid_circle_object', text='', icon='MESH_CIRCLE')

			colm = View_Flow.box()

			if axis_mode == "X": # Y

				View_Col = colm.row()
				View_Col.label(text="Arch")
				View_Col.operator('wm.add_ot_arch_object_x', text='', icon='SURFACE_NCURVE')

			elif axis_mode == "Y": # Y

				View_Col = colm.row()
				View_Col.label(text="Arch")
				View_Col.operator('wm.add_ot_arch_object_y', text='', icon='SURFACE_NCURVE')

				colm = View_Flow.box()

				View_Col = colm.row()
				View_Col.label(text="Pipe")
				View_Col.operator('wm.add_ot_pipe_line_object_y', text='', icon='OUTLINER_OB_CURVE')

			elif axis_mode == "Z": # Z

				View_Col = colm.row()
				View_Col.label(text="Arch")
				View_Col.operator('wm.add_ot_arch_object_z', text='', icon='SURFACE_NCURVE')

				colm = View_Flow.box()

				View_Col = colm.row()
				View_Col.label(text="Pipe")
				View_Col.operator('wm.add_ot_pipe_line_object_z', text='', icon='OUTLINER_OB_CURVE')

		#### Add Splines Tab Panel Layout Controllers #########################

		AddSplines_Col = Master_Col.column(align=True)
		AddSplines_SubCol = AddSplines_Col.column()
		AddSplines_Row = AddSplines_Col.row()

		#### Add Splines Tab  ############################################################################################################

		if check_splines == False:
			if axis_mode == "Y": # Y:
				AddSplines_Col.prop(scene, "check_splines", text="Add Splines", icon="RIGHTARROW")
		else:
			if axis_mode == "Y": # Y:
				AddSplines_Col.prop(scene, "check_splines", text="Add Splines", icon="DOWNARROW_HLT")

				AddSplines_Col = Master_Col.column() ###### Box if needed for Add Splines Panel #############
				AddSplines_SubCol = AddSplines_Col.column(align=True)

				AddSplines_Col.use_property_split = True
				AddSplines_Flow = AddSplines_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = AddSplines_Flow.box()

				AddSplines_Col = colm.row()
				AddSplines_Col.label(text="Basic Spline")
				AddSplines_Col.operator('wm.add_ot_basic_spline_y', text='', icon='CURVE_PATH')

				colm = AddSplines_Flow.box()

				AddSplines_Col = colm.row()
				AddSplines_Col.label(text="Smooth Spline")
				AddSplines_Col.operator('wm.add_ot_pipe_spline_y', text='', icon='CURVE_BEZCURVE')

				#AddSplines_Col = AddSplines_Flow.row()
				#AddSplines_Col.operator('wm.add_ot_spline_folow_y', text='Add Spline Follow Cube')





class DEC_PT_Edit_Panel(bpy.types.Panel):
	bl_idname = 'OBJECT_PT_dec_edit_panel'
	bl_category = 'Edit'
	bl_label = 'TMG Mod Tools'
	bl_context = "mesh_edit"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
 

	def draw(self, context):

		#obj = bpy.context.view_layer.objects.active
		sel_mode = context.tool_settings.mesh_select_mode

		scene = context.scene
		obj = context.object

		solid_offset = 1
		solid_thickness = 0.20

		check_view = context.scene.check_view
		check_modifiers = context.scene.check_modifiers
		check_modSettings = context.scene.check_modSettings
		check_mods = context.scene.check_mods
		check_adds = context.scene.check_adds
		check_splines = context.scene.check_splines
		check_decimations = context.scene.check_decimations
		check_tools = context.scene.check_tools

		check_inset_individual = context.scene.check_inset_individual
		check_inset_depth = context.scene.check_inset_depth
		check_inset_thickness = context.scene.check_inset_thickness

		modDrop_screw = context.scene.modDrop_screw
		modDrop_solid = context.scene.modDrop_solid
		modDrop_bevel = context.scene.modDrop_bevel
		modDrop_subsurf = context.scene.modDrop_subsurf
		modDrop_triangulate = context.scene.modDrop_triangulate
		modDrop_weightedNormals = context.scene.modDrop_weightedNormals

		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_bevel = context.scene.mod_bevel
		#bevel_segments = context.scene.bevel_segments
		mod_subsurf = context.scene.mod_subsurf
		subsurf_vlevel = 2
		subsurf_rlevel = 3
		mod_triangulate = context.scene.mod_triangulate
		mod_weightednormals = context.scene.mod_weightednormals

		ui_viewMode = context.scene.ui_viewMode
		ui_wireMode = context.scene.ui_wireMode
		#view_mod = context.scene.view_mod

		layout = self.layout

		layout.use_property_split = True
		layout.use_property_decorate = False  # No animation.

		#### Master Panel Layout Controllers ###############################

		Master_Col = layout.column(align=True)
		Master_Subcol = Master_Col.column()

		#### View Tab Panel Layout Controllers #########################

		View_Col = Master_Col.column(align=True)
		View_Subcol = View_Col.column()
		View_Row = View_Col.row()

		#### View Tab  ############################################################################################################

		if check_view == False:
			View_Col.prop(scene, "check_view", text="View", icon="RIGHTARROW")
		else:
			View_Col.prop(scene, "check_view", text="View", icon="DOWNARROW_HLT")

			View_Col = Master_Col.column() ###### Box if needed for View Panel #############
			View_Subcol = View_Col.column(align=True)

			View_Col.use_property_split = True
			View_Flow = View_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			#colm = View_Flow.box()

			#View_Col = colm.row()
			#View_Col.label(text="Apply Modifiers")
			#View_Col.operator('wm.mod_apply_object_ot_operator', text='', icon='MODIFIER')

			#colm = View_Flow.box()

			obj = context.object
			if obj is not None:
				colm = View_Flow.box()
				View_Col = colm.row()
				View_Col.label(text="Name")
				View_Col.prop(scene, "objectName", index=2, text="")

				colm = View_Flow.box()

				View_Col = colm.row()
				View_Col.label(text="Display As")
				View_Col.prop(scene, "viewMode", index=2, text="")

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Distraction Free")
			View_Col.operator('wm.ui_distraction_free_ot_operator', text='', icon='RESTRICT_RENDER_OFF')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Wireframe")
			View_Col.operator('wm.ui_wireframe_ot_operator', text='', icon='SHADING_WIRE')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Texel Check")
			View_Col.operator('wm.ui_texel_check_ot_operator', text='', icon='UV_DATA')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Flip Normals")
			View_Col.operator('wm.tool_ot_flip_normals_edit', text='', icon='NORMALS_FACE')

			colm = View_Flow.box()
			
			View_Col = colm.row()
			View_Col.label(text="Unwarp Update")
			View_Col.operator('wm.uv_margin_unwrap_ot_operator', text='', icon='NORMALS_FACE')


		#### Modifiers Tab Panel Layout Controllers #########################

		Modifiers_Col = Master_Col.column(align=True)
		Modifiers_Subcol = Modifiers_Col.column()
		Modifiers_Row = Modifiers_Col.row()

		#### Modifiers Tab  ############################################################################################################

		if check_modifiers == False:
			Modifiers_Col.prop(scene, "check_modifiers", text="Modifiers", icon="RIGHTARROW")
		else:
			Modifiers_Col.prop(scene, "check_modifiers", text="Modifiers", icon="DOWNARROW_HLT")

			Modifiers_Col = Master_Col.box()  ###### Box if needed for Modifiers Panel #############

			if context.view_layer.objects.active:

				Modifiers_Col.use_property_split = True
				Modifiers_Flow2 = Modifiers_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

				Mod_ColM = Modifiers_Flow2.column()
				Mod_ColM.operator('wm.mod_apply_object_ot_operator', text='Apply Modifiers', icon="MODIFIER")

				Mod_ColM = Modifiers_Flow2.column()
				Mod_ColM.operator('wm.mod_object_ot_operator', text='Add Modifiers', icon="PRESET_NEW")

			Modifiers_Col.use_property_split = True
			Modifiers_Flow2 = Modifiers_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

			Mod_ColM = Modifiers_Flow2.column()

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Screw")
			Modifiers_Col.prop(scene, "mod_screw", text="", icon="MOD_SCREW")
			
			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Mirror")
			Modifiers_Col.prop(scene, "mod_mirror", text="", icon="MOD_MIRROR")

			Mod_ColM = Modifiers_Flow2.column()

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Subsurface")
			Modifiers_Col.prop(scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Solidify")
			Modifiers_Col.prop(scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

			Mod_ColM = Modifiers_Flow2.column()

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Bevel")
			Modifiers_Col.prop(scene, "mod_bevel", text="", icon="MOD_BEVEL")

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Triangulate")
			Modifiers_Col.prop(scene, "mod_triangulate", text="", icon="MOD_TRIANGULATE")

			Mod_ColM = Modifiers_Flow2.column()

			Modifiers_Col = Mod_ColM.row()
			Modifiers_Col.label(text="Normal Edit")
			Modifiers_Col.prop(scene, "mod_weightednormals", text="", icon="MOD_NORMALEDIT")

			Mod_ColM = Modifiers_Flow2.column()

		#### Modifier Settings Tab Panel Layout Controllers #########################

		ModSettings_Col = Master_Col.column(align=True)
		ModSettings_Subcol = ModSettings_Col.column()
		ModSettings_Row = ModSettings_Col.row()

		#### Modifier Settings Tab  ############################################################################################################

		if check_modSettings == False:
			ModSettings_Col.prop(scene, "check_modSettings", text="Mod Settings", icon="RIGHTARROW")
		else:
			ModSettings_Col.prop(scene, "check_modSettings", text="Mod Settings", icon="DOWNARROW_HLT")

			ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
			ModSettings_Subcol = ModSettings_Col.column(align=True)

			ModSettings_Row = ModSettings_Subcol.row() #angle_limit
			ModSettings_Row.label(text="Global Settings")

			ModSettings_Row = ModSettings_Subcol.box()

			#ModSettings_Row.use_property_split = True
			#ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			#colm = ModSettings_Flow.row()

			#ModSettings_Col = colm.row()
			#ModSettings_Col.label(text="Apply Modifiers")

			#ModSettings_Col = colm.row()
			#ModSettings_Col.operator('wm.mod_apply_object_ot_operator', text='', icon='MODIFIER')

			#colm = ModSettings_Flow.row()

			#ModSettings_Col = colm.row()
			#ModSettings_Col.label(text="Add Modifiers")

			#ModSettings_Col = colm.row()
			#ModSettings_Col.operator('wm.mod_object_ot_operator', text='', icon="PRESET_NEW")

			#ModSettings_Row = ModSettings_Subcol.box()

			ModSettings_Row.use_property_split = True
			ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			colm = ModSettings_Flow.column()

			ModSettings_Col = colm.row()
			ModSettings_Col.label(text="Mod Axis")

			colm = ModSettings_Flow.row()

			ModSettings_Col = colm.row()
			ModSettings_Col.prop(scene, "axis_mod", text="")

			colm = ModSettings_Flow.row()

			ModSettings_Col = colm.row()
			ModSettings_Col.label(text="Angle Limit")

			colm = ModSettings_Flow.column()

			if obj is not None:
				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "angleLimit", index=2, text="")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "solidDropToggle", index=2, text="", icon="MOD_SOLIDIFY")

				ModSettings_Col = colm.row() #angle_limit
				ModSettings_Col.label(text="Solidify")

				if  modDrop_solid == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidToggle", index=2, text="", icon="MOD_SOLIDIFY")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidEToggle", index=2, text="", icon="EDITMODE_HLT")

					ModSettings_Row = ModSettings_Subcol.box()

					ModSettings_Row.use_property_split = True
					ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Offset")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidOffset", index=2, text="", slider=True)

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Thickness")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "solidThickness", index=2, text="", slider=True)

			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

				ModSettings_Col = colm.row() #angle_limit
				ModSettings_Col.label(text="Solidify")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "subsurfDropToggle", index=2, text="", icon="MOD_SUBSURF")

				ModSettings_Col = colm.row() #angle_limit
				ModSettings_Col.label(text="Subsurf")

				if  modDrop_subsurf == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subsurfToggle", index=2, text="", icon="MOD_SUBSURF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subsurfRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subsurfVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subsurfEToggle", index=2, text="", icon="EDITMODE_HLT")

					ModSettings_Row = ModSettings_Subcol.box()

					ModSettings_Row.use_property_split = True
					ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="View")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subdivisionView", index=2, text="")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Render")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "subdivisionRender", index=2, text="")

			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

				ModSettings_Col = colm.row() #angle_limit
				ModSettings_Col.label(text="Subsurf")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "bevelDropToggle", index=2, text="", icon="MOD_BEVEL")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Bevel")

				if modDrop_bevel == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelToggle", index=2, text="", icon="MOD_BEVEL")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelEToggle", index=2, text="", icon="EDITMODE_HLT")

					ModSettings_Row = ModSettings_Subcol.box()

					ModSettings_Row.use_property_split = True
					ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Segments")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelSegments", index=2, text="")

					colm = ModSettings_Flow.column()

					mod = obj.modifiers.get("Bevel")

					ModSettings_Col = colm.row()
					ModSettings_Col.label(text="Width")

					colm = ModSettings_Flow.column()

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "bevelWidth", index=2, text="", slider=True)

			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_bevel", text="", icon="MOD_BEVEL")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Bevel")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "triangulateDropToggle", index=2, text="", icon="MOD_TRIANGULATE")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Triangulate")

				if modDrop_triangulate == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "triangulateToggle", index=2, text="", icon="MOD_TRIANGULATE")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "triangulateRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "triangulateVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "triangulateEToggle", index=2, text="", icon="EDITMODE_HLT")
			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_triangulate", text="", icon="MOD_TRIANGULATE")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Triangulate")

			if  context.active_object is not None:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "weightedNormalsDropToggle", index=2, text="", icon="MOD_NORMALEDIT")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Weighted Normals")

				if modDrop_weightedNormals == True:

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "weightedNormalsToggle", index=2, text="", icon="MOD_NORMALEDIT")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "weightedNormalsRToggle", index=2, text="", icon="RESTRICT_RENDER_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "weightedNormalsVToggle", index=2, text="", icon="RESTRICT_VIEW_OFF")

					ModSettings_Col = colm.row()
					ModSettings_Col.prop(scene, "weightedNormalsEToggle", index=2, text="", icon="EDITMODE_HLT")
			else:
				ModSettings_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
				ModSettings_Subcol = ModSettings_Col.column(align=True)

				ModSettings_Row = ModSettings_Subcol.box()

				ModSettings_Row.use_property_split = True
				ModSettings_Flow = ModSettings_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = ModSettings_Flow.row()

				ModSettings_Col = colm.row()
				ModSettings_Col.prop(scene, "mod_weightednormals", text="", icon="MOD_TRIANGULATE")

				ModSettings_Col = colm.row()
				ModSettings_Col.label(text="Weighted Normals")

		#### Add Objects Tab  #############################################

		AddObjects_Col = Master_Col.column(align=True)
		AddObjects_SubCol = AddObjects_Col.column()
		AddObjects_Row = AddObjects_Col.row()

		#### Add Objects Tab  ############################################################################################################

		if check_adds == False:
			AddObjects_Col.prop(scene, "check_adds", text="Add Objects", icon="RIGHTARROW")
		else:
			AddObjects_Col.prop(scene, "check_adds", text="Add Objects", icon="DOWNARROW_HLT")

			View_Col = Master_Col.column() ###### Box if needed for View Panel #############
			View_Subcol = View_Col.column(align=True)

			View_Col.use_property_split = True
			View_Flow = View_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Plane")
			View_Col.operator('wm.add_ot_solid_plane_object', text='', icon='MESH_PLANE')

			colm = View_Flow.box()

			View_Col = colm.row()
			View_Col.label(text="Circle")
			View_Col.operator('wm.add_ot_solid_circle_object', text='', icon='MESH_CIRCLE')

			colm = View_Flow.box()

			if axis_mode == "X": # Y

				View_Col = colm.row()
				View_Col.label(text="Arch")
				View_Col.operator('wm.add_ot_arch_object_x', text='', icon='SURFACE_NCURVE')

			elif axis_mode == "Y": # Y

				View_Col = colm.row()
				View_Col.label(text="Arch")
				View_Col.operator('wm.add_ot_arch_object_y', text='', icon='SURFACE_NCURVE')

				colm = View_Flow.box()

				View_Col = colm.row()
				View_Col.label(text="Pipe")
				View_Col.operator('wm.add_ot_pipe_line_object_y', text='', icon='OUTLINER_OB_CURVE')

			elif axis_mode == "Z": # Z

				View_Col = colm.row()
				View_Col.label(text="Arch")
				View_Col.operator('wm.add_ot_arch_object_z', text='', icon='SURFACE_NCURVE')

				colm = View_Flow.box()

				View_Col = colm.row()
				View_Col.label(text="Pipe")
				View_Col.operator('wm.add_ot_pipe_line_object_z', text='', icon='OUTLINER_OB_CURVE')

		#### Add Splines Tab  ######################################

		AddSplines_Col = Master_Col.column(align=True)
		AddSplines_SubCol = AddSplines_Col.column()
		AddSplines_Row = AddSplines_Col.row()

		#### Add Splines Tab  ############################################################################################################

		if check_splines == False:
			if axis_mode == "Y": # Y:
				AddSplines_Col.prop(scene, "check_splines", text="Add Splines", icon="RIGHTARROW")
		else:
			if axis_mode == "Y": # Y:
				AddSplines_Col.prop(scene, "check_splines", text="Add Splines", icon="DOWNARROW_HLT")

				AddSplines_Col = Master_Col.column() ###### Box if needed for Add Splines Panel #############
				AddSplines_SubCol = AddSplines_Col.column(align=True)

				AddSplines_Col.use_property_split = True
				AddSplines_Flow = AddSplines_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

				colm = AddSplines_Flow.box()

				AddSplines_Col = colm.row()
				AddSplines_Col.label(text="Basic Spline")
				AddSplines_Col.operator('wm.add_ot_basic_spline_y', text='', icon='CURVE_PATH')

				colm = AddSplines_Flow.box()

				AddSplines_Col = colm.row()
				AddSplines_Col.label(text="Smooth Spline")
				AddSplines_Col.operator('wm.add_ot_pipe_spline_y', text='', icon='CURVE_BEZCURVE')

		#### Decimate Tools Tab  ######################################

		DecTools_Col = Master_Col.column(align=True)
		DecTools_SubCol = DecTools_Col.column()
		DecTools_Row = DecTools_Col.row()

		#### Decimate Tools Tab  ##########################################################################################################

		if check_decimations == False:
			DecTools_Col.prop(scene, "check_decimations", text="Decimate", icon="RIGHTARROW")
		else:
			DecTools_Col.prop(scene, "check_decimations", text="Decimate", icon="DOWNARROW_HLT")

			DecTools_Col = Master_Col.column() ###### Box if needed for Add Splines Panel #############
			DecTools_SubCol = DecTools_Col.column(align=True)

			DecTools_Col.use_property_split = True
			DecTools_Flow = DecTools_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			if sel_mode[1]: # edge

				colm = DecTools_Flow.box()

				DecTools_Col = colm.row()
				DecTools_Col.label(text="Verts")
				DecTools_Col.operator('wm.dec_verts_ot_operator', text='', icon='VERTEXSEL')

				colm = DecTools_Flow.box()

				DecTools_Col = colm.row()
				DecTools_Col.label(text="Checker Verts")
				DecTools_Col.operator('wm.dec_verts_random_ot_operator', text='', icon='STICKY_UVS_VERT')

				colm = DecTools_Flow.box()

				DecTools_Col = colm.row()
				DecTools_Col.label(text="Edges")
				DecTools_Col.operator('wm.dec_edge_ot_operator', text='', icon='EDGESEL')

				colm = DecTools_Flow.box()

				DecTools_Col = colm.row()
				DecTools_Col.label(text="Checker Edges")
				DecTools_Col.operator('wm.dec_edge_random_ot_operator', text='', icon='SNAP_EDGE')

			elif sel_mode[0]: # vertex
				colm = DecTools_Flow.box()

				DecTools_Col = colm.row()
				DecTools_Col.label(text="Verts")
				DecTools_Col.operator('wm.dec_verts_ot_operator', text='', icon='VERTEXSEL')


		#### Tools Tab  ######################################

		Tools_Col = Master_Col.column(align=True)
		Tools_SubCol = Tools_Col.column()
		Tools_Row = Tools_Col.row()

		#### Tools Tab  ##########################################################################################################

		if check_tools == False:
			Tools_Col.prop(scene, "check_tools", text="Tools", icon="RIGHTARROW")
		else:
			Tools_Col.prop(scene, "check_tools", text="Tools", icon="DOWNARROW_HLT")

			Tools_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
			Tools_Subcol = Tools_Col.column(align=True)

			Tools_Row = Tools_Subcol.row() #angle_limit
			Tools_Row.label(text="Inset Settings")

			Tools_Row = Tools_Subcol.column()

			# Tools_Row.use_property_split = True
			# Tools_Flow = Tools_Row.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

			Tools_Apply_Col = Master_Col.box() ###### Box if needed for Settings Panel #############
			Tools_Apply_SubCol = Tools_Apply_Col.column(align=True)

			Tools_Apply_Col.use_property_split = True
			Tools_Apply_Flow = Tools_Apply_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

			colm = Tools_Apply_Flow.column()

			Tools_Apply_Col = colm.row()
			Tools_Apply_Col.operator('wm.tool_ot_remove_doubles_edit', text='Remove Doubles')

			colm = Tools_Apply_Flow.column()

			Tools_Apply_Col = colm.row()
			Tools_Apply_Col.operator('wm.tool_ot_select_interior_faces_edit', text='Select Interior')

			colm = Tools_Apply_Flow.column()

			Tools_Apply_Col = colm.row()
			Tools_Apply_Col.operator('wm.tool_ot_inset_edit', text='Inset Selected')

			colm = Tools_Apply_Flow.column()

			Tools_Apply_Col = colm.row()
			Tools_Apply_Col.operator('wm.tool_ot_bevel_edge_edit', text='Bevel Selected')

			colm = Tools_Apply_Flow.column()

			Tools_Apply_Col = colm.row()
			Tools_Apply_Col.operator('wm.tool_ot_mesh_face_to_circle_edit', text='Face to Circle')

			colm = Tools_Apply_Flow.column()

			Tools_Apply_Col = colm.row()
			Tools_Apply_Col.operator('wm.tool_ot_knurl_face_edit', text='Knurl Face')

			colm = Tools_Apply_Flow.column()
			
			Tools_Apply_Col = colm.row()
			Tools_Apply_Col.operator('wm.tool_ot_slotted_grate_edit', text='Slotted Grate')

			colm = Tools_Apply_Flow.column()

			Tools_Apply_Col = colm.row()
			Tools_Apply_Col.operator('wm.tool_ot_wrinkle_face_edit', text='Wrinkle Selected')

			if sel_mode[1] or sel_mode[2]: # edge

				colm = Tools_Apply_Flow.column()

				Tools_Apply_Col = colm.row()
				Tools_Apply_Col.operator('wm.tool_ot_edge_slide_edit', text='Edge Slide')

















class Dec_Object_Modifier_Panel(bpy.types.Panel):
	bl_idname = 'OBJECT_PT_dec_object_modifier_panel'
	bl_category = 'Edit'
	bl_label = 'TMG Modifiers Panel'
	bl_context = "objectmode"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
 

	@classmethod
	def poll(cls, context):
		ob = context.object
		return ob and ob.type != 'GPENCIL'

	def draw(self, context):



		obj = bpy.context.view_layer.objects.active
		sel_mode = context.tool_settings.mesh_select_mode

		solid_offset = context.scene.solidOffset
		#solid_thickness = context.scene.solid_thickness
		#bevel_width = context.scene.bevel_width
		#bevel_width = context.object.modifiers["Bevel"].width
		#bevel_width = context.object.modifiers["Bevel"].width

		check_view = context.scene.check_view
		check_modifiers = context.scene.check_modifiers
		check_mods = context.scene.check_mods
		check_adds = context.scene.check_adds
		check_splines = context.scene.check_splines

		axis_mode = context.scene.axis_mod
		mod_solid = context.scene.mod_solid
		mod_bevel = context.scene.mod_bevel
		mod_subsurf = context.scene.mod_subsurf
		#subsurf_vlevel = context.scene.subsurf_vlevel
		#subsurf_rlevel = context.scene.subsurf_rlevel



		layout = self.layout

		ob = context.object

		layout.operator_menu_enum("object.modifier_add", "type")

		for md in ob.modifiers:
			box = layout.template_modifier(md)
			if box:
				# match enum type to our functions, avoids a lookup table.
				getattr(self, md.type)(box, ob, md)

	# the mt.type enum is (ab)used for a lookup on function names
	# ...to avoid lengthy if statements
	# so each type must have a function here.


	def ARMATURE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")
		col.prop(md, "use_deform_preserve_volume")

		col = split.column()
		col.label(text="Bind To:")
		col.prop(md, "use_vertex_groups", text="Vertex Groups")
		col.prop(md, "use_bone_envelopes", text="Bone Envelopes")

		layout.separator()

		split = layout.split()

		row = split.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = bool(md.vertex_group)
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		split.prop(md, "use_multi_modifier")

	def ARRAY(self, layout, _ob, md):
		layout.prop(md, "fit_type")

		if md.fit_type == 'FIXED_COUNT':
			layout.prop(md, "count")
		elif md.fit_type == 'FIT_LENGTH':
			layout.prop(md, "fit_length")
		elif md.fit_type == 'FIT_CURVE':
			layout.prop(md, "curve")

		layout.separator()

		split = layout.split()

		col = split.column()
		col.prop(md, "use_constant_offset")
		sub = col.column()
		sub.active = md.use_constant_offset
		sub.prop(md, "constant_offset_displace", text="")

		col.separator()

		col.prop(md, "use_merge_vertices", text="Merge")
		sub = col.column()
		sub.active = md.use_merge_vertices
		sub.prop(md, "use_merge_vertices_cap", text="First Last")
		sub.prop(md, "merge_threshold", text="Distance")

		col = split.column()
		col.prop(md, "use_relative_offset")
		sub = col.column()
		sub.active = md.use_relative_offset
		sub.prop(md, "relative_offset_displace", text="")

		col.separator()

		col.prop(md, "use_object_offset")
		sub = col.column()
		sub.active = md.use_object_offset
		sub.prop(md, "offset_object", text="")

		row = layout.row()
		split = row.split()
		col = split.column()
		col.label(text="UVs:")
		sub = col.column(align=True)
		sub.prop(md, "offset_u")
		sub.prop(md, "offset_v")
		layout.separator()

		layout.prop(md, "start_cap")
		layout.prop(md, "end_cap")

	def BEVEL(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		if md.offset_type == 'PERCENT':
			col.prop(md, "width_pct")
		else:
			col.prop(md, "width")
		col.prop(md, "segments")
		col.prop(md, "profile")
		col.prop(md, "material")

		col = split.column()
		col.prop(md, "use_only_vertices")
		col.prop(md, "use_clamp_overlap")
		col.prop(md, "loop_slide")
		col.prop(md, "mark_seam")
		col.prop(md, "mark_sharp")
		col.prop(md, "harden_normals")

		layout.label(text="Limit Method:")
		layout.row().prop(md, "limit_method", expand=True)
		if md.limit_method == 'ANGLE':
			layout.prop(md, "angle_limit")
		elif md.limit_method == 'VGROUP':
			layout.label(text="Vertex Group:")
			layout.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		layout.label(text="Width Method:")
		layout.row().prop(md, "offset_type", expand=True)

		layout.label(text="Set Face Strength Mode")
		layout.row().prop(md, "face_strength_mode", expand=True)

		layout.label(text="Miter Patterns")
		layout.row().prop(md, "miter_outer")
		layout.row().prop(md, "miter_inner")
		layout.row().prop(md, "spread")

	def BOOLEAN(self, layout, _ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Operation:")
		col.prop(md, "operation", text="")

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")

		layout.prop(md, "double_threshold")

		if bpy.app.debug:
			layout.prop(md, "debug_options")

	def BUILD(self, layout, _ob, md):
		split = layout.split()

		col = split.column()
		col.prop(md, "frame_start")
		col.prop(md, "frame_duration")
		col.prop(md, "use_reverse")

		col = split.column()
		col.prop(md, "use_random_order")
		sub = col.column()
		sub.active = md.use_random_order
		sub.prop(md, "seed")

	def MESH_CACHE(self, layout, _ob, md):
		layout.prop(md, "cache_format")
		layout.prop(md, "filepath")

		if md.cache_format == 'ABC':
			layout.prop(md, "sub_object")

		layout.label(text="Evaluation:")
		layout.prop(md, "factor", slider=True)
		layout.prop(md, "deform_mode")
		layout.prop(md, "interpolation")

		layout.label(text="Time Mapping:")

		row = layout.row()
		row.prop(md, "time_mode", expand=True)
		row = layout.row()
		row.prop(md, "play_mode", expand=True)
		if md.play_mode == 'SCENE':
			layout.prop(md, "frame_start")
			layout.prop(md, "frame_scale")
		else:
			time_mode = md.time_mode
			if time_mode == 'FRAME':
				layout.prop(md, "eval_frame")
			elif time_mode == 'TIME':
				layout.prop(md, "eval_time")
			elif time_mode == 'FACTOR':
				layout.prop(md, "eval_factor")

		layout.label(text="Axis Mapping:")
		split = layout.split(factor=0.5, align=True)
		split.alert = (md.forward_axis[-1] == md.up_axis[-1])
		split.label(text="Forward/Up Axis:")
		split.prop(md, "forward_axis", text="")
		split.prop(md, "up_axis", text="")
		split = layout.split(factor=0.5)
		split.label(text="Flip Axis:")
		row = split.row()
		row.prop(md, "flip_axis")

	def MESH_SEQUENCE_CACHE(self, layout, ob, md):
		layout.label(text="Cache File Properties:")
		box = layout.box()
		box.template_cache_file(md, "cache_file")

		cache_file = md.cache_file

		layout.label(text="Modifier Properties:")
		box = layout.box()

		if cache_file is not None:
			box.prop_search(md, "object_path", cache_file, "object_paths")

		if ob.type == 'MESH':
			box.row().prop(md, "read_data")

	def CAST(self, layout, ob, md):
		split = layout.split(factor=0.25)

		split.label(text="Cast Type:")
		split.prop(md, "cast_type", text="")

		split = layout.split(factor=0.25)

		col = split.column()
		col.prop(md, "use_x")
		col.prop(md, "use_y")
		col.prop(md, "use_z")

		col = split.column()
		col.prop(md, "factor")
		col.prop(md, "radius")
		col.prop(md, "size")
		col.prop(md, "use_radius_as_size")

		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		col = split.column()
		col.label(text="Control Object:")
		col.prop(md, "object", text="")
		if md.object:
			col.prop(md, "use_transform")

	def CLOTH(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def COLLISION(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def CURVE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")
		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		layout.label(text="Deformation Axis:")
		layout.row().prop(md, "deform_axis", expand=True)

	def DECIMATE(self, layout, ob, md):
		decimate_type = md.decimate_type

		row = layout.row()
		row.prop(md, "decimate_type", expand=True)

		if decimate_type == 'COLLAPSE':
			has_vgroup = bool(md.vertex_group)
			layout.prop(md, "ratio")

			split = layout.split()

			col = split.column()
			row = col.row(align=True)
			row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
			row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

			layout_info = col

			col = split.column()
			row = col.row()
			row.active = has_vgroup
			row.prop(md, "vertex_group_factor")

			col.prop(md, "use_collapse_triangulate")
			row = col.split(factor=0.75)
			row.prop(md, "use_symmetry")
			row.prop(md, "symmetry_axis", text="")

		elif decimate_type == 'UNSUBDIV':
			layout.prop(md, "iterations")
			layout_info = layout
		else:  # decimate_type == 'DISSOLVE':
			layout.prop(md, "angle_limit")
			layout.prop(md, "use_dissolve_boundaries")
			layout.label(text="Delimit:")
			row = layout.row()
			row.prop(md, "delimit")
			layout_info = layout

		layout_info.label(
			text=iface_("Face Count: {:,}".format(md.face_count)),
			translate=False,
		)

	def DISPLACE(self, layout, ob, md):
		has_texture = (md.texture is not None)

		col = layout.column(align=True)
		col.label(text="Texture:")
		col.template_ID(md, "texture", new="texture.new")

		split = layout.split()

		col = split.column(align=True)
		col.label(text="Direction:")
		col.prop(md, "direction", text="")
		if md.direction in {'X', 'Y', 'Z', 'RGB_TO_XYZ'}:
			col.label(text="Space:")
			col.prop(md, "space", text="")
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col = split.column(align=True)
		col.active = has_texture
		col.label(text="Texture Coordinates:")
		col.prop(md, "texture_coords", text="")
		if md.texture_coords == 'OBJECT':
			col.label(text="Object:")
			col.prop(md, "texture_coords_object", text="")
		elif md.texture_coords == 'UV' and ob.type == 'MESH':
			col.label(text="UV Map:")
			col.prop_search(md, "uv_layer", ob.data, "uv_layers", text="")

		layout.separator()

		row = layout.row()
		row.prop(md, "mid_level")
		row.prop(md, "strength")

	def DYNAMIC_PAINT(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def EDGE_SPLIT(self, layout, _ob, md):
		split = layout.split()

		col = split.column()
		col.prop(md, "use_edge_angle", text="Edge Angle")
		sub = col.column()
		sub.active = md.use_edge_angle
		sub.prop(md, "split_angle")

		split.prop(md, "use_edge_sharp", text="Sharp Edges")

	def EXPLODE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = col.column()
		sub.active = bool(md.vertex_group)
		sub.prop(md, "protect")
		col.label(text="Particle UV")
		col.prop_search(md, "particle_uv", ob.data, "uv_layers", text="")

		col = split.column()
		col.prop(md, "use_edge_cut")
		col.prop(md, "show_unborn")
		col.prop(md, "show_alive")
		col.prop(md, "show_dead")
		col.prop(md, "use_size")

		layout.operator("object.explode_refresh", text="Refresh")

	def FLUID_SIMULATION(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def HOOK(self, layout, ob, md):
		use_falloff = (md.falloff_type != 'NONE')
		split = layout.split()

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")
		if md.object and md.object.type == 'ARMATURE':
			col.label(text="Bone:")
			col.prop_search(md, "subtarget", md.object.data, "bones", text="")
		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		layout.separator()

		row = layout.row(align=True)
		if use_falloff:
			row.prop(md, "falloff_radius")
		row.prop(md, "strength", slider=True)
		layout.prop(md, "falloff_type")

		col = layout.column()
		if use_falloff:
			if md.falloff_type == 'CURVE':
				col.template_curve_mapping(md, "falloff_curve")

		split = layout.split()

		col = split.column()
		col.prop(md, "use_falloff_uniform")

		if ob.mode == 'EDIT':
			row = col.row(align=True)
			row.operator("object.hook_reset", text="Reset")
			row.operator("object.hook_recenter", text="Recenter")

			row = layout.row(align=True)
			row.operator("object.hook_select", text="Select")
			row.operator("object.hook_assign", text="Assign")

	def LAPLACIANDEFORM(self, layout, ob, md):
		is_bind = md.is_bind

		layout.prop(md, "iterations")

		row = layout.row()
		row.active = not is_bind
		row.label(text="Anchors Vertex Group:")

		row = layout.row()
		row.enabled = not is_bind
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		layout.separator()

		row = layout.row()
		row.enabled = bool(md.vertex_group)
		row.operator("object.laplaciandeform_bind", text="Unbind" if is_bind else "Bind")

	def LAPLACIANSMOOTH(self, layout, ob, md):
		layout.prop(md, "iterations")

		split = layout.split(factor=0.25)

		col = split.column()
		col.label(text="Axis:")
		col.prop(md, "use_x")
		col.prop(md, "use_y")
		col.prop(md, "use_z")

		col = split.column()
		col.label(text="Lambda:")
		col.prop(md, "lambda_factor", text="Factor")
		col.prop(md, "lambda_border", text="Border")

		col.separator()
		col.prop(md, "use_volume_preserve")
		col.prop(md, "use_normalized")

		layout.label(text="Vertex Group:")
		layout.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

	def LATTICE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		layout.separator()
		layout.prop(md, "strength", slider=True)

	def MASK(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Mode:")
		col.prop(md, "mode", text="")

		col = split.column()
		if md.mode == 'ARMATURE':
			col.label(text="Armature:")
			row = col.row(align=True)
			row.prop(md, "armature", text="")
			sub = row.row(align=True)
			sub.active = (md.armature is not None)
			sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
		elif md.mode == 'VERTEX_GROUP':
			col.label(text="Vertex Group:")
			row = col.row(align=True)
			row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
			sub = row.row(align=True)
			sub.active = bool(md.vertex_group)
			sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		col = layout.column()
		col.prop(md, "threshold")

	def MESH_DEFORM(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.enabled = not md.is_bound
		col.label(text="Object:")
		col.prop(md, "object", text="")

		col = split.column()
		col.label(text="Vertex Group:")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = bool(md.vertex_group)
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		layout.separator()
		row = layout.row()
		row.enabled = not md.is_bound
		row.prop(md, "precision")
		row.prop(md, "use_dynamic_bind")

		layout.separator()
		if md.is_bound:
			layout.operator("object.meshdeform_bind", text="Unbind")
		else:
			layout.operator("object.meshdeform_bind", text="Bind")

	def MIRROR(self, layout, _ob, md):
		axis_text = "XYZ"
		split = layout.split(factor=0.33)

		col = split.column()
		col.label(text="Axis:")
		for i, text in enumerate(axis_text):
			col.prop(md, "use_axis", text=text, index=i)

		col = split.column()
		col.label(text="Bisect:")
		for i, text in enumerate(axis_text):
			colsub = col.column()
			colsub.prop(md, "use_bisect_axis", text=text, index=i)
			colsub.active = md.use_axis[i]

		col = split.column()
		col.label(text="Flip:")
		for i, text in enumerate(axis_text):
			colsub = col.column()
			colsub.prop(md, "use_bisect_flip_axis", text=text, index=i)
			colsub.active = md.use_axis[i] and md.use_bisect_axis[i]

		layout.separator()

		col = layout.column()
		col.label(text="Mirror Object:")
		col.prop(md, "mirror_object", text="")

		layout.separator()

		col = layout.column()
		col.label(text="Options:")

		row = layout.row()
		row.prop(md, "use_mirror_vertex_groups", text="Vertex Groups")
		row.prop(md, "use_clip", text="Clipping")
		row = layout.row()
		row.prop(md, "use_mirror_merge", text="Merge")

		col = layout.column()
		if md.use_mirror_merge is True:
			col.prop(md, "merge_threshold")

		layout.separator()
		col = layout.column()

		col.label(text="Textures:")
		row = layout.row()
		row.prop(md, "use_mirror_u", text="Flip U")
		row.prop(md, "use_mirror_v", text="Flip V")

		col = layout.column(align=True)

		if md.use_mirror_u:
			col.prop(md, "mirror_offset_u")

		if md.use_mirror_v:
			col.prop(md, "mirror_offset_v")

		col = layout.column(align=True)
		col.prop(md, "offset_u")
		col.prop(md, "offset_v")

	def MULTIRES(self, layout, ob, md):
		layout.row().prop(md, "subdivision_type", expand=True)

		split = layout.split()
		col = split.column()
		col.prop(md, "levels", text="Preview")
		col.prop(md, "sculpt_levels", text="Sculpt")
		col.prop(md, "render_levels", text="Render")
		col.prop(md, "quality")

		col = split.column()

		col.enabled = ob.mode != 'EDIT'
		col.operator("object.multires_subdivide", text="Subdivide")
		col.operator("object.multires_higher_levels_delete", text="Delete Higher")
		col.operator("object.multires_reshape", text="Reshape")
		col.operator("object.multires_base_apply", text="Apply Base")
		col.prop(md, "uv_smooth", text="")
		col.prop(md, "show_only_control_edges")
		col.prop(md, "use_creases")

		layout.separator()

		col = layout.column()
		row = col.row()
		if md.is_external:
			row.operator("object.multires_external_pack", text="Pack External")
			row.label()
			row = col.row()
			row.prop(md, "filepath", text="")
		else:
			row.operator("object.multires_external_save", text="Save External...")
			row.label()

	def OCEAN(self, layout, _ob, md):
		if not bpy.app.build_options.mod_oceansim:
			layout.label(text="Built without OceanSim modifier")
			return

		layout.prop(md, "geometry_mode")

		if md.geometry_mode == 'GENERATE':
			row = layout.row()
			row.prop(md, "repeat_x")
			row.prop(md, "repeat_y")

		layout.separator()

		split = layout.split()

		col = split.column()
		col.prop(md, "time")
		col.prop(md, "depth")
		col.prop(md, "random_seed")

		col = split.column()
		col.prop(md, "resolution")
		col.prop(md, "size")
		col.prop(md, "spatial_size")

		layout.label(text="Waves:")

		split = layout.split()

		col = split.column()
		col.prop(md, "choppiness")
		col.prop(md, "wave_scale", text="Scale")
		col.prop(md, "wave_scale_min")
		col.prop(md, "wind_velocity")

		col = split.column()
		col.prop(md, "wave_alignment", text="Alignment")
		sub = col.column()
		sub.active = (md.wave_alignment > 0.0)
		sub.prop(md, "wave_direction", text="Direction")
		sub.prop(md, "damping")

		layout.separator()

		layout.prop(md, "use_normals")

		split = layout.split()

		col = split.column()
		col.prop(md, "use_foam")
		sub = col.row()
		sub.active = md.use_foam
		sub.prop(md, "foam_coverage", text="Coverage")

		col = split.column()
		col.active = md.use_foam
		col.label(text="Foam Data Layer Name:")
		col.prop(md, "foam_layer_name", text="")

		layout.separator()

		if md.is_cached:
			layout.operator("object.ocean_bake", text="Delete Bake").free = True
		else:
			layout.operator("object.ocean_bake").free = False

		split = layout.split()
		split.enabled = not md.is_cached

		col = split.column(align=True)
		col.prop(md, "frame_start", text="Start")
		col.prop(md, "frame_end", text="End")

		col = split.column(align=True)
		col.label(text="Cache path:")
		col.prop(md, "filepath", text="")

		split = layout.split()
		split.enabled = not md.is_cached

		col = split.column()
		col.active = md.use_foam
		col.prop(md, "bake_foam_fade")

		col = split.column()

	def PARTICLE_INSTANCE(self, layout, ob, md):
		layout.prop(md, "object")
		if md.object:
			layout.prop_search(md, "particle_system", md.object, "particle_systems", text="Particle System")
		else:
			layout.prop(md, "particle_system_index", text="Particle System")

		split = layout.split()
		col = split.column()
		col.label(text="Create From:")
		layout.prop(md, "space", text="")
		col.prop(md, "use_normal")
		col.prop(md, "use_children")
		col.prop(md, "use_size")

		col = split.column()
		col.label(text="Show Particles When:")
		col.prop(md, "show_alive")
		col.prop(md, "show_unborn")
		col.prop(md, "show_dead")

		row = layout.row(align=True)
		row.prop(md, "particle_amount", text="Amount")
		row.prop(md, "particle_offset", text="Offset")

		row = layout.row(align=True)
		row.prop(md, "axis", expand=True)

		layout.separator()

		layout.prop(md, "use_path", text="Create Along Paths")

		col = layout.column()
		col.active = md.use_path
		col.prop(md, "use_preserve_shape")

		row = col.row(align=True)
		row.prop(md, "position", slider=True)
		row.prop(md, "random_position", text="Random", slider=True)
		row = col.row(align=True)
		row.prop(md, "rotation", slider=True)
		row.prop(md, "random_rotation", text="Random", slider=True)

		layout.separator()

		col = layout.column()
		col.prop_search(md, "index_layer_name", ob.data, "vertex_colors", text="Index Layer")
		col.prop_search(md, "value_layer_name", ob.data, "vertex_colors", text="Value Layer")

	def PARTICLE_SYSTEM(self, layout, _ob, _md):
		layout.label(text="Settings can be found inside the Particle context")

	def SCREW(self, layout, _ob, md):
		split = layout.split()

		col = split.column()
		col.prop(md, "axis")
		col.prop(md, "object", text="AxisOb")
		col.prop(md, "angle")
		col.prop(md, "steps")
		col.prop(md, "render_steps")
		col.prop(md, "use_smooth_shade")
		col.prop(md, "use_merge_vertices")
		sub = col.column()
		sub.active = md.use_merge_vertices
		sub.prop(md, "merge_threshold")

		col = split.column()
		row = col.row()
		row.active = (md.object is None or md.use_object_screw_offset is False)
		row.prop(md, "screw_offset")
		row = col.row()
		row.active = (md.object is not None)
		row.prop(md, "use_object_screw_offset")
		col.prop(md, "use_normal_calculate")
		col.prop(md, "use_normal_flip")
		col.prop(md, "iterations")
		col.prop(md, "use_stretch_u")
		col.prop(md, "use_stretch_v")

	def SHRINKWRAP(self, layout, ob, md):
		split = layout.split()
		col = split.column()
		col.label(text="Target:")
		col.prop(md, "target", text="")
		col = split.column()
		col.label(text="Vertex Group:")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		split = layout.split()

		col = split.column()
		col.prop(md, "offset")

		col = split.column()
		col.label(text="Mode:")
		col.prop(md, "wrap_method", text="")

		if md.wrap_method in {'PROJECT', 'NEAREST_SURFACEPOINT', 'TARGET_PROJECT'}:
			col.prop(md, "wrap_mode", text="")

		if md.wrap_method == 'PROJECT':
			split = layout.split()
			col = split.column()
			col.prop(md, "subsurf_levels")
			col = split.column()

			col.prop(md, "project_limit", text="Limit")
			split = layout.split(factor=0.25)

			col = split.column()
			col.label(text="Axis:")
			col.prop(md, "use_project_x")
			col.prop(md, "use_project_y")
			col.prop(md, "use_project_z")

			col = split.column()
			col.label(text="Direction:")
			col.prop(md, "use_negative_direction")
			col.prop(md, "use_positive_direction")

			subcol = col.column()
			subcol.active = md.use_negative_direction and md.cull_face != 'OFF'
			subcol.prop(md, "use_invert_cull")

			col = split.column()
			col.label(text="Cull Faces:")
			col.prop(md, "cull_face", expand=True)

			layout.prop(md, "auxiliary_target")

	def SIMPLE_DEFORM(self, layout, ob, md):

		layout.row().prop(md, "deform_method", expand=True)

		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		split = layout.split()

		col = split.column()
		col.label(text="Axis, Origin:")
		col.prop(md, "origin", text="")

		col.prop(md, "deform_axis")

		if md.deform_method in {'TAPER', 'STRETCH', 'TWIST'}:
			row = col.row(align=True)
			row.label(text="Lock:")
			deform_axis = md.deform_axis
			if deform_axis != 'X':
				row.prop(md, "lock_x")
			if deform_axis != 'Y':
				row.prop(md, "lock_y")
			if deform_axis != 'Z':
				row.prop(md, "lock_z")

		col = split.column()
		col.label(text="Deform:")
		if md.deform_method in {'TAPER', 'STRETCH'}:
			col.prop(md, "factor")
		else:
			col.prop(md, "angle")
		col.prop(md, "limits", slider=True)

	def SMOKE(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def SMOOTH(self, layout, ob, md):
		split = layout.split(factor=0.25)

		col = split.column()
		col.label(text="Axis:")
		col.prop(md, "use_x")
		col.prop(md, "use_y")
		col.prop(md, "use_z")

		col = split.column()
		col.prop(md, "factor")
		col.prop(md, "iterations")
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

	def SOFT_BODY(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def SOLIDIFY(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.prop(md, "thickness")
		col.prop(md, "thickness_clamp")

		col.separator()

		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = bool(md.vertex_group)
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		sub = col.row()
		sub.active = bool(md.vertex_group)
		sub.prop(md, "thickness_vertex_group", text="Factor")

		col.label(text="Crease:")
		col.prop(md, "edge_crease_inner", text="Inner")
		col.prop(md, "edge_crease_outer", text="Outer")
		col.prop(md, "edge_crease_rim", text="Rim")

		col = split.column()

		col.prop(md, "offset")
		col.prop(md, "use_flip_normals")

		col.prop(md, "use_even_offset")
		col.prop(md, "use_quality_normals")
		col.prop(md, "use_rim")
		col_rim = col.column()
		col_rim.active = md.use_rim
		col_rim.prop(md, "use_rim_only")

		col.separator()

		col.label(text="Material Index Offset:")

		sub = col.column()
		row = sub.split(factor=0.4, align=True)
		row.prop(md, "material_offset", text="")
		row = row.row(align=True)
		row.active = md.use_rim
		row.prop(md, "material_offset_rim", text="Rim")

	def SUBSURF(self, layout, ob, md):
		from bpy import context
		layout.row().prop(md, "subdivision_type", expand=True)

		split = layout.split()
		col = split.column()

		scene = context.scene
		engine = context.engine
		show_adaptive_options = (
			engine == 'CYCLES' and md == ob.modifiers[-1] and
			scene.cycles.feature_set == 'EXPERIMENTAL'
		)
		if show_adaptive_options:
			col.label(text="Render:")
			col.prop(ob.cycles, "use_adaptive_subdivision", text="Adaptive")
			if ob.cycles.use_adaptive_subdivision:
				col.prop(ob.cycles, "dicing_rate")
			else:
				col.prop(md, "render_levels", text="Levels")

			col.separator()

			col.label(text="Viewport:")
			col.prop(md, "levels", text="Levels")
		else:
			col.label(text="Subdivisions:")
			sub = col.column(align=True)
			sub.prop(md, "render_levels", text="Render")
			sub.prop(md, "levels", text="Viewport")

			col.prop(md, "quality")

		col = split.column()
		col.label(text="Options:")

		sub = col.column()
		sub.active = (not show_adaptive_options) or (not ob.cycles.use_adaptive_subdivision)
		sub.prop(md, "uv_smooth", text="")

		col.prop(md, "show_only_control_edges")
		col.prop(md, "use_creases")

		if show_adaptive_options and ob.cycles.use_adaptive_subdivision:
			col = layout.column(align=True)
			col.scale_y = 0.6
			col.separator()
			col.label(text="Final Dicing Rate:")
			col.separator()

			render = max(scene.cycles.dicing_rate * ob.cycles.dicing_rate, 0.1)
			preview = max(scene.cycles.preview_dicing_rate * ob.cycles.dicing_rate, 0.1)
			col.label(text=f"Render {render:.2f} px, Preview {preview:.2f} px")

	def SURFACE(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def SURFACE_DEFORM(self, layout, _ob, md):
		col = layout.column()
		col.active = not md.is_bound

		col.prop(md, "target")
		col.prop(md, "falloff")

		layout.separator()

		col = layout.column()

		if md.is_bound:
			col.operator("object.surfacedeform_bind", text="Unbind")
		else:
			col.active = md.target is not None
			col.operator("object.surfacedeform_bind", text="Bind")

	def UV_PROJECT(self, layout, ob, md):
		split = layout.split()
		col = split.column()
		col.prop_search(md, "uv_layer", ob.data, "uv_layers")
		col.separator()

		col.prop(md, "projector_count", text="Projectors")
		for proj in md.projectors:
			col.prop(proj, "object", text="")

		col = split.column()
		sub = col.column(align=True)
		sub.prop(md, "aspect_x", text="Aspect X")
		sub.prop(md, "aspect_y", text="Aspect Y")

		sub = col.column(align=True)
		sub.prop(md, "scale_x", text="Scale X")
		sub.prop(md, "scale_y", text="Scale Y")

	def WARP(self, layout, ob, md):
		use_falloff = (md.falloff_type != 'NONE')
		split = layout.split()

		col = split.column()
		col.label(text="From:")
		col.prop(md, "object_from", text="")

		col.prop(md, "use_volume_preserve")

		col = split.column()
		col.label(text="To:")
		col.prop(md, "object_to", text="")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col = layout.column()

		row = col.row(align=True)
		row.prop(md, "strength")
		if use_falloff:
			row.prop(md, "falloff_radius")

		col.prop(md, "falloff_type")
		if use_falloff:
			if md.falloff_type == 'CURVE':
				col.template_curve_mapping(md, "falloff_curve")

		# 2 new columns
		split = layout.split()
		col = split.column()
		col.label(text="Texture:")
		col.template_ID(md, "texture", new="texture.new")

		col = split.column()
		col.label(text="Texture Coordinates:")
		col.prop(md, "texture_coords", text="")

		if md.texture_coords == 'OBJECT':
			layout.prop(md, "texture_coords_object", text="Object")
		elif md.texture_coords == 'UV' and ob.type == 'MESH':
			layout.prop_search(md, "uv_layer", ob.data, "uv_layers")

	def WAVE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Motion:")
		col.prop(md, "use_x")
		col.prop(md, "use_y")
		col.prop(md, "use_cyclic")

		col = split.column()
		col.prop(md, "use_normal")
		sub = col.column()
		sub.active = md.use_normal
		sub.prop(md, "use_normal_x", text="X")
		sub.prop(md, "use_normal_y", text="Y")
		sub.prop(md, "use_normal_z", text="Z")

		split = layout.split()

		col = split.column()
		col.label(text="Time:")
		sub = col.column(align=True)
		sub.prop(md, "time_offset", text="Offset")
		sub.prop(md, "lifetime", text="Life")
		col.prop(md, "damping_time", text="Damping")

		col = split.column()
		col.label(text="Position:")
		sub = col.column(align=True)
		sub.prop(md, "start_position_x", text="X")
		sub.prop(md, "start_position_y", text="Y")
		col.prop(md, "falloff_radius", text="Falloff")

		layout.separator()

		layout.prop(md, "start_position_object")
		layout.prop_search(md, "vertex_group", ob, "vertex_groups")
		split = layout.split(factor=0.33)
		col = split.column()
		col.label(text="Texture")
		col = split.column()
		col.template_ID(md, "texture", new="texture.new")
		layout.prop(md, "texture_coords")
		if md.texture_coords == 'UV' and ob.type == 'MESH':
			layout.prop_search(md, "uv_layer", ob.data, "uv_layers")
		elif md.texture_coords == 'OBJECT':
			layout.prop(md, "texture_coords_object")

		layout.separator()

		split = layout.split()

		col = split.column()
		col.prop(md, "speed", slider=True)
		col.prop(md, "height", slider=True)

		col = split.column()
		col.prop(md, "width", slider=True)
		col.prop(md, "narrowness", slider=True)

	def REMESH(self, layout, _ob, md):
		if not bpy.app.build_options.mod_remesh:
			layout.label(text="Built without Remesh modifier")
			return

		layout.prop(md, "mode")

		row = layout.row()
		row.prop(md, "octree_depth")
		row.prop(md, "scale")

		if md.mode == 'SHARP':
			layout.prop(md, "sharpness")

		layout.prop(md, "use_smooth_shade")
		layout.prop(md, "use_remove_disconnected")
		row = layout.row()
		row.active = md.use_remove_disconnected
		row.prop(md, "threshold")

	@staticmethod
	def vertex_weight_mask(layout, ob, md):
		layout.label(text="Influence/Mask Options:")

		split = layout.split(factor=0.4)
		split.label(text="Global Influence:")
		split.prop(md, "mask_constant", text="")

		if not md.mask_texture:
			split = layout.split(factor=0.4)
			split.label(text="Vertex Group Mask:")
			split.prop_search(md, "mask_vertex_group", ob, "vertex_groups", text="")

		if not md.mask_vertex_group:
			split = layout.split(factor=0.4)
			split.label(text="Texture Mask:")
			split.template_ID(md, "mask_texture", new="texture.new")
			if md.mask_texture:
				split = layout.split()

				col = split.column()
				col.label(text="Texture Coordinates:")
				col.prop(md, "mask_tex_mapping", text="")

				col = split.column()
				col.label(text="Use Channel:")
				col.prop(md, "mask_tex_use_channel", text="")

				if md.mask_tex_mapping == 'OBJECT':
					layout.prop(md, "mask_tex_map_object", text="Object")
				elif md.mask_tex_mapping == 'UV' and ob.type == 'MESH':
					layout.prop_search(md, "mask_tex_uv_layer", ob.data, "uv_layers")

	def VERTEX_WEIGHT_EDIT(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col.label(text="Default Weight:")
		col.prop(md, "default_weight", text="")

		col = split.column()
		col.prop(md, "use_add")
		sub = col.column()
		sub.active = md.use_add
		sub.prop(md, "add_threshold")

		col = col.column()
		col.prop(md, "use_remove")
		sub = col.column()
		sub.active = md.use_remove
		sub.prop(md, "remove_threshold")

		layout.separator()

		layout.prop(md, "falloff_type")
		if md.falloff_type == 'CURVE':
			layout.template_curve_mapping(md, "map_curve")

		# Common mask options
		layout.separator()
		self.vertex_weight_mask(layout, ob, md)

	def VERTEX_WEIGHT_MIX(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group A:")
		col.prop_search(md, "vertex_group_a", ob, "vertex_groups", text="")
		col.label(text="Default Weight A:")
		col.prop(md, "default_weight_a", text="")

		col.label(text="Mix Mode:")
		col.prop(md, "mix_mode", text="")

		col = split.column()
		col.label(text="Vertex Group B:")
		col.prop_search(md, "vertex_group_b", ob, "vertex_groups", text="")
		col.label(text="Default Weight B:")
		col.prop(md, "default_weight_b", text="")

		col.label(text="Mix Set:")
		col.prop(md, "mix_set", text="")

		# Common mask options
		layout.separator()
		self.vertex_weight_mask(layout, ob, md)

	def VERTEX_WEIGHT_PROXIMITY(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col = split.column()
		col.label(text="Target Object:")
		col.prop(md, "target", text="")

		split = layout.split()

		col = split.column()
		col.label(text="Distance:")
		col.prop(md, "proximity_mode", text="")
		if md.proximity_mode == 'GEOMETRY':
			col.row().prop(md, "proximity_geometry")

		col = split.column()
		col.label()
		col.prop(md, "min_dist")
		col.prop(md, "max_dist")

		layout.separator()
		layout.prop(md, "falloff_type")

		# Common mask options
		layout.separator()
		self.vertex_weight_mask(layout, ob, md)

	def SKIN(self, layout, _ob, md):
		row = layout.row()
		row.operator("object.skin_armature_create", text="Create Armature")
		row.operator("mesh.customdata_skin_add")

		layout.separator()

		row = layout.row(align=True)
		row.prop(md, "branch_smoothing")
		row.prop(md, "use_smooth_shade")

		split = layout.split()

		col = split.column()
		col.label(text="Selected Vertices:")
		sub = col.column(align=True)
		sub.operator("object.skin_loose_mark_clear", text="Mark Loose").action = 'MARK'
		sub.operator("object.skin_loose_mark_clear", text="Clear Loose").action = 'CLEAR'

		sub = col.column()
		sub.operator("object.skin_root_mark", text="Mark Root")
		sub.operator("object.skin_radii_equalize", text="Equalize Radii")

		col = split.column()
		col.label(text="Symmetry Axes:")
		col.prop(md, "use_x_symmetry")
		col.prop(md, "use_y_symmetry")
		col.prop(md, "use_z_symmetry")

	def TRIANGULATE(self, layout, _ob, md):
		row = layout.row()

		col = row.column()
		col.label(text="Quad Method:")
		col.prop(md, "quad_method", text="")
		col.prop(md, "keep_custom_normals")
		col = row.column()
		col.label(text="Ngon Method:")
		col.prop(md, "ngon_method", text="")
		col.label(text="Minimum Vertices:")
		col.prop(md, "min_vertices", text="")

	def UV_WARP(self, layout, ob, md):
		split = layout.split()
		col = split.column()
		col.prop(md, "center")

		col = split.column()
		col.label(text="UV Axis:")
		col.prop(md, "axis_u", text="")
		col.prop(md, "axis_v", text="")

		split = layout.split()
		col = split.column()
		col.label(text="From:")
		col.prop(md, "object_from", text="")

		col = split.column()
		col.label(text="To:")
		col.prop(md, "object_to", text="")

		split = layout.split()
		col = split.column()
		obj = md.object_from
		if obj and obj.type == 'ARMATURE':
			col.label(text="Bone:")
			col.prop_search(md, "bone_from", obj.data, "bones", text="")

		col = split.column()
		obj = md.object_to
		if obj and obj.type == 'ARMATURE':
			col.label(text="Bone:")
			col.prop_search(md, "bone_to", obj.data, "bones", text="")

		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col = split.column()
		col.label(text="UV Map:")
		col.prop_search(md, "uv_layer", ob.data, "uv_layers", text="")

	def WIREFRAME(self, layout, ob, md):
		has_vgroup = bool(md.vertex_group)

		split = layout.split()

		col = split.column()
		col.prop(md, "thickness", text="Thickness")

		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = has_vgroup
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
		row = col.row(align=True)
		row.active = has_vgroup
		row.prop(md, "thickness_vertex_group", text="Factor")

		col.prop(md, "use_crease", text="Crease Edges")
		row = col.row()
		row.active = md.use_crease
		row.prop(md, "crease_weight", text="Crease Weight")

		col = split.column()

		col.prop(md, "offset")
		col.prop(md, "use_even_offset", text="Even Thickness")
		col.prop(md, "use_relative_offset", text="Relative Thickness")
		col.prop(md, "use_boundary", text="Boundary")
		col.prop(md, "use_replace", text="Replace Original")

		col.prop(md, "material_offset", text="Material Offset")

	def DATA_TRANSFER(self, layout, ob, md):
		row = layout.row(align=True)
		row.prop(md, "object")
		sub = row.row(align=True)
		sub.active = bool(md.object)
		sub.prop(md, "use_object_transform", text="", icon='GROUP')

		layout.separator()

		split = layout.split(factor=0.333)
		split.prop(md, "use_vert_data")
		use_vert = md.use_vert_data
		row = split.row()
		row.active = use_vert
		row.prop(md, "vert_mapping", text="")
		if use_vert:
			col = layout.column(align=True)
			split = col.split(factor=0.333, align=True)
			sub = split.column(align=True)
			sub.prop(md, "data_types_verts")
			sub = split.column(align=True)
			row = sub.row(align=True)
			row.prop(md, "layers_vgroup_select_src", text="")
			row.label(icon='RIGHTARROW')
			row.prop(md, "layers_vgroup_select_dst", text="")
			row = sub.row(align=True)
			row.label(text="", icon='NONE')

		layout.separator()

		split = layout.split(factor=0.333)
		split.prop(md, "use_edge_data")
		use_edge = md.use_edge_data
		row = split.row()
		row.active = use_edge
		row.prop(md, "edge_mapping", text="")
		if use_edge:
			col = layout.column(align=True)
			split = col.split(factor=0.333, align=True)
			sub = split.column(align=True)
			sub.prop(md, "data_types_edges")

		layout.separator()

		split = layout.split(factor=0.333)
		split.prop(md, "use_loop_data")
		use_loop = md.use_loop_data
		row = split.row()
		row.active = use_loop
		row.prop(md, "loop_mapping", text="")
		if use_loop:
			col = layout.column(align=True)
			split = col.split(factor=0.333, align=True)
			sub = split.column(align=True)
			sub.prop(md, "data_types_loops")
			sub = split.column(align=True)
			row = sub.row(align=True)
			row.label(text="", icon='NONE')
			row = sub.row(align=True)
			row.prop(md, "layers_vcol_select_src", text="")
			row.label(icon='RIGHTARROW')
			row.prop(md, "layers_vcol_select_dst", text="")
			row = sub.row(align=True)
			row.prop(md, "layers_uv_select_src", text="")
			row.label(icon='RIGHTARROW')
			row.prop(md, "layers_uv_select_dst", text="")
			col.prop(md, "islands_precision")

		layout.separator()

		split = layout.split(factor=0.333)
		split.prop(md, "use_poly_data")
		use_poly = md.use_poly_data
		row = split.row()
		row.active = use_poly
		row.prop(md, "poly_mapping", text="")
		if use_poly:
			col = layout.column(align=True)
			split = col.split(factor=0.333, align=True)
			sub = split.column(align=True)
			sub.prop(md, "data_types_polys")

		layout.separator()

		split = layout.split()
		col = split.column()
		row = col.row(align=True)
		sub = row.row(align=True)
		sub.active = md.use_max_distance
		sub.prop(md, "max_distance")
		row.prop(md, "use_max_distance", text="", icon='STYLUS_PRESSURE')

		col = split.column()
		col.prop(md, "ray_radius")

		layout.separator()

		split = layout.split()
		col = split.column()
		col.prop(md, "mix_mode")
		col.prop(md, "mix_factor")

		col = split.column()
		row = col.row()
		row.active = bool(md.object)
		row.operator("object.datalayout_transfer", text="Generate Data Layers")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = bool(md.vertex_group)
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

	def NORMAL_EDIT(self, layout, ob, md):
		has_vgroup = bool(md.vertex_group)
		do_polynors_fix = not md.no_polynors_fix
		needs_object_offset = (((md.mode == 'RADIAL') and not md.target) or
							   ((md.mode == 'DIRECTIONAL') and md.use_direction_parallel))

		row = layout.row()
		row.prop(md, "mode", expand=True)

		split = layout.split()

		col = split.column()
		col.prop(md, "target", text="")
		sub = col.column(align=True)
		sub.active = needs_object_offset
		sub.prop(md, "offset")
		row = col.row(align=True)

		col = split.column()
		row = col.row()
		row.active = (md.mode == 'DIRECTIONAL')
		row.prop(md, "use_direction_parallel")

		subcol = col.column(align=True)
		subcol.label(text="Mix Mode:")
		subcol.prop(md, "mix_mode", text="")
		subcol.prop(md, "mix_factor")
		row = subcol.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = has_vgroup
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
		row = subcol.row(align=True)
		row.prop(md, "mix_limit")
		row.prop(md, "no_polynors_fix", text="", icon='UNLOCKED' if do_polynors_fix else 'LOCKED')

	def CORRECTIVE_SMOOTH(self, layout, ob, md):
		is_bind = md.is_bind

		layout.prop(md, "factor", text="Factor")
		layout.prop(md, "iterations")

		row = layout.row()
		row.prop(md, "smooth_type")

		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		col = split.column()
		col.prop(md, "use_only_smooth")
		col.prop(md, "use_pin_boundary")

		layout.prop(md, "rest_source")
		if md.rest_source == 'BIND':
			layout.operator("object.correctivesmooth_bind", text="Unbind" if is_bind else "Bind")

	def WEIGHTED_NORMAL(self, layout, ob, md):
		layout.label(text="Weighting Mode:")
		split = layout.split(align=True)
		col = split.column(align=True)
		col.prop(md, "mode", text="")
		col.prop(md, "weight", text="Weight")
		col.prop(md, "keep_sharp")

		col = split.column(align=True)
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		row.active = bool(md.vertex_group)
		row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
		col.prop(md, "thresh", text="Threshold")
		col.prop(md, "face_influence")













class Dec_Edit_Modifier_Panel(bpy.types.Panel):
	bl_idname = 'OBJECT_PT_dec_edit_modifier_panel'
	bl_category = 'Edit'
	bl_label = 'TMG Modifiers Panel'
	bl_context = "mesh_edit"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
 

	@classmethod
	def poll(cls, context):
		ob = context.object
		return ob and ob.type != 'GPENCIL'

	def draw(self, context):



		layout = self.layout

		ob = context.object

		layout.operator_menu_enum("object.modifier_add", "type")

		for md in ob.modifiers:
			box = layout.template_modifier(md)
			if box:
				# match enum type to our functions, avoids a lookup table.
				getattr(self, md.type)(box, ob, md)

	# the mt.type enum is (ab)used for a lookup on function names
	# ...to avoid lengthy if statements
	# so each type must have a function here.


	def ARMATURE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")
		col.prop(md, "use_deform_preserve_volume")

		col = split.column()
		col.label(text="Bind To:")
		col.prop(md, "use_vertex_groups", text="Vertex Groups")
		col.prop(md, "use_bone_envelopes", text="Bone Envelopes")

		layout.separator()

		split = layout.split()

		row = split.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = bool(md.vertex_group)
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		split.prop(md, "use_multi_modifier")

	def ARRAY(self, layout, _ob, md):
		layout.prop(md, "fit_type")

		if md.fit_type == 'FIXED_COUNT':
			layout.prop(md, "count")
		elif md.fit_type == 'FIT_LENGTH':
			layout.prop(md, "fit_length")
		elif md.fit_type == 'FIT_CURVE':
			layout.prop(md, "curve")

		layout.separator()

		split = layout.split()

		col = split.column()
		col.prop(md, "use_constant_offset")
		sub = col.column()
		sub.active = md.use_constant_offset
		sub.prop(md, "constant_offset_displace", text="")

		col.separator()

		col.prop(md, "use_merge_vertices", text="Merge")
		sub = col.column()
		sub.active = md.use_merge_vertices
		sub.prop(md, "use_merge_vertices_cap", text="First Last")
		sub.prop(md, "merge_threshold", text="Distance")

		col = split.column()
		col.prop(md, "use_relative_offset")
		sub = col.column()
		sub.active = md.use_relative_offset
		sub.prop(md, "relative_offset_displace", text="")

		col.separator()

		col.prop(md, "use_object_offset")
		sub = col.column()
		sub.active = md.use_object_offset
		sub.prop(md, "offset_object", text="")

		row = layout.row()
		split = row.split()
		col = split.column()
		col.label(text="UVs:")
		sub = col.column(align=True)
		sub.prop(md, "offset_u")
		sub.prop(md, "offset_v")
		layout.separator()

		layout.prop(md, "start_cap")
		layout.prop(md, "end_cap")

	def BEVEL(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		if md.offset_type == 'PERCENT':
			col.prop(md, "width_pct")
		else:
			col.prop(md, "width")
		col.prop(md, "segments")
		col.prop(md, "profile")
		col.prop(md, "material")

		col = split.column()
		col.prop(md, "use_only_vertices")
		col.prop(md, "use_clamp_overlap")
		col.prop(md, "loop_slide")
		col.prop(md, "mark_seam")
		col.prop(md, "mark_sharp")
		col.prop(md, "harden_normals")

		layout.label(text="Limit Method:")
		layout.row().prop(md, "limit_method", expand=True)
		if md.limit_method == 'ANGLE':
			layout.prop(md, "angle_limit")
		elif md.limit_method == 'VGROUP':
			layout.label(text="Vertex Group:")
			layout.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		layout.label(text="Width Method:")
		layout.row().prop(md, "offset_type", expand=True)

		layout.label(text="Set Face Strength Mode")
		layout.row().prop(md, "face_strength_mode", expand=True)

		layout.label(text="Miter Patterns")
		layout.row().prop(md, "miter_outer")
		layout.row().prop(md, "miter_inner")
		layout.row().prop(md, "spread")

	def BOOLEAN(self, layout, _ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Operation:")
		col.prop(md, "operation", text="")

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")

		layout.prop(md, "double_threshold")

		if bpy.app.debug:
			layout.prop(md, "debug_options")

	def BUILD(self, layout, _ob, md):
		split = layout.split()

		col = split.column()
		col.prop(md, "frame_start")
		col.prop(md, "frame_duration")
		col.prop(md, "use_reverse")

		col = split.column()
		col.prop(md, "use_random_order")
		sub = col.column()
		sub.active = md.use_random_order
		sub.prop(md, "seed")

	def MESH_CACHE(self, layout, _ob, md):
		layout.prop(md, "cache_format")
		layout.prop(md, "filepath")

		if md.cache_format == 'ABC':
			layout.prop(md, "sub_object")

		layout.label(text="Evaluation:")
		layout.prop(md, "factor", slider=True)
		layout.prop(md, "deform_mode")
		layout.prop(md, "interpolation")

		layout.label(text="Time Mapping:")

		row = layout.row()
		row.prop(md, "time_mode", expand=True)
		row = layout.row()
		row.prop(md, "play_mode", expand=True)
		if md.play_mode == 'SCENE':
			layout.prop(md, "frame_start")
			layout.prop(md, "frame_scale")
		else:
			time_mode = md.time_mode
			if time_mode == 'FRAME':
				layout.prop(md, "eval_frame")
			elif time_mode == 'TIME':
				layout.prop(md, "eval_time")
			elif time_mode == 'FACTOR':
				layout.prop(md, "eval_factor")

		layout.label(text="Axis Mapping:")
		split = layout.split(factor=0.5, align=True)
		split.alert = (md.forward_axis[-1] == md.up_axis[-1])
		split.label(text="Forward/Up Axis:")
		split.prop(md, "forward_axis", text="")
		split.prop(md, "up_axis", text="")
		split = layout.split(factor=0.5)
		split.label(text="Flip Axis:")
		row = split.row()
		row.prop(md, "flip_axis")

	def MESH_SEQUENCE_CACHE(self, layout, ob, md):
		layout.label(text="Cache File Properties:")
		box = layout.box()
		box.template_cache_file(md, "cache_file")

		cache_file = md.cache_file

		layout.label(text="Modifier Properties:")
		box = layout.box()

		if cache_file is not None:
			box.prop_search(md, "object_path", cache_file, "object_paths")

		if ob.type == 'MESH':
			box.row().prop(md, "read_data")

	def CAST(self, layout, ob, md):
		split = layout.split(factor=0.25)

		split.label(text="Cast Type:")
		split.prop(md, "cast_type", text="")

		split = layout.split(factor=0.25)

		col = split.column()
		col.prop(md, "use_x")
		col.prop(md, "use_y")
		col.prop(md, "use_z")

		col = split.column()
		col.prop(md, "factor")
		col.prop(md, "radius")
		col.prop(md, "size")
		col.prop(md, "use_radius_as_size")

		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		col = split.column()
		col.label(text="Control Object:")
		col.prop(md, "object", text="")
		if md.object:
			col.prop(md, "use_transform")

	def CLOTH(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def COLLISION(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def CURVE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")
		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		layout.label(text="Deformation Axis:")
		layout.row().prop(md, "deform_axis", expand=True)

	def DECIMATE(self, layout, ob, md):
		decimate_type = md.decimate_type

		row = layout.row()
		row.prop(md, "decimate_type", expand=True)

		if decimate_type == 'COLLAPSE':
			has_vgroup = bool(md.vertex_group)
			layout.prop(md, "ratio")

			split = layout.split()

			col = split.column()
			row = col.row(align=True)
			row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
			row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

			layout_info = col

			col = split.column()
			row = col.row()
			row.active = has_vgroup
			row.prop(md, "vertex_group_factor")

			col.prop(md, "use_collapse_triangulate")
			row = col.split(factor=0.75)
			row.prop(md, "use_symmetry")
			row.prop(md, "symmetry_axis", text="")

		elif decimate_type == 'UNSUBDIV':
			layout.prop(md, "iterations")
			layout_info = layout
		else:  # decimate_type == 'DISSOLVE':
			layout.prop(md, "angle_limit")
			layout.prop(md, "use_dissolve_boundaries")
			layout.label(text="Delimit:")
			row = layout.row()
			row.prop(md, "delimit")
			layout_info = layout

		layout_info.label(
			text=iface_("Face Count: {:,}".format(md.face_count)),
			translate=False,
		)

	def DISPLACE(self, layout, ob, md):
		has_texture = (md.texture is not None)

		col = layout.column(align=True)
		col.label(text="Texture:")
		col.template_ID(md, "texture", new="texture.new")

		split = layout.split()

		col = split.column(align=True)
		col.label(text="Direction:")
		col.prop(md, "direction", text="")
		if md.direction in {'X', 'Y', 'Z', 'RGB_TO_XYZ'}:
			col.label(text="Space:")
			col.prop(md, "space", text="")
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col = split.column(align=True)
		col.active = has_texture
		col.label(text="Texture Coordinates:")
		col.prop(md, "texture_coords", text="")
		if md.texture_coords == 'OBJECT':
			col.label(text="Object:")
			col.prop(md, "texture_coords_object", text="")
		elif md.texture_coords == 'UV' and ob.type == 'MESH':
			col.label(text="UV Map:")
			col.prop_search(md, "uv_layer", ob.data, "uv_layers", text="")

		layout.separator()

		row = layout.row()
		row.prop(md, "mid_level")
		row.prop(md, "strength")

	def DYNAMIC_PAINT(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def EDGE_SPLIT(self, layout, _ob, md):
		split = layout.split()

		col = split.column()
		col.prop(md, "use_edge_angle", text="Edge Angle")
		sub = col.column()
		sub.active = md.use_edge_angle
		sub.prop(md, "split_angle")

		split.prop(md, "use_edge_sharp", text="Sharp Edges")

	def EXPLODE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = col.column()
		sub.active = bool(md.vertex_group)
		sub.prop(md, "protect")
		col.label(text="Particle UV")
		col.prop_search(md, "particle_uv", ob.data, "uv_layers", text="")

		col = split.column()
		col.prop(md, "use_edge_cut")
		col.prop(md, "show_unborn")
		col.prop(md, "show_alive")
		col.prop(md, "show_dead")
		col.prop(md, "use_size")

		layout.operator("object.explode_refresh", text="Refresh")

	def FLUID_SIMULATION(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def HOOK(self, layout, ob, md):
		use_falloff = (md.falloff_type != 'NONE')
		split = layout.split()

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")
		if md.object and md.object.type == 'ARMATURE':
			col.label(text="Bone:")
			col.prop_search(md, "subtarget", md.object.data, "bones", text="")
		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		layout.separator()

		row = layout.row(align=True)
		if use_falloff:
			row.prop(md, "falloff_radius")
		row.prop(md, "strength", slider=True)
		layout.prop(md, "falloff_type")

		col = layout.column()
		if use_falloff:
			if md.falloff_type == 'CURVE':
				col.template_curve_mapping(md, "falloff_curve")

		split = layout.split()

		col = split.column()
		col.prop(md, "use_falloff_uniform")

		if ob.mode == 'EDIT':
			row = col.row(align=True)
			row.operator("object.hook_reset", text="Reset")
			row.operator("object.hook_recenter", text="Recenter")

			row = layout.row(align=True)
			row.operator("object.hook_select", text="Select")
			row.operator("object.hook_assign", text="Assign")

	def LAPLACIANDEFORM(self, layout, ob, md):
		is_bind = md.is_bind

		layout.prop(md, "iterations")

		row = layout.row()
		row.active = not is_bind
		row.label(text="Anchors Vertex Group:")

		row = layout.row()
		row.enabled = not is_bind
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		layout.separator()

		row = layout.row()
		row.enabled = bool(md.vertex_group)
		row.operator("object.laplaciandeform_bind", text="Unbind" if is_bind else "Bind")

	def LAPLACIANSMOOTH(self, layout, ob, md):
		layout.prop(md, "iterations")

		split = layout.split(factor=0.25)

		col = split.column()
		col.label(text="Axis:")
		col.prop(md, "use_x")
		col.prop(md, "use_y")
		col.prop(md, "use_z")

		col = split.column()
		col.label(text="Lambda:")
		col.prop(md, "lambda_factor", text="Factor")
		col.prop(md, "lambda_border", text="Border")

		col.separator()
		col.prop(md, "use_volume_preserve")
		col.prop(md, "use_normalized")

		layout.label(text="Vertex Group:")
		layout.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

	def LATTICE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Object:")
		col.prop(md, "object", text="")

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		layout.separator()
		layout.prop(md, "strength", slider=True)

	def MASK(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Mode:")
		col.prop(md, "mode", text="")

		col = split.column()
		if md.mode == 'ARMATURE':
			col.label(text="Armature:")
			row = col.row(align=True)
			row.prop(md, "armature", text="")
			sub = row.row(align=True)
			sub.active = (md.armature is not None)
			sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
		elif md.mode == 'VERTEX_GROUP':
			col.label(text="Vertex Group:")
			row = col.row(align=True)
			row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
			sub = row.row(align=True)
			sub.active = bool(md.vertex_group)
			sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		col = layout.column()
		col.prop(md, "threshold")

	def MESH_DEFORM(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.enabled = not md.is_bound
		col.label(text="Object:")
		col.prop(md, "object", text="")

		col = split.column()
		col.label(text="Vertex Group:")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = bool(md.vertex_group)
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		layout.separator()
		row = layout.row()
		row.enabled = not md.is_bound
		row.prop(md, "precision")
		row.prop(md, "use_dynamic_bind")

		layout.separator()
		if md.is_bound:
			layout.operator("object.meshdeform_bind", text="Unbind")
		else:
			layout.operator("object.meshdeform_bind", text="Bind")

	def MIRROR(self, layout, _ob, md):
		axis_text = "XYZ"
		split = layout.split(factor=0.33)

		col = split.column()
		col.label(text="Axis:")
		for i, text in enumerate(axis_text):
			col.prop(md, "use_axis", text=text, index=i)

		col = split.column()
		col.label(text="Bisect:")
		for i, text in enumerate(axis_text):
			colsub = col.column()
			colsub.prop(md, "use_bisect_axis", text=text, index=i)
			colsub.active = md.use_axis[i]

		col = split.column()
		col.label(text="Flip:")
		for i, text in enumerate(axis_text):
			colsub = col.column()
			colsub.prop(md, "use_bisect_flip_axis", text=text, index=i)
			colsub.active = md.use_axis[i] and md.use_bisect_axis[i]

		layout.separator()

		col = layout.column()
		col.label(text="Mirror Object:")
		col.prop(md, "mirror_object", text="")

		layout.separator()

		col = layout.column()
		col.label(text="Options:")

		row = layout.row()
		row.prop(md, "use_mirror_vertex_groups", text="Vertex Groups")
		row.prop(md, "use_clip", text="Clipping")
		row = layout.row()
		row.prop(md, "use_mirror_merge", text="Merge")

		col = layout.column()
		if md.use_mirror_merge is True:
			col.prop(md, "merge_threshold")

		layout.separator()
		col = layout.column()

		col.label(text="Textures:")
		row = layout.row()
		row.prop(md, "use_mirror_u", text="Flip U")
		row.prop(md, "use_mirror_v", text="Flip V")

		col = layout.column(align=True)

		if md.use_mirror_u:
			col.prop(md, "mirror_offset_u")

		if md.use_mirror_v:
			col.prop(md, "mirror_offset_v")

		col = layout.column(align=True)
		col.prop(md, "offset_u")
		col.prop(md, "offset_v")

	def MULTIRES(self, layout, ob, md):
		layout.row().prop(md, "subdivision_type", expand=True)

		split = layout.split()
		col = split.column()
		col.prop(md, "levels", text="Preview")
		col.prop(md, "sculpt_levels", text="Sculpt")
		col.prop(md, "render_levels", text="Render")
		col.prop(md, "quality")

		col = split.column()

		col.enabled = ob.mode != 'EDIT'
		col.operator("object.multires_subdivide", text="Subdivide")
		col.operator("object.multires_higher_levels_delete", text="Delete Higher")
		col.operator("object.multires_reshape", text="Reshape")
		col.operator("object.multires_base_apply", text="Apply Base")
		col.prop(md, "uv_smooth", text="")
		col.prop(md, "show_only_control_edges")
		col.prop(md, "use_creases")

		layout.separator()

		col = layout.column()
		row = col.row()
		if md.is_external:
			row.operator("object.multires_external_pack", text="Pack External")
			row.label()
			row = col.row()
			row.prop(md, "filepath", text="")
		else:
			row.operator("object.multires_external_save", text="Save External...")
			row.label()

	def OCEAN(self, layout, _ob, md):
		if not bpy.app.build_options.mod_oceansim:
			layout.label(text="Built without OceanSim modifier")
			return

		layout.prop(md, "geometry_mode")

		if md.geometry_mode == 'GENERATE':
			row = layout.row()
			row.prop(md, "repeat_x")
			row.prop(md, "repeat_y")

		layout.separator()

		split = layout.split()

		col = split.column()
		col.prop(md, "time")
		col.prop(md, "depth")
		col.prop(md, "random_seed")

		col = split.column()
		col.prop(md, "resolution")
		col.prop(md, "size")
		col.prop(md, "spatial_size")

		layout.label(text="Waves:")

		split = layout.split()

		col = split.column()
		col.prop(md, "choppiness")
		col.prop(md, "wave_scale", text="Scale")
		col.prop(md, "wave_scale_min")
		col.prop(md, "wind_velocity")

		col = split.column()
		col.prop(md, "wave_alignment", text="Alignment")
		sub = col.column()
		sub.active = (md.wave_alignment > 0.0)
		sub.prop(md, "wave_direction", text="Direction")
		sub.prop(md, "damping")

		layout.separator()

		layout.prop(md, "use_normals")

		split = layout.split()

		col = split.column()
		col.prop(md, "use_foam")
		sub = col.row()
		sub.active = md.use_foam
		sub.prop(md, "foam_coverage", text="Coverage")

		col = split.column()
		col.active = md.use_foam
		col.label(text="Foam Data Layer Name:")
		col.prop(md, "foam_layer_name", text="")

		layout.separator()

		if md.is_cached:
			layout.operator("object.ocean_bake", text="Delete Bake").free = True
		else:
			layout.operator("object.ocean_bake").free = False

		split = layout.split()
		split.enabled = not md.is_cached

		col = split.column(align=True)
		col.prop(md, "frame_start", text="Start")
		col.prop(md, "frame_end", text="End")

		col = split.column(align=True)
		col.label(text="Cache path:")
		col.prop(md, "filepath", text="")

		split = layout.split()
		split.enabled = not md.is_cached

		col = split.column()
		col.active = md.use_foam
		col.prop(md, "bake_foam_fade")

		col = split.column()

	def PARTICLE_INSTANCE(self, layout, ob, md):
		layout.prop(md, "object")
		if md.object:
			layout.prop_search(md, "particle_system", md.object, "particle_systems", text="Particle System")
		else:
			layout.prop(md, "particle_system_index", text="Particle System")

		split = layout.split()
		col = split.column()
		col.label(text="Create From:")
		layout.prop(md, "space", text="")
		col.prop(md, "use_normal")
		col.prop(md, "use_children")
		col.prop(md, "use_size")

		col = split.column()
		col.label(text="Show Particles When:")
		col.prop(md, "show_alive")
		col.prop(md, "show_unborn")
		col.prop(md, "show_dead")

		row = layout.row(align=True)
		row.prop(md, "particle_amount", text="Amount")
		row.prop(md, "particle_offset", text="Offset")

		row = layout.row(align=True)
		row.prop(md, "axis", expand=True)

		layout.separator()

		layout.prop(md, "use_path", text="Create Along Paths")

		col = layout.column()
		col.active = md.use_path
		col.prop(md, "use_preserve_shape")

		row = col.row(align=True)
		row.prop(md, "position", slider=True)
		row.prop(md, "random_position", text="Random", slider=True)
		row = col.row(align=True)
		row.prop(md, "rotation", slider=True)
		row.prop(md, "random_rotation", text="Random", slider=True)

		layout.separator()

		col = layout.column()
		col.prop_search(md, "index_layer_name", ob.data, "vertex_colors", text="Index Layer")
		col.prop_search(md, "value_layer_name", ob.data, "vertex_colors", text="Value Layer")

	def PARTICLE_SYSTEM(self, layout, _ob, _md):
		layout.label(text="Settings can be found inside the Particle context")

	def SCREW(self, layout, _ob, md):
		split = layout.split()

		col = split.column()
		col.prop(md, "axis")
		col.prop(md, "object", text="AxisOb")
		col.prop(md, "angle")
		col.prop(md, "steps")
		col.prop(md, "render_steps")
		col.prop(md, "use_smooth_shade")
		col.prop(md, "use_merge_vertices")
		sub = col.column()
		sub.active = md.use_merge_vertices
		sub.prop(md, "merge_threshold")

		col = split.column()
		row = col.row()
		row.active = (md.object is None or md.use_object_screw_offset is False)
		row.prop(md, "screw_offset")
		row = col.row()
		row.active = (md.object is not None)
		row.prop(md, "use_object_screw_offset")
		col.prop(md, "use_normal_calculate")
		col.prop(md, "use_normal_flip")
		col.prop(md, "iterations")
		col.prop(md, "use_stretch_u")
		col.prop(md, "use_stretch_v")

	def SHRINKWRAP(self, layout, ob, md):
		split = layout.split()
		col = split.column()
		col.label(text="Target:")
		col.prop(md, "target", text="")
		col = split.column()
		col.label(text="Vertex Group:")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		split = layout.split()

		col = split.column()
		col.prop(md, "offset")

		col = split.column()
		col.label(text="Mode:")
		col.prop(md, "wrap_method", text="")

		if md.wrap_method in {'PROJECT', 'NEAREST_SURFACEPOINT', 'TARGET_PROJECT'}:
			col.prop(md, "wrap_mode", text="")

		if md.wrap_method == 'PROJECT':
			split = layout.split()
			col = split.column()
			col.prop(md, "subsurf_levels")
			col = split.column()

			col.prop(md, "project_limit", text="Limit")
			split = layout.split(factor=0.25)

			col = split.column()
			col.label(text="Axis:")
			col.prop(md, "use_project_x")
			col.prop(md, "use_project_y")
			col.prop(md, "use_project_z")

			col = split.column()
			col.label(text="Direction:")
			col.prop(md, "use_negative_direction")
			col.prop(md, "use_positive_direction")

			subcol = col.column()
			subcol.active = md.use_negative_direction and md.cull_face != 'OFF'
			subcol.prop(md, "use_invert_cull")

			col = split.column()
			col.label(text="Cull Faces:")
			col.prop(md, "cull_face", expand=True)

			layout.prop(md, "auxiliary_target")

	def SIMPLE_DEFORM(self, layout, ob, md):

		layout.row().prop(md, "deform_method", expand=True)

		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		split = layout.split()

		col = split.column()
		col.label(text="Axis, Origin:")
		col.prop(md, "origin", text="")

		col.prop(md, "deform_axis")

		if md.deform_method in {'TAPER', 'STRETCH', 'TWIST'}:
			row = col.row(align=True)
			row.label(text="Lock:")
			deform_axis = md.deform_axis
			if deform_axis != 'X':
				row.prop(md, "lock_x")
			if deform_axis != 'Y':
				row.prop(md, "lock_y")
			if deform_axis != 'Z':
				row.prop(md, "lock_z")

		col = split.column()
		col.label(text="Deform:")
		if md.deform_method in {'TAPER', 'STRETCH'}:
			col.prop(md, "factor")
		else:
			col.prop(md, "angle")
		col.prop(md, "limits", slider=True)

	def SMOKE(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def SMOOTH(self, layout, ob, md):
		split = layout.split(factor=0.25)

		col = split.column()
		col.label(text="Axis:")
		col.prop(md, "use_x")
		col.prop(md, "use_y")
		col.prop(md, "use_z")

		col = split.column()
		col.prop(md, "factor")
		col.prop(md, "iterations")
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

	def SOFT_BODY(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def SOLIDIFY(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.prop(md, "thickness")
		col.prop(md, "thickness_clamp")

		col.separator()

		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = bool(md.vertex_group)
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		sub = col.row()
		sub.active = bool(md.vertex_group)
		sub.prop(md, "thickness_vertex_group", text="Factor")

		col.label(text="Crease:")
		col.prop(md, "edge_crease_inner", text="Inner")
		col.prop(md, "edge_crease_outer", text="Outer")
		col.prop(md, "edge_crease_rim", text="Rim")

		col = split.column()

		col.prop(md, "offset")
		col.prop(md, "use_flip_normals")

		col.prop(md, "use_even_offset")
		col.prop(md, "use_quality_normals")
		col.prop(md, "use_rim")
		col_rim = col.column()
		col_rim.active = md.use_rim
		col_rim.prop(md, "use_rim_only")

		col.separator()

		col.label(text="Material Index Offset:")

		sub = col.column()
		row = sub.split(factor=0.4, align=True)
		row.prop(md, "material_offset", text="")
		row = row.row(align=True)
		row.active = md.use_rim
		row.prop(md, "material_offset_rim", text="Rim")

	def SUBSURF(self, layout, ob, md):
		from bpy import context
		layout.row().prop(md, "subdivision_type", expand=True)

		split = layout.split()
		col = split.column()

		scene = context.scene
		engine = context.engine
		show_adaptive_options = (
			engine == 'CYCLES' and md == ob.modifiers[-1] and
			scene.cycles.feature_set == 'EXPERIMENTAL'
		)
		if show_adaptive_options:
			col.label(text="Render:")
			col.prop(ob.cycles, "use_adaptive_subdivision", text="Adaptive")
			if ob.cycles.use_adaptive_subdivision:
				col.prop(ob.cycles, "dicing_rate")
			else:
				col.prop(md, "render_levels", text="Levels")

			col.separator()

			col.label(text="Viewport:")
			col.prop(md, "levels", text="Levels")
		else:
			col.label(text="Subdivisions:")
			sub = col.column(align=True)
			sub.prop(md, "render_levels", text="Render")
			sub.prop(md, "levels", text="Viewport")

			col.prop(md, "quality")

		col = split.column()
		col.label(text="Options:")

		sub = col.column()
		sub.active = (not show_adaptive_options) or (not ob.cycles.use_adaptive_subdivision)
		sub.prop(md, "uv_smooth", text="")

		col.prop(md, "show_only_control_edges")
		col.prop(md, "use_creases")

		if show_adaptive_options and ob.cycles.use_adaptive_subdivision:
			col = layout.column(align=True)
			col.scale_y = 0.6
			col.separator()
			col.label(text="Final Dicing Rate:")
			col.separator()

			render = max(scene.cycles.dicing_rate * ob.cycles.dicing_rate, 0.1)
			preview = max(scene.cycles.preview_dicing_rate * ob.cycles.dicing_rate, 0.1)
			col.label(text=f"Render {render:.2f} px, Preview {preview:.2f} px")

	def SURFACE(self, layout, _ob, _md):
		layout.label(text="Settings are inside the Physics tab")

	def SURFACE_DEFORM(self, layout, _ob, md):
		col = layout.column()
		col.active = not md.is_bound

		col.prop(md, "target")
		col.prop(md, "falloff")

		layout.separator()

		col = layout.column()

		if md.is_bound:
			col.operator("object.surfacedeform_bind", text="Unbind")
		else:
			col.active = md.target is not None
			col.operator("object.surfacedeform_bind", text="Bind")

	def UV_PROJECT(self, layout, ob, md):
		split = layout.split()
		col = split.column()
		col.prop_search(md, "uv_layer", ob.data, "uv_layers")
		col.separator()

		col.prop(md, "projector_count", text="Projectors")
		for proj in md.projectors:
			col.prop(proj, "object", text="")

		col = split.column()
		sub = col.column(align=True)
		sub.prop(md, "aspect_x", text="Aspect X")
		sub.prop(md, "aspect_y", text="Aspect Y")

		sub = col.column(align=True)
		sub.prop(md, "scale_x", text="Scale X")
		sub.prop(md, "scale_y", text="Scale Y")

	def WARP(self, layout, ob, md):
		use_falloff = (md.falloff_type != 'NONE')
		split = layout.split()

		col = split.column()
		col.label(text="From:")
		col.prop(md, "object_from", text="")

		col.prop(md, "use_volume_preserve")

		col = split.column()
		col.label(text="To:")
		col.prop(md, "object_to", text="")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col = layout.column()

		row = col.row(align=True)
		row.prop(md, "strength")
		if use_falloff:
			row.prop(md, "falloff_radius")

		col.prop(md, "falloff_type")
		if use_falloff:
			if md.falloff_type == 'CURVE':
				col.template_curve_mapping(md, "falloff_curve")

		# 2 new columns
		split = layout.split()
		col = split.column()
		col.label(text="Texture:")
		col.template_ID(md, "texture", new="texture.new")

		col = split.column()
		col.label(text="Texture Coordinates:")
		col.prop(md, "texture_coords", text="")

		if md.texture_coords == 'OBJECT':
			layout.prop(md, "texture_coords_object", text="Object")
		elif md.texture_coords == 'UV' and ob.type == 'MESH':
			layout.prop_search(md, "uv_layer", ob.data, "uv_layers")

	def WAVE(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Motion:")
		col.prop(md, "use_x")
		col.prop(md, "use_y")
		col.prop(md, "use_cyclic")

		col = split.column()
		col.prop(md, "use_normal")
		sub = col.column()
		sub.active = md.use_normal
		sub.prop(md, "use_normal_x", text="X")
		sub.prop(md, "use_normal_y", text="Y")
		sub.prop(md, "use_normal_z", text="Z")

		split = layout.split()

		col = split.column()
		col.label(text="Time:")
		sub = col.column(align=True)
		sub.prop(md, "time_offset", text="Offset")
		sub.prop(md, "lifetime", text="Life")
		col.prop(md, "damping_time", text="Damping")

		col = split.column()
		col.label(text="Position:")
		sub = col.column(align=True)
		sub.prop(md, "start_position_x", text="X")
		sub.prop(md, "start_position_y", text="Y")
		col.prop(md, "falloff_radius", text="Falloff")

		layout.separator()

		layout.prop(md, "start_position_object")
		layout.prop_search(md, "vertex_group", ob, "vertex_groups")
		split = layout.split(factor=0.33)
		col = split.column()
		col.label(text="Texture")
		col = split.column()
		col.template_ID(md, "texture", new="texture.new")
		layout.prop(md, "texture_coords")
		if md.texture_coords == 'UV' and ob.type == 'MESH':
			layout.prop_search(md, "uv_layer", ob.data, "uv_layers")
		elif md.texture_coords == 'OBJECT':
			layout.prop(md, "texture_coords_object")

		layout.separator()

		split = layout.split()

		col = split.column()
		col.prop(md, "speed", slider=True)
		col.prop(md, "height", slider=True)

		col = split.column()
		col.prop(md, "width", slider=True)
		col.prop(md, "narrowness", slider=True)

	def REMESH(self, layout, _ob, md):
		if not bpy.app.build_options.mod_remesh:
			layout.label(text="Built without Remesh modifier")
			return

		layout.prop(md, "mode")

		row = layout.row()
		row.prop(md, "octree_depth")
		row.prop(md, "scale")

		if md.mode == 'SHARP':
			layout.prop(md, "sharpness")

		layout.prop(md, "use_smooth_shade")
		layout.prop(md, "use_remove_disconnected")
		row = layout.row()
		row.active = md.use_remove_disconnected
		row.prop(md, "threshold")

	@staticmethod
	def vertex_weight_mask(layout, ob, md):
		layout.label(text="Influence/Mask Options:")

		split = layout.split(factor=0.4)
		split.label(text="Global Influence:")
		split.prop(md, "mask_constant", text="")

		if not md.mask_texture:
			split = layout.split(factor=0.4)
			split.label(text="Vertex Group Mask:")
			split.prop_search(md, "mask_vertex_group", ob, "vertex_groups", text="")

		if not md.mask_vertex_group:
			split = layout.split(factor=0.4)
			split.label(text="Texture Mask:")
			split.template_ID(md, "mask_texture", new="texture.new")
			if md.mask_texture:
				split = layout.split()

				col = split.column()
				col.label(text="Texture Coordinates:")
				col.prop(md, "mask_tex_mapping", text="")

				col = split.column()
				col.label(text="Use Channel:")
				col.prop(md, "mask_tex_use_channel", text="")

				if md.mask_tex_mapping == 'OBJECT':
					layout.prop(md, "mask_tex_map_object", text="Object")
				elif md.mask_tex_mapping == 'UV' and ob.type == 'MESH':
					layout.prop_search(md, "mask_tex_uv_layer", ob.data, "uv_layers")

	def VERTEX_WEIGHT_EDIT(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col.label(text="Default Weight:")
		col.prop(md, "default_weight", text="")

		col = split.column()
		col.prop(md, "use_add")
		sub = col.column()
		sub.active = md.use_add
		sub.prop(md, "add_threshold")

		col = col.column()
		col.prop(md, "use_remove")
		sub = col.column()
		sub.active = md.use_remove
		sub.prop(md, "remove_threshold")

		layout.separator()

		layout.prop(md, "falloff_type")
		if md.falloff_type == 'CURVE':
			layout.template_curve_mapping(md, "map_curve")

		# Common mask options
		layout.separator()
		self.vertex_weight_mask(layout, ob, md)

	def VERTEX_WEIGHT_MIX(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group A:")
		col.prop_search(md, "vertex_group_a", ob, "vertex_groups", text="")
		col.label(text="Default Weight A:")
		col.prop(md, "default_weight_a", text="")

		col.label(text="Mix Mode:")
		col.prop(md, "mix_mode", text="")

		col = split.column()
		col.label(text="Vertex Group B:")
		col.prop_search(md, "vertex_group_b", ob, "vertex_groups", text="")
		col.label(text="Default Weight B:")
		col.prop(md, "default_weight_b", text="")

		col.label(text="Mix Set:")
		col.prop(md, "mix_set", text="")

		# Common mask options
		layout.separator()
		self.vertex_weight_mask(layout, ob, md)

	def VERTEX_WEIGHT_PROXIMITY(self, layout, ob, md):
		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col = split.column()
		col.label(text="Target Object:")
		col.prop(md, "target", text="")

		split = layout.split()

		col = split.column()
		col.label(text="Distance:")
		col.prop(md, "proximity_mode", text="")
		if md.proximity_mode == 'GEOMETRY':
			col.row().prop(md, "proximity_geometry")

		col = split.column()
		col.label()
		col.prop(md, "min_dist")
		col.prop(md, "max_dist")

		layout.separator()
		layout.prop(md, "falloff_type")

		# Common mask options
		layout.separator()
		self.vertex_weight_mask(layout, ob, md)

	def SKIN(self, layout, _ob, md):
		row = layout.row()
		row.operator("object.skin_armature_create", text="Create Armature")
		row.operator("mesh.customdata_skin_add")

		layout.separator()

		row = layout.row(align=True)
		row.prop(md, "branch_smoothing")
		row.prop(md, "use_smooth_shade")

		split = layout.split()

		col = split.column()
		col.label(text="Selected Vertices:")
		sub = col.column(align=True)
		sub.operator("object.skin_loose_mark_clear", text="Mark Loose").action = 'MARK'
		sub.operator("object.skin_loose_mark_clear", text="Clear Loose").action = 'CLEAR'

		sub = col.column()
		sub.operator("object.skin_root_mark", text="Mark Root")
		sub.operator("object.skin_radii_equalize", text="Equalize Radii")

		col = split.column()
		col.label(text="Symmetry Axes:")
		col.prop(md, "use_x_symmetry")
		col.prop(md, "use_y_symmetry")
		col.prop(md, "use_z_symmetry")

	def TRIANGULATE(self, layout, _ob, md):
		row = layout.row()

		col = row.column()
		col.label(text="Quad Method:")
		col.prop(md, "quad_method", text="")
		col.prop(md, "keep_custom_normals")
		col = row.column()
		col.label(text="Ngon Method:")
		col.prop(md, "ngon_method", text="")
		col.label(text="Minimum Vertices:")
		col.prop(md, "min_vertices", text="")

	def UV_WARP(self, layout, ob, md):
		split = layout.split()
		col = split.column()
		col.prop(md, "center")

		col = split.column()
		col.label(text="UV Axis:")
		col.prop(md, "axis_u", text="")
		col.prop(md, "axis_v", text="")

		split = layout.split()
		col = split.column()
		col.label(text="From:")
		col.prop(md, "object_from", text="")

		col = split.column()
		col.label(text="To:")
		col.prop(md, "object_to", text="")

		split = layout.split()
		col = split.column()
		obj = md.object_from
		if obj and obj.type == 'ARMATURE':
			col.label(text="Bone:")
			col.prop_search(md, "bone_from", obj.data, "bones", text="")

		col = split.column()
		obj = md.object_to
		if obj and obj.type == 'ARMATURE':
			col.label(text="Bone:")
			col.prop_search(md, "bone_to", obj.data, "bones", text="")

		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		col.prop_search(md, "vertex_group", ob, "vertex_groups", text="")

		col = split.column()
		col.label(text="UV Map:")
		col.prop_search(md, "uv_layer", ob.data, "uv_layers", text="")

	def WIREFRAME(self, layout, ob, md):
		has_vgroup = bool(md.vertex_group)

		split = layout.split()

		col = split.column()
		col.prop(md, "thickness", text="Thickness")

		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = has_vgroup
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
		row = col.row(align=True)
		row.active = has_vgroup
		row.prop(md, "thickness_vertex_group", text="Factor")

		col.prop(md, "use_crease", text="Crease Edges")
		row = col.row()
		row.active = md.use_crease
		row.prop(md, "crease_weight", text="Crease Weight")

		col = split.column()

		col.prop(md, "offset")
		col.prop(md, "use_even_offset", text="Even Thickness")
		col.prop(md, "use_relative_offset", text="Relative Thickness")
		col.prop(md, "use_boundary", text="Boundary")
		col.prop(md, "use_replace", text="Replace Original")

		col.prop(md, "material_offset", text="Material Offset")

	def DATA_TRANSFER(self, layout, ob, md):
		row = layout.row(align=True)
		row.prop(md, "object")
		sub = row.row(align=True)
		sub.active = bool(md.object)
		sub.prop(md, "use_object_transform", text="", icon='GROUP')

		layout.separator()

		split = layout.split(factor=0.333)
		split.prop(md, "use_vert_data")
		use_vert = md.use_vert_data
		row = split.row()
		row.active = use_vert
		row.prop(md, "vert_mapping", text="")
		if use_vert:
			col = layout.column(align=True)
			split = col.split(factor=0.333, align=True)
			sub = split.column(align=True)
			sub.prop(md, "data_types_verts")
			sub = split.column(align=True)
			row = sub.row(align=True)
			row.prop(md, "layers_vgroup_select_src", text="")
			row.label(icon='RIGHTARROW')
			row.prop(md, "layers_vgroup_select_dst", text="")
			row = sub.row(align=True)
			row.label(text="", icon='NONE')

		layout.separator()

		split = layout.split(factor=0.333)
		split.prop(md, "use_edge_data")
		use_edge = md.use_edge_data
		row = split.row()
		row.active = use_edge
		row.prop(md, "edge_mapping", text="")
		if use_edge:
			col = layout.column(align=True)
			split = col.split(factor=0.333, align=True)
			sub = split.column(align=True)
			sub.prop(md, "data_types_edges")

		layout.separator()

		split = layout.split(factor=0.333)
		split.prop(md, "use_loop_data")
		use_loop = md.use_loop_data
		row = split.row()
		row.active = use_loop
		row.prop(md, "loop_mapping", text="")
		if use_loop:
			col = layout.column(align=True)
			split = col.split(factor=0.333, align=True)
			sub = split.column(align=True)
			sub.prop(md, "data_types_loops")
			sub = split.column(align=True)
			row = sub.row(align=True)
			row.label(text="", icon='NONE')
			row = sub.row(align=True)
			row.prop(md, "layers_vcol_select_src", text="")
			row.label(icon='RIGHTARROW')
			row.prop(md, "layers_vcol_select_dst", text="")
			row = sub.row(align=True)
			row.prop(md, "layers_uv_select_src", text="")
			row.label(icon='RIGHTARROW')
			row.prop(md, "layers_uv_select_dst", text="")
			col.prop(md, "islands_precision")

		layout.separator()

		split = layout.split(factor=0.333)
		split.prop(md, "use_poly_data")
		use_poly = md.use_poly_data
		row = split.row()
		row.active = use_poly
		row.prop(md, "poly_mapping", text="")
		if use_poly:
			col = layout.column(align=True)
			split = col.split(factor=0.333, align=True)
			sub = split.column(align=True)
			sub.prop(md, "data_types_polys")

		layout.separator()

		split = layout.split()
		col = split.column()
		row = col.row(align=True)
		sub = row.row(align=True)
		sub.active = md.use_max_distance
		sub.prop(md, "max_distance")
		row.prop(md, "use_max_distance", text="", icon='STYLUS_PRESSURE')

		col = split.column()
		col.prop(md, "ray_radius")

		layout.separator()

		split = layout.split()
		col = split.column()
		col.prop(md, "mix_mode")
		col.prop(md, "mix_factor")

		col = split.column()
		row = col.row()
		row.active = bool(md.object)
		row.operator("object.datalayout_transfer", text="Generate Data Layers")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = bool(md.vertex_group)
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

	def NORMAL_EDIT(self, layout, ob, md):
		has_vgroup = bool(md.vertex_group)
		do_polynors_fix = not md.no_polynors_fix
		needs_object_offset = (((md.mode == 'RADIAL') and not md.target) or
							   ((md.mode == 'DIRECTIONAL') and md.use_direction_parallel))

		row = layout.row()
		row.prop(md, "mode", expand=True)

		split = layout.split()

		col = split.column()
		col.prop(md, "target", text="")
		sub = col.column(align=True)
		sub.active = needs_object_offset
		sub.prop(md, "offset")
		row = col.row(align=True)

		col = split.column()
		row = col.row()
		row.active = (md.mode == 'DIRECTIONAL')
		row.prop(md, "use_direction_parallel")

		subcol = col.column(align=True)
		subcol.label(text="Mix Mode:")
		subcol.prop(md, "mix_mode", text="")
		subcol.prop(md, "mix_factor")
		row = subcol.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		sub = row.row(align=True)
		sub.active = has_vgroup
		sub.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
		row = subcol.row(align=True)
		row.prop(md, "mix_limit")
		row.prop(md, "no_polynors_fix", text="", icon='UNLOCKED' if do_polynors_fix else 'LOCKED')

	def CORRECTIVE_SMOOTH(self, layout, ob, md):
		is_bind = md.is_bind

		layout.prop(md, "factor", text="Factor")
		layout.prop(md, "iterations")

		row = layout.row()
		row.prop(md, "smooth_type")

		split = layout.split()

		col = split.column()
		col.label(text="Vertex Group:")
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')

		col = split.column()
		col.prop(md, "use_only_smooth")
		col.prop(md, "use_pin_boundary")

		layout.prop(md, "rest_source")
		if md.rest_source == 'BIND':
			layout.operator("object.correctivesmooth_bind", text="Unbind" if is_bind else "Bind")

	def WEIGHTED_NORMAL(self, layout, ob, md):
		layout.label(text="Weighting Mode:")
		split = layout.split(align=True)
		col = split.column(align=True)
		col.prop(md, "mode", text="")
		col.prop(md, "weight", text="Weight")
		col.prop(md, "keep_sharp")

		col = split.column(align=True)
		row = col.row(align=True)
		row.prop_search(md, "vertex_group", ob, "vertex_groups", text="")
		row.active = bool(md.vertex_group)
		row.prop(md, "invert_vertex_group", text="", icon='ARROW_LEFTRIGHT')
		col.prop(md, "thresh", text="Threshold")
		col.prop(md, "face_influence")






class Dec_Object_Materials_Panel(bpy.types.Panel):
	bl_idname = 'OBJECT_PT_dec_object_materials_panel'
	bl_category = 'Edit'
	bl_label = 'TMG Materials Panel'
	bl_context = "objectmode"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'

	def draw(self, context):
		#mat = bpy.context.object.active_material
		#objs = []
		#for obj in bpy.data.objects:
			#for slot in obj.material_slots:
				#if slot.material == mat:
					#objs.append(obj)


		scene = context.scene
		scn = context.scene  

		#matList = context.scene.matList

		#for nr, mat in enumerate(bpy.data.materials):
			#matList.append(mat)
			#print('matList: ', mat_list)

		layout = self.layout

		layout.use_property_split = True
		layout.use_property_decorate = False  # No animation.

		#layout = self.layout
		#col = layout.column()
		#col.prop(context.active_object, "MyInt")

		#### Master Panel Layout Controllers ###############################

		Master_Col = layout.column(align=True)
		Master_Subcol = Master_Col.column()

		#### View Tab Panel Layout Controllers #########################

		View_Col = Master_Col.column(align=True)
		View_Subcol = View_Col.column()
		View_Row = View_Col.row()

		#### View Tab  ############################################################################################################

		#if check_view == False:
			#View_Col.prop(scene, "check_view", text="View", icon="RIGHTARROW")
		#else:
			#View_Col.prop(scene, "check_view", text="View", icon="DOWNARROW_HLT")

		View_Col = Master_Col.column() ###### Box if needed for View Panel #############
		View_Subcol = View_Col.column(align=True)

		View_Col.use_property_split = True
		View_Flow = View_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

		colm = View_Flow.box()

		View_Col = colm.row()
		View_Col.label(text="Materials maybe?")

		#if set(s.material for s in scn.material_slots).symmetric_difference(scn.materials):
			#col.prop(scn, "update_materials", toggle=True, icon='FILE_REFRESH')
		#col.template_list(
				#"MATERIAL_UL_extreme_matslot", 
				#"", 
				#scn, 
				#"material_slots", 
				#scn, 
				#"active_material_index")

		#if mat_list != empty:
		#View_Col = colm.row()
		#View_Col.prop(scene, "matList", text='')
			
			#View_Col.operator('wm.mod_apply_object_ot_operator', text='', icon='MODIFIER')
			#View_Col.operator("object.material_slot_move", icon='TRIA_UP', text="").direction = 'UP'
		

		










	#objectmode
	#mesh_edit
	#curve_edit
	#surface_edit
	#text_edit
	#armature_edit
	#mball_edit
	#lattice_edit
	#pose_mode
	#imagepaint
	#weightpaint
	#vertexpaint
	#particlemode
