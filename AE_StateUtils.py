
import AA_moves as m

solvedState = [
    ["y", "y", "y", "y", "y", "y", "y", "y", "y"],  # 0: top
    ["o", "o", "o", "o", "o", "o", "o", "o", "o"],  # 1: right
    ["r", "r", "r", "r", "r", "r", "r", "r", "r"],  # 2: left
    ["g", "g", "g", "g", "g", "g", "g", "g", "g"],  # 3: front
    ["w", "w", "w", "w", "w", "w", "w", "w", "w"],  # 4: down
    ["b", "b", "b", "b", "b", "b", "b", "b", "b"],  # 5: back
]

def StateToString(state):
    result = ""
    for i in range(len(state)):
        result += "".join(state[i])
    return result

# stateString = "yyyyyyyyyooooooooorrrrrrrrrgggggggggwwwwwwwwwbbbbbbbbb"
def StringToState(stateString):
    result = []
    for i in range(6):
        start = i*9
        end = (i+1)*9
        faceString = stateString[start:end]
        stickerList = [faceString[j] for j in range(9)]
        result.append(stickerList)
    return result


#----- Case recognition -----#
def PiCase(state):
    stateCpy = m.CopyState(state)
    for i in range(4):
        if stateCpy[2][0] == "y" and stateCpy[2][2] == "y" and stateCpy[3][2] == "y" and stateCpy[5][0] == "y":
            return [True, i]
        stateCpy = m.U(stateCpy)
    return [False, -1]

def HCase(state):
    stateCpy = m.CopyState(state)
    for i in range(4):
        if stateCpy[2][0] == "y" and stateCpy[2][2] == "y" and stateCpy[1][2] == "y" and stateCpy[1][0] == "y":
            return [True, i]
        stateCpy = m.U(stateCpy)
    return [False, -1]

def TCase(state):
    stateCpy = m.CopyState(state)
    for i in range(4):
        if stateCpy[0][0] == "y" and stateCpy[0][7] == "y" and stateCpy[3][2] == "y" and stateCpy[5][0] == "y":
            return [True, i]
        stateCpy = m.U(stateCpy)
    return [False, -1]

def UCase(state):
    stateCpy = m.CopyState(state)
    for i in range(4):
        if stateCpy[2][0] == "y" and stateCpy[2][2] == "y" and stateCpy[0][2] == "y" and stateCpy[0][8] == "y":
            return [True, i]
        stateCpy = m.U(stateCpy)
    return [False, -1]

def LCase(state):
    stateCpy = m.CopyState(state)
    for i in range(4):
        if stateCpy[2][0] == "y" and stateCpy[3][2] == "y" and stateCpy[0][2] == "y" and stateCpy[0][6] == "y":
            return [True, i]
        stateCpy = m.U(stateCpy)
    return [False, -1]

def SuneCase(state):
    stateCpy = m.CopyState(state)
    for i in range(4):
        if stateCpy[0][6] == "y" and stateCpy[1][2] == "y" and stateCpy[3][2] == "y" and stateCpy[5][2] == "y":
            return [True, i]
        stateCpy = m.U(stateCpy)
    return [False, -1]

def AntiSuneCase(state):
    stateCpy = m.CopyState(state)
    for i in range(4):
        if stateCpy[0][8] == "y" and stateCpy[2][0] == "y" and stateCpy[3][0] == "y" and stateCpy[5][0] == "y":
            return [True, i]
        stateCpy = m.U(stateCpy)
    return [False, -1]

def OrientedCase(state):
    stateCpy = m.CopyState(state)
    for i in range(4):
        if stateCpy[0][0] == "y" and stateCpy[0][2] == "y" and stateCpy[0][6] == "y" and stateCpy[0][8] == "y":
            return [True, i]
        stateCpy = m.U(stateCpy)
    return [False, -1]

def RecogizeCase(state):
    [caseFlag, uTurnCount] = PiCase(state)
    if caseFlag:
        return ["Pi", uTurnCount]

    [caseFlag, uTurnCount] = HCase(state)
    if caseFlag:
        return ["H", uTurnCount]

    [caseFlag, uTurnCount] = TCase(state)
    if caseFlag:
        return ["T", uTurnCount]

    [caseFlag, uTurnCount] = UCase(state)
    if caseFlag:
        return ["U", uTurnCount]

    [caseFlag, uTurnCount] = LCase(state)
    if caseFlag:
        return ["L", uTurnCount]

    [caseFlag, uTurnCount] = SuneCase(state)
    if caseFlag:
        return ["Sune", uTurnCount]

    [caseFlag, uTurnCount] = AntiSuneCase(state)
    if caseFlag:
        return ["AntiSune", uTurnCount]

    [caseFlag, uTurnCount] = OrientedCase(state)
    if caseFlag:
        return ["Oriented", uTurnCount]
    return "Unrecognized"
