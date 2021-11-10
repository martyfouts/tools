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

bl_info = {
    "name" : "TOOL",
    "description" : "quick scripts for common operations",
    "author" : "Marty Fouts <fouts@fogey.com>",
    "version" : (0, 0, 1),
    "blender" : (2, 93, 0),
    "location" : "View3D",
    "warning" : "",
    "support" : "COMMUNITY",
    "doc_url" : "",
    "category" : "3D View"
}

# This bit is here because Python doesn't do recursive reloading 
# This works for a single level but I don't know will it work
# if the imported modules import other modules for the package.
# This is only support for development. It's not meant to replace
# unregister operations in production.
if "bpy" in locals():
    print("UIX Reloading")
    from importlib import reload
    import sys
    for k, v in list(sys.modules.items()):
        if k.startswith("UI example."):
            reload(v)
# End of recursive reload support

import bpy

from . camera_op import TOOL_OT_place_camera, TOOL_OT_add_camera
from . tool_panel import TOOL_PT_tools, TOOL_PT_camera_panel, TOOL_PT_modifier_panel
from . modifiers import TOOL_OT_modifier_apply_all, TOOL_OT_modifier_remove_all
from . mesh_ops import TOOL_OT_mesh_duplicate

classes = [
    TOOL_OT_place_camera,
    TOOL_OT_add_camera,
    TOOL_PT_tools,
    TOOL_PT_camera_panel,
    TOOL_OT_modifier_apply_all,
    TOOL_OT_modifier_remove_all,
    TOOL_PT_modifier_panel,
    TOOL_OT_mesh_duplicate,
    ]

def register():
    for c in classes:
        bpy.utils.register_class(c)
        if "initialize" in dir(c):
            c.initialize()

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
        if "initialize" in dir(c):
            c.deinitialize()

if __name__ == "__main__":
    register()



