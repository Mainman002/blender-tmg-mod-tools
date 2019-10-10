import bpy
	
#### Object Mode ###################################################################

class MOD_Object_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_object_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Modifiers to object.'

    def execute(self, context):

        solid_offset = context.scene.solid_offset
        solid_thickness = context.scene.solid_thickness

        axis_mode = context.scene.axis_mod
        mod_screw = context.scene.mod_screw
        mod_solid = context.scene.mod_solid
        mod_mirror = context.scene.mod_mirror
        mod_bevel = context.scene.mod_bevel
        mod_subsurf = context.scene.mod_subsurf

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

                if mod_mirror == True:
                    if mod_solid == True:

                        mod = obj.modifiers.get("Solidify")
                        if mod is None:
                            obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                        obj.modifiers["Solidify"].offset = solid_offset
                        obj.modifiers["Solidify"].thickness = solid_thickness
                        obj.modifiers["Solidify"].use_even_offset = True
                        obj.modifiers["Solidify"].use_quality_normals = True
                        obj.modifiers["Solidify"].use_rim_only = True
                        obj.modifiers["Solidify"].show_expanded = False

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
                else:
                    if mod_solid == True:

                        mod = obj.modifiers.get("Solidify")
                        if mod is None:
                            obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                        obj.modifiers["Solidify"].offset = solid_offset
                        obj.modifiers["Solidify"].thickness = solid_thickness
                        obj.modifiers["Solidify"].use_even_offset = True
                        obj.modifiers["Solidify"].use_quality_normals = True
                        obj.modifiers["Solidify"].show_expanded = False
                
                if mod_bevel == True:

                    mod = obj.modifiers.get("Bevel")
                    if mod is None:
                        obj.modifiers.new(name='Bevel', type='BEVEL')

                    obj.modifiers["Bevel"].segments = 3
                    obj.modifiers["Bevel"].limit_method = 'ANGLE'
                    obj.modifiers["Bevel"].angle_limit = 0.785398
                    obj.modifiers["Bevel"].width = 0.035
                    obj.modifiers["Bevel"].offset_type = 'WIDTH'
                    obj.modifiers["Bevel"].miter_outer = 'MITER_ARC'
                    obj.modifiers["Bevel"].show_expanded = False

                if mod_subsurf == True:

                    mod = obj.modifiers.get("Subdivision")
                    if mod is None:
                        obj.modifiers.new(name='Subdivision', type='SUBSURF')
                    
                    obj.modifiers["Subdivision"].levels = 2
                    obj.modifiers["Subdivision"].show_expanded = False
                    obj.modifiers["Subdivision"].show_in_editmode = False
                
                mod = obj.modifiers.get("Triangulate")
                if mod is None:
                    obj.modifiers.new(name='Triangulate', type='TRIANGULATE')

                obj.modifiers["Triangulate"].keep_custom_normals = True
                obj.modifiers["Triangulate"].quad_method = 'BEAUTY'
                obj.modifiers["Triangulate"].show_expanded = False
                obj.modifiers["Triangulate"].show_in_editmode = False

                mod = obj.modifiers.get("Weighted Normal")
                if mod is None:
                    obj.modifiers.new(name='Weighted Normal', type='WEIGHTED_NORMAL')

                obj.modifiers["Weighted Normal"].keep_sharp = True
                obj.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
                obj.modifiers["Weighted Normal"].show_expanded = False
                obj.modifiers["Weighted Normal"].show_in_editmode = False

                bpy.ops.object.shade_smooth()
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
                        
                        if mod_mirror == True:
                            obj.modifiers["Solidify"].use_rim_only = True
                        else:
                            obj.modifiers["Solidify"].use_rim_only = False

                        obj.modifiers["Solidify"].show_expanded = False
                
                if mod_bevel == True:

                    mod = obj.modifiers.get("Bevel")
                    if mod is None:
                        obj.modifiers.new(name='Bevel', type='BEVEL')

                    obj.modifiers["Bevel"].segments = 3
                    obj.modifiers["Bevel"].limit_method = 'ANGLE'
                    obj.modifiers["Bevel"].angle_limit = 0.785398
                    obj.modifiers["Bevel"].width = 0.035
                    obj.modifiers["Bevel"].offset_type = 'WIDTH'
                    obj.modifiers["Bevel"].miter_outer = 'MITER_ARC'
                    obj.modifiers["Bevel"].show_expanded = False

                if mod_subsurf == True:

                    mod = obj.modifiers.get("Subdivision")
                    if mod is None:
                        obj.modifiers.new(name='Subdivision', type='SUBSURF')
                    
                    obj.modifiers["Subdivision"].levels = 2
                    obj.modifiers["Subdivision"].show_expanded = False
                    obj.modifiers["Subdivision"].show_in_editmode = False
                
                mod = obj.modifiers.get("Triangulate")
                if mod is None:
                    obj.modifiers.new(name='Triangulate', type='TRIANGULATE')

                obj.modifiers["Triangulate"].keep_custom_normals = True
                obj.modifiers["Triangulate"].quad_method = 'BEAUTY'
                obj.modifiers["Triangulate"].show_expanded = False
                obj.modifiers["Triangulate"].show_in_editmode = False

                bpy.ops.object.shade_smooth()


        return {'FINISHED'}
        return {'FINISHED'}

#### Edit Mode ###################################################################


class MOD_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spin Modifier to edge.'

    def execute(self, context):

        solid_offset = context.scene.solid_offset
        solid_thickness = context.scene.solid_thickness

        axis_mode = context.scene.axis_mod
        mod_screw = context.scene.mod_screw
        mod_solid = context.scene.mod_solid
        mod_mirror = context.scene.mod_mirror
        mod_bevel = context.scene.mod_bevel
        mod_subsurf = context.scene.mod_subsurf

        obj = bpy.context.active_object

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.faces_shade_smooth()

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

                if mod_mirror == True:
                    if mod_solid == True:

                        mod = obj.modifiers.get("Solidify")
                        if mod is None:
                            obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                        obj.modifiers["Solidify"].offset = solid_offset
                        obj.modifiers["Solidify"].thickness = solid_thickness
                        obj.modifiers["Solidify"].use_even_offset = True
                        obj.modifiers["Solidify"].use_quality_normals = True
                        obj.modifiers["Solidify"].use_rim_only = True
                        obj.modifiers["Solidify"].show_expanded = False

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
                else:
                    if mod_solid == True:

                        mod = obj.modifiers.get("Solidify")
                        if mod is None:
                            obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                        obj.modifiers["Solidify"].offset = solid_offset
                        obj.modifiers["Solidify"].thickness = solid_thickness
                        obj.modifiers["Solidify"].use_even_offset = True
                        obj.modifiers["Solidify"].use_quality_normals = True
                        obj.modifiers["Solidify"].show_expanded = False
                
                if mod_bevel == True:

                    mod = obj.modifiers.get("Bevel")
                    if mod is None:
                        obj.modifiers.new(name='Bevel', type='BEVEL')

                    obj.modifiers["Bevel"].segments = 3
                    obj.modifiers["Bevel"].limit_method = 'ANGLE'
                    obj.modifiers["Bevel"].angle_limit = 0.785398
                    obj.modifiers["Bevel"].width = 0.035
                    obj.modifiers["Bevel"].offset_type = 'WIDTH'
                    obj.modifiers["Bevel"].miter_outer = 'MITER_ARC'
                    obj.modifiers["Bevel"].show_expanded = False

                if mod_subsurf == True:

                    mod = obj.modifiers.get("Subdivision")
                    if mod is None:
                        obj.modifiers.new(name='Subdivision', type='SUBSURF')
                    
                    obj.modifiers["Subdivision"].levels = 2
                    obj.modifiers["Subdivision"].show_expanded = False
                    obj.modifiers["Subdivision"].show_in_editmode = False
                
                mod = obj.modifiers.get("Triangulate")
                if mod is None:
                    obj.modifiers.new(name='Triangulate', type='TRIANGULATE')

                obj.modifiers["Triangulate"].keep_custom_normals = True
                obj.modifiers["Triangulate"].quad_method = 'BEAUTY'
                obj.modifiers["Triangulate"].show_expanded = False
                obj.modifiers["Triangulate"].show_in_editmode = False

                mod = obj.modifiers.get("Weighted Normal")
                if mod is None:
                    obj.modifiers.new(name='Weighted Normal', type='WEIGHTED_NORMAL')

                obj.modifiers["Weighted Normal"].keep_sharp = True
                obj.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
                obj.modifiers["Weighted Normal"].show_expanded = False
                obj.modifiers["Weighted Normal"].show_in_editmode = False

                #bpy.ops.object.shade_smooth()
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
                        
                        if mod_mirror == True:
                            obj.modifiers["Solidify"].use_rim_only = True
                        else:
                            obj.modifiers["Solidify"].use_rim_only = False

                        obj.modifiers["Solidify"].show_expanded = False
                
                if mod_bevel == True:

                    mod = obj.modifiers.get("Bevel")
                    if mod is None:
                        obj.modifiers.new(name='Bevel', type='BEVEL')

                    obj.modifiers["Bevel"].segments = 3
                    obj.modifiers["Bevel"].limit_method = 'ANGLE'
                    obj.modifiers["Bevel"].angle_limit = 0.785398
                    obj.modifiers["Bevel"].width = 0.035
                    obj.modifiers["Bevel"].offset_type = 'WIDTH'
                    obj.modifiers["Bevel"].miter_outer = 'MITER_ARC'
                    obj.modifiers["Bevel"].show_expanded = False

                if mod_subsurf == True:

                    mod = obj.modifiers.get("Subdivision")
                    if mod is None:
                        obj.modifiers.new(name='Subdivision', type='SUBSURF')
                    
                    obj.modifiers["Subdivision"].levels = 2
                    obj.modifiers["Subdivision"].show_expanded = False
                    obj.modifiers["Subdivision"].show_in_editmode = False
                
                mod = obj.modifiers.get("Triangulate")
                if mod is None:
                    obj.modifiers.new(name='Triangulate', type='TRIANGULATE')

                obj.modifiers["Triangulate"].keep_custom_normals = True
                obj.modifiers["Triangulate"].quad_method = 'BEAUTY'
                obj.modifiers["Triangulate"].show_expanded = False
                obj.modifiers["Triangulate"].show_in_editmode = False


        return {'FINISHED'}
        return {'FINISHED'}


