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


class UI_Texel_Check_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.ui_texel_check_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Set checker pattern for selected objects.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        ob = bpy.context.view_layer.objects.active
        matName = "Texel Checker"

        # Get material
        mat = bpy.data.materials.get(matName)
        if mat is None:
        # create material
            mat = bpy.data.materials.new(name=matName)
            mat.use_nodes = True

        for nr, ob in enumerate(bpy.context.selected_objects):
            if ob is not "empty":
                types = ob.type
                if types == "MESH" or "CURVE" or "TEXT" or "METABALL":
                    #if bpy.context.object.mode == "OBJECT":      

                    # Assign it to object
                    if ob.data.materials:
                        # assign to 1st material slot
                        ob.data.materials[0] = mat
                    else:
                        # no slots
                        ob.data.materials.append(mat)

                    tree = ob.active_material.node_tree
                    nodes = tree.nodes
                    links = tree.links

                    # clear all nodes to start clean
                    nodes.clear()

                    # UV Input node
                    mat.node_tree.nodes.new('ShaderNodeTexCoord')
                    node_add = mat
                    texCoordNode = mat.node_tree.nodes[len(mat.node_tree.nodes)-1]
                    texCoordNode.location = (0,0)
                    texCoordNode.name = "Tex Coords"
                    texCoordNode.label = texCoordNode.name

                    # Checker Pattern node
                    mat.node_tree.nodes.new('ShaderNodeTexChecker')
                    node_add = mat
                    checkerNode = mat.node_tree.nodes[len(mat.node_tree.nodes)-1]
                    checkerNode.inputs[3].default_value = 20.0
                    checkerNode.location = (200,0)
                    checkerNode.name = "Checker Pattern"
                    checkerNode.label = checkerNode.name

                    # Principled BSDF node
                    mat.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
                    node_add = mat
                    principledBSDFNode = mat.node_tree.nodes[len(mat.node_tree.nodes)-1]
                    principledBSDFNode.location = (400,0)
                    principledBSDFNode.name = "principledBSDFNode BSDF"
                    principledBSDFNode.label = principledBSDFNode.name

                    # Output node
                    mat.node_tree.nodes.new('ShaderNodeOutputMaterial')
                    node_add = mat
                    outputNode = mat.node_tree.nodes[len(mat.node_tree.nodes)-1]
                    outputNode.location = (700,0)
                    outputNode.name = "Material Output"
                    outputNode.label = outputNode.name

                    # link nodes
                    links = mat.node_tree.links
                    link = links.new(texCoordNode.outputs[2], checkerNode.inputs[0])
                    link = links.new(checkerNode.outputs[0], principledBSDFNode.inputs[0])
                    link = links.new(principledBSDFNode.outputs[0], outputNode.inputs[0])

                    # get specific link
                    #from_s = texCoordNode.outputs[0]
                    #to_s = checkerNode.inputs[0]
                    #link = next(l for l in links if l.from_socket == from_s and l.to_socket == to_s)

                    # remove links
                    #links.remove(link)

        return {'FINISHED'}
        return {'FINISHED'}


