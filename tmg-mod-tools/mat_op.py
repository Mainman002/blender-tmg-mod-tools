import bpy


##################### Update Material List #############################
def matList_changed(self, context):
    matList = context.scene.matList

    obj = bpy.context.active_object

    for nr, mat in enumerate(bpy.data.materials):
        mat_list.append(mat)
        #print('matList: ', mat_list)

    #for nr, obj in enumerate(bpy.context.selected_objects):

        #if obj.type == 'MESH':
            #obj.name = text_text


class Mat_Check_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mat_check_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Check materials'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        #materials = context.scene.materials

        scene = context.scene
        obj = bpy.context.active_object
        mat_list = []

        for nr, mat in enumerate(bpy.data.materials):
            mat_list.append(mat)
            print('matList: ', mat_list)

        for nr, obj in enumerate(bpy.context.selected_objects):

            if obj.type == 'MESH':
                matIndex = obj.active_material_index = 0
                matName = obj.active_material.name = "Material"

                obj.data.materials.append(mat_list[1])

                print('Mat ID', matIndex)
                print('Mat Name', matName)
                
        return {'FINISHED'}
        return {'FINISHED'}




