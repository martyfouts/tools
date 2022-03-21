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

def object_mesh_duplicate_draw(self, context):
    """Menu entry for mesh Duplicator"""
    self.layout.separator()
    self.layout.operator("tool.mesh_duplicate",
                    icon="OUTLINER_DATA_MESH")

# This function was provided by Blender StackExchange User scurest
# I've modified it to work in the context of the existing code.
# https://blender.stackexchange.com/a/242565/42221 for details
def do_copy_pure_geometry(src_mesh):
    dst_mesh = bpy.data.meshes.new(name=src_mesh.name)
 
    def copy_over(attr_name, sub_name, components=1):
        src_attr = getattr(src_mesh, attr_name)
        dst_attr = getattr(dst_mesh, attr_name)
 
        if len(dst_attr) != len(src_attr):
            dst_attr.add(len(src_attr))
 
        arr = [None] * (len(dst_attr) * components)
        src_attr.foreach_get(sub_name, arr)
        dst_attr.foreach_set(sub_name, arr)
 
    copy_over("vertices", "co", components=3)
    copy_over("edges", "vertices", components=2)
    copy_over("loops", "vertex_index")
    copy_over("polygons", "loop_start")
    copy_over("polygons", "loop_total")
 
    dst_mesh.validate()
    dst_mesh.update(calc_edges_loose=True)
 
    return dst_mesh

class TOOL_OT_mesh_duplicate(Operator):
    """Copy only the mesh of an object when duplicating it"""
    bl_idname = "tool.mesh_duplicate"
    bl_label = "duplicate mesh"
    bl_description = "Duplicate only the mesh of an object"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        if context.mode != 'OBJECT':
            cls.poll_message_set("Must be in Object mode")
            return False
        if not context.active_object:
            cls.poll_message_set("No object selected")
            return False
        if not context.active_object.type == 'MESH':
            cls.poll_message_set("Selected object is not a mesh")
            return False
        return True
    
    def execute(self, context):
        object = context.object
    
        new_mesh = do_copy_pure_geometry(object.data)
        new_object = bpy.data.objects.new(object.name, new_mesh)
        context.collection.objects.link(new_object)

        new_object.select_set(True)
        object.select_set(False)
        context.view_layer.objects.active = new_object
        return {'FINISHED'}

    def initialize():
        bpy.types.VIEW3D_MT_object.append(object_mesh_duplicate_draw)

    def deinitialize():
        bpy.types.VIEW3D_MT_object.remove(object_mesh_duplicate_draw)
