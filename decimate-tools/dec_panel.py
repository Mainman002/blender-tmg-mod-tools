import bpy
from bpy.types import Panel

class DEC_PT_Edit_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_edit_panel'
    bl_category = 'Edit'
    bl_label = 'Decimate Tools'
    bl_context = "mesh_edit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
 
    def draw(self, context):

        obj = bpy.context.view_layer.objects.active
        obj = context.object

        solid_offset = context.scene.solid_offset
        solid_thickness = context.scene.solid_thickness

        check_settings = context.scene.check_settings
        check_mods = context.scene.check_mods
        check_adds = context.scene.check_adds

        sel_mode = context.tool_settings.mesh_select_mode
        axis_mode = context.scene.axis_mod
        mod_solid = context.scene.mod_solid
        mod_bevel = context.scene.mod_bevel
        mod_subsurf = context.scene.mod_subsurf

        layout = self.layout

        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        view = context.space_data

        col = layout.column(align=True)
        subcol = col.column()

        if check_settings == False:
            subcol.prop(context.scene, "check_settings", text="Settings", icon="RIGHTARROW")
        else:
            subcol.prop(context.scene, "check_settings", text="Settings", icon="DOWNARROW_HLT")

            col = layout.column(align=True)
            subcol = col.row()
            row = subcol

            row = subcol.row()
            row.label(text="Mod Axis:")

            #row = subcol.row()
            row.prop(context.scene, "axis_mod", text="")

            col = layout.column(align=True)
            subcol = col.row()
            row = subcol
            row.label(text="Solidify:")

            col = layout.column(align=True)
            subcol = col.column()
            row = subcol
            row.prop(context.scene, "solid_offset", text="Offset")

            row = subcol.row()
            row.prop(context.scene, "solid_thickness", text="Thickness")

            if context.view_layer.objects.active:

                col.operator('wm.mod_edit_ot_operator', text='Add Modifiers', icon="MODIFIER")

            row = col.column()

            #layout = self.layout    
            layout.use_property_split = True
            flow = layout.grid_flow(row_major=True, columns=0, even_columns=False, even_rows=False, align=True)

            colm = flow.column()

            col = colm.row()
            col.label(text="Screw")
            col.prop(context.scene, "mod_screw", text="", icon="MOD_SCREW")
            
            col = colm.row()
            col.label(text="Mirror")
            col.prop(context.scene, "mod_mirror", text="", icon="MOD_MIRROR")

            colm = flow.column()

            col = colm.row()
            col.label(text="Subsurface")
            col.prop(context.scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

            col = colm.row()
            col.label(text="Solidify")
            col.prop(context.scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

            colm = flow.column()

            col = colm.row()
            col.label(text="Bevel")
            col.prop(context.scene, "mod_bevel", text="", icon="MOD_BEVEL")

            row = subcol.column()

            row_smooth = row.row()
            col_smooth_lbl = row_smooth.row()
            row = col_smooth_lbl.row()

            #if context.view_layer.objects.active:

                #row_smooth.operator('wm.mod_edit_ot_operator', text='Add Modifiers', icon="MODIFIER")

        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        view = context.space_data

        col = layout.column(align=True)
        subcol = col.column()

        if check_mods == False:
            subcol.prop(context.scene, "check_mods", text="Add Mods", icon="RIGHTARROW")
        else:
            subcol.prop(context.scene, "check_mods", text="Add Mods", icon="DOWNARROW_HLT")

            row = layout.row(align=True)

            if sel_mode[1]: # edge

                row_smooth = col.row()
                col_smooth_lbl = row_smooth.column()
                col_smooth_lbl.label(text="Decimate Tools")

                row = col.column()
                row.operator('wm.dec_verts_ot_operator', text='Decimate Verts')
                row.operator('wm.dec_edge_ot_operator', text='Decimate Edges')

            elif sel_mode[0]: # vertex

                row_smooth = col.row()
                col_smooth_lbl = row_smooth.column()
                col_smooth_lbl.label(text="Decimate Tools")

                row = col.column()
                row.operator('wm.dec_verts_ot_operator', text='Decimate Verts')

class DEC_PT_Object_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_object_panel'
    bl_category = 'Edit'
    bl_label = 'Decimate Tools'
    bl_context = "objectmode"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):

        obj = bpy.context.view_layer.objects.active
        #OB.select_set(action='SELECT')
        #obj = context.object

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

        view = context.space_data

        col = layout.column(align=True)
        subcol = col.column()

        if check_settings == False:
            subcol.prop(context.scene, "check_settings", text="Settings", icon="RIGHTARROW")
        else:
            subcol.prop(context.scene, "check_settings", text="Settings", icon="DOWNARROW_HLT")

            col = layout.column(align=True)
            subcol = col.row()
            row = subcol

            row = subcol.row()
            row.label(text="Mod Axis:")

            #row = subcol.row()
            row.prop(context.scene, "axis_mod", text="")

            col = layout.column(align=True)
            subcol = col.row()
            row = subcol
            row.label(text="Solidify:")

            col = layout.column(align=True)
            subcol = col.column()
            row = subcol
            row.prop(context.scene, "solid_offset", text="Offset")

            row = subcol.row()
            row.prop(context.scene, "solid_thickness", text="Thickness")

            if context.view_layer.objects.active:

                col.operator('wm.mod_object_ot_operator', text='Add Modifiers', icon="MODIFIER")

            row = col.column()

            #layout = self.layout    
            layout.use_property_split = True
            flow = layout.grid_flow(row_major=True, columns=0, even_columns=False, even_rows=False, align=True)

            colm = flow.column()

            col = colm.row()
            col.label(text="Screw")
            col.prop(context.scene, "mod_screw", text="", icon="MOD_SCREW")
            
            col = colm.row()
            col.label(text="Mirror")
            col.prop(context.scene, "mod_mirror", text="", icon="MOD_MIRROR")

            colm = flow.column()

            col = colm.row()
            col.label(text="Subsurface")
            col.prop(context.scene, "mod_subsurf", text="", icon="MOD_SUBSURF")

            col = colm.row()
            col.label(text="Solidify")
            col.prop(context.scene, "mod_solid", text="", icon="MOD_SOLIDIFY")

            colm = flow.column()

            col = colm.row()
            col.label(text="Bevel")
            col.prop(context.scene, "mod_bevel", text="", icon="MOD_BEVEL")

            row = subcol.column()

        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        view = context.space_data

        col = layout.column(align=True)
        subcol = col.column()

        if check_adds == False:
            subcol.prop(context.scene, "check_adds", text="Add Objects", icon="RIGHTARROW")
        else:
            subcol.prop(context.scene, "check_adds", text="Add Objects", icon="DOWNARROW_HLT")

            col.operator('wm.add_solid_plane_object_ot_operator', text='Add Plane Object')
            col.operator('wm.add_solid_circle_object_ot_operator', text='Add Circle Object')

            if axis_mode == "X": # Y
                col.operator('wm.add_arch_object_x_ot_operator', text='Add Arch Object')
            elif axis_mode == "Y": # Y
                col.operator('wm.add_arch_object_y_ot_operator', text='Add Arch Object')
                col.operator('wm.add_pipe_line_object_y_ot_operator', text='Add Pipe Object')
            elif axis_mode == "Z": # Z
                col.operator('wm.add_arch_object_z_ot_operator', text='Add Arch Object')
                col.operator('wm.add_pipe_line_object_z_ot_operator', text='Add Pipe Object')

        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        view = context.space_data

        col = layout.column(align=True)
        subcol = col.column()

        if check_splines == False:
            if axis_mode == "Y": # Y:
                subcol.prop(context.scene, "check_splines", text="Add Splines", icon="RIGHTARROW")
        else:
            if axis_mode == "Y": # Y:
                subcol.prop(context.scene, "check_splines", text="Add Splines", icon="DOWNARROW_HLT")

                col.operator('wm.add_basic_spline_y_ot_operator', text='Add Basic Spline')
                col.operator('wm.add_pipe_spline_y_ot_operator', text='Add Smooth Spline')



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
