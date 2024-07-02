#!/usr/bin/python3
"""Solution for lockboxes proplem"""


def canUnlockAll(boxes):
    """function to check if all lockboxes are unlocked"""
    opened = {0}
    keys = list(boxes[0])
    while keys:
        key = keys.pop(0)
        if key not in opened and key < len(boxes):
            keys.extend(boxes[key])
            opened.add(key)

    return len(opened) == len(boxes)
