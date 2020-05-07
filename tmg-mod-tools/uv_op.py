import bpy

class UV_OT_MarginUnwrap(bpy.types.Operator):
	"""Quick test :)"""
	bl_idname = 'wm.uv_margin_unwrap_ot_operator'
	bl_label = 'UV Margin Unwrap'
	bl_description = 'UV smart unwarp.'
	bl_options = {'REGISTER', 'UNDO'}

	name: bpy.props.StringProperty(
	name="UV Name",
	description="Name for UV Map.",
	default="Custom UVmap"
	)

	margin: bpy.props.FloatProperty(
	name="Island Margin",
	description="Margin between UV islands.",
	default=0.03,
	min=0.01,
	soft_max=1.0
	)
	
	weight: bpy.props.FloatProperty(
	name="Area Weight",
	description="Area uv weight.",
	default=0.03,
	min=0.01,
	soft_max=1.0
	)

	@classmethod
	def poll(cls, context):
		#print(f"My area is: {context.area.type}")
		return context.area.type == 'VIEW_3D' or context.area.type == 'IMAGE_EDITOR'

	def execute(self, context):
		for obj in (bpy.context.selected_objects):
			if (obj.type == "MESH"):
				# bpy.ops.mesh.uv_texture_add()
				bpy.ops.mesh.uv_texture_add()
				obj.data.uv_layers.active.name = self.name
				bpy.ops.uv.smart_project(island_margin=self.margin, user_area_weight=self.weight)
				return {'FINISHED'}

# mesh_owners = {}
# name = 'Test UVs'

# for obj in (bpy.context.selected_objects):
#     if (obj.type == "MESH"):
#         mesh = obj.data
#         mesh_owners.setdefault(obj.data, []).append(obj)
#         bpy.ops.mesh.uv_texture_add()
#         obj.data.uv_layers.active.name = name
#         #bpy.ops.uv.smart_project(island_margin=0.3, user_area_weight=0.3)
#         print(mesh_owners[mesh])



# import bpy

# sel_objs = bpy.context.selected_objects
# objs_loop = []
# ob_count = 0
# uvName = 'Test UV'
# pack_multiple = True
# finished = False

# for ob in (sel_objs):
#     if ob.type == 'MESH':
#         objs_loop.append(ob)

# if pack_multiple == True:
#     for ib in (objs_loop):
#         bpy.ops.object.select_all(action='DESELECT')
#         if ib == objs_loop[ob_count]:
#             print(f'Loop: ', {ib.name})
#             bpy.context.view_layer.objects.active = objs_loop[ob_count]
#             bpy.ops.mesh.uv_texture_add()
#             ib.data.uv_layers.active.name = uvName
        
#             if ob_count < len(objs_loop):
#                 ob_count += 1
#             elif ob_count == len(objs_loop)-1:
#                 print("done")
# else:
#     for ib in (objs_loop):
#         bpy.ops.object.select_all(action='DESELECT')
#         if ib == objs_loop[ob_count]:
#             print(f'Loop: ', {ib.name})
#             bpy.context.view_layer.objects.active = objs_loop[ob_count]
#             bpy.ops.mesh.uv_texture_add()
#             ib.data.uv_layers.active.name = uvName
        
#             try:
#                 bpy.ops.uv.smart_project({'object': ib}, island_margin=0.3, user_area_weight=0.3)
#             except RuntimeError:
#                 pass
        
#             if ob_count < len(objs_loop):
#                 ob_count += 1    
