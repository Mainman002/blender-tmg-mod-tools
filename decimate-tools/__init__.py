bl_info = {
    "name" : "Decimate_Tools",
    "author" : "Johnathan Mueller, Jayanam",
    "descrtion" : "Checker decimate edges in your selected edge loops.",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 0),
    "location" : "View3D (EditMode) > Sidebar > Edit Tab",
    "warning" : "",
    "category" : "Mesh"
}

import bpy
from bpy.props import *

from . dec_op import *
from . mod_op import * 
from . add_op import * 
from . dec_panel import * 

#bpy.types.Scene.apply_modifiers = BoolProperty(name="Apply modifiers",
                #default=True,
                #description="Applies modifiers")

bpy.types.Scene.axis_mod = EnumProperty(
    name="Axis",
    description="Defines the Axis for objects",
    items=(
        ('X', 'Axis X', 'Face the X axis',0),
        ('Y', 'Axis Y', 'Face the Y axis',1),
        ('Z', 'Axis Z', 'Face the Z axis',2)
        ),
    default='Z'
    )


classes = ( DEC_Edge_OT_Operator, DEC_Verts_OT_Operator, MOD_Spin_Object_OT_Operator, MOD_Solidify_Plane_Object_OT_Operator, MOD_Spin_Edit_OT_Operator, MOD_Solidify_Plane_Edit_OT_Operator, ADD_Solid_Plane_Object_OT_Operator, ADD_Solid_Circle_Object_OT_Operator, ADD_Arch_Object_X_OT_Operator, ADD_Arch_Object_Y_OT_Operator, ADD_Arch_Object_Z_OT_Operator, ADD_Pipe_Line_Object_Y_OT_Operator, ADD_Pipe_Line_Object_Z_OT_Operator, ADD_Basic_Spline_Y_OT_Operator, ADD_Pipe_Spline_Y_OT_Operator, DEC_PT_Object_Panel, DEC_PT_Edit_Panel )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
