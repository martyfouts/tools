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
from bpy.props import BoolProperty, EnumProperty, FloatVectorProperty

# get_active_node_tree, get_node_types, and NODES_OT_color_by_type are all taken
# from a stack exchange answer by user Gorgious:
# from https://blender.stackexchange.com/a/256213/42221

def get_active_node_tree(context):
    node_area = context.area if context.area.type == "NODE_EDITOR" else None
    if node_area is None:
        return
    return node_area.spaces[0].edit_tree


def get_node_types(_, context):
    node_types = set()
    for node in get_active_node_tree(context).nodes:
        node_types.add(node.type)
    node_types = list(node_types)
    node_types.sort()
    return [(node_type,) * 3 for node_type in node_types]

class NODES_OT_color_by_type(bpy.types.Operator):
    bl_idname = "nodes.color_by_type"
    bl_label = "Color all nodes of a given type"
    bl_options = {"UNDO", "REGISTER"}

    @classmethod
    def poll(cls, context):
        return get_active_node_tree(context) is not None

    node_type: EnumProperty(name="Type", items=get_node_types)
    node_color: FloatVectorProperty(
        name="Color",
        subtype="COLOR",
        min=0,
        max=1,
        default=(0.5, 0.5, 0.5)
    )
    select_nodes: BoolProperty(
        name="Select nodes after operation",
        default=False)

    def invoke(self, context, event):
        if context.active_node is not None:
            self.node_type = context.active_node.type
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        node_type = self.node_type
        for node in get_active_node_tree(context).nodes:
            if node.type == node_type:
                node.use_custom_color = True
                node.color = self.node_color
                if self.select_nodes:
                    node.select = True
        return {"FINISHED"}