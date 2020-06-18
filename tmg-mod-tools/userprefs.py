
import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty


class TMG_User_Preferences(AddonPreferences):
    bl_idname = 'tmg-mod-tools'

    Sculpt_Button_Mode: bpy.props.BoolProperty(
        name="Button Icon Mode",
        description="Choose if the sculpt panel buttons are text labels or icons.",
        default=False
    )

    Sculpt_Keyframe_Timeline: bpy.props.BoolProperty(
        name="Keyframe Layers",
        description="Keyframes timeline when you add a shape layer.",
        default=False
    )

    shape_settings_menu: bpy.props.BoolProperty(
        name="Layer Panel Settings",
        description="Show shape layer settings.",
        default=False
    )

    # def invoke(self, context, event):
    #     bpy.types.Scene.sculpt_shape_keys_icon_view = self.Sculpt_Button_Mode
    #     return self.execute(context)

    def execute(self, context):
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences
        return {'FINISHED'}

    def draw(self, context):
        self.layout.prop(self, "Sculpt_Button_Mode")
        self.layout.prop(self, "Sculpt_Keyframe_Timeline")
        self.layout.prop(self, "shape_settings_menu")


def register():
    properties.register()
    ui.register()
    events.register()
    operators.register()
    bpy.utils.register_class(TMG_User_Preferences)

    # Make sure the intial preferences value gets set.
    user_preferences = bpy.context.user_preferences
    addon_prefs = user_preferences.addons["tmg-mod-tools"].preferences

    # Sculpt Panel Variables
    bpy.types.Scene.sculpt_shape_keys_icon_view = self.Sculpt_Button_Mode
    bpy.types.Scene.keyframe_timeline = self.Sculpt_Keyframe_Timeline
    bpy.types.Scene.shape_settings_menu = self.shape_settings_menu

