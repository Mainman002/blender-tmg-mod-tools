import bpy
from bpy.types import Panel

# define classes for registration
#DEC_Classes = (
    #VIEW3D_MT_edit_mesh_looptools,
    #LoopToolsProps,
    #DEC_PT_Edit_Panel,
    #DEC_PT_Object_Panel,
#)

class DEC_PT_Edit_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_edit_panel'
    bl_category = 'Edit'
    bl_label = 'Decimate Tools'
    bl_context = "mesh_edit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
 
    def draw(self, context):
        sel_mode = context.tool_settings.mesh_select_mode
        axis_mode = context.scene.axis_mod
        layout = self.layout

        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Modifier Tools")

        row = layout.column()
        row.operator('wm.mod_spin_edit_ot_operator', text='Modifier Spin Edge')
        row.operator('wm.mod_solidify_plane_edit_ot_operator', text='Modifier Solidify Plane')

        if sel_mode[1]: # edge

            row_smooth = layout.row()
            col_smooth_lbl = row_smooth.column()
            col_smooth_lbl.label(text="Decimate Tools")

            row = layout.column()
            row.operator('wm.dec_edge_ot_operator', text='Decimate Edges')
        elif sel_mode[0]: # vertex
            row_smooth = layout.row()
            col_smooth_lbl = row_smooth.column()
            col_smooth_lbl.label(text="Decimate Tools")

            row = layout.column()
            row.operator('wm.dec_verts_ot_operator', text='Decimate Verts')

class DEC_PT_Object_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_object_panel'
    bl_category = 'Edit'
    bl_label = 'Decimate Tools'
    bl_context = "objectmode"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        axis_mode = context.scene.axis_mod
        layout = self.layout

        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Modifier Tools")

        row = layout.column()
        row.operator('wm.mod_spin_object_ot_operator', text='Modifier Spin Edge')
        row.operator('wm.mod_solidify_plane_object_ot_operator', text='Modifier Solidify Plane')

        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Add Objects")

        row = layout.column()
        row.prop(context.scene, "axis_mod", text="Object axis.")

        row = layout.column()
        row.operator('wm.add_solid_plane_object_ot_operator', text='Add Plane Object')
        row.operator('wm.add_solid_circle_object_ot_operator', text='Add Circle Object')

        row = layout.column()
        if axis_mode == "X": # Y
            row.operator('wm.add_arch_object_x_ot_operator', text='Add Arch Object')
        if axis_mode == "Y": # Y
            row.operator('wm.add_arch_object_y_ot_operator', text='Add Arch Object')
            row.operator('wm.add_pipe_line_object_y_ot_operator', text='Add Pipe Object')
        if axis_mode == "Z": # Z
            row.operator('wm.add_arch_object_z_ot_operator', text='Add Arch Object')
            row.operator('wm.add_pipe_line_object_z_ot_operator', text='Add Pipe Object')

        row_smooth = layout.row()
        col_smooth_lbl = row_smooth.column()
        col_smooth_lbl.label(text="Add Splines")

        if axis_mode == "Y": # Y
            row = layout.column()
            row.operator('wm.add_basic_spline_y_ot_operator', text='Add Basic Spline')
            row.operator('wm.add_pipe_spline_y_ot_operator', text='Add Pipe Spline')


# menu containing all tools
#class VIEW3D_MT_edit_mesh_looptools(Menu):
    #bl_label = "LoopTools"

    #def draw(self, context):
        #layout = self.layout

        #layout.operator("mesh.looptools_bridge", text="Bridge").loft = False

# property group containing all properties for the gui in the panel
#class LoopToolsProps(PropertyGroup):
    #"""
    #Fake module like class
    #bpy.context.window_manager.looptools
    #"""
    # general display properties
    #display_bridge: BoolProperty(
        #name="Bridge settings",
        #description="Display settings of the Bridge tool",
        #default=False
        #)

#row = layout.column()
#bl_options = {'DEFAULT_CLOSED'}



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
