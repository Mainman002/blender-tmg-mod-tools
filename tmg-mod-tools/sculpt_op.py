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


##################### Update Sculpt Hide Other Shape Layers #############################
def sculpt_single_shape_layer_changed(self, context):
    sculpt_single_shape_layer = context.scene.sculpt_single_shape_layer

    ob = bpy.context.active_object

    current_frame = bpy.context.active_object.active_shape_key_index
    keys = ob.data.shape_keys.key_blocks.keys()
    for shape in ob.data.shape_keys.key_blocks:
        if shape.name == ob.active_shape_key.name or shape.name == 'Base Shape':
            print('found: ' + shape.name)
            shape.mute = False
        else:
            print('other: ' + shape.name)
            shape.mute = sculpt_single_shape_layer


class Sculpt_Brush_Panel(bpy.types.Panel):
    bl_idname = 'SCULPT_PT_sculpt_brush_panel'
    bl_category = 'Edit'
    bl_label = 'TMG Sculpt Brush Panel'
    bl_context = "sculpt_mode"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):

        scene = context.scene

        obj = context.object

        sculpt_spacingDistance = context.scene.sculpt_spacingDistance

        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        # layout = self.layout
        # col = layout.column()
        # col.prop(context.active_object, "MyInt")

        #### Master Panel Layout Controllers ###############################

        Master_Col = layout.column(align=True)
        Master_Subcol = Master_Col.column()

        #### View Tab Panel Layout Controllers #########################

        Sculpt_Col = Master_Col.column(align=True)
        Sculpt_Subcol = Sculpt_Col.column()
        Sculpt_Row = Sculpt_Col.row()

        #### View Tab  ############################################################################################################

        # if check_view == False:
        # View_Col.prop(scene, "check_view", text="View", icon="RIGHTARROW")
        # else:
        # View_Col.prop(scene, "check_view", text="View", icon="DOWNARROW_HLT")

        Sculpt_Col = Master_Col.column()  # Box if needed for View Panel #############
        Sculpt_Subcol = Sculpt_Col.column(align=True)

        Sculpt_Col.use_property_split = True
        Sculpt_Flow = Sculpt_Col.grid_flow(
            row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

        # if obj is not None:
        # if obj.type == 'FONT':
        colm = Sculpt_Flow.box()

        Sculpt_Flow = colm.row()
        Sculpt_Flow.label(text="Sculpt Distance")

        Sculpt_Flow = colm.row()
        Sculpt_Flow.prop(scene, "sculpt_spacingDistance", text='')

        # Sculpt_Flow = colm.row()
        # Sculpt_Flow.label(text="Use Face Sets")

        # Sculpt_Flow = colm.row()
        # Sculpt_Flow.prop(scene, "sculpt_faceSets", text='')


class Sculpt_Referance_Panel(bpy.types.Panel):
    bl_idname = 'SCULPT_PT_sculpt_referance_panel'
    bl_category = 'Edit'
    bl_label = 'TMG Sculpt Referance Panel'
    bl_context = "sculpt_mode"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):

        scene = context.scene

        obj = context.object

        sculpt_spacingDistance = context.scene.sculpt_spacingDistance

        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        # layout = self.layout
        # col = layout.column()
        # col.prop(context.active_object, "MyInt")

        #### Master Panel Layout Controllers ###############################

        Master_Col = layout.column(align=True)
        Master_Subcol = Master_Col.column()

        #### View Tab Panel Layout Controllers #########################

        Sculpt_Col = Master_Col.column(align=True)
        Sculpt_Subcol = Sculpt_Col.column()
        Sculpt_Row = Sculpt_Col.row()

        #### View Tab  ############################################################################################################

        # if check_view == False:
        # View_Col.prop(scene, "check_view", text="View", icon="RIGHTARROW")
        # else:
        # View_Col.prop(scene, "check_view", text="View", icon="DOWNARROW_HLT")

        Sculpt_Col = Master_Col.column()  # Box if needed for View Panel #############
        Sculpt_Subcol = Sculpt_Col.column(align=True)

        Sculpt_Col.use_property_split = True
        Sculpt_Flow = Sculpt_Col.grid_flow(
            row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

        colb = Sculpt_Flow.box()
        row = colb.row(align=True)
        colm = row.row(align=True)

        Sculpt_Flow = colm.column(align=True)
        Sculpt_Flow.alignment = 'RIGHT'
        Sculpt_Flow.label(text="Referance Transparency")
        Sculpt_Flow.label(text="Referance Position X")
        Sculpt_Flow.label(text="Referance Position Y")
        Sculpt_Flow.label(text="Referance Size")

        Sculpt_Flow = colm.column(align=True)
        Sculpt_Flow.prop(scene, "sculpt_referanceTransparency", text='')
        Sculpt_Flow.prop(scene, "sculpt_referancePositionX", text='')
        Sculpt_Flow.prop(scene, "sculpt_referancePositionY", text='')
        Sculpt_Flow.prop(scene, "sculpt_referanceSize", text='')


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

        scene = context.scene
        keyframe_timeline = context.scene.keyframe_timeline
        sculpt_single_shape_layer = context.scene.sculpt_single_shape_layer
        button_mode = context.scene.sculpt_shape_keys_icon_view
        # button_mode = context.preferences.addons[__name__].preferences.sculpt_shape_keys_icon_view

        # if button_mode:
        #     button_mode = False
        #     button_mode = True
        #     print("True: % s" % button_mode)
        # else:
        #     button_mode = True
        #     button_mode = False
        #     print("False: % s" % button_mode)

        # user_preferences = bpy.context.user_preferences
        # addon_prefs = user_preferences.addons["tmg_mod_tools"].preferences
        # button_mode = addon_prefs.sculpt_shape_keys_icon_view

        # button_mode = bpy.ops.scene.sculpt_shape_keys_icon_view

        layout = self.layout
        # row = layout.row(align=True)

        ob = context.object
        key = ob.data.shape_keys
        kb = ob.active_shape_key

        # if button_mode == False:

        # layout.column(align=True).use_property_split = True
        # col = layout.column(align=True).grid_flow(
        #     row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

        # # colb = col.box()
        # row = col.row(align=True)
        # colm = row.row(align=True)

        col = self.layout.column(align=True)
        # # row = col.row(align=True)

        # # props = row.separator()

        laya = self.layout.row(align=True)
        # boxed = laya.box()
        row = laya.row(align=True)
        colm = row.row(align=True)

        if button_mode == False:
            props = row.operator('mesh.sculpt_ot_add_new_shape_layer',
                                    text='Add Layer',
                                    icon='ADD')

        if button_mode == True:
            props = row.operator('mesh.sculpt_ot_add_new_shape_layer',
                                    text='',
                                    icon='ADD')

        row.label(text="Keyframe")
        row.prop(scene, "keyframe_timeline", text="")

        props = col.separator()

        if button_mode == False:

            if bpy.context.active_object.active_shape_key_index > 0:

                # layout.column(align=True).use_property_split = True
                # col = layout.column(align=True).grid_flow(
                #     row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

                # # colb = col.box()
                # row = col.row(align=True)
                # colm = row.column(align=True)

                # col = colm.column(align=True)
                # # row = col.row(align=True)

                # props = row.separator()

                laya = self.layout.column(align=True)
                boxed = laya.box()
                row = boxed.column(align=True)
                colm = row.column(align=True)

                props = colm.operator('mesh.sculpt_ot_shape_key_hide_others',
                                      text='Toggle Other Layers',
                                      icon='RESTRICT_RENDER_OFF')

                props = colm.operator('mesh.sculpt_ot_keyframe_shape_keys',
                                      text='Keyframe Layers',
                                      icon='KEYINGSET')

                props = colm.operator('mesh.sculpt_ot_clear_all_keyframes',
                                      text='Clear All Keyframes',
                                      icon='KEYFRAME',
                                      )

                props = colm.operator('mesh.sculpt_ot_merge_shape_keys',
                                      text='Merge Layers',
                                      icon='SHAPEKEY_DATA',
                                      )

                props = colm.operator('mesh.sculpt_ot_apply_shape_keys',
                                      text='Apply Object',
                                      icon='MESH_CUBE',
                                      )

        if button_mode == True:

            if bpy.context.active_object.active_shape_key_index > 0:

                laya = self.layout.row(align=True)
                boxed = laya.box()
                row = boxed.row(align=True)
                colm = row.row(align=True)

                props = colm.operator('mesh.sculpt_ot_shape_key_hide_others',
                                    text='',
                                    icon='RESTRICT_RENDER_OFF')

                props = colm.operator('mesh.sculpt_ot_keyframe_shape_keys',
                                    text='',
                                    icon='KEYINGSET')

                props = colm.operator('mesh.sculpt_ot_clear_all_keyframes',
                                    text='',
                                    icon='KEYFRAME',
                                    )

                props = colm.operator('mesh.sculpt_ot_merge_shape_keys',
                                    text='',
                                    icon='SHAPEKEY_DATA',
                                    )

                props = colm.operator('mesh.sculpt_ot_apply_shape_keys',
                                    text='',
                                    icon='MESH_CUBE',
                                    )

        enable_edit = ob.mode != 'EDIT'
        enable_edit_value = False

        if ob.show_only_shape_key is False:
            if enable_edit or (ob.type == 'MESH' and ob.use_shape_key_edit_mode):
                enable_edit_value = True

        row = layout.row()

        rows = 3
        if kb:
            rows = 6

        row.template_list("MESH_UL_shape_keys", "", key,
                          "key_blocks", ob, "active_shape_key_index", rows=rows)

        col = row.column(align=True)

        props = col.operator('mesh.sculpt_ot_add_new_shape_layer',
                             text='',
                             icon='ADD')
        # props.mode = 0

        col.operator("object.shape_key_remove",
                     icon='REMOVE', text="").all = False

        col.separator()

        col.menu("MESH_MT_shape_key_context_menu",
                 icon='DOWNARROW_HLT', text="")

        if kb:
            col.separator()

            sub = col.column(align=True)
            sub.operator("object.shape_key_move",
                         icon='TRIA_UP', text="").type = 'UP'
            sub.operator("object.shape_key_move",
                         icon='TRIA_DOWN', text="").type = 'DOWN'

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
                sub.operator("object.shape_key_retime",
                             icon='RECOVER_LAST', text="")

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

                    col.prop_search(kb, "vertex_group", ob,
                                    "vertex_groups", text="Vertex Group")
                    col.prop_search(kb, "relative_key", key,
                                    "key_blocks", text="Relative To")

            else:
                layout.prop(kb, "interpolation")
                row = layout.column()
                row.active = enable_edit_value
                row.prop(key, "eval_time")


class Sculpt_OT_ADD_New_Shape_Layer(bpy.types.Operator):
    """Sculpt ADD New Shape Layer"""
    bl_idname = 'mesh.sculpt_ot_add_new_shape_layer'
    bl_label = 'New Layer'
    bl_description = 'Add a new shape layer.'
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        # print(f"My area is: {context.area.type}")
        # sculpt_single_shape_layer = context.scene.sculpt_single_shape_layer
        return context.area.type == 'VIEW_3D'

    def execute(self, context):

        keys = 0
        ob = bpy.context.active_object
        current_frame = bpy.context.active_object.active_shape_key_index

        keyframe_timeline = context.scene.keyframe_timeline

        # Adds Layer with timeline keyframe
        if keyframe_timeline:
            bpy.ops.object.shape_key_add(from_mix=False)
            current_frame = bpy.context.active_object.active_shape_key_index
            keys = ob.data.shape_keys.key_blocks.keys()

            for shape in ob.data.shape_keys.key_blocks:
                if (current_frame == 0):
                    shape.name = 'Base Shape'
                    shape.keyframe_insert("value", frame=0)
                elif (shape.name == ob.active_shape_key.name):
                    shape.name = "Layer " + str(current_frame)
                    shape.value = 1.0
                    shape.keyframe_insert(
                        "value", frame=ob.active_shape_key_index)
                    bpy.data.scenes['Scene'].frame_current = ob.active_shape_key_index

        # Adds Layer without timeline keyframe
        else:
            bpy.ops.object.shape_key_add(from_mix=False)
            current_frame = bpy.context.active_object.active_shape_key_index
            keys = ob.data.shape_keys.key_blocks.keys()

            for shape in ob.data.shape_keys.key_blocks:
                if (current_frame == 0):
                    shape.name = 'Base Shape'
                elif (shape.name == ob.active_shape_key.name):
                    shape.name = "Layer " + str(current_frame)
                    shape.value = 1.0

        return {'FINISHED'}


class Sculpt_OT_Shape_Key_Hide_Others(bpy.types.Operator):
    """Sculpt Shape Key Hide Other Shape Layers"""
    bl_idname = 'mesh.sculpt_ot_shape_key_hide_others'
    bl_label = 'View Single Shape Layer'
    bl_description = 'Only view selected shape layer.'
    bl_options = {'REGISTER'}

    # check_layer_mute: bpy.props.BoolProperty(
    # name="Solo Layer",
    # description="Hides all other shape layers.",
    # default=False
    # )

    @classmethod
    def poll(cls, context):
        # print(f"My area is: {context.area.type}")
        # sculpt_single_shape_layer = context.scene.sculpt_single_shape_layer
        return context.area.type == 'VIEW_3D'

    def execute(self, context):

        ob = bpy.context.active_object
        sculpt_single_shape_layer = context.scene.sculpt_single_shape_layer

        if context.scene.sculpt_single_shape_layer == True:
            sculpt_single_shape_layer = False
            context.scene.sculpt_single_shape_layer = False
        else:
            sculpt_single_shape_layer = True
            context.scene.sculpt_single_shape_layer = True

            # bpy.ops.preferences.addon_show(module="tmg-mod-tools")

        # current_frame = bpy.context.active_object.active_shape_key_index
        # keys = ob.data.shape_keys.key_blocks.keys()
        # for shape in ob.data.shape_keys.key_blocks:
        # 	if shape.name == ob.active_shape_key.name:
        # 		print('found: ' + shape.name)
        # 		shape.mute = False
        # 	else:
        # 		print('other: ' + shape.name)
        # 		shape.mute = sculpt_single_shape_layer

        return {'FINISHED'}


class Sculpt_OT_Merge_Shape_Keys(bpy.types.Operator):
    """Sculpt Merge Shape Layers To New Layer"""
    bl_idname = 'mesh.sculpt_ot_merge_shape_keys'
    bl_label = 'Merge Visible'
    bl_description = 'Merge visible shape layers to a new layer.'
    bl_options = {'REGISTER'}

    @ classmethod
    def poll(cls, context):
        # print(f"My area is: {context.area.type}")
        # sculpt_single_shape_layer = context.scene.sculpt_single_shape_layer
        return context.area.type == 'VIEW_3D'

    def execute(self, context):

        keys = 0
        ob = bpy.context.active_object
        current_frame = bpy.context.active_object.active_shape_key_index
        keyframe_timeline = context.scene.keyframe_timeline

        for shape in ob.data.shape_keys.key_blocks:
            if keyframe_timeline:
                shape.keyframe_insert(
                    "value", frame=bpy.data.scenes['Scene'].frame_current)
                bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

        bpy.ops.object.shape_key_add(from_mix=True)

        for shape in ob.data.shape_keys.key_blocks:
            if shape.name == ob.active_shape_key.name:
                shape.name = "Applied Shape " + str(current_frame)
                shape.value = 0.0
                if keyframe_timeline:
                    shape.keyframe_insert(
                        "value", frame=ob.active_shape_key_index)
                    bpy.data.scenes['Scene'].frame_current = ob.active_shape_key_index

        return {'FINISHED'}


class Sculpt_OT_Keyframe_Shape_Keys(bpy.types.Operator):
    """Set all shape layer's value on current frame"""
    bl_idname = 'mesh.sculpt_ot_keyframe_shape_keys'
    bl_label = 'Keyframe Layers'
    bl_description = 'Set all shape layers value to current keyframe.'
    bl_options = {'REGISTER'}

    @ classmethod
    def poll(cls, context):
        # print(f"My area is: {context.area.type}")
        return context.area.type == 'VIEW_3D'

    def execute(self, context):

        shape_list = []
        keys = 0
        ob = bpy.context.active_object
        current_frame = bpy.context.active_object.active_shape_key_index
        keys = ob.data.shape_keys.key_blocks.keys()

        for shape in ob.data.shape_keys.key_blocks:
            shape.keyframe_insert(
                "value", frame=bpy.data.scenes['Scene'].frame_current)
            bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

        bpy.ops.object.shape_key_add(from_mix=True)

        for shape in ob.data.shape_keys.key_blocks:
            if shape.name == ob.active_shape_key.name:
                shape.name = "Applied Shape " + str(current_frame)
                shape.value = 0.0
                shape.keyframe_insert("value", frame=ob.active_shape_key_index)
                bpy.data.scenes['Scene'].frame_current = ob.active_shape_key_index

        return {'FINISHED'}


class Sculpt_OT_Keyframe_Shape_Keys(bpy.types.Operator):
    """Set all shape layer's value on current frame"""
    bl_idname = 'mesh.sculpt_ot_keyframe_shape_keys'
    bl_label = 'Keyframe Layers'
    bl_description = 'Set all shape layers value to current keyframe.'
    bl_options = {'REGISTER'}

    @ classmethod
    def poll(cls, context):
        # print(f"My area is: {context.area.type}")
        return context.area.type == 'VIEW_3D'

    def execute(self, context):

        shape_list = []
        keys = 0
        ob = bpy.context.active_object
        current_frame = bpy.context.active_object.active_shape_key_index
        keys = ob.data.shape_keys.key_blocks.keys()

        for shape in ob.data.shape_keys.key_blocks:
            shape.keyframe_insert(
                "value", frame=bpy.data.scenes['Scene'].frame_current)
            bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

        return {'FINISHED'}


class Sculpt_OT_Clear_All_Keyframes(bpy.types.Operator):
    """Clears all keyframes from timeline"""
    bl_idname = 'mesh.sculpt_ot_clear_all_keyframes'
    bl_label = 'Clear All Keyframes'
    bl_description = 'Clears all keyframes from timeline.'
    bl_options = {'REGISTER'}

    @ classmethod
    def poll(cls, context):
        # print(f"My area is: {context.area.type}")
        return context.area.type == 'VIEW_3D'

    def execute(self, context):

        ob = bpy.context.active_object
        keys = ob.data.shape_keys.key_blocks.keys()

        s = bpy.data.scenes['Scene']

        for fr in range(0, len(keys)):
            s.frame_current = fr
            for shape in ob.data.shape_keys.key_blocks:
                if bpy.data.actions:
                    try:
                        shape.keyframe_delete(
                            "value", index=-1, frame=fr, group="")
                        # print("Removed Frame: % s" % fr)
                    except RuntimeError:
                        break

        bpy.data.scenes['Scene'].frame_current = 0

        return {'FINISHED'}


class Sculpt_OT_Apply_Shape_Keys(bpy.types.Operator):
    """Sculpt Apply Layers"""
    bl_idname = 'mesh.sculpt_ot_apply_shape_keys'
    bl_label = 'Apply Layers'
    bl_description = 'Merges all layers then removes all shape keys from the selected object.'
    bl_options = {'REGISTER'}

    # check_layer_mute: bpy.props.BoolProperty(
    # name="Solo Layer",
    # description="Hides all other shape layers.",
    # default=False
    # )

    @ classmethod
    def poll(cls, context):
        # print(f"My area is: {context.area.type}")
        return context.area.type == 'VIEW_3D'

    def execute(self, context):

        shape_list = []
        keys = 0
        ob = bpy.context.active_object
        current_frame = bpy.context.active_object.active_shape_key_index
        keys = ob.data.shape_keys.key_blocks.keys()

        # Apply all layers to shape
        for shape in ob.data.shape_keys.key_blocks:
            shape.keyframe_insert(
                "value", frame=bpy.data.scenes['Scene'].frame_current)
            bpy.data.scenes['Scene'].frame_current = bpy.data.scenes['Scene'].frame_current

        bpy.ops.object.shape_key_add(from_mix=True)

        for shape in ob.data.shape_keys.key_blocks:
            if shape.name == ob.active_shape_key.name:
                shape.name = "Applied Shape"
                shape.value = 1.0
                shape.keyframe_insert("value", frame=ob.active_shape_key_index)
                bpy.data.scenes['Scene'].frame_current = ob.active_shape_key_index
            else:
                shape_list.append(shape)

        for i in (shape_list):
            # setting the active shapekey
            iIndex = ob.data.shape_keys.key_blocks.keys().index(i.name)
            ob.active_shape_key_index = iIndex

            # delete it
            bpy.ops.object.shape_key_remove()

        bpy.ops.object.shape_key_remove()
        bpy.data.scenes['Scene'].frame_current = 0

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

# for creating an object that wraps around the sculpt object
# subdiv_loop = []
# subdivisions = 3

# if subdivisions > 0:
#     subdiv_loop.append(int(subdivisions))
#     subdivisions -= 1

# ## Add Multires
# bpy.ops.object.modifier_add(type='MULTIRES')

# for i in subdiv_loop:
#     bpy.ops.object.multires_subdivide(modifier="Multires")
#     print(str(id))

# ## Add Shrinkwrap
# bpy.ops.object.modifier_add(type='SHRINKWRAP')
# bpy.context.object.modifiers["Shrinkwrap"].target = bpy.data.objects["rock"]
# bpy.context.object.modifiers["Shrinkwrap"].wrap_mode = 'ABOVE_SURFACE'
# bpy.context.object.modifiers["Shrinkwrap"].wrap_method = 'TARGET_PROJECT'

# ## Add Smooth
# bpy.ops.object.modifier_add(type='SMOOTH')
# bpy.context.object.modifiers["Smooth"].factor = 2

# ## Object Smooth Shading
# bpy.ops.object.shade_smooth()
