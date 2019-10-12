import bpy

class UI_Distraction_Free_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.ui_distraction_free_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Set view to distraction free.'

    def execute(self, context):

        ui_viewMode = bpy.types.Scene.ui_viewMode

        if bpy.types.Scene.ui_viewMode == False:
            bpy.types.Scene.ui_viewMode = True
        else:
            bpy.types.Scene.ui_viewMode = False
            
        bpy.context.space_data.overlay.show_floor = bpy.types.Scene.ui_viewMode
        bpy.context.space_data.overlay.show_axis_x = bpy.types.Scene.ui_viewMode
        bpy.context.space_data.overlay.show_axis_y = bpy.types.Scene.ui_viewMode
        bpy.context.space_data.overlay.show_cursor = bpy.types.Scene.ui_viewMode
        bpy.context.space_data.overlay.show_object_origins = bpy.types.Scene.ui_viewMode

        return {'FINISHED'}
        return {'FINISHED'}


