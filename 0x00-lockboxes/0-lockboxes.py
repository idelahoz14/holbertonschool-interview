#!/usr/bin/python3


def canUnlockAll(boxes):
    """ Checks if all boxes can be opened """
    box = len(boxes)

    if box == 0:
        return True
    boxposition = [False] * box
    boxposition[0] = True
    s = [0]

    while s:
        for k in boxes[s.pop()]:
            if k > 0 and k < box and not boxposition[k]:
                boxposition[k] = True
                s.append(k)

    return all(boxposition)
