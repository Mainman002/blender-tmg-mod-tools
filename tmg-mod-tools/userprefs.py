
import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty


def Update_TMG_User_Preferences_changed(self, context):
    bpy.types.Scene.sculpt_shape_keys_icon_view = self.Sculpt_Button_Mode
    # print(bpy.types.Scene.sculpt_shape_keys_icon_view)
    print("New Test: % s" % bpy.types.Scene.sculpt_shape_keys_icon_view)


class TMG_User_Preferences(AddonPreferences):
    # This must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

# category: StringProperty(
    # 	name="Tab Category",
    # 	description="Choose a name for the category of the panel",
    # 	default="Edit",
    # 	update=update_panel
    # )

    Sculpt_Button_Mode: bpy.props.BoolProperty(
        name="Sculpt Button Mode",
        description="Choose if the sculpt panel buttons are text labels or icons.",
        default=False,
        update=Update_TMG_User_Preferences_changed
    )

    def invoke(self, context, event):
        bpy.types.Scene.sculpt_shape_keys_icon_view = self.Sculpt_Button_Mode
        return self.execute(context)

    def execute(self, context):
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences
        info = ("Path: %s, Number: %d, Boolean %r" %
                (addon_prefs.filepath, addon_prefs.number, addon_prefs.boolean))

        self.report({'INFO'}, info)
        print(info)

        return {'FINISHED'}

    def draw(self, context):
        self.layout.prop(self, "Sculpt_Button_Mode")


def register():
    properties.register()
    ui.register()
    events.register()
    operators.register()
    bpy.utils.register_class(TMG_User_Preferences)

    # Make sure the intial preferences value gets set.
    user_preferences = bpy.context.user_preferences
    addon_prefs = user_preferences.addons["tmg_mod_tools"].preferences
    # context.scene.sculpt_shape_keys_icon_view = addon_prefs.Sculpt_Button_Mode
    # self.Sculpt_Button_Mode = addon_prefs.Sculpt_Button_Mode
    # context.scene.sculpt_shape_keys_icon_view = addon_prefs.Sculpt_Button_Mode
