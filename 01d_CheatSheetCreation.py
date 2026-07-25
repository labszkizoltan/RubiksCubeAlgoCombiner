
import numpy as np
import pandas as pd
import skimage.io as io
import os

import AA_moves as m
import AB_AlgorithmUtils as au
import AC_DrawingUtils as du
import AD2_HtmlUtils2 as hu

_currentCS = "CheatSheet_v4"
_cheatSheetFolder_base = r"D:\Projects\15_RubiksCube\03_ScriptIO\CheatSheets"

_htmlPath = os.path.join(_cheatSheetFolder_base, _currentCS, _currentCS + ".html")
_imagesFolder = os.path.join(_cheatSheetFolder_base, _currentCS, "Images")

if not os.path.exists(_imagesFolder):
    os.makedirs(_imagesFolder)

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
    "R'U'RU'R'U2R",
    "RU'L'UR'U'L",
    "L'URU'LUR'"
]

intermediateList = ["", "U", "U2", "U'"]

htmlBase = hu.htmlTemplate

nuiqueID = 0

idx1=0
idx2=0
k=0
for idx1 in range(len(algoList)):
    for idx2 in range(len(algoList)):
        currentTable = hu.tableTemplate
        headerString = "Combining algorithms: ( " + algoList[idx1] + " ) &  ( " + algoList[idx2] + ")"
        currentTable = currentTable.replace("ALGORITHM_COMBINATION_PLACEHOLDER", headerString)

        for k in range(4):
            algoString = "( " + algoList[idx1] + " ) " + intermediateList[k] + " ( " + algoList[idx2] + ")"
            inverseAlgo = au.InvertAlgorithm(algoString)

            algoResult = au.ApplyAlgorithm(inverseAlgo, state)
            algoImage = du.DrawState(algoResult)
            imagePath = os.path.join(_imagesFolder, str(idx1)+ str(k) + str(idx2) + ".png")
            io.imsave(imagePath, algoImage)

            tableRow = hu.CreateTableRow(imagePath, algoString)
            tableRow = tableRow.replace("UNIQUE_ID_PLACEHOLDER", str(nuiqueID))
            nuiqueID += 1
            currentTable = currentTable.replace("TABLE_ROW_PLACEHOLDER", tableRow)

        htmlBase = htmlBase.replace("TABLE_PLACEHOLDER", currentTable)


htmlBase = htmlBase.replace("TABLE_ROW_PLACEHOLDER", "<br>")
htmlBase = htmlBase.replace("TABLE_PLACEHOLDER", "")

with open(_htmlPath, "a") as f:
    f.write(htmlBase)

















