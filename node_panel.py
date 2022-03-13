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

class NODES_common_settings:
    """Setting shared by all panels in this file"""
    bl_space_type = "NODE_EDITOR"
    bl_label = "My Tools"
    bl_region_type = "UI"
    bl_category = "Tool"

class NODES_PT_tools(Panel, NODES_common_settings):

    def draw(self, context):
        self.layout.operator("nodes.color_by_type")