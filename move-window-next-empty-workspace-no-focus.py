#!/usr/bin/env python

import os

import i3ipc

SWAYSOCK = os.environ['SWAYSOCK']
SCRATCHPAD_NAME = "__i3_scratch"
SCRATCHPAD_NAME2 = "scratchpad"


def get_next_empty_workspace(workspaces: list[int]):
    first = 1
    chosen = 0
    for number in range(first, 11):
        if number not in workspaces:
            chosen = number
            break
    return chosen


sway = i3ipc.Connection(socket_path=SWAYSOCK)

root = sway.get_tree()
descendants = root.descendants()

existing_workspaces = [int(workspace.name) for workspace in descendants
                       if workspace.type == "workspace"
                       and workspace.name != SCRATCHPAD_NAME
                       and workspace.name != SCRATCHPAD_NAME2]

existing_workspaces.sort()

focused_window = root.find_focused()
focused_workspace = focused_window.workspace()
workspace_name = int(focused_workspace.name)
num_of_containers_in_focused_workspace = len(focused_workspace.descendants())

to_workspace = get_next_empty_workspace(workspaces=existing_workspaces)

sway.command(f"move container to workspace number {to_workspace}")

exit(0)
