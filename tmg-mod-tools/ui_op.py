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

class UI_Wireframe_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.ui_wireframe_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Set view to wireframe.'

    def execute(self, context):

        ui_wireMode = bpy.types.Scene.ui_wireMode

        if bpy.types.Scene.ui_wireMode == False:
            bpy.types.Scene.ui_wireMode = True
            bpy.context.space_data.overlay.show_wireframes = False
        else:
            bpy.types.Scene.ui_wireMode = False
            bpy.context.space_data.overlay.show_wireframes = True

        bpy.ops.wm.context_toggle(data_path="space_data.shading.show_xray")
        bpy.ops.wm.context_toggle(data_path="space_data.shading.show_backface_culling")
        #bpy.ops.wm.context.space_data.shading.xray_alpha = 0.182

        #bpy.data.screens["Layout"].shading.xray_alpha = 0.374126
        #bpy.types.View3DShading.light = 'FLAT'
        #bpy.types.View3DShading.show_backface_culling = True
        #bpy.types.View3DShading.single_color = (0.180435, 0.433631, 0.778542)
        
        return {'FINISHED'}
        return {'FINISHED'}


class UI_View_Mode_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.ui_view_mode_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Set view mode for objects.'

    def execute(self, context):

        obj = bpy.context.active_object

        for nr, obj in enumerate(bpy.context.selected_objects):

            if obj is not "empty":
                types = obj.type

                if types == "MESH" or "CURVE" or "TEXT" or "METABALL":
                    if bpy.context.scene.view_mod == '0':
                        obj.display_type = 'TEXTURED'
                    elif bpy.context.scene.view_mod == '1':
                        obj.display_type = 'WIRE'
                    elif bpy.context.scene.view_mod == '2':
                        obj.display_type = 'BOUNDS'

        return {'FINISHED'}
        return {'FINISHED'}

