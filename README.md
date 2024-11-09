# Deprecated
This repository is now deprecated. The examples apply to Blender versions 3.x. It has not been tested on newer versions of Blender.

# Introduction

This Blender Add-on is a growing collection of tools that are meant to speed
up my workflow.  As I notice repetitive tasks that can be automated I will
add them to the tool set.

The set is divided into categories based on the general nature of the tools.

The add-on creates a side panel tab 'My Tools' to hold the tools.  Each
category of tools has its own subpanel in the tab.

# Operators

## camera_ops.py

### `TOOL_OT_place_camera`
Tries very hard to find an existing camera
- Finds all of the camera in the list
- If exactly 1 is selected use it.
- If more than 1 is selected complain but do nothing
- If there aren't any, add one
Positions the selected camera to frame the view (`camera_to_view`)

### `TOOL_OT_add_camera`
Adds a new camera.
Makes it active.
Positions it to frame the view (`camera_to_view`)

## mesh_ops.py

### `TOOL_OT_mesh_duplicate`
Duplicates an object, but only copies the mesh.

This operator adds itself to the 3D Viewport Object menu as
*duplicate mesh*

## modifiers.py

These operators operate on the active object.
### `TOOL_OT_modifier_apply_all`
Applies all of the modifiers on the object stack

### `TOOL_OT_modifier_remove_all`
Removes all of the modifiers from the object stack

## node_ops.py

### `get_active_node_tree`

finds the active tree for the node editor.  Needs to be updated to work
with the compositor and geometry nodes editors

### `get_node_types`

returns a list of node types currently in use in this editor

### `NODES_OT_color_by_type`

sets the color of every node that has the same type as the selected node

# Node Panel

The code to manage the add-on's node editor sidebar

# Tool Panel

The code to manage the add-on's view3d sidebar panel and its subpanels.

The subpanels match the categories of tools but a category is only included if
at least one of the category tools does not add itself to a menu.
