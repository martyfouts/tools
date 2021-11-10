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


class TOOL_OT_place_camera(Operator):
    bl_idname = "camera.place"
    bl_label = "place camera"
    bl_description = "place a camera in the viewport"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        """ Try very hard to find a camera to use
            If you can't find one create one
            If that all fails says so and cancel
            otherwise move the camera to the 3d view
            and make it the scene camera if it isn't already
        """
        my_camera = None
        scene_cameras = [object for object in context.scene.objects if object.type == "CAMERA"]
        # Alternative formulation
        # scene_cameras = [camera for camera in bpy.data.cameras if bpy.context.scene.objects.get(camera.name)]
        # Use only if profiling shows a good reason.
        selected_cameras = [object for object in context.selected_objects if object.type == "CAMERA"]

        # if exactly one camera is selected, use it
        if len(selected_cameras) == 1:
            my_camera = selected_cameras[0]
            print("using selected camera")
  
        # if more than one camera is select report the error
        elif len(selected_cameras):
            print("Please select only one camera")
  
         # No selected camera, see if the scene camera is a camera
        elif context.scene.camera and context.scene.camera.type == "CAMERA":
            my_camera = context.scene.camera
            print("Using scene camera")
  
        # If there is one camera in the scene, use it
        elif len(scene_cameras) == 1:
            my_camera = scene_cameras[0]
            print("Using available camera")
  
        # If there is more than one camera in the scene, report the error
        elif len(scene_cameras):
            print("Please select a camera")
  
        # There are no useable camers, create one
        else:
            print("There are no cameras, attempting to add one")
            camera_data = bpy.data.cameras.new(name="Camera")
            my_camera = bpy.data.objects.new("Camera", camera_data)
            bpy.context.scene.collection.objects.link(my_camera)

        if my_camera is None:
            return{"CANCELLED"}

        # make the chosen camera the scene camera if it isn't already
        if not my_camera is context.scene.camera:
            print("Setting scene camera to {my_camera.name}")
            context.scene.camera = my_camera

        bpy.ops.view3d.camera_to_view()
        return {"FINISHED"}

class TOOL_OT_add_camera(Operator):
    bl_idname = "camera.add"
    bl_label = "add camera"
    bl_description = "add a camera in the viewport"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        """ Add a new camera to the scene, make it the active camera,
            and match it to the current view.
        """

        camera_data = bpy.data.cameras.new(name="Camera")
        if camera_data is None:
            return {"CANCELLED"}

        my_camera = bpy.data.objects.new("Camera", camera_data)

        if my_camera is None:
            return {"CANCELLED"}

        bpy.context.scene.collection.objects.link(my_camera)
        context.scene.camera = my_camera

        bpy.ops.view3d.camera_to_view()
        return {"FINISHED"}