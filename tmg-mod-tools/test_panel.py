import bpy

class Object_Test_Panel(bpy.types.Panel):
	bl_idname = 'OBJECT_PT_test_panel'
	bl_category = 'Edit'
	bl_label = 'TMG Test Panel'
	bl_context = "mesh_edit"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	# mesh_edit objectmode

	@classmethod
	def poll(cls, context):
		engine = context.engine
		obj = context.object
		return (obj and obj.type in {'MESH', 'LATTICE', 'CURVE', 'SURFACE'} and (engine in cls.COMPAT_ENGINES))

	def draw(self, context):

		scene = context.scene
		sculpt_single_shape_layer = context.scene.sculpt_single_shape_layer
		button_mode = context.scene.sculpt_shape_keys_icon_view

		layout = self.layout
		row = layout.row(align=True)

		ob = context.object
		key = ob.data.shape_keys
		kb = ob.active_shape_key

		scene = context.scene

		# ob = bpy.context.view_layer.objects.active

		obj = context.object

		#sel_mode = context.tool_settings.mesh_select_mode
		
		textNameLink = context.scene.textNameLink
		text_name = context.scene.textName
		text_text = context.scene.textText
		text_vAlign = context.scene.text_vAlign
		text_hAlign = context.scene.text_hAlign

		layout = self.layout

		layout.use_property_split = True
		layout.use_property_decorate = False  # No animation.

		#### Master Panel Layout Controllers ###############################

		Master_Col = layout.column(align=True)
		Master_Subcol = Master_Col.column()

		#### View Tab Panel Layout Controllers #########################

		Text_Col = Master_Col.column(align=True)
		Text_Subcol = Text_Col.column()
		Text_Row = Text_Col.row()

		#### View Tab  ############################################################################################################

		Text_Col = Master_Col.column() ###### Box if needed for View Panel #############
		Text_Subcol = Text_Col.column(align=True)

		Text_Col.use_property_split = True
		Text_Flow = Text_Col.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=True, align=True)

		colb = Text_Flow.box()
		row = colb.row(align=True)
		colm = row.row(align=True)

		Text_Flow = colm.column(align=True)
		Text_Flow.alignment = 'RIGHT'
		Text_Flow.label(text="Test 1")

		enable_edit = ob.mode == 'EDIT'
		enable_edit_value = False

		if ob.show_only_shape_key is False:
			if enable_edit or (ob.type == 'MESH' and ob.use_shape_key_edit_mode):
				enable_edit_value = True

		row = layout.row()

		rows = 3
		if kb:
			rows = 6

		row.template_list("MESH_UL_shape_keys", "", key, "key_blocks", ob, "active_shape_key_index", rows=rows)













# import bpy

# # Singleton for storing global state
# class _MyState:
#     __slots__ = (
#         "custom_list",
#     )
    
#     def __init__(self):
#         self.custom_list = ["test", "1", "2", "blurg!"]
        
#         my_state = _MyState()
#         del _MyState


# def comboCanged(self, context):
#     current = bpy.context.scene.comboBox
#     print("change to: ", current)

# def updateComboContent(cItems):
#     if cItems:
#         bpy.types.Scene.comboBox = bpy.props.EnumProperty(
#             items=cItems,
#             name="Items",
#             description="Item",
#             default=None,
#             update=comboCanged
#         )
        
# def mySceneProperties():
#     bpy.types.Scene.Iname = bpy.props.StringProperty( name = "", default = "", description = "Item Name")

#     comboItems = [
#         ("no_items", "No items", "", 1),
#     ]
#     updateComboContent(comboItems)



# class MATERIAL_UL_matslots_example(bpy.types.UIList):
#     # The draw_item function is called for each item of the collection that is visible in the list.
#     #   data is the RNA object containing the collection,
#     #   item is the current drawn item of the collection,
#     #   icon is the "computed" icon for the item (as an integer, because some objects like materials or textures
#     #   have custom icons ID, which are not available as enum items).
#     #   active_data is the RNA object containing the active property for the collection (i.e. integer pointing to the
#     #   active item of the collection).
#     #   active_propname is the name of the active property (use 'getattr(active_data, active_propname)').
#     #   index is index of the current item in the collection.
#     #   flt_flag is the result of the filtering process for this item.
#     #   Note: as index and flt_flag are optional arguments, you do not have to use/declare them here if you don't
#     #         need them.
#     def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
#         ob = data
#         slot = item
#         ma = slot.material
#         # draw_item must handle the three layout types... Usually 'DEFAULT' and 'COMPACT' can share the same code.
#         if self.layout_type in {'DEFAULT', 'COMPACT'}:
#             # You should always start your row layout by a label (icon + text), or a non-embossed text field,
#             # this will also make the row easily selectable in the list! The later also enables ctrl-click rename.
#             # We use icon_value of label, as our given icon is an integer value, not an enum ID.
#             # Note "data" names should never be translated!
#             if ma:
#                 layout.prop(ma, "name", text="", emboss=False, icon_value=icon)
#             else:
#                 layout.label(text="", translate=False, icon_value=icon)
#         # 'GRID' layout type should be as compact as possible (typically a single icon!).
#         elif self.layout_type in {'GRID'}:
#             layout.alignment = 'CENTER'
#             layout.label(text="", icon_value=icon)


# # And now we can use this list everywhere in Blender. Here is a small example panel.
# class UIListPanelExample(bpy.types.Panel):
#     """Creates a Panel in the Object properties window"""
#     bl_label = "UIList Panel"
#     bl_idname = "OBJECT_PT_ui_list_example"
#     bl_space_type = 'PROPERTIES'
#     bl_region_type = 'WINDOW'
#     bl_context = "object"

#     def draw(self, context):
#         layout = self.layout
        
#         obj = context.object
#         custom_list = ["test", "1", "maybe", "_bla?_", "test"]
#         bpy.types.Scene.custom_list = custom_list
        
#         layout.label(text="Custom box")
        
#         #layout.template_list("MATERIAL_UL_matslots_example", "", obj, "material_slots", obj, "active_material_index")
#         #layout.template_list("UI_UL_list", "MATERIAL_UL_matslots_example", obj, "material_slots", obj, "active_material_index")
        
#         row = layout.row(align=True)
        
#         row.operator("wm.add_ot_some_value", text="", icon='ADD')
#         row.operator("wm.add_ot_some_value", text="", icon='REMOVE')
        
#         container = layout.box()
#         colm = container.column(align=True)

#         for i in bpy.types.Scene.custom_list:
#             row = colm.row(align=True)
#             #row.label(text=i)
#             row.operator("wm.add_ot_some_value", text=i)
#             row.operator("wm.add_ot_some_value", text="", icon='REMOVE')
#             #row.label(text="", icon='REMOVE')
#             #row.label(text="", icon='ADD')


# class ADD_OT_Some_Value(bpy.types.Operator):
#     bl_idname = 'wm.add_ot_some_value'
#     bl_label = 'Add Some Value'
#     bl_description = 'Add Solid Circle.'
#     bl_options = {'REGISTER', 'UNDO'}


#     def execute(self, context):
        
#         print("bla")
#         #_MyState.custom_list.append("some_test")

#         return {'FINISHED'}


# def register():
#     bpy.utils.register_class(MATERIAL_UL_matslots_example)
#     bpy.utils.register_class(UIListPanelExample)
#     bpy.utils.register_class(ADD_OT_Some_Value)
#     #bpy.utils.register_class(_MyState)


# def unregister():
#     bpy.utils.unregister_class(MATERIAL_UL_matslots_example)
#     bpy.utils.unregister_class(UIListPanelExample)
#     bpy.utils.unregister_class(ADD_OT_Some_Value)
#     #bpy.utils.unregister_class(_MyState)


# if __name__ == "__main__":
#     register()













import bpy
import bmesh
from mathutils import Vector

bl_info = {
    'name': 'Add Empties',
    'author': 'Dealga McArdle (zeffii)',
    'description': 'adds new Empty while in edit mode',
    'blender': (2, 7, 3),
    'version': (2, 80, 0),
    'location': 'Add > Empties',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'Mesh'
}

def add_to_selected(context, kind):
    D = bpy.data
    scn = context.scene
    obj = context.edit_object
    obj_name = obj.name
    mesh = obj.data

    bm = bmesh.from_edit_mesh(mesh)

    def add_empty(coordinate, kind='PLAIN_AXES'):
        empty = D.objects.new('MT_' + obj_name, None)
        empty.location = coordinate
        empty.empty_draw_size = 0.45
        empty.empty_draw_type = kind
        scn.objects.link(empty)
        scn.update()

    coordinates = [v.co[:] for v in bm.verts if v.select]

    # must be in object mode to add objects to the scene.
    myob = D.objects[obj_name]
    bpy.ops.object.mode_set(mode='OBJECT')

    if not coordinates:
        coordinate = context.scene.cursor_location
        add_empty(coordinate, kind)
    else:
        for co in coordinates:
            vert_coordinate = myob.matrix_world * Vector(co)
            add_empty(vert_coordinate, kind)

    # set original object to active, selects it, place back into editmode
    scn.objects.active = myob
    myob.select = True
    bpy.ops.object.mode_set(mode='EDIT')
    return


class AddEmpties(bpy.types.Operator):
    """Add a vertex to 3d cursor location"""
    bl_idname = "object.empties_add"
    bl_label = "Add Empties"
    bl_options = {'REGISTER', 'UNDO'}

    kind = bpy.props.StringProperty(default='PLAIN_AXES')

    def execute(self, context):
        add_to_selected(context, self.kind)
        return {'FINISHED'}


class EDITMODE_MT_PlaceEmpties(bpy.types.Menu):
    bl_label = "Adding Empties.."

    def draw(self, context):
        options = [
            'PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW',
            'CIRCLE', 'CUBE', 'SPHERE', 'CONE', 'IMAGE']

        layout = self.layout
        for opt in options:
            layout.operator("object.empties_add", text=opt).kind = opt


def menu_func(self, context):
    self.layout.menu("EDITMODE_MT_PlaceEmpties", icon='EMPTY_DATA')
    
    
    
classes = (
    AddEmpties,
    EDITMODE_MT_PlaceEmpties,
    
)


def register():
    for rsclass in classes:
        bpy.utils.register_class(rsclass)
    #bpy.types.VIEW3D_MT_mesh_add.append(mesh_add_menu_draw)
    # user_preferences = bpy.ops.scene.user_preferences
    # addon_prefs = user_preferences.addons["tmg_mod_tools"].preferences
    # context.scene.sculpt_shape_keys_icon_view = addon_prefs.Sculpt_Button_Mode


def unregister():
    for rsclass in classes:
        bpy.utils.unregister_class(rsclass)
    #bpy.types.VIEW3D_MT_mesh_add.remove(mesh_add_menu_draw)
    

if __name__ == "__main__":
    register()













import bpy
import bmesh
from bpy_extras.object_utils import AddObjectHelper
from bpy.types import Operator
from math import radians
from mathutils import Matrix, Vector, Euler

C = bpy.context
cursor = C.scene.cursor
obj = C.active_object
p = obj.data.polygons

### Set Rotation
def rotate_to_vec(thevector):
    from bpy import context
    vec = thevector
    obj = context.object
    # object axis to align with vector vec
    axis = Vector((0, 0, 1.0))

    # rotation difference
    #q = axis.rotation_difference(vec)
    # or
    # track quaternion
    q = vec.to_track_quat('Z', 'Y')

    loc, rot, scale = obj.matrix_world.decompose()

    mat_scale = Matrix()
    for i in range(3):
        mat_scale[i][i] = scale[i]

    obj.matrix_world = (Matrix.Translation(loc) @ q.to_matrix().to_4x4() @ mat_scale)
    #print(Matrix.Translation(loc) @ mat_scale)

### Get Active Faces
def _active_faces():
    face_count = []
    
    # Get a BMesh representation
    bm = bmesh.new()   # create an empty BMesh
    bm.from_mesh(obj.data)   # fill it in from a Mesh
    
    # Get all selected faces
    # Note: bm.select_history lacks geometry selected via border select, lasso, etc.
    #       (mass-selection operators)!

    for face in bm.faces:
        if face.select:
            face_count.append(face) # BMFace | index | totverts
            #print(repr(face))
            
    print("new count")
    face_index = len(face_count)

    while face_index:
        face_index -= 1
        if face_index == 0:
            print("Active Face: % a " % face_count[face_index].index)
            _add_objects()
        elif face_index > 0:
            _add_objects()
            face_count.pop(face_index)
        print(face_index)

### Add Objects
def _add_objects():
    bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='CURSOR', location=cursor_loc)
    rotate_to_vec(vec)
    print("Added Object")

        

bpy.ops.object.editmode_toggle()

#get the normal and center of the selected face
normal = obj.data.polygons[p.active].normal
center = obj.data.polygons[p.active].center

#generate a quaternion rotation from the normal vector
up = normal.to_track_quat('X', 'Y')

#set the cursor to the center location and rotate it to match the up vector
cursor.location = center
cursor.rotation_quaternion = up

cursor_loc = bpy.context.scene.cursor.location
vec = obj.closest_point_on_mesh( cursor_loc )[2]

_active_faces()















