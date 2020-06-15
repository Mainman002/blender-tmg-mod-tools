import bpy

from . dec_panel import *
from . uv_op import *
from . mat_op import *
from . sculpt_op import *
from . text_op import *
from . tool_op import *
from . add_op import *
from . mod_op import *
from . dec_op import *
from . ui_op import *
from . userprefs import *

from bpy.props import *
from mathutils import Vector
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from bpy.props import FloatVectorProperty
from bpy.types import Operator
from bpy.types import PropertyGroup
from bpy.props import StringProperty, IntProperty, BoolProperty
from bpy.types import Operator, AddonPreferences

bl_info = {
    "name": "TMG_Mod_Tools",
    "author": "Johnathan Mueller, Jayanam",
    "descrtion": "Checker decimate edges in your selected edge loops.",
    "blender": (2, 80, 0),
    "version": (0, 2, 3),
    "location": "View3D (EditMode) > Sidebar > Edit Tab",
    "warning": "",
    "category": "Mesh"
}


# from . test_panel import *


##################### Update Defs Start #############################
def objectStart_Values(self, context):
    if context.active_object is not None:
        ob = "None"  # bpy.context.scene
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
        ob = context.scene
        if ob is not None:
            if ob.myBool:
                ob.data.body = "On"
            else:
                ob.data.body = "Off"


def zlayer_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        zlayer = ob.zlayer
        if zlayer > 0:
            ob.location.z = float(zlayer) * 0.3
        else:
            ob.zlayer = 1


##################### Update Tri Count #############################
def triCount_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
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
        ob = context.scene
        angleLimit = ob.angleLimit
        for nr, ob in enumerate(bpy.context.selected_objects):
            types = ob.type
            if ob is not None and types == "MESH":
                ob.data.auto_smooth_angle = angleLimit


##################### Update Bevel #############################

def bevelDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelDropToggle = ob.bevelDropToggle
        context.scene.modDrop_bevel = bevelDropToggle


def bevelToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
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
        ob = context.scene
        bevelRToggle = ob.bevelRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_render = bool(bevelRToggle)


def bevelVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelVToggle = ob.bevelVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_viewport = bool(bevelVToggle)


def bevelEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelEToggle = ob.bevelEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_in_editmode = bool(bevelEToggle)


def bevelWidth_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelWidth = ob.bevelWidth
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].width = float(bevelWidth)  # * 0.3


def bevelSegments_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelSegments = ob.bevelSegments
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].segments = int(bevelSegments)


##################### Update Subdivision #############################

def subsurfDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfDropToggle = ob.subsurfDropToggle
        context.scene.modDrop_subsurf = subsurfDropToggle


def subsurfToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
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
                ob.modifiers["Subdivision"].show_in_editmode = bool(
                    subsurfToggle)


def subsurfRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfRToggle = ob.subsurfRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_render = bool(subsurfRToggle)


def subsurfVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfVToggle = ob.subsurfVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_viewport = bool(
                    subsurfVToggle)


def subsurfEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfEToggle = ob.subsurfEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_in_editmode = bool(
                    subsurfEToggle)


def subdivisionView_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subdivisionView = ob.subdivisionView
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].levels = int(subdivisionView)


def subdivisionRender_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subdivisionRender = ob.subdivisionRender
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].render_levels = int(
                    subdivisionRender)


##################### Update Solidify #############################

def solidDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidDropToggle = ob.solidDropToggle
        context.scene.modDrop_solid = solidDropToggle


def solidToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidToggle = ob.solidToggle
        context.scene.mod_solid = solidToggle
        ob.solidEToggle = solidToggle
        ob.solidVToggle = solidToggle
        ob.solidRToggle = solidToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_render = bool(solidToggle)
                ob.modifiers["Solidify"].show_viewport = bool(solidToggle)
                ob.modifiers["Solidify"].show_in_editmode = bool(solidToggle)


def solidRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidRToggle = ob.solidRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_render = bool(solidRToggle)


def solidVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidVToggle = ob.solidVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_viewport = bool(solidVToggle)


def solidEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidEToggle = ob.solidEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_in_editmode = bool(solidEToggle)


def solidThickness_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidThickness = ob.solidThickness
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].thickness = float(
                    solidThickness)  # * 0.3


def solidOffset_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidOffset = ob.solidOffset
        #context.scene.mod_solidifyOffset = solidifyOffset
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].offset = float(solidOffset)  # * 0.3


##################### Update Triangulate #############################

def triangulateDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateDropToggle = ob.triangulateDropToggle
        context.scene.modDrop_triangulate = triangulateDropToggle


def triangulateToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateToggle = ob.triangulateToggle
        context.scene.mod_triangulate = triangulateToggle
        ob.triangulateEToggle = triangulateToggle
        ob.triangulateVToggle = triangulateToggle
        ob.triangulateRToggle = triangulateToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_render = bool(
                    triangulateToggle)
                ob.modifiers["Triangulate"].show_viewport = bool(
                    triangulateToggle)
                ob.modifiers["Triangulate"].show_in_editmode = bool(
                    triangulateToggle)
                #mod_triangulate = triangulateToggle


def triangulateRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateRToggle = ob.triangulateRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_render = bool(
                    triangulateRToggle)


def triangulateVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateVToggle = ob.triangulateVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_viewport = bool(
                    triangulateVToggle)


def triangulateEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateEToggle = ob.triangulateEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_in_editmode = bool(
                    triangulateEToggle)


##################### Update Weighted Normals #############################

def weightedNormalsDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsDropToggle = ob.weightedNormalsDropToggle
        context.scene.modDrop_weightedNormals = weightedNormalsDropToggle


def weightedNormalsToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsToggle = ob.weightedNormalsToggle
        context.scene.mod_weightednormals = weightedNormalsToggle
        ob.weightedNormalsEToggle = weightedNormalsToggle
        ob.weightedNormalsVToggle = weightedNormalsToggle
        ob.weightedNormalsRToggle = weightedNormalsToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_render = bool(
                    weightedNormalsToggle)
                ob.modifiers["Weighted Normal"].show_viewport = bool(
                    weightedNormalsToggle)
                ob.modifiers["Weighted Normal"].show_in_editmode = bool(
                    weightedNormalsToggle)
                #mod_triangulate = triangulateToggle


def weightedNormalsRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsRToggle = ob.weightedNormalsRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_render = bool(
                    weightedNormalsRToggle)


def weightedNormalsVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsVToggle = ob.weightedNormalsVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_viewport = bool(
                    weightedNormalsVToggle)


def weightedNormalsEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsEToggle = ob.weightedNormalsEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_in_editmode = bool(
                    weightedNormalsEToggle)


##################### Update View Mode #############################
def viewMode_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        viewMode = ob.viewMode
        for nr, ob in enumerate(bpy.context.selected_objects):
            types = ob.type
            if ob is not "empty":
                if types == "MESH" or "CURVE" or "TEXT" or "METABALL":
                    ob.display_type = viewMode


##################### Update Object Name #############################
def objectName_changed(self, context):
    object_name = context.scene.objectName

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        if obj.type is not 'TEXT':
            obj.name = object_name
            obj.data.name = object_name


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


##################### Update Material List #############################
def matList_changed(self, context):
    matList = context.scene.matList

    obj = bpy.context.active_object

    for nr, mat in enumerate(bpy.data.materials):
        mat_list.append(mat)
        #print('matList: ', mat_list)

    # for nr, obj in enumerate(bpy.context.selected_objects):

        # if obj.type == 'MESH':
        #obj.name = text_text


##################### Update Values #############################
bpy.types.Object.myBool = bpy.props.BoolProperty(
    name="Switch", default=False, update=myBool_changed)
bpy.types.Object.zlayer = bpy.props.IntProperty(
    name="Z Layer", default=1, update=zlayer_changed)


##### Material List #######
#bpy.types.Scene.matList = bpy.props.ArrayProperty(name = "Material List", update=matList_changed)


##### Tri Count ##########
bpy.types.Object.triCount = bpy.props.IntProperty(
    name="Tri Count", default=0, update=triCount_changed)


##### Auto Smooth ##########
bpy.types.Scene.angleLimit = bpy.props.FloatProperty(
    name="Angle Limit", default=0.523599, min=0.0, max=3.133, update=angleLimit_changed)


##### Bevel ##########
bpy.types.Scene.bevelDropToggle = bpy.props.BoolProperty(
    name="Bevel Dropdown Toggle", default=False, update=bevelDropToggle_changed)

bpy.types.Scene.bevelToggle = bpy.props.BoolProperty(
    name="Bevel Toggle", default=False, update=bevelToggle_changed)
bpy.types.Scene.bevelEToggle = bpy.props.BoolProperty(
    name="Bevel Edit Toggle", default=False, update=bevelEToggle_changed)
bpy.types.Scene.bevelVToggle = bpy.props.BoolProperty(
    name="Bevel View Toggle", default=False, update=bevelVToggle_changed)
bpy.types.Scene.bevelRToggle = bpy.props.BoolProperty(
    name="Bevel Render Toggle", default=False, update=bevelRToggle_changed)
bpy.types.Scene.bevelSegments = bpy.props.IntProperty(
    name="Bevel Segments", default=3, min=1, max=6, update=bevelSegments_changed)
bpy.types.Scene.bevelWidth = bpy.props.FloatProperty(
    name="Bevel Width", default=0.3, min=0.0, max=1.40, update=bevelWidth_changed)


##### Subdivision ##########
bpy.types.Scene.subsurfDropToggle = bpy.props.BoolProperty(
    name="Subdivision Dropdown Toggle", default=False, update=subsurfDropToggle_changed)

bpy.types.Scene.subsurfToggle = bpy.props.BoolProperty(
    name="Subdivision Toggle", default=False, update=subsurfToggle_changed)
bpy.types.Scene.subsurfEToggle = bpy.props.BoolProperty(
    name="Subdivision Edit Toggle", default=False, update=subsurfEToggle_changed)
bpy.types.Scene.subsurfVToggle = bpy.props.BoolProperty(
    name="Subdivision View Toggle", default=False, update=subsurfVToggle_changed)
bpy.types.Scene.subsurfRToggle = bpy.props.BoolProperty(
    name="Subdivision Render Toggle", default=False, update=subsurfRToggle_changed)
bpy.types.Scene.subdivisionView = bpy.props.IntProperty(
    name="Subdivision View Levels", default=1, min=0, max=5, update=subdivisionView_changed)
bpy.types.Scene.subdivisionRender = bpy.props.IntProperty(
    name="Subdivision Render Levels", default=4, min=0, max=8, update=subdivisionRender_changed)


##### Solidify ##########
bpy.types.Scene.solidDropToggle = bpy.props.BoolProperty(
    name="Solidify Dropdown Toggle", default=False, update=solidDropToggle_changed)

bpy.types.Scene.solidToggle = bpy.props.BoolProperty(
    name="Solidify Toggle", default=False, update=solidToggle_changed)
bpy.types.Scene.solidEToggle = bpy.props.BoolProperty(
    name="Solidify Edit Toggle", default=False, update=solidEToggle_changed)
bpy.types.Scene.solidVToggle = bpy.props.BoolProperty(
    name="Solidify View Toggle", default=False, update=solidVToggle_changed)
bpy.types.Scene.solidRToggle = bpy.props.BoolProperty(
    name="Solidify Render Toggle", default=False, update=solidRToggle_changed)
bpy.types.Scene.solidThickness = bpy.props.FloatProperty(
    name="Solidify Thickness", default=0.3, min=0.1, max=20.0, update=solidThickness_changed)
bpy.types.Scene.solidOffset = bpy.props.FloatProperty(
    name="Solidify Offset", default=0.0, min=-1.0, max=1.0, update=solidOffset_changed)


##### Triangulate ##########
bpy.types.Scene.triangulateDropToggle = bpy.props.BoolProperty(
    name="Triangulate Dropdown Toggle", default=False, update=triangulateDropToggle_changed)

bpy.types.Scene.triangulateToggle = bpy.props.BoolProperty(
    name="Triangulate Toggle", default=False, update=triangulateToggle_changed)
bpy.types.Scene.triangulateEToggle = bpy.props.BoolProperty(
    name="Triangulate Edit Toggle", default=False, update=triangulateEToggle_changed)
bpy.types.Scene.triangulateVToggle = bpy.props.BoolProperty(
    name="Triangulate View Toggle", default=False, update=triangulateVToggle_changed)
bpy.types.Scene.triangulateRToggle = bpy.props.BoolProperty(
    name="Triangulate Render Toggle", default=False, update=triangulateRToggle_changed)


##### Weighted Normals ##########
bpy.types.Scene.weightedNormalsDropToggle = bpy.props.BoolProperty(
    name="Weighted Normals Dropdown Toggle", default=False, update=weightedNormalsDropToggle_changed)

bpy.types.Scene.weightedNormalsToggle = bpy.props.BoolProperty(
    name="Weighted Normals Toggle", default=False, update=weightedNormalsToggle_changed)
bpy.types.Scene.weightedNormalsEToggle = bpy.props.BoolProperty(
    name="Weighted Normals Edit Toggle", default=False, update=weightedNormalsEToggle_changed)
bpy.types.Scene.weightedNormalsVToggle = bpy.props.BoolProperty(
    name="Weighted Normals View Toggle", default=False, update=weightedNormalsVToggle_changed)
bpy.types.Scene.weightedNormalsRToggle = bpy.props.BoolProperty(
    name="Weighted Normals Render Toggle", default=False, update=weightedNormalsRToggle_changed)


##### Object Update ############
bpy.types.Scene.objectName = bpy.props.StringProperty(
    name="Object Name", default="Object", update=objectName_changed)


##### Text Update ############
bpy.types.Scene.textName = bpy.props.StringProperty(
    name="Text Name", default="Text", update=textName_changed)
bpy.types.Scene.textText = bpy.props.StringProperty(
    name="Text Text", default="Blank", update=textText_changed)


##### Sculpt Update #########
# bpy.types.Scene.sculpt_single_shape_layer = bpy.props.BoolProperty(name = "sculpt single shape layer", default = False, update=sculpt_single_shape_layer_changed)
# bpy.types.Scene.sculpt_shape_keys_icon_view = bpy.props.BoolProperty(name = "sculpt panel icon view", default = False, update=Update_TMG_User_Preferences_changed)


# def Update_TMG_User_Preferences_changed(self, context):
# 	# ob = context.scene
# 	button_mode = bpy.types.Scene.sculpt_shape_keys_icon_view
# 	if button_mode == True:
# 		button_mode = False
# 	else:
# 		button_mode = True

# 	bpy.types.Scene.sculpt_shape_keys_icon_view = button_mode
# 	print(bpy.types.Scene.sculpt_shape_keys_icon_view)

def myBool_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        if ob is not None:
            if ob.myBool:
                ob.data.body = "On"
            else:
                ob.data.body = "Off"


def objectName_changed(self, context):
    object_name = context.scene.objectName

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        if obj.type is not 'TEXT':
            obj.name = object_name
            obj.data.name = object_name


##### Object View Mode ##########
bpy.types.Scene.viewMode = bpy.props.EnumProperty(
    name="View Mode",
    description="Defines the Viewport mode for objects",
    items=(
                ('TEXTURED', 'TEXTURED', 'TEXTURED View', 0),
                ('WIRE', 'WIRE', 'WIRE View', 1),
                ('BOUNDS', 'BOUNDS', 'BOUNDS View', 2)
    ),
    default='TEXTURED',
    update=viewMode_changed
)


#### Sculpt Shape Keys Panel Mode Switch #########################
bpy.types.Scene.sculpt_shape_keys_icon_view = BoolProperty(name="Icon View",
                                                           default=False,
                                                           description="Switches the shape key panel from labeled buttons, to icons."
                                                           )

##### Sculpt Space Distance ##########
bpy.types.Scene.sculpt_spacingDistance = bpy.props.EnumProperty(
    name="Spacing Distance",
    description="View mode for sculpt brush distance.",
    items=(
                ('VIEW', 'VIEW', 'VIEW View', 0),
                ('SCENE', 'SCENE', 'SCENE Scene', 1)
    ),
    default='VIEW',
    update=sculpt_spacingDistance_changed
)

#### Sculpt Keframe Timeline #################################

bpy.types.Scene.keyframe_timeline = BoolProperty(name="Keframe Timeline",
                                                           default=False,
                                                           description="Keyframes timeline when you add a shape layer."
                                                           )

#### Sculpt Face Sets #################################
bpy.types.Scene.sculpt_faceSets = BoolProperty(name="Sculpt Face Sets.",
                                               default=False,
                                               update=sculpt_faceSets_changed,
                                               description="Sculpt face sets toggle.")

#### Sculpt Referance Transparency #########################
bpy.types.Scene.sculpt_referanceTransparency = FloatProperty(name="Referance Transparency",
                                                             default=0.5,
                                                             min=0.0,
                                                             max=1.0,
                                                             update=sculpt_referanceTransparency_changed,
                                                             description="Set referance image transparency.")

#### Sculpt Referance PositionX #########################
bpy.types.Scene.sculpt_referancePositionX = FloatProperty(name="Referance Position X",
                                                          default=0.5,
                                                          update=sculpt_referancePosition_changed,
                                                          description="Set referance image Position X.")

#### Sculpt Referance PositionY #########################
bpy.types.Scene.sculpt_referancePositionY = FloatProperty(name="Referance Position Y",
                                                          default=0.5,
                                                          update=sculpt_referancePosition_changed,
                                                          description="Set referance image Position Y.")

#### Sculpt Referance Size #########################
bpy.types.Scene.sculpt_referanceSize = FloatProperty(name="Referance Size",
                                                     default=0.5,
                                                     min=0.0,
                                                     update=sculpt_referanceSize_changed,
                                                     description="Set referance image size.")

#### Sculpt Show Selected Shape Layer #########################
bpy.types.Scene.sculpt_single_shape_layer = BoolProperty(name="Only show selected shape layer.",
                                                         default=False,
                                                         update=sculpt_single_shape_layer_changed,
                                                         description="Only show selected shape layer.")

# Text VAlign ########## ( TOP_BASELINE TOP CENTER BOTTOM BOTTOM_BASELINE )
bpy.types.Scene.text_vAlign = bpy.props.EnumProperty(
    name="Vertical Align",
    description="Text Vertical Align.",
    items=(
                ('TOP_BASELINE', 'BOTTOM_BASELINE', 'TOP_BASELINE', 0),
                ('TOP', 'BOTTOM', 'TOP', 1),
                ('CENTER', 'CENTER', 'CENTER', 2),
                ('BOTTOM', 'TOP', 'BOTTOM', 3),
                ('BOTTOM_BASELINE', 'TOP_BASELINE', 'BOTTOM_BASELINE', 4)
    ),
    default='TOP_BASELINE',
    update=text_vAlign_changed
)


# Text HAlign ########## ( LEFT CENTER RIGHT JUSTIFY FLUSH )
bpy.types.Scene.text_hAlign = bpy.props.EnumProperty(
    name="Horizontal Align",
    description="Text Horizontal Align.",
    items=(
                ('RIGHT', 'LEFT', 'RIGHT', 0),
                ('CENTER', 'CENTER', 'CENTER', 1),
                ('LEFT', 'RIGHT', 'LEFT', 2),
                ('JUSTIFY', 'JUSTIFY', 'JUSTIFY', 3),
                ('FLUSH', 'FLUSH', 'FLUSH', 4)
    ),
    default='RIGHT',
    update=text_hAlign_changed
)


##################### Update Defs End #############################

#### Text Bools #################################

bpy.types.Scene.textNameLink = BoolProperty(name="Text Object Name Link",
                                            default=False,
                                            description="Text Object Name Link To Text.")

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
                ('X', 'Axis X', 'Face the X axis', 0),
                ('Y', 'Axis Y', 'Face the Y axis', 1),
                ('Z', 'Axis Z', 'Face the Z axis', 2)
    ),
    default='Y'
)

#### Inset Values #########################

bpy.types.Scene.inset_thickness = FloatProperty(name="Inset thickness",
                                                default=0.1,
                                                min=0.0,
                                                description="Set inset thickness value.")

bpy.types.Scene.inset_depth = FloatProperty(name="Inset depth",
                                            default=0.0,
                                            description="Set inset depth value.")


class MAT_Object_Set_Mat_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mat_object_set_mat_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Apply Modifiers to object.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = bpy.context.active_object
        scene = context.scene
        scn = context.scene
        ob = obj.data

        mat_list = []

        # for nr, mat in enumerate(scene.materials):
        # mat_list.append(mat)

        for nr, mat in enumerate(bpy.data.materials):
            mat_list.append(mat)
            print('matList: ', mat_list)

        for nr, obj in enumerate(bpy.context.selected_objects):

            if obj.type == 'MESH':
                matIndex = obj.active_material_index = 0
                #matName = obj.active_material.name = "Material"

                obj.data.materials.append(mat_list[1])

                #print('Mat ID', matIndex)
                print('Mat ID', scene.active_material_index)
                print('Mat NAME', mat_list[scene.active_material_index].name)

                #print('Mat Name', matName)

            return {'FINISHED'}
            return {'FINISHED'}


def update_scene_materials(self, context):
    self.material_slots.clear()
    for m in self.materials:
        s = self.material_slots.add()
        s.name = m.name
        s.material = m


def get_scene_materials(self):
    return set(s.material for o in self.objects
               for s in o.material_slots if s.material
               )


class MaterialSlot(PropertyGroup):
    def get_name(self):
        return getattr(self.material, "name", "")
    material: PointerProperty(type=bpy.types.Material)
    #name : StringProperty(get=get_name)


class MATERIAL_UL_extreme_matslot(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        ob = data
        slot = item
        ma = slot.material
        mat_update = False

        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            if ma:
                layout.prop(ma, "name", text="", emboss=False,
                            icon_value=layout.icon(ma))


# class SCENE_PT_materials(bpy.types.Panel):
#
#    bl_label = "My label"
#    bl_idname = "SCENE_PT_materials"
#    bl_space_type = "VIEW_3D"
#    bl_region_type = "UI"
#    bl_category = "My Category"
#
#    def draw(self, context):
#
#        scn = context.scene
#        layout = self.layout
#        col = layout.column()
#
        #col.label(text="Set Material")
        #col.operator('wm.mat_object_set_mat_ot_operator', text='', icon='UV_DATA')
#
#        if set(s.material for s in scn.material_slots).symmetric_difference(scn.materials):
#            col.prop(scn, "update_materials", toggle=True, icon='FILE_REFRESH')
#        col.template_list(
#                "MATERIAL_UL_extreme_matslot",
#                "",
#                scn,
#                "material_slots",
#                scn,
#                "active_material_index")


def mesh_add_menu_draw(self, context):
    props = self.layout.separator()
    # props = self.layout.label(text='TMG Objects')
    props = self.layout.operator('mesh.add_ot_subd_cube',
                                 text='Add Subdivided Cube',
                                 icon='MESH_CUBE')
    props.size = 1
    props.cuts = 3
    props.smoothness = 0

    props = self.layout.operator('mesh.add_ot_subd_cylinder',
                                 text='Add Subdivided Cylinder',
                                 icon='MESH_CYLINDER')
    props.size = 0.5
    props.depth = 1
    props.vert_cuts = 8
    props.cuts = 0
    props.smoothness = 0


classes = (
    # Preferances Panel
    TMG_User_Preferences,
    Sculpt_OT_Show_TMG_Addon_Prefs,

    # UV Operators
    UV_OT_MarginUnwrap,

    # Text Operators
    Text_Update_OT_Operator,
    Text_Object_Text_Panel,

    # UI Operators
    UI_Distraction_Free_OT_Operator,
    UI_Wireframe_OT_Operator,
    UI_View_Mode_OT_Operator,
    UI_Texel_Check_OT_Operator,

    # Mod Operators
    MOD_Object_OT_Operator,
    MOD_Apply_Object_OT_Operator,

    # Dec Operators
    DEC_Edge_OT_Operator,
    DEC_Edge_Random_OT_Operator,
    DEC_Verts_OT_Operator,
    DEC_Verts_Random_OT_Operator,
    DEC_PT_Object_Panel,
    DEC_PT_Edit_Panel,
    TOOL_OT_Inset_Edit,
    Dec_Edit_Modifier_Panel,
    Dec_Object_Modifier_Panel,
    Dec_Object_Materials_Panel,

    # Tool Operators
    TOOL_OT_Bevel_Edge_Edit,
    TOOL_OT_Remove_Doubles_Edit,
    TOOL_OT_Select_Interior_Faces_Edit,
    TOOL_OT_Flip_Normals_Edit,
    TOOL_OT_Mesh_Face_To_Circle_Edit,
    TOOL_OT_Wrinkle_Face_Edit,
    TOOL_OT_Knurl_Face_Edit,
    TOOL_OT_Edge_Slide_Edit,
    TOOL_OT_Slotted_Grate_Edit,

    # Add Objects
    ADD_OT_Solid_Plane_Object,
    ADD_OT_Solid_Circle_Object,
    ADD_OT_Arch_Object_X,
    ADD_OT_Arch_Object_Y,
    ADD_OT_Arch_Object_Z,
    ADD_OT_Pipe_Line_Object_Y,
    ADD_OT_Pipe_Line_Object_Z,
    ADD_OT_Basic_Spline_Y,
    ADD_OT_Pipe_Spline_Y,
    ADD_OT_Spline_Follow_Y,
    ADD_OT_SubDCube,
    ADD_OT_SubDCylinder,

    # Sculpt Operators
    Sculpt_Brush_Panel,
    Sculpt_Referance_Panel,
    Sculpt_Shape_Keys_Panel,
    Sculpt_OT_ADD_New_Shape_Layer,
    # Sculpt_OT_Shape_Key_Set,
    Sculpt_OT_Shape_Key_Hide_Others,
    Sculpt_OT_Merge_Shape_Keys,
    Sculpt_OT_Keyframe_Shape_Keys,
    Sculpt_OT_Apply_Shape_Keys,
    Sculpt_OT_Clear_All_Keyframes,
    Sculpt_OT_Remove_Selected_Layer,

    # Test Panel
    # Object_Test_Panel,
)


def register():
    for rsclass in classes:
        bpy.utils.register_class(rsclass)
    bpy.types.VIEW3D_MT_mesh_add.append(mesh_add_menu_draw)
    # user_preferences = bpy.ops.scene.user_preferences
    # user_preferences = bpy.ops.scene.user_preferences
    # addon_prefs = user_preferences.addons["tmg_mod_tools"].preferences
    # bpy.ops.scene.sculpt_shape_keys_icon_view = addon_prefs.Sculpt_Button_Mode
    # bpy.ops.scene.sculpt_shape_keys_icon_view = addon_prefs.Sculpt_Button_Mode

    # preferences = context.preferences
    # addon_prefs = preferences.addons[__init__].preferences

    # bpy.types.Scene.sculpt_shape_keys_icon_view = context.preferences.addons[__init__].preferences.sculpt_shape_keys_icon_view


def unregister():
    for rsclass in classes:
        bpy.utils.unregister_class(rsclass)
    bpy.types.VIEW3D_MT_mesh_add.remove(mesh_add_menu_draw)


if __name__ == "__main__":
    register()
