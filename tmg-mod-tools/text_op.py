import bpy


##################### Update Text Objects #############################
def textName_changed(self, context):
	text_name = context.scene.textName

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		if obj.type == 'FONT':
			#print('font object: ', obj.type)
			obj.name = text_name
			obj.data.name = text_name


##################### Update Text Objects #############################
def textText_changed(self, context):
	textNameLink = context.scene.textNameLink
	#textName = context.scene.textName
	text_text = context.scene.textText

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		if obj.type == 'FONT':
			#print('font object: ', obj.type)
			
			if textNameLink == True:
				obj.name = text_text
				obj.data.name = text_text
			obj.data.body = text_text


##################### Update Text Vertical Alignment #############################
def text_vAlign_changed(self, context):
	text_vAlign = context.scene.text_vAlign

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		if obj.type == 'FONT':
			obj.data.align_y = text_vAlign


##################### Update Text Horizontal Alignment #############################
def text_hAlign_changed(self, context):
	text_hAlign = context.scene.text_hAlign

	obj = bpy.context.active_object

	for nr, obj in enumerate(bpy.context.selected_objects):

		if obj.type == 'FONT':
			obj.data.align_x = text_hAlign




class Text_Object_Text_Panel(bpy.types.Panel):
	bl_idname = 'OBJECT_PT_text_object_text_panel'
	bl_category = 'Edit'
	bl_label = 'TMG Text Panel'
	bl_context = "objectmode"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'

	def draw(self, context):

		scene = context.scene

		#obj = bpy.context.view_layer.objects.active

		obj = context.object

		#sel_mode = context.tool_settings.mesh_select_mode
		
		textNameLink = context.scene.textNameLink
		text_name = context.scene.textName
		text_text = context.scene.textText
		text_vAlign = context.scene.text_vAlign
		text_hAlign = context.scene.text_hAlign

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

		Text_Col = Master_Col.column(align=True)
		Text_Subcol = Text_Col.column()
		Text_Row = Text_Col.row()

		#### View Tab  ############################################################################################################

		#if check_view == False:
			#View_Col.prop(scene, "check_view", text="View", icon="RIGHTARROW")
		#else:
			#View_Col.prop(scene, "check_view", text="View", icon="DOWNARROW_HLT")

		Text_Col = Master_Col.column() ###### Box if needed for View Panel #############
		Text_Subcol = Text_Col.column(align=True)

		Text_Col.use_property_split = True
		Text_Flow = Text_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

		colb = Text_Flow.box()
		row = colb.row(align=True)
		colm = row.row(align=True)

		if textNameLink == False: # UNLINKED / LINKED

			Text_Flow = colm.column(align=True)
			Text_Flow.alignment = 'RIGHT'
			Text_Flow.label(text="Link Object To Text")
			Text_Flow.label(text="Object Name")
			Text_Flow.label(text="Text")
			Text_Flow.label(text="Vertical Align")
			Text_Flow.label(text="Horizontal Align")

			Text_Flow = colm.column(align=True)
			Text_Flow.prop(scene, "textNameLink", text='', icon='LINKED')
			Text_Flow.prop(scene, "textName", text='')
			Text_Flow.prop(scene, "textText", text='')

		else: # UNLINKED / LINKED

			Text_Flow = colm.column(align=True)
			Text_Flow.alignment = 'RIGHT'
			Text_Flow.label(text="UnLink Object From Text")
			Text_Flow.label(text="Text")
			Text_Flow.label(text="Vertical Align")
			Text_Flow.label(text="Horizontal Align")

			Text_Flow = colm.column(align=True)
			Text_Flow.prop(scene, "textNameLink", text='', icon='UNLINKED')
			Text_Flow.prop(scene, "textText", text='')

		Text_Flow.prop(scene, "text_vAlign", text='')
		Text_Flow.prop(scene, "text_hAlign", text='')

		#else:

			#colm = Text_Flow.row()

			#Text_Flow = colm.column()
			#Text_Flow.label(text="No Text")

		#colm = Text_Flow.column()

		#Text_Flow = colm.row()
		#Text_Flow.prop(scene, "bevelWidth", index=2, text="", slider=True)




class Text_Update_OT_Operator(bpy.types.Operator):
	bl_idname = 'wm.text_update_ot_operator'
	bl_label = 'Decimate Panel'
	bl_description = 'Update text.'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		#textNameLink = context.scene.textNameLink
		#text_name = context.scene.textName
		text_text = context.scene.textText

		obj = bpy.context.active_object

		for nr, obj in enumerate(bpy.context.selected_objects):

			if obj.type == 'FONT':
				#print('font object: ', obj.type)
				obj.data.body = text_text
			#else:
				#print('bad type: ', obj.type)
		
				   
		return {'FINISHED'}
		return {'FINISHED'}









