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


        #self.mod = obj.modifiers.get("Screw")
        #if self.mod is 'Screw':
            # otherwise add a modifier to selected object
            #obj.modifiers.remove(name='Screw', type='SCREW')
        
        #self.mod = obj.modifiers.get("Solidify")
        #if self.mod is 'Solidify':
            # otherwise add a modifier to selected object
            #obj.modifiers.remove(name='Solidify', type='SOLIDIFY')

        #self.mod = obj.modifiers.get("Mirror")
        #if self.mod is 'Mirror':
            # otherwise add a modifier to selected object
            #obj.modifiers.remove(name='Mirror', type='MIRROR')

        #self.mod = obj.modifiers.get("Bevel")
        #if self.mod is 'Bevel':
            # otherwise add a modifier to selected object
            #obj.modifiers.remove(name='Bevel', type='BEVEL')

        #self.mod = obj.modifiers.get("Subdivision")
        #if self.mod is 'Subdivision':
            # otherwise add a modifier to selected object
            #obj.modifiers.remove(name='Subdivision', type='SUBSURF')

        #self.mod = obj.modifiers.get("Triangulate")
        #if self.mod is 'Triangulate':
            # otherwise add a modifier to selected object
            #obj.modifiers.remove(name='Triangulate', type='TRIANGULATE')

        #self.mod = obj.modifiers.get("Weighted Normal")
        #if self.mod is 'Weighted Normal':
            # otherwise add a modifier to selected object
            #obj.modifiers.remove(name='Weighted Normal', type='WEIGHTED_NORMAL')


        #sel = bpy.context.selected_objects
        #act = bpy.context.active_object

        #for obj in sel:
            #if obj != act:
                #bpy.context.active_object = obj #sets the obj accessible to bpy.ops
                #bpy.ops.object.modifier_add(type='SOLIDIFY')
                #bpy.context.object.modifiers["Solidify"].thickness = 0.1

        #obj = bpy.context.view_layer.objects.active

        #bpy.context.object.modifiers["Solidify.001"].name = "Solidify.001"

        if mod_screw == True:

            self.mod = obj.modifiers.get("Screw")
            if self.mod is None:
                # otherwise add a modifier to selected object
                obj.modifiers.new(name='Screw', type='SCREW')

            bpy.context.object.modifiers["Screw"].axis = 'Y'
            bpy.context.object.modifiers["Screw"].use_normal_calculate = True
            bpy.context.object.modifiers["Screw"].show_expanded = False
            bpy.context.object.modifiers["Screw"].use_merge_vertices = True
            #bpy.context.object.modifiers["Screw"].show_in_editmode = False

        if mod_mirror == True:
            if mod_solid == True:

                self.mod = obj.modifiers.get("Solidify")
                if self.mod is None:
                    # otherwise add a modifier to selected object
                    obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                bpy.context.object.modifiers["Solidify"].offset = solid_offset
                bpy.context.object.modifiers["Solidify"].thickness = solid_thickness
                bpy.context.object.modifiers["Solidify"].use_even_offset = True
                bpy.context.object.modifiers["Solidify"].use_quality_normals = True
                bpy.context.object.modifiers["Solidify"].use_rim_only = True
                bpy.context.object.modifiers["Solidify"].show_expanded = False

                self.mod = obj.modifiers.get("Mirror")
                if self.mod is None:
                    # otherwise add a modifier to selected object
                    obj.modifiers.new(name='Mirror', type='MIRROR')

            bpy.context.object.modifiers["Mirror"].use_axis[0] = False

            if axis_mode == "X":
                bpy.context.object.modifiers["Mirror"].use_axis[0] = True
                bpy.context.object.modifiers["Mirror"].use_bisect_axis[0] = True
            elif axis_mode == "Y":
                bpy.context.object.modifiers["Mirror"].use_axis[1] = True
                bpy.context.object.modifiers["Mirror"].use_bisect_axis[1] = True
            elif axis_mode == "Z":
                bpy.context.object.modifiers["Mirror"].use_axis[2] = True
                bpy.context.object.modifiers["Mirror"].use_bisect_axis[2] = True
            
            bpy.context.object.modifiers["Mirror"].use_clip = True
            bpy.context.object.modifiers["Mirror"].show_expanded = False
        else:
            if mod_solid == True:

                self.mod = obj.modifiers.get("Solidify")
                if self.mod is None:
                    # otherwise add a modifier to selected object
                    obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                bpy.context.object.modifiers["Solidify"].offset = solid_offset
                bpy.context.object.modifiers["Solidify"].thickness = solid_thickness
                bpy.context.object.modifiers["Solidify"].use_even_offset = True
                bpy.context.object.modifiers["Solidify"].use_quality_normals = True
                bpy.context.object.modifiers["Solidify"].show_expanded = False
                #bpy.context.object.modifiers["Solidify"].show_in_editmode = False
        
        if mod_bevel == True:

            self.mod = obj.modifiers.get("Bevel")
            if self.mod is None:
                 # otherwise add a modifier to selected object
                obj.modifiers.new(name='Bevel', type='BEVEL')

            bpy.context.object.modifiers["Bevel"].segments = 3
            bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
            bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
            bpy.context.object.modifiers["Bevel"].width = 0.035
            bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
            bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
            bpy.context.object.modifiers["Bevel"].show_expanded = False
            #bpy.context.object.modifiers["Bevel"].show_in_editmode = False

        if mod_subsurf == True:

            self.mod = obj.modifiers.get("Subdivision")
            if self.mod is None:
                 # otherwise add a modifier to selected object
                obj.modifiers.new(name='Subdivision', type='SUBSURF')
            
            bpy.context.object.modifiers["Subdivision"].levels = 2
            bpy.context.object.modifiers["Subdivision"].show_expanded = False
            bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
        
        self.mod = obj.modifiers.get("Triangulate")
        if self.mod is None:
            # otherwise add a modifier to selected object
            obj.modifiers.new(name='Triangulate', type='TRIANGULATE')

        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].quad_method = 'BEAUTY'
        bpy.context.object.modifiers["Triangulate"].show_expanded = False
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False

        self.mod = obj.modifiers.get("Weighted Normal")
        if self.mod is None:
            # otherwise add a modifier to selected object
            obj.modifiers.new(name='Weighted Normal', type='WEIGHTED_NORMAL')

        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False

        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398

        return {'FINISHED'}
        return {'FINISHED'}

#### Edit Mode ###################################################################


class MOD_Edit_OT_Operator(bpy.types.Operator):
    bl_idname = 'wm.mod_edit_ot_operator'
    bl_label = 'Decimate Panel'
    bl_description = 'Add Spin Modifier to edge.'

    def execute(self, context):

        obj = bpy.context.active_object

        solid_offset = context.scene.solid_offset
        solid_thickness = context.scene.solid_thickness

        axis_mode = context.scene.axis_mod
        mod_screw = context.scene.mod_screw
        mod_solid = context.scene.mod_solid
        mod_mirror = context.scene.mod_mirror
        mod_bevel = context.scene.mod_bevel
        mod_subsurf = context.scene.mod_subsurf

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.faces_shade_smooth()

        if mod_mirror == True:

            if mod_solid == True:

                self.mod = obj.modifiers.get("Solidify")
                if self.mod is None:
                    # otherwise add a modifier to selected object
                    obj.modifiers.new(name='Solidify', type='SOLIDIFY')
                
                bpy.context.object.modifiers["Solidify"].offset = solid_offset
                bpy.context.object.modifiers["Solidify"].thickness = solid_thickness
                bpy.context.object.modifiers["Solidify"].use_even_offset = True
                bpy.context.object.modifiers["Solidify"].use_quality_normals = True
                bpy.context.object.modifiers["Solidify"].use_rim_only = True
                bpy.context.object.modifiers["Solidify"].show_expanded = False

            self.mod = obj.modifiers.get("Mirror")
            if self.mod is None:
                # otherwise add a modifier to selected object
                obj.modifiers.new(name='Mirror', type='MIRROR')
            
            bpy.context.object.modifiers["Mirror"].use_axis[0] = False
            bpy.context.object.modifiers["Mirror"].use_axis[2] = True
            bpy.context.object.modifiers["Mirror"].use_bisect_axis[2] = True
            bpy.context.object.modifiers["Mirror"].use_clip = True
            bpy.context.object.modifiers["Mirror"].show_expanded = False

        else:
            if mod_solid == True:

                self.mod = obj.modifiers.get("Solidify")
                if self.mod is None:
                    # otherwise add a modifier to selected object
                    obj.modifiers.new(name='Solidify', type='SOLIDIFY')

                bpy.context.object.modifiers["Solidify"].offset = solid_offset
                bpy.context.object.modifiers["Solidify"].use_even_offset = True
                bpy.context.object.modifiers["Solidify"].use_quality_normals = True
                bpy.context.object.modifiers["Solidify"].thickness = solid_thickness
                bpy.context.object.modifiers["Solidify"].show_expanded = False
                bpy.context.object.modifiers["Solidify"].show_on_cage = True

        if mod_screw == True:

            self.mod = obj.modifiers.get("Screw")
            if self.mod is None:
                # otherwise add a modifier to selected object
                obj.modifiers.new(name='Screw', type='SCREW')

            bpy.context.object.modifiers["Screw"].axis = 'Y'
            bpy.context.object.modifiers["Screw"].use_normal_calculate = True
            bpy.context.object.modifiers["Screw"].show_expanded = False
            bpy.context.object.modifiers["Screw"].use_merge_vertices = True
            #bpy.context.object.modifiers["Screw"].show_in_editmode = False

        if mod_bevel == True:
            
            self.mod = obj.modifiers.get("Bevel")
            if self.mod is None:
                 # otherwise add a modifier to selected object
                obj.modifiers.new(name='Bevel', type='BEVEL')

            bpy.context.object.modifiers["Bevel"].segments = 2
            bpy.context.object.modifiers["Bevel"].segments = 3
            bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
            bpy.context.object.modifiers["Bevel"].angle_limit = 0.785398
            bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
            bpy.context.object.modifiers["Bevel"].miter_outer = 'MITER_ARC'
            bpy.context.object.modifiers["Bevel"].width = 0.04
            bpy.context.object.modifiers["Bevel"].show_in_editmode = False
            bpy.context.object.modifiers["Bevel"].show_expanded = False

        if mod_subsurf == True:
            
            self.mod = obj.modifiers.get("Subdivision")
            if self.mod is None:
                 # otherwise add a modifier to selected object
                obj.modifiers.new(name='Subdivision', type='SUBSURF')

            bpy.context.object.modifiers["Subdivision"].levels = 2
            bpy.context.object.modifiers["Subdivision"].show_in_editmode = False
            bpy.context.object.modifiers["Subdivision"].show_expanded = False

        self.mod = obj.modifiers.get("Triangulate")
        if self.mod is None:
            # otherwise add a modifier to selected object
            obj.modifiers.new(name='Triangulate', type='TRIANGULATE')

        bpy.context.object.modifiers["Triangulate"].keep_custom_normals = True
        bpy.context.object.modifiers["Triangulate"].quad_method = 'BEAUTY'
        bpy.context.object.modifiers["Triangulate"].show_expanded = False

        self.mod = obj.modifiers.get("Weighted Normal")
        if self.mod is None:
            # otherwise add a modifier to selected object
            obj.modifiers.new(name='Weighted Normal', type='WEIGHTED_NORMAL')

        bpy.context.object.modifiers["Weighted Normal"].keep_sharp = True
        bpy.context.object.modifiers["Weighted Normal"].mode = 'FACE_AREA_WITH_ANGLE'
        bpy.context.object.modifiers["Triangulate"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_in_editmode = False
        bpy.context.object.modifiers["Weighted Normal"].show_expanded = False

        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398

        return {'FINISHED'}
        return {'FINISHED'}


