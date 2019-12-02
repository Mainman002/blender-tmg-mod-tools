bl_info = {
    "name" : "TMG_Mod_Tools",
    "author" : "Johnathan Mueller, Jayanam",
    "descrtion" : "Checker decimate edges in your selected edge loops.",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 9),
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


##################### Update Tri Count #############################
def triCount_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        objmesh = ob.data
        tri_count = ob.triCount
        for poly in mesh.polygons:
            if len(poly.vertices) == 3:
                tri_count += 1
                ob.triCount = tri_count
    else:
        tri_count = 0
        ob.triCount = 0


##################### Update Auto Smooth #############################
def angleLimit_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        angleLimit = ob.angleLimit
        for nr, ob in enumerate(bpy.context.selected_objects):
            types = ob.type
            if ob is not None and types == "MESH":
                ob.data.auto_smooth_angle = angleLimit


##################### Update Bevel #############################

def bevelDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelDropToggle = ob.bevelDropToggle
        context.scene.modDrop_bevel = bevelDropToggle

def bevelToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelToggle = ob.bevelToggle
        context.scene.mod_bevel = bevelToggle
        ob.bevelEToggle = bevelToggle
        ob.bevelVToggle = bevelToggle
        ob.bevelRToggle = bevelToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_render = bool(bevelToggle)
                ob.modifiers["Bevel"].show_viewport = bool(bevelToggle)
                ob.modifiers["Bevel"].show_in_editmode = bool(bevelToggle)

def bevelRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelRToggle = ob.bevelRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_render = bool(bevelRToggle)

def bevelVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelVToggle = ob.bevelVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_viewport = bool(bevelVToggle)

def bevelEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelEToggle = ob.bevelEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_in_editmode = bool(bevelEToggle)

def bevelWidth_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelWidth = ob.bevelWidth
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].width = float(bevelWidth) #* 0.3

def bevelSegments_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        bevelSegments = ob.bevelSegments
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].segments = int(bevelSegments)


##################### Update Subdivision #############################

def subsurfDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        subsurfDropToggle = ob.subsurfDropToggle
        context.scene.modDrop_subsurf = subsurfDropToggle

def subsurfToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        subsurfToggle = ob.subsurfToggle
        context.scene.mod_subsurf = subsurfToggle
        ob.subsurfEToggle = subsurfToggle
        ob.subsurfVToggle = subsurfToggle
        ob.subsurfRToggle = subsurfToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_render = bool(subsurfToggle)
                ob.modifiers["Subdivision"].show_viewport = bool(subsurfToggle)
                ob.modifiers["Subdivision"].show_in_editmode = bool(subsurfToggle)

def subsurfRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        subsurfRToggle = ob.subsurfRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_render = bool(subsurfRToggle)

def subsurfVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        subsurfVToggle = ob.subsurfVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_viewport = bool(subsurfVToggle)

def subsurfEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        subsurfEToggle = ob.subsurfEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_in_editmode = bool(subsurfEToggle)

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

def solidifyDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        solidifyDropToggle = ob.solidifyDropToggle
        context.scene.modDrop_solid = solidifyDropToggle

def solidifyToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        solidifyToggle = ob.solidifyToggle
        context.scene.mod_solid = solidifyToggle
        ob.solidifyEToggle = solidifyToggle
        ob.solidifyVToggle = solidifyToggle
        ob.solidifyRToggle = solidifyToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_render = bool(solidifyToggle)
                ob.modifiers["Solidify"].show_viewport = bool(solidifyToggle)
                ob.modifiers["Solidify"].show_in_editmode = bool(solidifyToggle)

def solidifyRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        solidifyRToggle = ob.solidifyRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_render = bool(solidifyRToggle)

def solidifyVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        solidifyVToggle = ob.solidifyVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_viewport = bool(solidifyVToggle)

def solidifyEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        solidifyEToggle = ob.solidifyEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_in_editmode = bool(solidifyEToggle)


def solidifyThickness_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        solidifyThickness = ob.solidifyThickness
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].thickness = float(solidifyThickness) #* 0.3


def solidifyOffset_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        solidifyOffset = ob.solidifyOffset
        #context.scene.mod_solidifyOffset = solidifyOffset
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].offset = float(solidifyOffset) #* 0.3


##################### Update Triangulate #############################

def triangulateDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        triangulateDropToggle = ob.triangulateDropToggle
        context.scene.modDrop_triangulate = triangulateDropToggle

def triangulateToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        triangulateToggle = ob.triangulateToggle
        context.scene.mod_triangulate = triangulateToggle
        ob.triangulateEToggle = triangulateToggle
        ob.triangulateVToggle = triangulateToggle
        ob.triangulateRToggle = triangulateToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_render = bool(triangulateToggle)
                ob.modifiers["Triangulate"].show_viewport = bool(triangulateToggle)
                ob.modifiers["Triangulate"].show_in_editmode = bool(triangulateToggle)
                #mod_triangulate = triangulateToggle

def triangulateRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        triangulateRToggle = ob.triangulateRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_render = bool(triangulateRToggle)

def triangulateVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        triangulateVToggle = ob.triangulateVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_viewport = bool(triangulateVToggle)

def triangulateEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        triangulateEToggle = ob.triangulateEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_in_editmode = bool(triangulateEToggle)


##################### Update Weighted Normals #############################

def weightedNormalsDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        weightedNormalsDropToggle = ob.weightedNormalsDropToggle
        context.scene.modDrop_weightedNormals = weightedNormalsDropToggle

def weightedNormalsToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        weightedNormalsToggle = ob.weightedNormalsToggle
        context.scene.mod_weightednormals = weightedNormalsToggle
        ob.weightedNormalsEToggle = weightedNormalsToggle
        ob.weightedNormalsVToggle = weightedNormalsToggle
        ob.weightedNormalsRToggle = weightedNormalsToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_render = bool(weightedNormalsToggle)
                ob.modifiers["Weighted Normal"].show_viewport = bool(weightedNormalsToggle)
                ob.modifiers["Weighted Normal"].show_in_editmode = bool(weightedNormalsToggle)
                #mod_triangulate = triangulateToggle

def weightedNormalsRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        weightedNormalsRToggle = ob.weightedNormalsRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_render = bool(weightedNormalsRToggle)

def weightedNormalsVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        weightedNormalsVToggle = ob.weightedNormalsVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_viewport = bool(weightedNormalsVToggle)

def weightedNormalsEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.object
        weightedNormalsEToggle = ob.weightedNormalsEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_in_editmode = bool(weightedNormalsEToggle)


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


##### Tri Count ##########
bpy.types.Object.triCount = bpy.props.IntProperty(name = "Tri Count", default = 0, update=triCount_changed)


##### Auto Smooth ##########
bpy.types.Object.angleLimit = bpy.props.FloatProperty(name = "Angle Limit", default = 0.523599, min = 0.0, max = 3.133, update=angleLimit_changed)


##### Bevel ##########
bpy.types.Object.bevelDropToggle = bpy.props.BoolProperty(name = "Bevel Dropdown Toggle", default = False, update=bevelDropToggle_changed)

bpy.types.Object.bevelToggle = bpy.props.BoolProperty(name = "Bevel Toggle", default = False, update=bevelToggle_changed)
bpy.types.Object.bevelEToggle = bpy.props.BoolProperty(name = "Bevel Edit Toggle", default = False, update=bevelEToggle_changed)
bpy.types.Object.bevelVToggle = bpy.props.BoolProperty(name = "Bevel View Toggle", default = False, update=bevelVToggle_changed)
bpy.types.Object.bevelRToggle = bpy.props.BoolProperty(name = "Bevel Render Toggle", default = False, update=bevelRToggle_changed)
bpy.types.Object.bevelSegments = bpy.props.IntProperty(name = "Bevel Segments", default = 3, min = 1, max = 6, update=bevelSegments_changed)
bpy.types.Object.bevelWidth = bpy.props.FloatProperty(name = "Bevel Width", default = 0.3, min = 0.03, max = 1.40, update=bevelWidth_changed)


##### Subdivision ##########
bpy.types.Object.subsurfDropToggle = bpy.props.BoolProperty(name = "Subdivision Dropdown Toggle", default = False, update=subsurfDropToggle_changed)

bpy.types.Object.subsurfToggle = bpy.props.BoolProperty(name = "Subdivision Toggle", default = False, update=subsurfToggle_changed)
bpy.types.Object.subsurfEToggle = bpy.props.BoolProperty(name = "Subdivision Edit Toggle", default = False, update=subsurfEToggle_changed)
bpy.types.Object.subsurfVToggle = bpy.props.BoolProperty(name = "Subdivision View Toggle", default = False, update=subsurfVToggle_changed)
bpy.types.Object.subsurfRToggle = bpy.props.BoolProperty(name = "Subdivision Render Toggle", default = False, update=subsurfRToggle_changed)
bpy.types.Object.subdivisionView = bpy.props.IntProperty(name = "Subdivision View Levels", default = 1, min = 0, max = 5, update=subdivisionView_changed)
bpy.types.Object.subdivisionRender = bpy.props.IntProperty(name = "Subdivision Render Levels", default = 4, min = 0, max = 8, update=subdivisionRender_changed)


##### Solidify ##########
bpy.types.Object.solidifyDropToggle = bpy.props.BoolProperty(name = "Solidify Dropdown Toggle", default = False, update=solidifyDropToggle_changed)

bpy.types.Object.solidifyToggle = bpy.props.BoolProperty(name = "Solidify Toggle", default = False, update=solidifyToggle_changed)
bpy.types.Object.solidifyEToggle = bpy.props.BoolProperty(name = "Solidify Edit Toggle", default = False, update=solidifyEToggle_changed)
bpy.types.Object.solidifyVToggle = bpy.props.BoolProperty(name = "Solidify View Toggle", default = False, update=solidifyVToggle_changed)
bpy.types.Object.solidifyRToggle = bpy.props.BoolProperty(name = "Solidify Render Toggle", default = False, update=solidifyRToggle_changed)
bpy.types.Object.solidifyThickness = bpy.props.FloatProperty(name = "Solidify Thickness", default = 0.3, min = 0.1, max = 20.0, update=solidifyThickness_changed)
bpy.types.Object.solidifyOffset = bpy.props.FloatProperty(name = "Solidify Offset", default = 0.0, min = -1.0, max = 1.0, update=solidifyOffset_changed)


##### Triangulate ##########
bpy.types.Object.triangulateDropToggle = bpy.props.BoolProperty(name = "Triangulate Dropdown Toggle", default = False, update=triangulateDropToggle_changed)

bpy.types.Object.triangulateToggle = bpy.props.BoolProperty(name = "Triangulate Toggle", default = False, update=triangulateToggle_changed)
bpy.types.Object.triangulateEToggle = bpy.props.BoolProperty(name = "Triangulate Edit Toggle", default = False, update=triangulateEToggle_changed)
bpy.types.Object.triangulateVToggle = bpy.props.BoolProperty(name = "Triangulate View Toggle", default = False, update=triangulateVToggle_changed)
bpy.types.Object.triangulateRToggle = bpy.props.BoolProperty(name = "Triangulate Render Toggle", default = False, update=triangulateRToggle_changed)


##### Weighted Normals ##########
bpy.types.Object.weightedNormalsDropToggle = bpy.props.BoolProperty(name = "Weighted Normals Dropdown Toggle", default = False, update=weightedNormalsDropToggle_changed)

bpy.types.Object.weightedNormalsToggle = bpy.props.BoolProperty(name = "Weighted Normals Toggle", default = False, update=weightedNormalsToggle_changed)
bpy.types.Object.weightedNormalsEToggle = bpy.props.BoolProperty(name = "Weighted Normals Edit Toggle", default = False, update=weightedNormalsEToggle_changed)
bpy.types.Object.weightedNormalsVToggle = bpy.props.BoolProperty(name = "Weighted Normals View Toggle", default = False, update=weightedNormalsVToggle_changed)
bpy.types.Object.weightedNormalsRToggle = bpy.props.BoolProperty(name = "Weighted Normals Render Toggle", default = False, update=weightedNormalsRToggle_changed)


##### Object View Mode ##########
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
                default=False,
                description="Adds solidify modifier")

bpy.types.Scene.mod_mirror = BoolProperty(name="Add mirror modifier",
                default=False,
                description="Adds mirror modifier")

bpy.types.Scene.mod_bevel = BoolProperty(name="Add bevel modifier",
                default=False,
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

#### Modifier Dropdown List #########################

bpy.types.Scene.modDrop_screw = BoolProperty(name="Dropdown screw modifier",
                default=False,
                description="Dropdown screw modifier")

bpy.types.Scene.modDrop_solid = BoolProperty(name="Dropdown solidify modifier",
                default=False,
                description="Dropdown solidify modifier")

bpy.types.Scene.modDrop_mirror = BoolProperty(name="Dropdown mirror modifier",
                default=False,
                description="Dropdown mirror modifier")

bpy.types.Scene.modDrop_bevel = BoolProperty(name="Dropdown bevel modifier",
                default=False,
                description="Dropdown bevel modifier")

bpy.types.Scene.modDrop_subsurf = BoolProperty(name="Dropdown subsurface modifier",
                default=False,
                description="Dropdown subsurface modifier")

bpy.types.Scene.modDrop_triangulate = BoolProperty(name="Dropdown triangulate modifier",
                default=False,
                description="Dropdown triangulate modifier")

bpy.types.Scene.modDrop_weightedNormals = BoolProperty(name="Dropdown weighted normals modifier",
                default=False,
                description="Dropdown weighted normals modifier")

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
