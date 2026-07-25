
import numpy as np

def ColoringAtRectangle(image, rect, colour):
    [x, y, w, h] = rect
    [r, g, b] = colour
    image[y:(y+h), x:(x+w), 0] = r
    image[y:(y+h), x:(x+w), 1] = g
    image[y:(y+h), x:(x+w), 2] = b
    return image




rectList = [
    [ 10,  10, 40, 40],  # 0,0
    [ 55,  10, 40, 40],  # 0,1
    [100,  10, 40, 40],  # 0,2
    [ 10,  55, 40, 40],  # 0,3
    [ 55,  55, 40, 40],  # 0,4
    [100,  55, 40, 40],  # 0,5
    [ 10, 100, 40, 40],  # 0,6
    [ 55, 100, 40, 40],  # 0,7
    [100, 100, 40, 40],  # 0,8

    [ 10,  0, 40, 5],
    [ 55,  0, 40, 5],
    [100,  0, 40, 5],

    [0,  10, 5, 40],
    [0,  55, 5, 40],
    [0, 100, 5, 40],

    [ 10, 145, 40, 5],
    [ 55, 145, 40, 5],
    [100, 145, 40, 5],

    [145,  10, 5, 40],
    [145,  55, 5, 40],
    [145, 100, 5, 40],
]

idxList = [
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7],
    [0, 8],

    [5, 2],
    [5, 1],
    [5, 0],
    [2, 0],
    [2, 1],
    [2, 2],
    [3, 0],
    [3, 1],
    [3, 2],
    [1, 2],
    [1, 1],
    [1, 0],
]

colorMap = {
    "r":[255, 0, 0],
    "y":[255, 255, 0],
    "o":[255, 172, 28],
    "g":[0, 255, 0],
    "b":[0, 0, 255],
    "w":[255, 255, 255],
}


def DrawState(state):
    img = np.zeros((150, 150, 3), dtype=np.uint8)+0
    for i in range(len(idxList)):
        i1, i2 = idxList[i]
        img = ColoringAtRectangle(img, rectList[i], colorMap[state[i1][i2]])
    result = np.zeros((160, 160, 3), dtype=np.uint8)
    result[5:-5, 5:-5, :] = img
    return result




