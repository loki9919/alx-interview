#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    indx = 0

    while indx < length:
        oldi = indx
        opened_boxes.append(indx)
        keys.update(boxes[indx])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                indx = key
                break
        if oldi != indx:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
