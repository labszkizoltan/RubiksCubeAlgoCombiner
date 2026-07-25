# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import numpy as np
import skimage.io as io

import AA_moves as m


state = [
    ["y", "y", "y", "y", "y", "y", "y", "y", "y"],  # 0: top
    ["o", "o", "o", "o", "o", "o", "o", "o", "o"],  # 1: right
    ["r", "r", "r", "r", "r", "r", "r", "r", "r"],  # 2: left
    ["g", "g", "g", "g", "g", "g", "g", "g", "g"],  # 3: front
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],  # 4: down
    ["b", "b", "b", "b", "b", "b", "b", "b", "b"],  # 5: back
]



# algorithmString = "RUR'U'"
def ApplyAlgorithm(algorithmString, state):
    algo = algorithmString

    return state


state
newstate = m.CopyState(state)
newstate[0][0] = "asd"

newstate = m.CopyState(state)

for i in range(6):
    newstate = m.R(newstate)
    newstate = m.U(newstate)
    newstate = m.RInv(newstate)
    newstate = m.UInv(newstate)



newstate = m.CopyState(state)
for i in range(6):
    newstate = m.LInv(newstate)
    newstate = m.UInv(newstate)
    newstate = m.L(newstate)
    newstate = m.U(newstate)



newstate = m.CopyState(state)
for i in range(6):
    newstate = m.RInv(newstate)
    newstate = m.F(newstate)
    newstate = m.R(newstate)
    newstate = m.FInv(newstate)



newstate = m.CopyState(state)
newstate = m.R(newstate)
newstate = m.U(newstate)
newstate = m.RInv(newstate)
newstate = m.UInv(newstate)
newstate = m.RInv(newstate)
newstate = m.F(newstate)
newstate = m.R(newstate)
newstate = m.FInv(newstate)


newstate = m.CopyState(state)
for i in range(6):
    newstate = m.RInv(newstate)
    newstate = m.D(newstate)
    newstate = m.R(newstate)
    newstate = m.DInv(newstate)


newstate = m.CopyState(state)
for i in range(6):
    newstate = m.B(newstate)
    newstate = m.R(newstate)
    newstate = m.BInv(newstate)
    newstate = m.RInv(newstate)



newstate = m.CopyState(state)
newstate = m.R(newstate)
newstate = m.B(newstate)
newstate = m.L(newstate)
newstate = m.F(newstate)
newstate = m.D(newstate)
newstate = m.U(newstate)



newstate = m.CopyState(state)
newstate = m.RInv(newstate)
newstate = m.BInv(newstate)
newstate = m.LInv(newstate)
newstate = m.FInv(newstate)
newstate = m.DInv(newstate)
newstate = m.UInv(newstate)



img = np.zeros((100, 120), dtype=np.uint8)
for y in range(100):
    for x in range(120):
        img[y, x] = x+y

io.imsave(r"D:\Projects\15_RubiksCube\03_ScriptIO\01_testImage.png", img)


img = np.zeros((100, 120, 3), dtype=np.uint8)

img = ColoringAtRectangle(img, [10, 15, 11, 12], [10, 200, 50])
io.imsave(r"D:\Projects\15_RubiksCube\03_ScriptIO\02_testImage.png", img)


# do sune algo:
newstate = m.CopyState(state)
newstate = m.R(newstate)
newstate = m.U(newstate)
newstate = m.U(newstate)
newstate = m.RInv(newstate)
newstate = m.UInv(newstate)
newstate = m.R(newstate)
newstate = m.UInv(newstate)
newstate = m.RInv(newstate)

def DrawState(state):
    img = np.zeros((150, 150, 3), dtype=np.uint8)+0
    for i in range(len(idxList)):
        i1, i2 = idxList[i]
        img = ColoringAtRectangle(img, rectList[i], colorMap[state[i1][i2]])
    result = np.zeros((160, 160, 3), dtype=np.uint8)
    result[5:-5, 5:-5, :] = img
    return result

io.imsave(r"D:\Projects\15_RubiksCube\03_ScriptIO\03_testImage.png", img)
io.imsave(r"D:\Projects\15_RubiksCube\03_ScriptIO\04_SuneEffect.png", result)

suneImage = DrawState(newstate)
io.imsave(r"D:\Projects\15_RubiksCube\03_ScriptIO\04_SuneEffect.png", suneImage)

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
    #"w":[0, 0, 0],
}







