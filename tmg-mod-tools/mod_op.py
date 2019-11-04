import bpy

class MOD_Apply_Object_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_apply_object_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Apply Modifiers to object.'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = bpy.context.view_layer.objects.active
        #sel_mode = context.tool_settings.mesh_select_mode
        #obj = bpy.context.active_object

        for nr, obj in enumerate(bpy.context.selected_objects):

            if obj is not "empty":
                types = obj.type

                if types == "MESH" or "CURVE" or "TEXT" or "METABALL":
                    if bpy.context.object.mode == "OBJECT":
                        bpy.ops.object.convert(target='MESH')
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

                if mod_weightednormals == True:
                    mod = obj.modifiers.get("Weighted Normal")
                    if mod is None:
                        obj.modifiers.new(name='Weighted Normal', type='WEIGHTED_NORMAL')

                    obj.modifiers["Weighted Normal"].keep_sharp = True
                    obj.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
                    obj.modifiers["Weighted Normal"].show_expanded = False
                    obj.modifiers["Weighted Normal"].show_in_editmode = False

                obj.data.use_auto_smooth = True
                obj.data.auto_smooth_angle = 0.785398


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



