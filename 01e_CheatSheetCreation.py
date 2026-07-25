
import numpy as np
import pandas as pd
import skimage.io as io
import os

import AA_moves as m
import AB_AlgorithmUtils as au
import AC_DrawingUtils as du
import AD2_HtmlUtils2 as hu
import AE_StateUtils as su

_currentCS = "CheatSheet_v5"
_cheatSheetFolder_base = r"D:\Projects\15_RubiksCube\03_ScriptIO\CheatSheets"

_htmlPath = os.path.join(_cheatSheetFolder_base, _currentCS, _currentCS + ".html")
_imagesFolder = os.path.join(_cheatSheetFolder_base, _currentCS, "Images")

if not os.path.exists(_imagesFolder):
    os.makedirs(_imagesFolder)

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

stateList = []
algoStringList = []
caseList = []
uTurnCountList = []

idx1=0
idx2=0
k=0
for idx1 in range(len(algoList)):
    for idx2 in range(len(algoList)):

        for k in range(len(intermediateList)):
            algoString = "( " + algoList[idx1] + " ) " + intermediateList[k] + " ( " + algoList[idx2] + ")"
            inverseAlgo = au.InvertAlgorithm(algoString)
            algoResult = au.ApplyAlgorithm(inverseAlgo, su.solvedState)
            algoStringList.append(algoString)
            stateList.append(su.StateToString(algoResult))
            [currentCase, uTurnCount] = su.RecogizeCase(algoResult)
            caseList.append(currentCase)
            uTurnCountList.append(uTurnCount)

df = pd.DataFrame.from_dict({"state": stateList, "algo": algoStringList, "case": caseList, "uCount": uTurnCountList})

#----- visualization: -----#
# distinctCases = set(caseList)
distinctCases = ["Pi", "H", "U", "T", "L", "Sune", "AntiSune", "Oriented"]

# i=0
uniqueID = 0
# case = distinctCases[0]
for case in distinctCases:
    subsetDf = df[df["case"] == case]
    currentTable = hu.tableTemplate
    headerString = case + " cases"
    currentTable = currentTable.replace("ALGORITHM_COMBINATION_PLACEHOLDER", headerString)

    for i in range(len(subsetDf)):
        currentAlgo = subsetDf.iloc[i]
        algoImage = du.DrawState(su.StringToState(currentAlgo.state))

        imagePath = os.path.join(_imagesFolder, str(uniqueID) + ".png")
        io.imsave(imagePath, algoImage)

        tableRow = hu.CreateTableRow(imagePath, currentAlgo.algo)
        tableRow = tableRow.replace("UNIQUE_ID_PLACEHOLDER", str(uniqueID))
        currentTable = currentTable.replace("TABLE_ROW_PLACEHOLDER", tableRow)
        uniqueID += 1

    htmlBase = htmlBase.replace("TABLE_PLACEHOLDER", currentTable)


htmlBase = htmlBase.replace("TABLE_ROW_PLACEHOLDER", "<br>")
htmlBase = htmlBase.replace("TABLE_PLACEHOLDER", "")

with open(_htmlPath, "a") as f:
    f.write(htmlBase)





# resultState = au.ApplyAlgorithm("rUR'U'r'FRF'", su.solvedState)
# resultState = au.ApplyAlgorithm("l'U'lL'U'LUl'Ul", su.solvedState)









