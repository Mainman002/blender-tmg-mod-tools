import bpy

class Text_Update_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.text_update_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Update text.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        #textNameLink = context.scene.textNameLink
        #text_name = context.scene.textName
        text_text = context.scene.textText

        obj = bpy.context.active_object

        for nr, obj in enumerate(bpy.context.selected_objects):

            if obj.type == 'FONT':
                #print('font object: ', obj.type)
                obj.data.body = text_text
            #else:
                #print('bad type: ', obj.type)
        
                   

        return {'FINISHED'}
        return {'FINISHED'}




