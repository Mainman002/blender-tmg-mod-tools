bl_info = {
    "name" : "TMG_Mod_Tools",
    "author" : "Johnathan Mueller, Jayanam",
    "descrtion" : "Checker decimate edges in your selected edge loops.",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 3),
    "location" : "View3D (EditMode) > Sidebar > Edit Tab",
    "warning" : "",
    "category" : "Mesh"
}

import bpy
from bpy.props import *

from . ui_op import *
from . dec_op import *
from . mod_op import * 
from . add_op import * 
from . tool_op import * 
from . dec_panel import * 

#### Menu Float Sliders #########################

bpy.types.Scene.solid_offset = FloatProperty(name="Menu solidify offset slider",
                default=1.0,
                min=-1.0,
                max=1.0,
                description="Menu solidify offset slider.")

bpy.types.Scene.solid_thickness = FloatProperty(name="Menu solidify thickness slider",
                default=0.20,
                min=-200.0,
                max=200.0,
                description="Menu solidify thickness slider.")

#### Menu Tabs #########################

bpy.types.Scene.check_view = BoolProperty(name="Menu toggle view tab",
                default=False,
                description="Menu show | hide view tab.")

bpy.types.Scene.check_modifiers = BoolProperty(name="Menu toggle modifiers tab",
                default=False,
                description="Menu show | hide modifier tab.")

bpy.types.Scene.check_mods = BoolProperty(name="Menu toggle modifiers tab",
                default=False,
                description="Menu show | hide modifiers tab.")

bpy.types.Scene.check_adds = BoolProperty(name="Menu toggle add objects tab",
                default=False,
                description="Menu show | hide add objects tab.")

bpy.types.Scene.check_splines = BoolProperty(name="Menu toggle add splines tab",
                default=False,
                description="Menu show | hide add splines tab.")

bpy.types.Scene.check_decimations = BoolProperty(name="Menu toggle decimate tools tab",
                default=False,
                description="Menu show | hide decimate tools tab.")

bpy.types.Scene.check_tools = BoolProperty(name="Menu toggle tools tab",
                default=False,
                description="Menu show | hide tools tab.")

#### Modifier Checkboxes #########################

bpy.types.Scene.mod_screw = BoolProperty(name="Add screw modifier",
                default=False,
                description="Adds screw modifier")

bpy.types.Scene.mod_solid = BoolProperty(name="Add solidify modifier",
                default=True,
                description="Adds solidify modifier")

bpy.types.Scene.mod_mirror = BoolProperty(name="Add mirror modifier",
                default=False,
                description="Adds mirror modifier")

bpy.types.Scene.mod_bevel = BoolProperty(name="Add bevel modifier",
                default=True,
                description="Adds bevel modifier")

bpy.types.Scene.mod_subsurf = BoolProperty(name="Add subsurface modifier",
                default=False,
                description="Adds subsurface modifier")

#### Ui Checkboxes #########################

bpy.types.Scene.ui_viewMode = BoolProperty(name="Set view mode",
                default=False,
                description="Set view to distraction view / normal view mode")

#### Dropdown Buttons #########################

bpy.types.Scene.axis_mod = EnumProperty(
    name="Axis",
    description="Defines the Axis for objects",
    items=(
        ('X', 'Axis X', 'Face the X axis',0),
        ('Y', 'Axis Y', 'Face the Y axis',1),
        ('Z', 'Axis Z', 'Face the Z axis',2)
        ),
    default='Y'
    )


classes = ( DEC_Edge_OT_Operator, DEC_Verts_OT_Operator, MOD_Object_OT_Operator, MOD_Apply_Object_OT_Operator, ADD_Solid_Plane_Object_OT_Operator, ADD_Solid_Circle_Object_OT_Operator, ADD_Arch_Object_X_OT_Operator, ADD_Arch_Object_Y_OT_Operator, ADD_Arch_Object_Z_OT_Operator, ADD_Pipe_Line_Object_Y_OT_Operator, ADD_Pipe_Line_Object_Z_OT_Operator, ADD_Basic_Spline_Y_OT_Operator, ADD_Pipe_Spline_Y_OT_Operator, ADD_Spline_Folow_Y_OT_Operator, DEC_PT_Object_Panel, DEC_PT_Edit_Panel, TOOL_Inset_Edit_OT_Operator, TOOL_Inset_Depth_Edit_OT_Operator, TOOL_Inset_Individual_Edit_OT_Operator, TOOL_Bevel_Edge_Edit_OT_Operator, UI_Distraction_Free_OT_Operator )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
