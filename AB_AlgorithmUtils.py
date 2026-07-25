import AA_moves as m


def CleanAlgoString(algorithmString):
    result = algorithmString.replace(" ", "")
    result = result.replace("(", "")
    result = result.replace(")", "")
    return result


# algorithmString = "RUR'U'RU2R'"
def ExtractNextMove(algorithmString):
    move = algorithmString[0]
    modifier = ""
    if len(algorithmString) > 1:
        modifier = algorithmString[1]
        if modifier not in ["'", "2"]:
            modifier = ""
    if modifier == "":
        remainder = algorithmString[1:]
    else:
        remainder = algorithmString[2:]
    return [move + modifier, remainder]


def ApplyMove(state, move):
    if move == "R":
        return m.R(state)
    if move == "R'":
        return m.RInv(state)
    if move == "R2":
        result = m.R(state)
        return m.R(result)
    if move == "r":
        return m.RWide(state)
    if move == "r'":
        return m.RWideInv(state)
    if move == "r2":
        result = m.RWide(state)
        return m.RWide(result)

    if move == "U":
        return m.U(state)
    if move == "U'":
        return m.UInv(state)
    if move == "U2":
        result = m.U(state)
        return m.U(result)
    if move == "u":
        return m.UWide(state)
    if move == "u'":
        return m.UWideInv(state)
    if move == "u2":
        result = m.UWide(state)
        return m.UWide(result)

    if move == "F":
        return m.F(state)
    if move == "F'":
        return m.FInv(state)
    if move == "F2":
        result = m.F(state)
        return m.F(result)
    if move == "f":
        return m.FWide(state)
    if move == "f'":
        return m.FWideInv(state)
    if move == "f2":
        result = m.FWide(state)
        return m.FWide(result)

    if move == "L":
        return m.L(state)
    if move == "L'":
        return m.LInv(state)
    if move == "L2":
        result = m.L(state)
        return m.L(result)
    if move == "l":
        return m.LWide(state)
    if move == "l'":
        return m.LWideInv(state)
    if move == "l2":
        result = m.LWide(state)
        return m.LWide(result)

    if move == "D":
        return m.D(state)
    if move == "D'":
        return m.DInv(state)
    if move == "D2":
        result = m.D(state)
        return m.D(result)
    if move == "d":
        return m.DWide(state)
    if move == "d'":
        return m.DWideInv(state)
    if move == "d2":
        result = m.DWide(state)
        return m.DWide(result)

    if move == "B":
        return m.B(state)
    if move == "B'":
        return m.BInv(state)
    if move == "B2":
        result = m.B(state)
        return m.B(result)
    if move == "b":
        return m.BWide(state)
    if move == "b'":
        return m.BWideInv(state)
    if move == "b2":
        result = m.BWide(state)
        return m.BWide(result)

    # slice moves:
    if move == "E":
        return m.E(state)
    if move == "E'":
        return m.EInv(state)
    if move == "E2":
        result = m.E(state)
        return m.E(result)
    if move == "M":
        return m.M(state)
    if move == "M'":
        return m.MInv(state)
    if move == "M2":
        result = m.M(state)
        return m.M(result)
    if move == "S":
        return m.S(state)
    if move == "S'":
        return m.SInv(state)
    if move == "S2":
        result = m.S(state)
        return m.S(result)

    # cube rotations:
    if move == "x":
        return m.x(state)
    if move == "x'":
        return m.xInv(state)
    if move == "x2":
        result = m.x(state)
        return m.x(result)
    if move == "y":
        return m.y(state)
    if move == "y'":
        return m.yInv(state)
    if move == "y2":
        result = m.y(state)
        return m.y(result)
    if move == "z":
        return m.z(state)
    if move == "z'":
        return m.zInv(state)
    if move == "z2":
        result = m.z(state)
        return m.z(result)

    return state


# algorithmString = "RUR'U'RU2R'"
def ApplyAlgorithm(algorithmString, state):
    remainder = CleanAlgoString(algorithmString)
    resultState = m.CopyState(state)
    stateList = []
    while remainder != "":
        # print(remainder)
        [move, remainder] = ExtractNextMove(remainder)
        resultState = ApplyMove(resultState, move)
        # stateList.append(m.CopyState(resultState))
    return resultState


def InvertMove(move):
    if move == "R":
        return "R'"
    if move == "R'":
        return "R"
    if move == "R2":
        return "R2"
    if move == "r":
        return "r'"
    if move == "r'":
        return "r"
    if move == "r2":
        return "r2"

    if move == "U":
        return "U'"
    if move == "U'":
        return "U"
    if move == "U2":
        return "U2"
    if move == "u":
        return "u'"
    if move == "u'":
        return "u"
    if move == "u2":
        return "u2"

    if move == "F":
        return "F'"
    if move == "F'":
        return "F"
    if move == "F2":
        return "F2"
    if move == "f":
        return "f'"
    if move == "f'":
        return "f"
    if move == "f2":
        return "f2"

    if move == "L":
        return "L'"
    if move == "L'":
        return "L"
    if move == "L2":
        return "L2"
    if move == "l":
        return "l'"
    if move == "l'":
        return "l"
    if move == "l2":
        return "l2"

    if move == "D":
        return "D'"
    if move == "D'":
        return "D"
    if move == "D2":
        return "D2"
    if move == "d":
        return "d'"
    if move == "d'":
        return "d"
    if move == "d2":
        return "d2"

    if move == "B":
        return "B'"
    if move == "B'":
        return "B"
    if move == "B2":
        return "B2"
    if move == "b":
        return "b'"
    if move == "b'":
        return "b"
    if move == "b2":
        return "b2"

    # Slice moves rotations:
    if move == "M":
        return "M'"
    if move == "M'":
        return "M"
    if move == "M2":
        return "M2"
    if move == "E":
        return "E'"
    if move == "E'":
        return "E"
    if move == "E2":
        return "E2"
    if move == "S":
        return "S'"
    if move == "S'":
        return "S"
    if move == "S2":
        return "S2"

    # cube rotations:
    if move == "x":
        return "x'"
    if move == "x'":
        return "x"
    if move == "x2":
        return "x2"
    if move == "y":
        return "y'"
    if move == "y'":
        return "y"
    if move == "y2":
        return "y2"
    if move == "z":
        return "z'"
    if move == "z'":
        return "z"
    if move == "z2":
        return "z2"

    return ""


def InvertAlgorithm(algorithmString):
    moves = []
    remainder = CleanAlgoString(algorithmString)
    while remainder != "":
        [move, remainder] = ExtractNextMove(remainder)
        moves.append(move)
    result = ""
    for move in reversed(moves):
        result += InvertMove(move)
    return result



















