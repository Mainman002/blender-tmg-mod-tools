import bpy


##################### Update Auto Smooth #############################
def angleLimit_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        angleLimit = ob.angleLimit
        for nr, ob in enumerate(bpy.context.selected_objects):
            types = ob.type
            if ob is not None and types == "MESH":
                ob.data.auto_smooth_angle = angleLimit


##################### Update Bevel #############################

def bevelDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelDropToggle = ob.bevelDropToggle
        context.scene.modDrop_bevel = bevelDropToggle

def bevelToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelToggle = ob.bevelToggle
        context.scene.mod_bevel = bevelToggle
        ob.bevelEToggle = bevelToggle
        ob.bevelVToggle = bevelToggle
        ob.bevelRToggle = bevelToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_render = bool(bevelToggle)
                ob.modifiers["Bevel"].show_viewport = bool(bevelToggle)
                ob.modifiers["Bevel"].show_in_editmode = bool(bevelToggle)

def bevelRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelRToggle = ob.bevelRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_render = bool(bevelRToggle)

def bevelVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelVToggle = ob.bevelVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_viewport = bool(bevelVToggle)

def bevelEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelEToggle = ob.bevelEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].show_in_editmode = bool(bevelEToggle)

def bevelWidth_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelWidth = ob.bevelWidth
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].width = float(bevelWidth) #* 0.3

def bevelSegments_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        bevelSegments = ob.bevelSegments
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Bevel")
            if ob is not None and mod is not None:
                ob.modifiers["Bevel"].segments = int(bevelSegments)


##################### Update Subdivision #############################

def subsurfDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfDropToggle = ob.subsurfDropToggle
        context.scene.modDrop_subsurf = subsurfDropToggle

def subsurfToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfToggle = ob.subsurfToggle
        context.scene.mod_subsurf = subsurfToggle
        ob.subsurfEToggle = subsurfToggle
        ob.subsurfVToggle = subsurfToggle
        ob.subsurfRToggle = subsurfToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_render = bool(subsurfToggle)
                ob.modifiers["Subdivision"].show_viewport = bool(subsurfToggle)
                ob.modifiers["Subdivision"].show_in_editmode = bool(subsurfToggle)

def subsurfRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfRToggle = ob.subsurfRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_render = bool(subsurfRToggle)

def subsurfVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfVToggle = ob.subsurfVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_viewport = bool(subsurfVToggle)

def subsurfEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subsurfEToggle = ob.subsurfEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].show_in_editmode = bool(subsurfEToggle)

def subdivisionView_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subdivisionView = ob.subdivisionView
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].levels = int(subdivisionView)

def subdivisionRender_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        subdivisionRender = ob.subdivisionRender
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Subdivision")
            if ob is not None and mod is not None:
                ob.modifiers["Subdivision"].render_levels = int(subdivisionRender)


##################### Update Solidify #############################

def solidDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidDropToggle = ob.solidDropToggle
        context.scene.modDrop_solid = solidDropToggle

def solidToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidToggle = ob.solidToggle
        context.scene.mod_solid = solidToggle
        ob.solidEToggle = solidToggle
        ob.solidVToggle = solidToggle
        ob.solidRToggle = solidToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_render = bool(solidToggle)
                ob.modifiers["Solidify"].show_viewport = bool(solidToggle)
                ob.modifiers["Solidify"].show_in_editmode = bool(solidToggle)

def solidRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidRToggle = ob.solidRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_render = bool(solidRToggle)

def solidVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidVToggle = ob.solidVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_viewport = bool(solidVToggle)

def solidEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidEToggle = ob.solidEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].show_in_editmode = bool(solidEToggle)


def solidThickness_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidThickness = ob.solidThickness
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].thickness = float(solidThickness) #* 0.3


def solidOffset_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        solidOffset = ob.solidOffset
        #context.scene.mod_solidifyOffset = solidifyOffset
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Solidify")
            if ob is not None and mod is not None:
                ob.modifiers["Solidify"].offset = float(solidOffset) #* 0.3


##################### Update Triangulate #############################

def triangulateDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateDropToggle = ob.triangulateDropToggle
        context.scene.modDrop_triangulate = triangulateDropToggle

def triangulateToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateToggle = ob.triangulateToggle
        context.scene.mod_triangulate = triangulateToggle
        ob.triangulateEToggle = triangulateToggle
        ob.triangulateVToggle = triangulateToggle
        ob.triangulateRToggle = triangulateToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_render = bool(triangulateToggle)
                ob.modifiers["Triangulate"].show_viewport = bool(triangulateToggle)
                ob.modifiers["Triangulate"].show_in_editmode = bool(triangulateToggle)
                #mod_triangulate = triangulateToggle

def triangulateRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateRToggle = ob.triangulateRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_render = bool(triangulateRToggle)

def triangulateVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateVToggle = ob.triangulateVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_viewport = bool(triangulateVToggle)

def triangulateEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        triangulateEToggle = ob.triangulateEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Triangulate")
            if ob is not None and mod is not None:
                ob.modifiers["Triangulate"].show_in_editmode = bool(triangulateEToggle)


##################### Update Weighted Normals #############################

def weightedNormalsDropToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsDropToggle = ob.weightedNormalsDropToggle
        context.scene.modDrop_weightedNormals = weightedNormalsDropToggle

def weightedNormalsToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsToggle = ob.weightedNormalsToggle
        context.scene.mod_weightednormals = weightedNormalsToggle
        ob.weightedNormalsEToggle = weightedNormalsToggle
        ob.weightedNormalsVToggle = weightedNormalsToggle
        ob.weightedNormalsRToggle = weightedNormalsToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_render = bool(weightedNormalsToggle)
                ob.modifiers["Weighted Normal"].show_viewport = bool(weightedNormalsToggle)
                ob.modifiers["Weighted Normal"].show_in_editmode = bool(weightedNormalsToggle)
                #mod_triangulate = triangulateToggle

def weightedNormalsRToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsRToggle = ob.weightedNormalsRToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_render = bool(weightedNormalsRToggle)

def weightedNormalsVToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsVToggle = ob.weightedNormalsVToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_viewport = bool(weightedNormalsVToggle)

def weightedNormalsEToggle_changed(self, context):
    if context.active_object is not None:
        ob = context.scene
        weightedNormalsEToggle = ob.weightedNormalsEToggle
        for nr, ob in enumerate(bpy.context.selected_objects):
            mod = ob.modifiers.get("Weighted Normal")
            if ob is not None and mod is not None:
                ob.modifiers["Weighted Normal"].show_in_editmode = bool(weightedNormalsEToggle)


class MOD_Apply_Object_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_apply_object_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Apply Modifiers to object.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        #obj = bpy.context.view_layer.objects.active
        #sel_mode = context.tool_settings.mesh_select_mode
        obj = bpy.context.active_object
        scene = context.scene

        for nr, obj in enumerate(bpy.context.selected_objects):

            #if obj is not None:
                #types = obj.type

            if obj.type == "MESH" or "CURVE" or "TEXT" or "METABALL":
                if bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.convert(target='MESH')
                    #print('Object: ', bpy.ops.object)
                elif bpy.context.object.mode == "EDIT":
                    bpy.ops.object.mode_set(mode="OBJECT")
                    bpy.ops.object.convert(target='MESH')
                    bpy.ops.object.mode_set(mode="EDIT")


            return {'FINISHED'}
            return {'FINISHED'}


class MOD_Object_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_object_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Modifiers to object.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        solid_offset = 1
        solid_thickness = 0.20
        axis_mode = context.scene.axis_mod
        bevel_segments = 3
        bevel_width = 0.15
        subsurf_vlevel = 2
        subsurf_rlevel = 3
        angle_limit = 0.523599
        mod_solid = context.scene.mod_solid
        mod_mirror = context.scene.mod_mirror
        mod_bevel = context.scene.mod_bevel
        mod_subsurf = context.scene.mod_subsurf
        mod_screw = context.scene.mod_screw
        mod_triangulate = context.scene.mod_triangulate
        mod_weightednormals = context.scene.mod_weightednormals

        obj = bpy.context.active_object

        for nr, obj in enumerate(bpy.context.selected_objects):

            types = obj.type

            if types == "MESH":
                if mod_screw == True:
                    mod = obj.modifiers.get("Screw")
                    if mod is None:
                        obj.modifiers.new(name='Screw', type='SCREW')

                    obj.modifiers["Screw"].axis = 'Y'
                    obj.modifiers["Screw"].use_normal_calculate = True
                    obj.modifiers["Screw"].show_expanded = False
                    obj.modifiers["Screw"].use_merge_vertices = True

                if mod_solid == True:
                    mod = obj.modifiers.get("Solidify")
                    if mod is None:
                        obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                    obj.modifiers["Solidify"].offset = solid_offset
                    obj.modifiers["Solidify"].thickness = solid_thickness
                    obj.modifiers["Solidify"].use_even_offset = True
                    obj.modifiers["Solidify"].use_quality_normals = True
                    obj.modifiers["Solidify"].show_expanded = False

                    if mod_mirror == True:
                        obj.modifiers["Solidify"].use_rim_only = True
                    else:
                        obj.modifiers["Solidify"].use_rim_only = False

                if mod_mirror == True:
                    mod = obj.modifiers.get("Mirror")
                    if mod is None:
                        obj.modifiers.new(name='Mirror', type='MIRROR')

                        obj.modifiers["Mirror"].use_axis[0] = False

                        if axis_mode == "X":
                            obj.modifiers["Mirror"].use_axis[0] = True
                            obj.modifiers["Mirror"].use_bisect_axis[0] = True
                        elif axis_mode == "Y":
                            obj.modifiers["Mirror"].use_axis[1] = True
                            obj.modifiers["Mirror"].use_bisect_axis[1] = True
                        elif axis_mode == "Z":
                            obj.modifiers["Mirror"].use_axis[2] = True
                            obj.modifiers["Mirror"].use_bisect_axis[2] = True
                        
                        obj.modifiers["Mirror"].show_expanded = False
                
                if mod_bevel == True:

                    mod = obj.modifiers.get("Bevel")
                    if mod is None:
                        obj.modifiers.new(name='Bevel', type='BEVEL')

                    obj.modifiers["Bevel"].segments = bevel_segments
                    obj.modifiers["Bevel"].limit_method = 'ANGLE'
                    obj.modifiers["Bevel"].angle_limit = angle_limit
                    obj.modifiers["Bevel"].width = bevel_width
                    obj.modifiers["Bevel"].offset_type = 'WIDTH'
                    obj.modifiers["Bevel"].miter_outer = 'MITER_ARC'
                    obj.modifiers["Bevel"].show_expanded = False

                if mod_subsurf == True:

                    mod = obj.modifiers.get("Subdivision")
                    if mod is None:
                        obj.modifiers.new(name='Subdivision', type='SUBSURF')
                    
                    obj.modifiers["Subdivision"].levels = subsurf_vlevel
                    obj.modifiers["Subdivision"].render_levels = subsurf_rlevel
                    obj.modifiers["Subdivision"].show_expanded = False
                    obj.modifiers["Subdivision"].show_in_editmode = False
                
                if mod_triangulate == True:
                    mod = obj.modifiers.get("Triangulate")
                    if mod is None:
                        obj.modifiers.new(name='Triangulate', type='TRIANGULATE')

                    obj.modifiers["Triangulate"].keep_custom_normals = True
                    obj.modifiers["Triangulate"].quad_method = 'BEAUTY'
                    obj.modifiers["Triangulate"].show_expanded = False
                    obj.modifiers["Triangulate"].show_in_editmode = False

                obj.data.use_auto_smooth = True
                obj.data.auto_smooth_angle = 0.785398

                if mod_weightednormals == True:
                    mod = obj.modifiers.get("Weighted Normal")
                    if mod is None:
                        obj.modifiers.new(name='Weighted Normal', type='WEIGHTED_NORMAL')

                    obj.modifiers["Weighted Normal"].keep_sharp = True
                    obj.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
                    obj.modifiers["Weighted Normal"].show_expanded = False
                    obj.modifiers["Weighted Normal"].show_in_editmode = False


            elif types == "CURVE":
                if mod_screw == True:
                    mod = obj.modifiers.get("Screw")
                    if mod is None:
                        obj.modifiers.new(name='Screw', type='SCREW')

                    obj.modifiers["Screw"].axis = 'Y'
                    obj.modifiers["Screw"].use_normal_calculate = True
                    obj.modifiers["Screw"].show_expanded = False
                    obj.modifiers["Screw"].use_merge_vertices = True

                if mod_mirror == True:
                    mod = obj.modifiers.get("Mirror")
                    if mod is None:
                        obj.modifiers.new(name='Mirror', type='MIRROR')

                    obj.modifiers["Mirror"].use_axis[0] = False

                    if axis_mode == "X":
                        obj.modifiers["Mirror"].use_axis[0] = True
                        obj.modifiers["Mirror"].use_bisect_axis[0] = True
                    elif axis_mode == "Y":
                        obj.modifiers["Mirror"].use_axis[1] = True
                        obj.modifiers["Mirror"].use_bisect_axis[1] = True
                    elif axis_mode == "Z":
                        obj.modifiers["Mirror"].use_axis[2] = True
                        obj.modifiers["Mirror"].use_bisect_axis[2] = True
                    
                    obj.modifiers["Mirror"].use_clip = True
                    obj.modifiers["Mirror"].show_expanded = False

                if mod_solid == True:
                    mod = obj.modifiers.get("Solidify")
                    if mod is None:
                        obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                    obj.modifiers["Solidify"].offset = solid_offset
                    obj.modifiers["Solidify"].thickness = solid_thickness
                    obj.modifiers["Solidify"].use_even_offset = True
                    obj.modifiers["Solidify"].use_quality_normals = True
                    obj.modifiers["Solidify"].show_expanded = False

                    if mod_mirror == True:
                        obj.modifiers["Solidify"].use_rim_only = True
                    else:
                        obj.modifiers["Solidify"].use_rim_only = False
                
                if mod_bevel == True:

                    mod = obj.modifiers.get("Bevel")
                    if mod is None:
                        obj.modifiers.new(name='Bevel', type='BEVEL')

                    obj.modifiers["Bevel"].segments = 3
                    obj.modifiers["Bevel"].limit_method = 'ANGLE'
                    obj.modifiers["Bevel"].angle_limit = angle_limit
                    obj.modifiers["Bevel"].width = bevel_width
                    obj.modifiers["Bevel"].offset_type = 'WIDTH'
                    obj.modifiers["Bevel"].miter_outer = 'MITER_ARC'
                    obj.modifiers["Bevel"].show_expanded = False

                if mod_subsurf == True:

                    mod = obj.modifiers.get("Subdivision")
                    if mod is None:
                        obj.modifiers.new(name='Subdivision', type='SUBSURF')
                    
                    obj.modifiers["Subdivision"].levels = subsurf_vlevel
                    obj.modifiers["Subdivision"].render_levels = subsurf_rlevel
                    obj.modifiers["Subdivision"].show_expanded = False
                    obj.modifiers["Subdivision"].show_in_editmode = False
                
                if mod_triangulate == True:
                    mod = obj.modifiers.get("Triangulate")
                    if mod is None:
                        obj.modifiers.new(name='Triangulate', type='TRIANGULATE')

                    obj.modifiers["Triangulate"].keep_custom_normals = True
                    obj.modifiers["Triangulate"].quad_method = 'BEAUTY'
                    obj.modifiers["Triangulate"].show_expanded = False
                    obj.modifiers["Triangulate"].show_in_editmode = False

            if bpy.context.object.mode == "OBJECT":
                bpy.ops.object.shade_smooth()
            elif bpy.context.object.mode == "EDIT":
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.faces_shade_smooth()

            #obj.data.use_auto_smooth = True
            #obj.data.auto_smooth_angle = 0.785398


        return {'FINISHED'}
        return {'FINISHED'}



