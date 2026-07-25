
import numpy as np
import skimage.io as io

import AA_moves as m
import AB_AlgorithmUtils as au
import AC_DrawingUtils as du
import AD_HtmlUtils as hu


state = [
    ["y", "y", "y", "y", "y", "y", "y", "y", "y"],  # 0: top
    ["o", "o", "o", "o", "o", "o", "o", "o", "o"],  # 1: right
    ["r", "r", "r", "r", "r", "r", "r", "r", "r"],  # 2: left
    ["g", "g", "g", "g", "g", "g", "g", "g", "g"],  # 3: front
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],  # 4: down
    ["b", "b", "b", "b", "b", "b", "b", "b", "b"],  # 5: back
]

algoList = [
    "R'U2RUR'UR",
    "RU2R'U'RU'R'",
    "RUR'URU2R'",
    "R'U'RU'R'U2R"
]

intermediateList = ["", "U", "U2", "U'"]

htmlBase = hu.htmlTemplate

for i in range(4):
    for j in range(4):
        for k in range(4):
            algoString = "( " + algoList[i] + " ) " + intermediateList[k] + " ( " + algoList[j] + ")"
            inverseAlgo = au.InvertAlgorithm(algoString)

            algoResult = au.ApplyAlgorithm(inverseAlgo, state)
            algoImage = du.DrawState(algoResult)
            imagePath = r"D:\Projects\15_RubiksCube\03_ScriptIO\Images\algo_" + str(i)+ str(k) + str(j) + ".png"
            io.imsave(imagePath, algoImage)

            tableRow = hu.CreateTableRow(imagePath, algoString)
            htmlBase = hu.AddTableRowToTemplate(htmlBase, tableRow)

htmlBase = htmlBase.replace("TABLE_ROW_PLACEHOLDER", "")

with open(r"D:\Projects\15_RubiksCube\03_ScriptIO\HtmlFiles\CheatSheet_v3.html", "a") as f:
    f.write(htmlBase)





















