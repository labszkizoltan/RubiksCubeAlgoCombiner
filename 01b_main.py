# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import numpy as np
import skimage.io as io

import AA_moves as m
import AB_AlgorithmUtils as au
import AC_DrawingUtils as du


state = [
    ["y", "y", "y", "y", "y", "y", "y", "y", "y"],  # 0: top
    ["o", "o", "o", "o", "o", "o", "o", "o", "o"],  # 1: right
    ["r", "r", "r", "r", "r", "r", "r", "r", "r"],  # 2: left
    ["g", "g", "g", "g", "g", "g", "g", "g", "g"],  # 3: front
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],  # 4: down
    ["b", "b", "b", "b", "b", "b", "b", "b", "b"],  # 5: back
]

suneResult = au.ApplyAlgorithm("RUR'URU2R'", state)
suneImage = du.DrawState(suneResult)
io.imsave(r"D:\Projects\15_RubiksCube\03_ScriptIO\05a_AlgoEffect_RUR'URU2R'.png", suneImage)

algoResult = au.ApplyAlgorithm("RU'L'UR'U'LU", state)
algoImage = du.DrawState(algoResult)
io.imsave(r"D:\Projects\15_RubiksCube\03_ScriptIO\05b_AlgoEffect_RU'L'UR'U'LU.png", algoImage)




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

suneImage = DrawState(newstate)
io.imsave(r"D:\Projects\15_RubiksCube\03_ScriptIO\04_SuneEffect.png", suneImage)








