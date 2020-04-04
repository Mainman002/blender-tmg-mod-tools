import bpy

class UV_OT_MarginUnwrap(bpy.types.Operator):
	"""Quick test :)"""
	bl_idname = 'wm.uv_margin_unwrap_ot_operator'
	bl_label = 'UV Margin Unwrap'
	bl_description = 'UV smart unwarp.'
	bl_options = {'REGISTER', 'UNDO'}

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
				bpy.ops.uv.smart_project(island_margin=self.margin, user_area_weight=self.weight)
		return {'FINISHED'}
