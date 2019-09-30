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
#from bpy.props import *

from . dec_op import DEC_OT_Operator
from . dec_panel import Dec_PT_Panel

classes = ( DEC_OT_Operator, Dec_PT_Panel )

register, unregister = bpy.utils.register_classes_factory(classes)
    
if __name__ == "__main__":
    register()
