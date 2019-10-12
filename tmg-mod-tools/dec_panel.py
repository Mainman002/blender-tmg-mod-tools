import bpy

class DEC_PT_Object_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_object_panel'
    bl_category = 'Edit'
    bl_label = 'TMG Mod Tools'
    bl_context = "objectmode"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):

        obj = bpy.context.view_layer.objects.active
        sel_mode = context.tool_settings.mesh_select_mode

        solid_offset = context.scene.solid_offset
        solid_thickness = context.scene.solid_thickness

        check_view = context.scene.check_view
        check_modifiers = context.scene.check_modifiers
        check_mods = context.scene.check_mods
        check_adds = context.scene.check_adds
        check_splines = context.scene.check_splines

        axis_mode = context.scene.axis_mod
        mod_solid = context.scene.mod_solid
        mod_bevel = context.scene.mod_bevel
        mod_subsurf = context.scene.mod_subsurf

        ui_viewMode = context.scene.ui_viewMode

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
            View_Col.prop(context.scene, "check_view", text="View", icon="RIGHTARROW")
        else:
            View_Col.prop(context.scene, "check_view", text="View", icon="DOWNARROW_HLT")

            View_Col = Master_Col.column() ###### Box if needed for View Panel #############
            View_Subcol = View_Col.column(align=True)

            View_Col.use_property_split = True
            View_Flow = View_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            colm = View_Flow.column()

            View_Col = colm.row()
            View_Col.label(text="Apply Modifiers:")
            View_Col.operator('wm.mod_apply_object_ot_operator', text='', icon='MODIFIER')

            colm = View_Flow.column()

            View_Col = colm.row()
            View_Col.label(text="Distraction Free View:")
            View_Col.operator('wm.ui_distraction_free_ot_operator', text='', icon='RESTRICT_RENDER_OFF')

        #### Modifiers Tab Panel Layout Controllers #########################

        Modifiers_Col = Master_Col.column(align=True)
        Modifiers_Subcol = Modifiers_Col.column()
        Modifiers_Row = Modifiers_Col.row()

        #### Modifiers Tab  ############################################################################################################

        if check_modifiers == False:
            Modifiers_Col.prop(context.scene, "check_modifiers", text="Modifiers", icon="RIGHTARROW")
        else:
            Modifiers_Col.prop(context.scene, "check_modifiers", text="Modifiers", icon="DOWNARROW_HLT")

            Modifiers_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
            Modifiers_Subcol = Modifiers_Col.column(align=True)

            Modifiers_Row = Modifiers_Subcol.row()
            Modifiers_Row.label(text="Mod Axis:")

            Modifiers_Row = Modifiers_Subcol.row()
            Modifiers_Row.prop(context.scene, "axis_mod", text="")

            Modifiers_Row = Modifiers_Subcol.row()
            Modifiers_Row.label(text="Solidify:")

            Modifiers_Row = Modifiers_Subcol.column()

            Modifiers_Col.use_property_split = True
            Modifiers_Flow = Modifiers_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            colm = Modifiers_Flow.column()

            Modifiers_Col = colm.row()
            Modifiers_Col.label(text="Offset")
            Modifiers_Col.prop(context.scene, "solid_offset", text="")

            colm = Modifiers_Flow.column()

            Modifiers_Col = colm.row()
            Modifiers_Col.label(text="Thickness")
            Modifiers_Col.prop(context.scene, "solid_thickness", text="")

            Modifiers_Col = Master_Col.column()  ###### Box if needed for Modifiers Panel #############

            if context.view_layer.objects.active:

                Modifiers_Col.operator('wm.mod_object_ot_operator', text='Add Modifiers', icon="MODIFIER")
 
            Modifiers_Col.use_property_split = True
            Modifiers_Flow2 = Modifiers_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

            Mod_ColM = Modifiers_Flow2.column()

            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Screw")
            Modifiers_Col.prop(context.scene, "mod_screw", text="", icon="MOD_SCREW")
            
            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Mirror")
            Modifiers_Col.prop(context.scene, "mod_mirror", text="", icon="MOD_MIRROR")

            Mod_ColM = Modifiers_Flow2.column()

            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Subsurface")
            Modifiers_Col.prop(context.scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Solidify")
            Modifiers_Col.prop(context.scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

            Mod_ColM = Modifiers_Flow2.column()

            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Bevel")
            Modifiers_Col.prop(context.scene, "mod_bevel", text="", icon="MOD_BEVEL")

            Mod_ColM = Modifiers_Flow2.column()

        #### Add Objects Tab Panel Layout Controllers #########################

        AddObjects_Col = Master_Col.column(align=True)
        AddObjects_SubCol = AddObjects_Col.column()
        AddObjects_Row = AddObjects_Col.row()

        #### Add Objects Tab  ############################################################################################################

        if check_adds == False:
            AddObjects_Col.prop(context.scene, "check_adds", text="Add Objects", icon="RIGHTARROW")
        else:
            AddObjects_Col.prop(context.scene, "check_adds", text="Add Objects", icon="DOWNARROW_HLT")

            AddObjects_Col = Master_Col.column() ###### Box if needed for Add Objects Panel #############
            AddObjects_SubCol = AddObjects_Col.column(align=True)

            AddObjects_Col.use_property_split = True
            AddObjects_Flow = AddObjects_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            AddObjects_ColM = AddObjects_Flow.column()

            AddObjects_Col = AddObjects_ColM.row()
            AddObjects_Col.operator('wm.add_solid_plane_object_ot_operator', text='Add Plane Object')

            AddObjects_ColM = AddObjects_Flow.column()

            AddObjects_Col = AddObjects_ColM.row()
            AddObjects_Col.operator('wm.add_solid_circle_object_ot_operator', text='Add Circle Object')

            AddObjects_ColM = AddObjects_Flow.column()

            if axis_mode == "X": # Y

                AddObjects_Col = AddObjects_ColM.row()
                AddObjects_Col.operator('wm.add_arch_object_x_ot_operator', text='Add Arch Object')

            elif axis_mode == "Y": # Y

                AddObjects_Col = AddObjects_ColM.row()
                AddObjects_Col.operator('wm.add_arch_object_y_ot_operator', text='Add Arch Object')

                AddObjects_ColM = AddObjects_Flow.column()

                AddObjects_Col = AddObjects_ColM.row() 
                AddObjects_Col.operator('wm.add_pipe_line_object_y_ot_operator', text='Add Pipe Object')

            elif axis_mode == "Z": # Z

                AddObjects_Col = AddObjects_ColM.row()
                AddObjects_Col.operator('wm.add_arch_object_z_ot_operator', text='Add Arch Object')

                AddObjects_ColM = AddObjects_Flow.column()

                AddObjects_Col = AddObjects_ColM.row()
                AddObjects_Col.operator('wm.add_pipe_line_object_z_ot_operator', text='Add Pipe Object')

        #### Add Splines Tab Panel Layout Controllers #########################

        AddSplines_Col = Master_Col.column(align=True)
        AddSplines_SubCol = AddSplines_Col.column()
        AddSplines_Row = AddSplines_Col.row()

        #### Add Splines Tab  ############################################################################################################

        if check_splines == False:
            if axis_mode == "Y": # Y:
                AddSplines_Col.prop(context.scene, "check_splines", text="Add Splines", icon="RIGHTARROW")
        else:
            if axis_mode == "Y": # Y:
                AddSplines_Col.prop(context.scene, "check_splines", text="Add Splines", icon="DOWNARROW_HLT")

                AddSplines_Col = Master_Col.column() ###### Box if needed for Add Splines Panel #############
                AddSplines_SubCol = AddSplines_Col.column(align=True)

                AddSplines_Col.use_property_split = True
                AddSplines_Flow = AddSplines_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

                AddSplines_Col = AddSplines_Flow.row()
                AddSplines_Col.operator('wm.add_basic_spline_y_ot_operator', text='Add Basic Spline')

                AddSplines_Col = AddSplines_Flow.row()
                AddSplines_Col.operator('wm.add_pipe_spline_y_ot_operator', text='Add Smooth Spline')

                #AddSplines_Col = AddSplines_Flow.row()
                #AddSplines_Col.operator('wm.add_spline_folow_y_ot_operator', text='Add Spline Follow Cube')


class DEC_PT_Edit_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_edit_panel'
    bl_category = 'Edit'
    bl_label = 'TMG Mod Tools'
    bl_context = "mesh_edit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
 
    def draw(self, context):

        obj = bpy.context.view_layer.objects.active
        sel_mode = context.tool_settings.mesh_select_mode

        solid_offset = context.scene.solid_offset
        solid_thickness = context.scene.solid_thickness

        check_view = context.scene.check_view
        check_modifiers = context.scene.check_modifiers
        check_mods = context.scene.check_mods
        check_adds = context.scene.check_adds
        check_splines = context.scene.check_splines
        check_decimations = context.scene.check_decimations

        axis_mode = context.scene.axis_mod
        mod_solid = context.scene.mod_solid
        mod_bevel = context.scene.mod_bevel
        mod_subsurf = context.scene.mod_subsurf

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
            View_Col.prop(context.scene, "check_view", text="View", icon="RIGHTARROW")
        else:
            View_Col.prop(context.scene, "check_view", text="View", icon="DOWNARROW_HLT")

            View_Col = Master_Col.column() ###### Box if needed for View Panel #############
            View_Subcol = View_Col.column(align=True)

            View_Col.use_property_split = True
            View_Flow = View_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            colm = View_Flow.column()

            View_Col = colm.row()
            View_Col.label(text="Apply Modifiers:")
            View_Col.operator('wm.mod_apply_object_ot_operator', text='', icon='MODIFIER')

            colm = View_Flow.column()

            View_Col = colm.row()
            View_Col.label(text="Distraction Free View:")
            View_Col.operator('wm.ui_distraction_free_ot_operator', text='', icon='RESTRICT_RENDER_OFF')

        #### Modifiers Tab Panel Layout Controllers #########################

        Modifiers_Col = Master_Col.column(align=True)
        Modifiers_Subcol = Modifiers_Col.column()
        Modifiers_Row = Modifiers_Col.row()

        #### Modifiers Tab  ############################################################################################################

        if check_modifiers == False:
            Modifiers_Col.prop(context.scene, "check_modifiers", text="Modifiers", icon="RIGHTARROW")
        else:
            Modifiers_Col.prop(context.scene, "check_modifiers", text="Modifiers", icon="DOWNARROW_HLT")

            Modifiers_Col = Master_Col.column() ###### Box if needed for Modifiers Panel #############
            Modifiers_Subcol = Modifiers_Col.column(align=True)

            Modifiers_Row = Modifiers_Subcol.row()
            Modifiers_Row.label(text="Mod Axis:")

            Modifiers_Row = Modifiers_Subcol.row()
            Modifiers_Row.prop(context.scene, "axis_mod", text="")

            Modifiers_Row = Modifiers_Subcol.row()
            Modifiers_Row.label(text="Solidify:")

            Modifiers_Row = Modifiers_Subcol.column()

            Modifiers_Col.use_property_split = True
            Modifiers_Flow = Modifiers_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            colm = Modifiers_Flow.column()

            Modifiers_Col = colm.row()
            Modifiers_Col.label(text="Offset")
            Modifiers_Col.prop(context.scene, "solid_offset", text="")

            colm = Modifiers_Flow.column()

            Modifiers_Col = colm.row()
            Modifiers_Col.label(text="Thickness")
            Modifiers_Col.prop(context.scene, "solid_thickness", text="")

            Modifiers_Col = Master_Col.column()  ###### Box if needed for Modifiers Panel #############

            if context.view_layer.objects.active:

                Modifiers_Col.operator('wm.mod_object_ot_operator', text='Add Modifiers', icon="MODIFIER")

            Modifiers_Row = Modifiers_Col.column()
 
            Modifiers_Col.use_property_split = True
            Modifiers_Flow2 = Modifiers_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

            Mod_ColM = Modifiers_Flow2.column()

            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Screw")
            Modifiers_Col.prop(context.scene, "mod_screw", text="", icon="MOD_SCREW")
            
            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Mirror")
            Modifiers_Col.prop(context.scene, "mod_mirror", text="", icon="MOD_MIRROR")

            Mod_ColM = Modifiers_Flow2.column()

            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Subsurface")
            Modifiers_Col.prop(context.scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Solidify")
            Modifiers_Col.prop(context.scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

            Mod_ColM = Modifiers_Flow2.column()

            Modifiers_Col = Mod_ColM.row()
            Modifiers_Col.label(text="Bevel")
            Modifiers_Col.prop(context.scene, "mod_bevel", text="", icon="MOD_BEVEL")

            Mod_ColM = Modifiers_Flow2.column()

        #### Add Objects Tab  #############################################

        AddObjects_Col = Master_Col.column(align=True)
        AddObjects_SubCol = AddObjects_Col.column()
        AddObjects_Row = AddObjects_Col.row()

        #### Add Objects Tab  ############################################################################################################

        if check_adds == False:
            AddObjects_Col.prop(context.scene, "check_adds", text="Add Objects", icon="RIGHTARROW")
        else:
            AddObjects_Col.prop(context.scene, "check_adds", text="Add Objects", icon="DOWNARROW_HLT")

            AddObjects_Col = Master_Col.column() ###### Box if needed for Settings Panel #############
            AddObjects_SubCol = AddObjects_Col.column(align=True)

            AddObjects_Col.use_property_split = True
            AddObjects_Flow = AddObjects_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            AddObjects_ColM = AddObjects_Flow.column()

            AddObjects_Col = AddObjects_ColM.row()
            AddObjects_Col.operator('wm.add_solid_plane_object_ot_operator', text='Add Plane Object')

            AddObjects_ColM = AddObjects_Flow.column()

            AddObjects_Col = AddObjects_ColM.row()
            AddObjects_Col.operator('wm.add_solid_circle_object_ot_operator', text='Add Circle Object')

            AddObjects_ColM = AddObjects_Flow.column()

            if axis_mode == "X": # Y

                AddObjects_Col = AddObjects_ColM.row()
                AddObjects_Col.operator('wm.add_arch_object_x_ot_operator', text='Add Arch Object')

            elif axis_mode == "Y": # Y

                AddObjects_Col = AddObjects_ColM.row()
                AddObjects_Col.operator('wm.add_arch_object_y_ot_operator', text='Add Arch Object')

                AddObjects_ColM = AddObjects_Flow.column()

                AddObjects_Col = AddObjects_ColM.row() 
                AddObjects_Col.operator('wm.add_pipe_line_object_y_ot_operator', text='Add Pipe Object')

            elif axis_mode == "Z": # Z

                AddObjects_Col = AddObjects_ColM.row()
                AddObjects_Col.operator('wm.add_arch_object_z_ot_operator', text='Add Arch Object')

                AddObjects_ColM = AddObjects_Flow.column()

                AddObjects_Col = AddObjects_ColM.row()
                AddObjects_Col.operator('wm.add_pipe_line_object_z_ot_operator', text='Add Pipe Object')

        #### Add Splines Tab  ######################################

        AddSplines_Col = Master_Col.column(align=True)
        AddSplines_SubCol = AddSplines_Col.column()
        AddSplines_Row = AddSplines_Col.row()

        #### Add Splines Tab  ############################################################################################################

        if check_splines == False:
            if axis_mode == "Y": # Y:
                AddSplines_Col.prop(context.scene, "check_splines", text="Add Splines", icon="RIGHTARROW")
        else:
            if axis_mode == "Y": # Y:
                AddSplines_Col.prop(context.scene, "check_splines", text="Add Splines", icon="DOWNARROW_HLT")

                AddSplines_Col = Master_Col.column() ###### Box if needed for Settings Panel #############
                AddSplines_SubCol = AddSplines_Col.column(align=True)

                AddSplines_Col.use_property_split = True
                AddSplines_Flow = AddSplines_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

                AddSplines_Col = AddSplines_Flow.row()
                AddSplines_Col.operator('wm.add_basic_spline_y_ot_operator', text='Add Basic Spline')

                AddSplines_Col = AddSplines_Flow.row()
                AddSplines_Col.operator('wm.add_pipe_spline_y_ot_operator', text='Add Smooth Spline')

        #### Decimate Tools Tab  ######################################

        DecTools_Col = Master_Col.column(align=True)
        DecTools_SubCol = DecTools_Col.column()
        DecTools_Row = DecTools_Col.row()

        #### Decimate Tools Tab  ##########################################################################################################

        if check_decimations == False:
            DecTools_Col.prop(context.scene, "check_decimations", text="Decimate", icon="RIGHTARROW")
        else:
            DecTools_Col.prop(context.scene, "check_decimations", text="Decimate", icon="DOWNARROW_HLT")

            DecTools_Col = Master_Col.column() ###### Box if needed for Settings Panel #############
            DecTools_SubCol = DecTools_Col.column(align=True)

            DecTools_Col.use_property_split = True
            DecTools_Flow = DecTools_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            DecTools_ColM = DecTools_Flow.column()

            DecTools_Col = DecTools_ColM.row()

            if sel_mode[1]: # edge

                DecTools_Col = DecTools_ColM.row()
                DecTools_Col.operator('wm.dec_verts_ot_operator', text='Decimate Verts')

                DecTools_ColM = DecTools_Flow.column()

                DecTools_Col = DecTools_ColM.row()
                DecTools_Col.operator('wm.dec_edge_ot_operator', text='Decimate Edges')

            elif sel_mode[0]: # vertex

                DecTools_Col = DecTools_ColM.row()
                DecTools_Col.operator('wm.dec_verts_ot_operator', text='Decimate Verts')


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
