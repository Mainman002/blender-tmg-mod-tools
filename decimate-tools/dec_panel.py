import bpy

class DEC_PT_Object_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_object_panel'
    bl_category = 'Edit'
    bl_label = 'Decimate Tools'
    bl_context = "objectmode"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):

        obj = bpy.context.view_layer.objects.active
        sel_mode = context.tool_settings.mesh_select_mode

        solid_offset = context.scene.solid_offset
        solid_thickness = context.scene.solid_thickness

        check_settings = context.scene.check_settings
        check_mods = context.scene.check_mods
        check_adds = context.scene.check_adds
        check_splines = context.scene.check_splines

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

        #### Settings Tab Panel Layout Controllers #########################

        Settings_Col = Master_Col.column(align=True)
        Settings_Subcol = Settings_Col.column()
        Settings_Row = Settings_Col.row()

        #### Settings Tab  ############################################################################################################

        if check_settings == False:
            Settings_Col.prop(context.scene, "check_settings", text="Settings", icon="RIGHTARROW")
        else:
            Settings_Col.prop(context.scene, "check_settings", text="Settings", icon="DOWNARROW_HLT")

            Settings_Col = Master_Col.column() ###### Box if needed for Settings Panel #############
            Settings_Subcol = Settings_Col.column(align=True)

            Settings_Row = Settings_Subcol.row()
            Settings_Row.label(text="Mod Axis:")

            Settings_Row = Settings_Subcol.row()
            Settings_Row.prop(context.scene, "axis_mod", text="")

            Settings_Row = Settings_Subcol.row()
            Settings_Row.label(text="Solidify:")

            Settings_Row = Settings_Subcol.column()

            Settings_Col.use_property_split = True
            Settings_Flow = Settings_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            colm = Settings_Flow.column()

            Settings_Col = colm.row()
            Settings_Col.label(text="Offset")
            Settings_Col.prop(context.scene, "solid_offset", text="")

            colm = Settings_Flow.column()

            Settings_Col = colm.row()
            Settings_Col.label(text="Thickness")
            Settings_Col.prop(context.scene, "solid_thickness", text="")

            Settings_Col = Master_Col.column()  ###### Box if needed for Settings Panel #############

            if context.view_layer.objects.active:

                Settings_Col.operator('wm.mod_object_ot_operator', text='Add Modifiers', icon="MODIFIER")

            Settings_Row = Settings_Col.column()
 
            Settings_Col.use_property_split = True
            Settings_Flow2 = Settings_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

            Mod_ColM = Settings_Flow2.column()

            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Screw")
            Settings_Col.prop(context.scene, "mod_screw", text="", icon="MOD_SCREW")
            
            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Mirror")
            Settings_Col.prop(context.scene, "mod_mirror", text="", icon="MOD_MIRROR")

            Mod_ColM = Settings_Flow2.column()

            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Subsurface")
            Settings_Col.prop(context.scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Solidify")
            Settings_Col.prop(context.scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

            Mod_ColM = Settings_Flow2.column()

            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Bevel")
            Settings_Col.prop(context.scene, "mod_bevel", text="", icon="MOD_BEVEL")

            Mod_ColM = Settings_Flow2.column()

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


class DEC_PT_Edit_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_edit_panel'
    bl_category = 'Edit'
    bl_label = 'Decimate Tools'
    bl_context = "mesh_edit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
 
    def draw(self, context):

        obj = bpy.context.view_layer.objects.active
        sel_mode = context.tool_settings.mesh_select_mode

        solid_offset = context.scene.solid_offset
        solid_thickness = context.scene.solid_thickness

        check_settings = context.scene.check_settings
        check_mods = context.scene.check_mods
        check_adds = context.scene.check_adds
        check_splines = context.scene.check_splines

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

        #### Settings Tab Panel Layout Controllers #########################

        Settings_Col = Master_Col.column(align=True)
        Settings_Subcol = Settings_Col.column()
        Settings_Row = Settings_Col.row()

        #### Settings Tab  ############################################################################################################

        if check_settings == False:
            Settings_Col.prop(context.scene, "check_settings", text="Settings", icon="RIGHTARROW")
        else:
            Settings_Col.prop(context.scene, "check_settings", text="Settings", icon="DOWNARROW_HLT")

            Settings_Col = Master_Col.column() ###### Box if needed for Settings Panel #############
            Settings_Subcol = Settings_Col.column(align=True)

            Settings_Row = Settings_Subcol.row()
            Settings_Row.label(text="Mod Axis:")

            Settings_Row = Settings_Subcol.row()
            Settings_Row.prop(context.scene, "axis_mod", text="")

            Settings_Row = Settings_Subcol.row()
            Settings_Row.label(text="Solidify:")

            Settings_Row = Settings_Subcol.column()

            Settings_Col.use_property_split = True
            Settings_Flow = Settings_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

            colm = Settings_Flow.column()

            Settings_Col = colm.row()
            Settings_Col.label(text="Offset")
            Settings_Col.prop(context.scene, "solid_offset", text="")

            colm = Settings_Flow.column()

            Settings_Col = colm.row()
            Settings_Col.label(text="Thickness")
            Settings_Col.prop(context.scene, "solid_thickness", text="")

            Settings_Col = Master_Col.column()  ###### Box if needed for Settings Panel #############

            if context.view_layer.objects.active:

                Settings_Col.operator('wm.mod_edit_ot_operator', text='Add Modifiers', icon="MODIFIER")

            Settings_Row = Settings_Col.column()
 
            Settings_Col.use_property_split = True
            Settings_Flow2 = Settings_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=True)

            Mod_ColM = Settings_Flow2.column()

            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Screw")
            Settings_Col.prop(context.scene, "mod_screw", text="", icon="MOD_SCREW")
            
            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Mirror")
            Settings_Col.prop(context.scene, "mod_mirror", text="", icon="MOD_MIRROR")

            Mod_ColM = Settings_Flow2.column()

            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Subsurface")
            Settings_Col.prop(context.scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Solidify")
            Settings_Col.prop(context.scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

            Mod_ColM = Settings_Flow2.column()

            Settings_Col = Mod_ColM.row()
            Settings_Col.label(text="Bevel")
            Settings_Col.prop(context.scene, "mod_bevel", text="", icon="MOD_BEVEL")

            Mod_ColM = Settings_Flow2.column()

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

        DecTools_Col = Master_Col.column(align=True)
        DecTools_SubCol = DecTools_Col.column()
        DecTools_Row = DecTools_Col.row()

        if check_mods == False:
            DecTools_Col.prop(context.scene, "check_mods", text="Decimate Tools", icon="RIGHTARROW")
        else:
            DecTools_Col.prop(context.scene, "check_mods", text="Decimate Tools", icon="DOWNARROW_HLT")

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

                DecTools_ColM = DecTools_Flow.column()

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
