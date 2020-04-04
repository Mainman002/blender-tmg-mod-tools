import bpy


##################### Update Sculpt View Distance #############################
def sculpt_spacingDistance_changed(self, context):
    sculpt_spacingDistance = context.scene.sculpt_spacingDistance

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        if obj.type == 'MESH':
            bpy.context.scene.tool_settings.unified_paint_settings.use_locked_size = sculpt_spacingDistance
            bpy.data.brushes["SculptDraw"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Draw Sharp"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Clay"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Clay Strips"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Clay Thumb"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Layer"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Inflate/Deflate"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Blob"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Crease"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Smooth"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Flatten/Contrast"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Fill/Deepen"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Scrape/Peaks"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Pinch/Magnify"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Grab"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Elastic Deform"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Snake Hook"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Thumb"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Pose"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Nudge"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Rotate"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Simplify"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Multi-plane Scrape"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Slide Relax"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Cloth"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Simplify"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Mask"].use_scene_spacing = sculpt_spacingDistance

##################### Update Sculpt Face Sets #############################
def sculpt_faceSets_changed(self, context):
    sculpt_faceSets = context.scene.sculpt_faceSets

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        if obj.type == 'MESH':

            bpy.data.brushes["SculptDraw"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Draw Sharp"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Clay"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Clay Strips"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Clay Thumb"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Layer"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Inflate/Deflate"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Blob"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Crease"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Smooth"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Flatten/Contrast"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Fill/Deepen"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Scrape/Peaks"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Pinch/Magnify"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Grab"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Elastic Deform"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Snake Hook"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Thumb"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Pose"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Nudge"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Rotate"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Simplify"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Multi-plane Scrape"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Slide Relax"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Cloth"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Simplify"].use_automasking_face_sets = sculpt_faceSets
            bpy.data.brushes["Mask"].use_automasking_face_sets = sculpt_faceSets
            # bpy.data.brushes["Draw Face Sets"].use_automasking_face_sets = False
            #bpy.ops.sculpt.mesh_filter(use_face_sets=sculpt_faceSets)

##################### Update Sculpt Referance View Transparency #############################
def sculpt_referanceTransparency_changed(self, context):
    sculpt_referanceTransparency = context.scene.sculpt_referanceTransparency

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        types = obj.type

        if types == "EMPTY":
            if obj.use_empty_image_alpha == False:
                obj.use_empty_image_alpha = True
            obj.color[3] = sculpt_referanceTransparency


##################### Update Sculpt Referance Position #############################
def sculpt_referancePosition_changed(self, context):
    sculpt_referancePositionX = context.scene.sculpt_referancePositionX
    sculpt_referancePositionY = context.scene.sculpt_referancePositionY

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        types = obj.type

        if types == "EMPTY":
            obj.empty_image_offset[0] = sculpt_referancePositionX
            obj.empty_image_offset[1] = sculpt_referancePositionY


##################### Update Sculpt Referance Size #############################
def sculpt_referanceSize_changed(self, context):
    sculpt_referanceSize = context.scene.sculpt_referanceSize

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        types = obj.type

        if types == "EMPTY":
            obj.empty_display_size = sculpt_referanceSize


# obj.empty_display_size = 14.92
