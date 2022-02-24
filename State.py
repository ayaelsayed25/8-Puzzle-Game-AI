class State:
    value = ""
    zeroIndex = 0
    zeroIndexI = 0
    zeroIndexJ = 0
    cost = 0

    def __init__(self, value, zeroIndex):
        self.value = value
        self.zeroIndex = zeroIndex
        self.zeroIndexI = zeroIndex // 3
        self.zeroIndexJ = zeroIndex - (self.zeroIndexI * 3)

    def findElementIndex(self, indexI, indexJ):
        return (indexI * 3) + indexJ

    def isGoalState(self, goal):
        return self.value == goal.value

    def constructNextState(currentState, action):
        elementIndexI = currentState.zeroIndexI
        elementIndexJ = currentState.zeroIndexJ
        if action == 'up' and currentState.zeroIndexI != 0:
            elementIndexI -= 1
        elif action == 'down' and currentState.zeroIndexI != 2:
            elementIndexI += 1
        elif action == 'right' and currentState.zeroIndexJ != 2:
            elementIndexJ += 1
        elif action == 'left' and currentState.zeroIndexJ != 0:
            elementIndexJ -= 1
        else:
            return None

        elementIndex = currentState.findElementIndex(elementIndexI, elementIndexJ)
        value = currentState.value
        # string is immutable  value[currentState.zeroIndex] = value[elementIndex]
        value = value[:currentState.zeroIndex] + value[elementIndex] + value[currentState.zeroIndex + 1:]
        value = value[:elementIndex] + '0' + value[elementIndex + 1:]

        newState = State(value, elementIndex)
        return newState


