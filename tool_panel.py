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
from bpy.types import Panel  

class TOOL_common_settings:
    """Setting shared by all panels in this file"""
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Tools"
    bl_options = {"HIDE_HEADER"}

class TOOL_PT_tools(Panel, TOOL_common_settings):
    """Parent of all of the tool panels"""
    bl_label = "My Tools"
    bl_description = "Workflow support"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Tool Collection")
 
class TOOL_PT_camera_panel(Panel, TOOL_common_settings):
    """Tools specific to cameras"""
    bl_label = "Camera"
    bl_parent_id = "TOOL_PT_tools"
    bl_description = "Camera Placement tools"

    @classmethod
    def poll(self, context):
        return context.mode == "OBJECT"
        
    def draw(self, context):
        layout = self.layout
        layout.label(text="Camera")
        row = layout.row()
        row.operator("camera.place", text="place camera")
        row = layout.row()
        row.operator("camera.add", text="add camera")

class TOOL_PT_modifier_panel(Panel, TOOL_common_settings):
    """Tools specific to manipulating modifiers"""
    bl_label = "Modifiers"
    bl_parent_id = "TOOL_PT_tools"
    bl_description = "Camera Placement tools"

    @classmethod
    def poll(self, context):
        return context.mode == "OBJECT"
        
    def draw(self, context):
        layout = self.layout
        layout.label(text="Modifiers")
        row = layout.row()
        col = row.column()
        col.operator("modifier.apply_all", text="apply All")
        col = row.column()
        col.operator("modifier.remove_all", text="remove All")
