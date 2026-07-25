def CopyState(state):
    newState = []
    for i in range(len(state)):
        newState.append(state[i].copy())
    return newState


# basic side turns
def U(state):
    newState = CopyState(state)

    newState[0][0] = state[0][6]  # top
    newState[0][1] = state[0][3]
    newState[0][2] = state[0][0]
    newState[0][3] = state[0][7]
    newState[0][5] = state[0][1]
    newState[0][6] = state[0][8]
    newState[0][7] = state[0][5]
    newState[0][8] = state[0][2]

    newState[1][0] = state[5][0]  # right
    newState[1][1] = state[5][1]
    newState[1][2] = state[5][2]

    newState[2][0] = state[3][0]  # left
    newState[2][1] = state[3][1]
    newState[2][2] = state[3][2]

    newState[3][0] = state[1][0]  # down
    newState[3][1] = state[1][1]
    newState[3][2] = state[1][2]

    newState[5][0] = state[2][0]  # back
    newState[5][1] = state[2][1]
    newState[5][2] = state[2][2]

    return newState

def UInv(state):
    newState = CopyState(state)

    newState[0][6] = state[0][0]  # top
    newState[0][3] = state[0][1]
    newState[0][0] = state[0][2]
    newState[0][7] = state[0][3]
    newState[0][1] = state[0][5]
    newState[0][8] = state[0][6]
    newState[0][5] = state[0][7]
    newState[0][2] = state[0][8]

    newState[5][0] = state[1][0]  # right
    newState[5][1] = state[1][1]
    newState[5][2] = state[1][2]

    newState[3][0] = state[2][0]  # left
    newState[3][1] = state[2][1]
    newState[3][2] = state[2][2]

    newState[1][0] = state[3][0]  # down
    newState[1][1] = state[3][1]
    newState[1][2] = state[3][2]

    newState[2][0] = state[5][0]  # back
    newState[2][1] = state[5][1]
    newState[2][2] = state[5][2]

    return newState

def R(state):
    newState = CopyState(state)
    newState[0][2] = state[3][2]  # top
    newState[0][5] = state[3][5]
    newState[0][8] = state[3][8]

    newState[1][0] = state[1][6]  # right
    newState[1][1] = state[1][3]
    newState[1][2] = state[1][0]
    newState[1][3] = state[1][7]
    newState[1][5] = state[1][1]
    newState[1][6] = state[1][8]
    newState[1][7] = state[1][5]
    newState[1][8] = state[1][2]

    newState[3][2] = state[4][2]  # front
    newState[3][5] = state[4][5]
    newState[3][8] = state[4][8]

    newState[4][2] = state[5][6]  # down
    newState[4][5] = state[5][3]
    newState[4][8] = state[5][0]

    newState[5][0] = state[0][8]  # back
    newState[5][3] = state[0][5]
    newState[5][6] = state[0][2]

    return newState

def RInv(state):
    newState = CopyState(state)
    newState[3][2] = state[0][2]  # top
    newState[3][5] = state[0][5]
    newState[3][8] = state[0][8]

    newState[1][6] = state[1][0]  # right
    newState[1][3] = state[1][1]
    newState[1][0] = state[1][2]
    newState[1][7] = state[1][3]
    newState[1][1] = state[1][5]
    newState[1][8] = state[1][6]
    newState[1][5] = state[1][7]
    newState[1][2] = state[1][8]

    newState[4][2] = state[3][2]  # front
    newState[4][5] = state[3][5]
    newState[4][8] = state[3][8]

    newState[5][6] = state[4][2]  # down
    newState[5][3] = state[4][5]
    newState[5][0] = state[4][8]

    newState[0][8] = state[5][0]  # back
    newState[0][5] = state[5][3]
    newState[0][2] = state[5][6]

    return newState

def L(state):
    newState = CopyState(state)
    newState[0][0] = state[5][8]  # top
    newState[0][3] = state[5][5]
    newState[0][6] = state[5][2]

    newState[2][0] = state[2][6]  # left
    newState[2][1] = state[2][3]
    newState[2][2] = state[2][0]
    newState[2][3] = state[2][7]
    newState[2][5] = state[2][1]
    newState[2][6] = state[2][8]
    newState[2][7] = state[2][5]
    newState[2][8] = state[2][2]

    newState[3][0] = state[0][0]  # front
    newState[3][3] = state[0][3]
    newState[3][6] = state[0][6]

    newState[4][0] = state[3][0]  # down
    newState[4][3] = state[3][3]
    newState[4][6] = state[3][6]

    newState[5][2] = state[4][6]  # back
    newState[5][5] = state[4][3]
    newState[5][8] = state[4][0]

    return newState

def LInv(state):
    newState = CopyState(state)
    newState[5][8] = state[0][0]  # top
    newState[5][5] = state[0][3]
    newState[5][2] = state[0][6]

    newState[2][6] = state[2][0]  # left
    newState[2][3] = state[2][1]
    newState[2][0] = state[2][2]
    newState[2][7] = state[2][3]
    newState[2][1] = state[2][5]
    newState[2][8] = state[2][6]
    newState[2][5] = state[2][7]
    newState[2][2] = state[2][8]

    newState[0][0] = state[3][0]  # front
    newState[0][3] = state[3][3]
    newState[0][6] = state[3][6]

    newState[3][0] = state[4][0]  # down
    newState[3][3] = state[4][3]
    newState[3][6] = state[4][6]

    newState[4][6] = state[5][2]  # back
    newState[4][3] = state[5][5]
    newState[4][0] = state[5][8]

    return newState

def F(state):
    newState = CopyState(state)
    newState[0][6] = state[2][8]  # top
    newState[0][7] = state[2][5]
    newState[0][8] = state[2][2]

    newState[1][0] = state[0][6]  # right
    newState[1][3] = state[0][7]
    newState[1][6] = state[0][8]

    newState[2][2] = state[4][0]  # left
    newState[2][5] = state[4][1]
    newState[2][8] = state[4][2]

    newState[3][0] = state[3][6]  # front
    newState[3][1] = state[3][3]
    newState[3][2] = state[3][0]
    newState[3][3] = state[3][7]
    newState[3][5] = state[3][1]
    newState[3][6] = state[3][8]
    newState[3][7] = state[3][5]
    newState[3][8] = state[3][2]

    newState[4][0] = state[1][6]  # down
    newState[4][1] = state[1][3]
    newState[4][2] = state[1][0]

    return newState

def FInv(state):
    newState = CopyState(state)
    newState[2][8] = state[0][6]  # top
    newState[2][5] = state[0][7]
    newState[2][2] = state[0][8]
    newState[0][6] = state[1][0]  # right
    newState[0][7] = state[1][3]
    newState[0][8] = state[1][6]
    newState[4][0] = state[2][2]  # left
    newState[4][1] = state[2][5]
    newState[4][2] = state[2][8]
    newState[3][6] = state[3][0]  # front
    newState[3][3] = state[3][1]
    newState[3][0] = state[3][2]
    newState[3][7] = state[3][3]
    newState[3][1] = state[3][5]
    newState[3][8] = state[3][6]
    newState[3][5] = state[3][7]
    newState[3][2] = state[3][8]
    newState[1][6] = state[4][0]  # down
    newState[1][3] = state[4][1]
    newState[1][0] = state[4][2]

    return newState

def D(state):
    newState = CopyState(state)
    newState[1][6] = state[3][6]  # right
    newState[1][7] = state[3][7]
    newState[1][8] = state[3][8]

    newState[2][6] = state[5][6]  # left
    newState[2][7] = state[5][7]
    newState[2][8] = state[5][8]

    newState[3][6] = state[2][6]  # front
    newState[3][7] = state[2][7]
    newState[3][8] = state[2][8]

    newState[4][0] = state[4][6]  # down
    newState[4][1] = state[4][3]
    newState[4][2] = state[4][0]
    newState[4][3] = state[4][7]
    newState[4][5] = state[4][1]
    newState[4][6] = state[4][8]
    newState[4][7] = state[4][5]
    newState[4][8] = state[4][2]

    newState[5][6] = state[1][6]  # back
    newState[5][7] = state[1][7]
    newState[5][8] = state[1][8]

    return newState

def DInv(state):
    newState = CopyState(state)
    newState[3][6] = state[1][6]  # right
    newState[3][7] = state[1][7]
    newState[3][8] = state[1][8]

    newState[5][6] = state[2][6]  # left
    newState[5][7] = state[2][7]
    newState[5][8] = state[2][8]

    newState[2][6] = state[3][6]  # front
    newState[2][7] = state[3][7]
    newState[2][8] = state[3][8]

    newState[4][6] = state[4][0]  # down
    newState[4][3] = state[4][1]
    newState[4][0] = state[4][2]
    newState[4][7] = state[4][3]
    newState[4][1] = state[4][5]
    newState[4][8] = state[4][6]
    newState[4][5] = state[4][7]
    newState[4][2] = state[4][8]

    newState[1][6] = state[5][6]  # back
    newState[1][7] = state[5][7]
    newState[1][8] = state[5][8]

    return newState

def B(state):
    newState = CopyState(state)
    newState[0][0] = state[1][2]  # top
    newState[0][1] = state[1][5]
    newState[0][2] = state[1][8]

    newState[1][2] = state[4][8]  # right
    newState[1][5] = state[4][7]
    newState[1][8] = state[4][6]

    newState[2][0] = state[0][2]  # left
    newState[2][3] = state[0][1]
    newState[2][6] = state[0][0]

    newState[4][6] = state[2][0]  # down
    newState[4][7] = state[2][3]
    newState[4][8] = state[2][6]

    newState[5][0] = state[5][6]  # back
    newState[5][1] = state[5][3]
    newState[5][2] = state[5][0]
    newState[5][3] = state[5][7]
    newState[5][5] = state[5][1]
    newState[5][6] = state[5][8]
    newState[5][7] = state[5][5]
    newState[5][8] = state[5][2]

    return newState

def BInv(state):
    newState = CopyState(state)
    newState[1][2] = state[0][0]  # top
    newState[1][5] = state[0][1]
    newState[1][8] = state[0][2]

    newState[4][8] = state[1][2]  # right
    newState[4][7] = state[1][5]
    newState[4][6] = state[1][8]

    newState[0][2] = state[2][0]  # left
    newState[0][1] = state[2][3]
    newState[0][0] = state[2][6]

    newState[2][0] = state[4][6]  # down
    newState[2][3] = state[4][7]
    newState[2][6] = state[4][8]

    newState[5][6] = state[5][0]  # back
    newState[5][3] = state[5][1]
    newState[5][0] = state[5][2]
    newState[5][7] = state[5][3]
    newState[5][1] = state[5][5]
    newState[5][8] = state[5][6]
    newState[5][5] = state[5][7]
    newState[5][2] = state[5][8]

    return newState


#----- Slice moves -----#
def M(state):
    newState = CopyState(state)
    newState[3][1] = state[0][1]  # top
    newState[3][4] = state[0][4]
    newState[3][7] = state[0][7]
    newState[4][1] = state[3][1]  # front
    newState[4][4] = state[3][4]
    newState[4][7] = state[3][7]
    newState[5][7] = state[4][1]  # down
    newState[5][4] = state[4][4]
    newState[5][1] = state[4][7]
    newState[0][7] = state[5][1]  # back
    newState[0][4] = state[5][4]
    newState[0][1] = state[5][7]
    return newState

def MInv(state):
    newState = CopyState(state)
    newState[0][1] = state[3][1]  # top
    newState[0][4] = state[3][4]
    newState[0][7] = state[3][7]
    newState[3][1] = state[4][1]  # front
    newState[3][4] = state[4][4]
    newState[3][7] = state[4][7]
    newState[4][1] = state[5][7]  # down
    newState[4][4] = state[5][4]
    newState[4][7] = state[5][1]
    newState[5][1] = state[0][7]  # back
    newState[5][4] = state[0][4]
    newState[5][7] = state[0][1]
    return newState

def E(state):
    newState = CopyState(state)
    newState[5][3] = state[1][3]  # right
    newState[5][4] = state[1][4]
    newState[5][5] = state[1][5]
    newState[3][3] = state[2][3]  # left
    newState[3][4] = state[2][4]
    newState[3][5] = state[2][5]
    newState[1][3] = state[3][3]  # front
    newState[1][4] = state[3][4]
    newState[1][5] = state[3][5]
    newState[2][3] = state[5][3]  # back
    newState[2][4] = state[5][4]
    newState[2][5] = state[5][5]
    return newState

def EInv(state):
    newState = CopyState(state)
    newState[1][3] = state[5][3]  # right
    newState[1][4] = state[5][4]
    newState[1][5] = state[5][5]
    newState[2][3] = state[3][3]  # left
    newState[2][4] = state[3][4]
    newState[2][5] = state[3][5]
    newState[3][3] = state[1][3]  # front
    newState[3][4] = state[1][4]
    newState[3][5] = state[1][5]
    newState[5][3] = state[2][3]  # back
    newState[5][4] = state[2][4]
    newState[5][5] = state[2][5]
    return state

def S(state):
    newState = CopyState(state)
    newState[0][3] = state[2][1]  # top
    newState[0][4] = state[2][4]
    newState[0][5] = state[2][7]
    newState[1][1] = state[0][1]  # right
    newState[1][4] = state[0][4]
    newState[1][7] = state[0][7]
    newState[2][1] = state[4][3]  # left
    newState[2][4] = state[4][4]
    newState[2][7] = state[4][5]
    newState[4][3] = state[1][7]  # down
    newState[4][4] = state[1][4]
    newState[4][5] = state[1][1]
    return newState

def SInv(state):
    newState = CopyState(state)
    newState[2][1] = state[0][3]  # top
    newState[2][4] = state[0][4]
    newState[2][7] = state[0][5]
    newState[0][1] = state[1][1]  # right
    newState[0][4] = state[1][4]
    newState[0][7] = state[1][7]
    newState[4][3] = state[2][1]  # left
    newState[4][4] = state[2][4]
    newState[4][5] = state[2][7]
    newState[1][7] = state[4][3]  # down
    newState[1][4] = state[4][4]
    newState[1][1] = state[4][5]
    return newState

# Wide moves
def UWide(state):
    newState = CopyState(state)

    newState[0][0] = state[0][6]  # top
    newState[0][1] = state[0][3]
    newState[0][2] = state[0][0]
    newState[0][3] = state[0][7]
    newState[0][5] = state[0][1]
    newState[0][6] = state[0][8]
    newState[0][7] = state[0][5]
    newState[0][8] = state[0][2]

    newState[1][0] = state[5][0]  # right
    newState[1][1] = state[5][1]
    newState[1][2] = state[5][2]

    newState[2][0] = state[3][0]  # left
    newState[2][1] = state[3][1]
    newState[2][2] = state[3][2]

    newState[3][0] = state[1][0]  # front
    newState[3][1] = state[1][1]
    newState[3][2] = state[1][2]

    newState[5][0] = state[2][0]  # back
    newState[5][1] = state[2][1]
    newState[5][2] = state[2][2]

    # slice move part, E':
    newState[1][3] = state[5][3]  # right
    newState[1][4] = state[5][4]
    newState[1][5] = state[5][5]
    newState[2][3] = state[3][3]  # left
    newState[2][4] = state[3][4]
    newState[2][5] = state[3][5]
    newState[3][3] = state[1][3]  # front
    newState[3][4] = state[1][4]
    newState[3][5] = state[1][5]
    newState[5][3] = state[2][3]  # back
    newState[5][4] = state[2][4]
    newState[5][5] = state[2][5]

    return newState

def UWideInv(state):
    newState = CopyState(state)

    newState[0][6] = state[0][0]  # top
    newState[0][3] = state[0][1]
    newState[0][0] = state[0][2]
    newState[0][7] = state[0][3]
    newState[0][1] = state[0][5]
    newState[0][8] = state[0][6]
    newState[0][5] = state[0][7]
    newState[0][2] = state[0][8]

    newState[5][0] = state[1][0]  # right
    newState[5][1] = state[1][1]
    newState[5][2] = state[1][2]

    newState[3][0] = state[2][0]  # left
    newState[3][1] = state[2][1]
    newState[3][2] = state[2][2]

    newState[1][0] = state[3][0]  # down
    newState[1][1] = state[3][1]
    newState[1][2] = state[3][2]

    newState[2][0] = state[5][0]  # back
    newState[2][1] = state[5][1]
    newState[2][2] = state[5][2]

    # slice move part E:
    newState[5][3] = state[1][3]  # right
    newState[5][4] = state[1][4]
    newState[5][5] = state[1][5]
    newState[3][3] = state[2][3]  # left
    newState[3][4] = state[2][4]
    newState[3][5] = state[2][5]
    newState[1][3] = state[3][3]  # front
    newState[1][4] = state[3][4]
    newState[1][5] = state[3][5]
    newState[2][3] = state[5][3]  # back
    newState[2][4] = state[5][4]
    newState[2][5] = state[5][5]

    return newState

def RWide(state):
    newState = CopyState(state)
    newState[0][2] = state[3][2]  # top
    newState[0][5] = state[3][5]
    newState[0][8] = state[3][8]

    newState[1][0] = state[1][6]  # right
    newState[1][1] = state[1][3]
    newState[1][2] = state[1][0]
    newState[1][3] = state[1][7]
    newState[1][5] = state[1][1]
    newState[1][6] = state[1][8]
    newState[1][7] = state[1][5]
    newState[1][8] = state[1][2]

    newState[3][2] = state[4][2]  # front
    newState[3][5] = state[4][5]
    newState[3][8] = state[4][8]

    newState[4][2] = state[5][6]  # down
    newState[4][5] = state[5][3]
    newState[4][8] = state[5][0]

    newState[5][0] = state[0][8]  # back
    newState[5][3] = state[0][5]
    newState[5][6] = state[0][2]

    # slice move part (M'):
    newState[0][1] = state[3][1]  # top
    newState[0][4] = state[3][4]
    newState[0][7] = state[3][7]
    newState[3][1] = state[4][1]  # front
    newState[3][4] = state[4][4]
    newState[3][7] = state[4][7]
    newState[4][1] = state[5][7]  # down
    newState[4][4] = state[5][4]
    newState[4][7] = state[5][1]
    newState[5][1] = state[0][7]  # back
    newState[5][4] = state[0][4]
    newState[5][7] = state[0][1]

    return newState

def RWideInv(state):
    newState = CopyState(state)
    newState[3][2] = state[0][2]  # top
    newState[3][5] = state[0][5]
    newState[3][8] = state[0][8]

    newState[1][6] = state[1][0]  # right
    newState[1][3] = state[1][1]
    newState[1][0] = state[1][2]
    newState[1][7] = state[1][3]
    newState[1][1] = state[1][5]
    newState[1][8] = state[1][6]
    newState[1][5] = state[1][7]
    newState[1][2] = state[1][8]

    newState[4][2] = state[3][2]  # front
    newState[4][5] = state[3][5]
    newState[4][8] = state[3][8]

    newState[5][6] = state[4][2]  # down
    newState[5][3] = state[4][5]
    newState[5][0] = state[4][8]

    newState[0][8] = state[5][0]  # back
    newState[0][5] = state[5][3]
    newState[0][2] = state[5][6]

    # slice move part (M):
    newState[3][1] = state[0][1]  # top
    newState[3][4] = state[0][4]
    newState[3][7] = state[0][7]
    newState[4][1] = state[3][1]  # front
    newState[4][4] = state[3][4]
    newState[4][7] = state[3][7]
    newState[5][7] = state[4][1]  # down
    newState[5][4] = state[4][4]
    newState[5][1] = state[4][7]
    newState[0][7] = state[5][1]  # back
    newState[0][4] = state[5][4]
    newState[0][1] = state[5][7]

    return newState

def LWide(state):
    newState = CopyState(state)
    newState[0][0] = state[5][8]  # top
    newState[0][3] = state[5][5]
    newState[0][6] = state[5][2]

    newState[2][0] = state[2][6]  # left
    newState[2][1] = state[2][3]
    newState[2][2] = state[2][0]
    newState[2][3] = state[2][7]
    newState[2][5] = state[2][1]
    newState[2][6] = state[2][8]
    newState[2][7] = state[2][5]
    newState[2][8] = state[2][2]

    newState[3][0] = state[0][0]  # front
    newState[3][3] = state[0][3]
    newState[3][6] = state[0][6]

    newState[4][0] = state[3][0]  # down
    newState[4][3] = state[3][3]
    newState[4][6] = state[3][6]

    newState[5][2] = state[4][6]  # back
    newState[5][5] = state[4][3]
    newState[5][8] = state[4][0]

    # slice move part M:
    newState[3][1] = state[0][1]  # top
    newState[3][4] = state[0][4]
    newState[3][7] = state[0][7]
    newState[4][1] = state[3][1]  # front
    newState[4][4] = state[3][4]
    newState[4][7] = state[3][7]
    newState[5][7] = state[4][1]  # down
    newState[5][4] = state[4][4]
    newState[5][1] = state[4][7]
    newState[0][7] = state[5][1]  # back
    newState[0][4] = state[5][4]
    newState[0][1] = state[5][7]
    return newState

def LWideInv(state):
    newState = CopyState(state)

    newState[5][8] = state[0][0]  # top
    newState[5][5] = state[0][3]
    newState[5][2] = state[0][6]

    newState[2][6] = state[2][0]  # left
    newState[2][3] = state[2][1]
    newState[2][0] = state[2][2]
    newState[2][7] = state[2][3]
    newState[2][1] = state[2][5]
    newState[2][8] = state[2][6]
    newState[2][5] = state[2][7]
    newState[2][2] = state[2][8]

    newState[0][0] = state[3][0]  # front
    newState[0][3] = state[3][3]
    newState[0][6] = state[3][6]

    newState[3][0] = state[4][0]  # down
    newState[3][3] = state[4][3]
    newState[3][6] = state[4][6]

    newState[4][6] = state[5][2]  # back
    newState[4][3] = state[5][5]
    newState[4][0] = state[5][8]

    # slice move part M':
    newState[0][1] = state[3][1]  # top
    newState[0][4] = state[3][4]
    newState[0][7] = state[3][7]
    newState[3][1] = state[4][1]  # front
    newState[3][4] = state[4][4]
    newState[3][7] = state[4][7]
    newState[4][1] = state[5][7]  # down
    newState[4][4] = state[5][4]
    newState[4][7] = state[5][1]
    newState[5][1] = state[0][7]  # back
    newState[5][4] = state[0][4]
    newState[5][7] = state[0][1]
    return newState

def FWide(state):
    newState = CopyState(state)
    newState[0][6] = state[2][8]  # top
    newState[0][7] = state[2][5]
    newState[0][8] = state[2][2]

    newState[1][0] = state[0][6]  # right
    newState[1][3] = state[0][7]
    newState[1][6] = state[0][8]

    newState[2][2] = state[4][0]  # left
    newState[2][5] = state[4][1]
    newState[2][8] = state[4][2]

    newState[3][0] = state[3][6]  # front
    newState[3][1] = state[3][3]
    newState[3][2] = state[3][0]
    newState[3][3] = state[3][7]
    newState[3][5] = state[3][1]
    newState[3][6] = state[3][8]
    newState[3][7] = state[3][5]
    newState[3][8] = state[3][2]

    newState[4][0] = state[1][6]  # down
    newState[4][1] = state[1][3]
    newState[4][2] = state[1][0]

    # slice move S:
    newState[0][3] = state[2][1]  # top
    newState[0][4] = state[2][4]
    newState[0][5] = state[2][7]
    newState[1][1] = state[0][1]  # right
    newState[1][4] = state[0][4]
    newState[1][7] = state[0][7]
    newState[2][1] = state[4][3]  # left
    newState[2][4] = state[4][4]
    newState[2][7] = state[4][5]
    newState[4][3] = state[1][7]  # down
    newState[4][4] = state[1][4]
    newState[4][5] = state[1][1]

    return newState

def FWideInv(state):
    newState = CopyState(state)
    newState[2][8] = state[0][6]  # top
    newState[2][5] = state[0][7]
    newState[2][2] = state[0][8]
    newState[0][6] = state[1][0]  # right
    newState[0][7] = state[1][3]
    newState[0][8] = state[1][6]
    newState[4][0] = state[2][2]  # left
    newState[4][1] = state[2][5]
    newState[4][2] = state[2][8]
    newState[3][6] = state[3][0]  # front
    newState[3][3] = state[3][1]
    newState[3][0] = state[3][2]
    newState[3][7] = state[3][3]
    newState[3][1] = state[3][5]
    newState[3][8] = state[3][6]
    newState[3][5] = state[3][7]
    newState[3][2] = state[3][8]
    newState[1][6] = state[4][0]  # down
    newState[1][3] = state[4][1]
    newState[1][0] = state[4][2]

    # slice move S':
    newState[2][1] = state[0][3]  # top
    newState[2][4] = state[0][4]
    newState[2][7] = state[0][5]
    newState[0][1] = state[1][1]  # right
    newState[0][4] = state[1][4]
    newState[0][7] = state[1][7]
    newState[4][3] = state[2][1]  # left
    newState[4][4] = state[2][4]
    newState[4][5] = state[2][7]
    newState[1][7] = state[4][3]  # down
    newState[1][4] = state[4][4]
    newState[1][1] = state[4][5]

    return newState

def DWide(state):
    newState = CopyState(state)
    newState[1][6] = state[3][6]  # right
    newState[1][7] = state[3][7]
    newState[1][8] = state[3][8]

    newState[2][6] = state[5][6]  # left
    newState[2][7] = state[5][7]
    newState[2][8] = state[5][8]

    newState[3][6] = state[2][6]  # front
    newState[3][7] = state[2][7]
    newState[3][8] = state[2][8]

    newState[4][0] = state[4][6]  # down
    newState[4][1] = state[4][3]
    newState[4][2] = state[4][0]
    newState[4][3] = state[4][7]
    newState[4][5] = state[4][1]
    newState[4][6] = state[4][8]
    newState[4][7] = state[4][5]
    newState[4][8] = state[4][2]

    newState[5][6] = state[1][6]  # back
    newState[5][7] = state[1][7]
    newState[5][8] = state[1][8]

    # slice move E:
    newState[5][3] = state[1][3]  # right
    newState[5][4] = state[1][4]
    newState[5][5] = state[1][5]
    newState[3][3] = state[2][3]  # left
    newState[3][4] = state[2][4]
    newState[3][5] = state[2][5]
    newState[1][3] = state[3][3]  # front
    newState[1][4] = state[3][4]
    newState[1][5] = state[3][5]
    newState[2][3] = state[5][3]  # back
    newState[2][4] = state[5][4]
    newState[2][5] = state[5][5]

    return newState

def DWideInv(state):
    newState = CopyState(state)
    newState[3][6] = state[1][6]  # right
    newState[3][7] = state[1][7]
    newState[3][8] = state[1][8]

    newState[5][6] = state[2][6]  # left
    newState[5][7] = state[2][7]
    newState[5][8] = state[2][8]

    newState[2][6] = state[3][6]  # front
    newState[2][7] = state[3][7]
    newState[2][8] = state[3][8]

    newState[4][6] = state[4][0]  # down
    newState[4][3] = state[4][1]
    newState[4][0] = state[4][2]
    newState[4][7] = state[4][3]
    newState[4][1] = state[4][5]
    newState[4][8] = state[4][6]
    newState[4][5] = state[4][7]
    newState[4][2] = state[4][8]

    newState[1][6] = state[5][6]  # back
    newState[1][7] = state[5][7]
    newState[1][8] = state[5][8]

    # slice move E':
    newState[1][3] = state[5][3]  # right
    newState[1][4] = state[5][4]
    newState[1][5] = state[5][5]
    newState[2][3] = state[3][3]  # left
    newState[2][4] = state[3][4]
    newState[2][5] = state[3][5]
    newState[3][3] = state[1][3]  # front
    newState[3][4] = state[1][4]
    newState[3][5] = state[1][5]
    newState[5][3] = state[2][3]  # back
    newState[5][4] = state[2][4]
    newState[5][5] = state[2][5]

    return newState

def BWide(state):
    newState = CopyState(state)
    newState[0][0] = state[1][2]  # top
    newState[0][1] = state[1][5]
    newState[0][2] = state[1][8]

    newState[1][2] = state[4][8]  # right
    newState[1][5] = state[4][7]
    newState[1][8] = state[4][6]

    newState[2][0] = state[0][2]  # left
    newState[2][3] = state[0][1]
    newState[2][6] = state[0][0]

    newState[4][6] = state[2][0]  # down
    newState[4][7] = state[2][3]
    newState[4][8] = state[2][6]

    newState[5][0] = state[5][6]  # back
    newState[5][1] = state[5][3]
    newState[5][2] = state[5][0]
    newState[5][3] = state[5][7]
    newState[5][5] = state[5][1]
    newState[5][6] = state[5][8]
    newState[5][7] = state[5][5]
    newState[5][8] = state[5][2]

    # wide move S':
    newState[2][1] = state[0][3]  # top
    newState[2][4] = state[0][4]
    newState[2][7] = state[0][5]
    newState[0][1] = state[1][1]  # right
    newState[0][4] = state[1][4]
    newState[0][7] = state[1][7]
    newState[4][3] = state[2][1]  # left
    newState[4][4] = state[2][4]
    newState[4][5] = state[2][7]
    newState[1][7] = state[4][3]  # down
    newState[1][4] = state[4][4]
    newState[1][1] = state[4][5]

    return newState

def BWideInv(state):
    newState = CopyState(state)
    newState[1][2] = state[0][0]  # top
    newState[1][5] = state[0][1]
    newState[1][8] = state[0][2]

    newState[4][8] = state[1][2]  # right
    newState[4][7] = state[1][5]
    newState[4][6] = state[1][8]

    newState[0][2] = state[2][0]  # left
    newState[0][1] = state[2][3]
    newState[0][0] = state[2][6]

    newState[2][0] = state[4][6]  # down
    newState[2][3] = state[4][7]
    newState[2][6] = state[4][8]

    newState[5][6] = state[5][0]  # back
    newState[5][3] = state[5][1]
    newState[5][0] = state[5][2]
    newState[5][7] = state[5][3]
    newState[5][1] = state[5][5]
    newState[5][8] = state[5][6]
    newState[5][5] = state[5][7]
    newState[5][2] = state[5][8]

    # wide move S:
    newState[0][3] = state[2][1]  # top
    newState[0][4] = state[2][4]
    newState[0][5] = state[2][7]
    newState[1][1] = state[0][1]  # right
    newState[1][4] = state[0][4]
    newState[1][7] = state[0][7]
    newState[2][1] = state[4][3]  # left
    newState[2][4] = state[4][4]
    newState[2][7] = state[4][5]
    newState[4][3] = state[1][7]  # down
    newState[4][4] = state[1][4]
    newState[4][5] = state[1][1]

    return newState


# Cube rotations
def x(state):
    newState = RWide(state)
    return LInv(newState)

def xInv(state):
    newState = RWideInv(state)
    return L(newState)

def y(state):
    newState = UWide(state)
    return DInv(newState)

def yInv(state):
    newState = UWideInv(state)
    return D(newState)

def z(state):
    newState = FWide(state)
    return BInv(newState)

def zInv(state):
    newState = FWideInv(state)
    return B(newState)


