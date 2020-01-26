import bpy

class Text_Update_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.text_update_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Update text.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        #obj = bpy.context.view_layer.objects.active

        text_name = context.scene.text_name
        text_text = context.scene.text_text

        obj = bpy.context.active_object

        for nr, obj in enumerate(bpy.context.selected_objects):

            if obj is not "empty":
                types = obj.type
                if types == "MESH":
                    return {'FINISHED'}
                elif types == "CURVE" or "TEXT":
                    #obj.name = text_name
                    #obj.data.name = text_name
                    obj.data.body = text_text
                   

        return {'FINISHED'}
        return {'FINISHED'}




