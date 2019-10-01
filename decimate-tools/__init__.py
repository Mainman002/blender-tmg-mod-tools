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
from . dec_panel import * 

classes = ( DEC_Edge_OT_Operator, DEC_Verts_OT_Operator, MOD_Spin_Object_OT_Operator, MOD_Solidify_Plane_Object_OT_Operator, MOD_Spin_Edit_OT_Operator, MOD_Solidify_Plane_Edit_OT_Operator, MOD_Add_Arch_Object_OT_Operator, MOD_Add_Spiral_Object_OT_Operator, DEC_PT_Object_Panel, DEC_PT_Edit_Panel )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
