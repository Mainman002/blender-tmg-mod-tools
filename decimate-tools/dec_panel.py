import bpy
#from bpy.types import Panel

class Dec_PT_Panel(bpy.types.Panel):
    bl_idname = 'object.dec_pt_panel'
    bl_label = 'Decimate Tools'
    bl_category = 'Edit'
    bl_context = "mesh_edit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
 
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('wm.dec_ot_operator', text='Decimate Cylinder')
