# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
 
import bpy
from bpy.types import Operator

class TOOL_OT_modifier_apply_all(Operator):
    """Apply all modifiers to the active object
        There must be an active object and it must be in object mode.
    """
    bl_idname = "modifier.apply_all"
    bl_label = "Apply All"
    bl_description = "apply all modifiers to active object"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(self, context):
        object = context.object
        return object and object.mode == "OBJECT"

    def execute(self, context):
        active_object = context.view_layer.objects.active
        for modifier in active_object.modifiers:
           bpy.ops.object.modifier_apply(modifier = modifier.name)
        return {"FINISHED"}

class TOOL_OT_modifier_remove_all(Operator):
    """Remove all modifiers from the active object
        There must be an active object and it must be in object mode.
    """
    bl_idname = "modifier.remove_all"
    bl_label = "Remove All"
    bl_description = "remove all modifiers from active object"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        object = context.object
        if not object:
            cls.poll_message_set("No object selected")
            return False
        if object.mode != "OBJECT":
            cls.poll_message_set("Not in object mode")
            return False
        return True

    def execute(self, context):
        active_object = context.view_layer.objects.active
        active_object.modifiers.clear()
        return {"FINISHED"}