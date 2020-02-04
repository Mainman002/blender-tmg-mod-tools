import bpy


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


##################### Update Text Vertical Alignment #############################
def text_vAlign_changed(self, context):
    text_vAlign = context.scene.text_vAlign

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        if obj.type == 'FONT':
            obj.data.align_y = text_vAlign


##################### Update Text Horizontal Alignment #############################
def text_hAlign_changed(self, context):
    text_hAlign = context.scene.text_hAlign

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        if obj.type == 'FONT':
            obj.data.align_x = text_hAlign


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









