import bpy


##################### Update Sculpt View Distance #############################
def sculpt_spacingDistance_changed(self, context):
    sculpt_spacingDistance = context.scene.sculpt_spacingDistance

    obj = bpy.context.active_object

    for nr, obj in enumerate(bpy.context.selected_objects):

        if obj.type == 'MESH':

            bpy.data.brushes["SculptDraw"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["SculptDraw"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["SculptDraw"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Draw Sharp"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Draw Sharp"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Clay"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Clay Strips"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Layer"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Inflate/Deflate"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Inflate/Deflate"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Blob"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Crease"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Smooth"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Flatten/Contrast"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Fill/Deepen"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Scrape/Peaks"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Multiplane Scrape"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Pinch/Magnify"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Grab"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Elastic Deform"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Snake Hook"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Thumb"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Pose"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Nudge"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Rotate"].use_scene_spacing = sculpt_spacingDistance
            bpy.data.brushes["Simplify"].use_scene_spacing = sculpt_spacingDistance
            #bpy.data.brushes["Topology"].use_scene_spacing = sculpt_spacingDistance
            #bpy.data.brushes["Mask"].use_scene_spacing = sculpt_spacingDistance




