bl_info = {
    "name" : "TMG_Mod_Tools",
    "author" : "Johnathan Mueller, Jayanam",
    "descrtion" : "Checker decimate edges in your selected edge loops.",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 8),
    "location" : "View3D (EditMode) > Sidebar > Edit Tab",
    "warning" : "",
    "category" : "Mesh"
}

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
from bpy.props import *

from . ui_op import *
from . dec_op import *
from . mod_op import * 
from . add_op import * 
from . tool_op import * 
from . dec_panel import * 


##################### Update Defs Start #############################

def objectStart_Values(self, context):
    if context.active_object is not None:
        ob = "None" #bpy.context.object
        obs = ob
        obj = bpy.context.active_object
        objs = bpy.context.selected_objects
        ob.location.z = 0.3
        if ob.type == "Label":
            ob.data.body = "Off"
        mod = ob.modifiers.get("Bevel")
        if mod is not None:
            ob.modifiers["Bevel"].width = 0.3
            ob.modifiers["Bevel"].segments = 3
        mod = ob.modifiers.get("Solidify")
        if mod is not None:
            ob.modifiers["Solidify"].thickness = 0.3

def myBool_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        if ob is not None:
            if ob.myBool:
                ob.data.body = "On"
            else:
                ob.data.body = "Off"

def zlayer_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        zlayer = ob.zlayer
        if zlayer > 0:
            ob.location.z = float(zlayer) * 0.3
        else:
            ob.zlayer = 1

##################### Update Bevel #############################

def bevelToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelToggle = ob.bevelToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_render = bool(bevelToggle)
                ob.modifiers["Bevel"].show_viewport = bool(bevelToggle)
                ob.modifiers["Bevel"].show_in_editmode = bool(bevelToggle)


def bevelWidth_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelWidth = ob.bevelWidth
        if bevelWidth < 0.1:
            ob.bevelWidth = 0.1
        elif bevelWidth > 4.7:
            ob.bevelWidth = 4.7
        else:
            for nr, ob in enumerate(bpy.context.selected_objects):
                mod = ob.modifiers.get("Bevel")
                if ob is not None and mod is not None:
                    ob.modifiers["Bevel"].width = float(bevelWidth) * 0.3

def bevelSegments_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelSegments = ob.bevelSegments
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].segments = int(bevelSegments)

##################### Update Subdivision #############################

def subdivisionToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        subdivisionToggle = ob.subdivisionToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_viewport = bool(subdivisionToggle)

def subdivisionView_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        subdivisionView = ob.subdivisionView
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].levels = int(subdivisionView)

def subdivisionRender_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        subdivisionRender = ob.subdivisionRender
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].render_levels = int(subdivisionRender)

##################### Update Solidify #############################

def solidifyThickness_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        solidifyThickness = ob.solidifyThickness
        if solidifyThickness < 0.1:
            ob.solidifyThickness = 0.1
        elif solidifyThickness > 4.7:
            ob.solidifyThickness = 4.7
        else:
            for nr, ob in enumerate(bpy.context.selected_objects):
                mod = ob.modifiers.get("Solidify")
                if ob is not None and mod is not None:
                    ob.modifiers["Solidify"].thickness = float(solidifyThickness) * 0.3

##################### Update View Mode #############################

def viewMode_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        viewMode = ob.viewMode
        for nr, ob in enumerate(bpy.context.selected_objects):
            types = ob.type
            if ob is not "empty":
                if types == "MESH" or "CURVE" or "TEXT" or "METABALL":
                    ob.display_type = viewMode

##################### Update Values #############################

bpy.types.Object.myBool = bpy.props.BoolProperty(name = "Switch", default = False, update=myBool_changed)

bpy.types.Object.zlayer = bpy.props.IntProperty(name = "Z Layer", default = 1, update=zlayer_changed)

##### Bevel ##########
bpy.types.Object.bevelToggle = bpy.props.BoolProperty(name = "Bevel Toggle", default = True, update=bevelToggle_changed)
bpy.types.Object.bevelSegments = bpy.props.IntProperty(name = "Bevel Segments", default = 1, min = 1, max = 6, update=bevelSegments_changed)
bpy.types.Object.bevelWidth = bpy.props.FloatProperty(name = "Bevel Width", default = 0.3, min = 0.1, max = 4.7, update=bevelWidth_changed)

##### Subdivision ##########
bpy.types.Object.subdivisionToggle = bpy.props.BoolProperty(name = "Subdivision Toggle", default = True, update=subdivisionToggle_changed)
bpy.types.Object.subdivisionView = bpy.props.IntProperty(name = "Subdivision View Levels", default = 1, min = 0, max = 5, update=subdivisionView_changed)
bpy.types.Object.subdivisionRender = bpy.props.IntProperty(name = "Subdivision Render Levels", default = 4, min = 0, max = 8, update=subdivisionRender_changed)


##### Solidify ##########
bpy.types.Object.solidifyThickness = bpy.props.FloatProperty(name = "Solidify Thickness", default = 0.3, min = 0.1, max = 4.7, update=solidifyThickness_changed)

##### Object View Mode ##########
bpy.types.Object.solidifyThickness = bpy.props.FloatProperty(name = "Solidify Thickness", default = 0.3, min = 0.1, max = 4.7, update=solidifyThickness_changed)


bpy.types.Object.viewMode = bpy.props.EnumProperty(
    name="View Mode",
    description="Defines the Viewport mode for objects",
    items=(
        ('TEXTURED', 'TEXTURED', 'TEXTURED View',0),
        ('WIRE', 'WIRE', 'WIRE View',1),
        ('BOUNDS', 'BOUNDS', 'BOUNDS View',2)
        ),
    default='TEXTURED', 
    update=viewMode_changed
    )


##################### Update Defs End #############################


#### Menu Float Sliders #########################

bpy.types.Scene.subsurf_rlevel = IntProperty(name="Menu subsurf render level slider",
                default=2,
                min=0,
                max=6,
                description="Menu subsurf render level slider.")

bpy.types.Scene.subsurf_vlevel = IntProperty(name="Menu subsurf view level slider",
                default=2,
                min=0,
                max=5,
                description="Menu subsurf view level slider.")

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

bpy.types.Scene.inset_thickness = FloatProperty(name="Menu inset thickness slider",
                default=0.07,
                min=0.00,
                max=200.0,
                description="Menu inset thickness slider.")

bpy.types.Scene.inset_depth = FloatProperty(name="Menu inset depth slider",
                default=0.75,
                min=-50.0,
                max=50.0,
                description="Menu inset depth slider.")

bpy.types.Scene.bevel_width = FloatProperty(name="Menu bevel width slider",
                default=0.15,
                min=0.03,
                max=1.37,
                description="Menu bevel width slider.")

bpy.types.Scene.bevel_segments = IntProperty(name="Menu bevel segments slider",
                default=3,
                min=1,
                max=6,
                description="Menu bevel segments slider.")

bpy.types.Scene.angle_limit = FloatProperty(name="Menu angle limit slider",
                default=0.523599,
                min=0.00174533,
                max=3.14159,
                description="Menu angle limit slider.")

#### Menu Tabs #########################

bpy.types.Scene.check_view = BoolProperty(name="Menu toggle view tab",
                default=False,
                description="Menu show | hide view tab.")

bpy.types.Scene.check_modifiers = BoolProperty(name="Menu toggle modifiers tab",
                default=False,
                description="Menu show | hide modifier tab.")

bpy.types.Scene.check_modSettings = BoolProperty(name="Menu toggle modifiers settings tab",
                default=False,
                description="Menu show | hide modifier settings tab.")

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

bpy.types.Scene.mod_triangulate = BoolProperty(name="Add triangulate modifier",
                default=False,
                description="Adds triangulate modifier")

bpy.types.Scene.mod_weightednormals = BoolProperty(name="Add weighted normals modifier",
                default=False,
                description="Adds weighted normals modifier")

#### Tools Checkboxes #########################

bpy.types.Scene.check_inset_individual = BoolProperty(name="Inset individual check",
                default=False,
                description="Inset individual check")

bpy.types.Scene.check_inset_depth = BoolProperty(name="Inset depth check",
                default=False,
                description="Inset depth check")

bpy.types.Scene.check_inset_thickness = BoolProperty(name="Inset thickness check",
                default=False,
                description="Inset thickness check")

#### Ui Checkboxes #########################

bpy.types.Scene.ui_viewMode = BoolProperty(name="Set view mode",
                default=False,
                description="Set view to distraction view / normal view mode")

bpy.types.Scene.ui_wireMode = BoolProperty(name="Set wireframe view mode",
                default=False,
                description="Set wireframe view / normal view mode")

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

classes = (

DEC_Edge_OT_Operator, DEC_Edge_Random_OT_Operator, DEC_Verts_OT_Operator, DEC_Verts_Random_OT_Operator, 
MOD_Object_OT_Operator, MOD_Apply_Object_OT_Operator, 
ADD_Solid_Plane_Object_OT_Operator, ADD_Solid_Circle_Object_OT_Operator, ADD_Arch_Object_X_OT_Operator, ADD_Arch_Object_Y_OT_Operator, 
ADD_Arch_Object_Z_OT_Operator, ADD_Pipe_Line_Object_Y_OT_Operator, ADD_Pipe_Line_Object_Z_OT_Operator, 
ADD_Basic_Spline_Y_OT_Operator, ADD_Pipe_Spline_Y_OT_Operator, ADD_Spline_Folow_Y_OT_Operator, 
DEC_PT_Object_Panel, DEC_PT_Edit_Panel, 
TOOL_Inset_Edit_OT_Operator, TOOL_Bevel_Edge_Edit_OT_Operator, TOOL_Remove_Doubles_Edit_OT_Operator, 
UI_Distraction_Free_OT_Operator, UI_Wireframe_OT_Operator, UI_View_Mode_OT_Operator, Dec_Edit_Modifier_Panel, Dec_Object_Modifier_Panel,
UI_Texel_Check_OT_Operator, Dec_Object_Materials_Panel 

)

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()

    bpy.ops.wm.mod_object_ot_operator()
