from math import sqrt

from State import State



# AStar(initialState,goalState)

def constructNextState (currentState , action ):
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


# DFS solving
import time


def Dfs(initialState, goalState):
    frontierStack = [initialState]
    parentSet = {initialState.value: initialState}

    while (len(frontierStack) != 0):
        left = 0
        down = 0
        # print(frontierStack)
        # time.sleep(5)
        state = frontierStack.pop()
        # print(state.value)
        # time.sleep(5)

        if state.isGoalState(goalState):
            path = []
            # starting from goal until the root of the path
            while (parentSet[state.value] != state):
                path.append(state)
                state = parentSet[state.value]
            path.append(state)
            print(len(path))
            return True

        # adding state childern up down right left
        movements = ['up', 'down', 'right', 'left']
        for move in movements:
            newState = constructNextState(state, move)
            if newState == None:
                continue
                # search if not in frontier or explored = not in parent set
            print(newState.value)
            if parentSet.get(newState.value) == None:
                parentSet[newState.value] = state
                frontierStack.append(newState)

    # print(state.value)
    return False

print("input")
value = input().replace(",", "")
zeroIndex = value.find('0')
initialState = State(value ,zeroIndex)
goalState = State("012345678" ,0)
# DFS call
Dfs(initialState, goalState)

# A* Search:
from queue import PriorityQueue


def AStar(initialState, goalState):
    frontier = PriorityQueue()
    initHeuristics = manhattanHeuristics(initialState)
    frontier.put((initHeuristics, initialState))
    parentSet = {initialState.value: initialState}

    costSet = {initialState.value: initHeuristics}

    while not frontier.empty():
        theCost = frontier[0][0]
        if theCost == costSet[frontier[0][1].value]:
            state = frontier.get()[1]

            if state.isGoalState(goalState):
                path = []
                # starting from goal until the root of the path
                print("cost = " + str(state.cost))
                while (parentSet[state.value] != state):
                    path.append(state)
                    state = parentSet[state.value]
                path.append(state)
                print(len(path))
                return True

            for i in ['up', 'down', 'right', 'left']:
                newState = None
                if newState is not None:
                    newCost = state.cost + 1
                    newState.cost = newCost
                    totalCost = newCost + manhattanHeuristics(newState)
                    if parentSet.get(newState.value) == None:
                        parentSet[newState.value] = state
                        frontier.put((totalCost, newState))
                        costSet[newState.value] = totalCost
                    elif costSet[newState.value].value > totalCost:
                        parentSet[newState.value] = state
                        frontier.put((totalCost, newState))
                        costSet[newState.value] = totalCost
                        # decrease key in frontier + costset in less than n
                        # dictionary : get min in n, search in 1, insert in 1
        else:
            frontier.get()

    return False


# Manhattan distance heuristics
def manhattanHeuristics(currentState):
    sum = 0
    for ch in range(len(currentState.value)):
        icurrent = ch // 3
        jcurrent = ch - (icurrent * 3)
        truePosition = int(currentState.value[ch])
        i = truePosition // 3
        j = truePosition - (i * 3)
        distance = abs(icurrent - i) + abs(jcurrent - j)
        sum = sum + distance
    return sum


# Euclidean distance heuristics
def euclideanHeuristics(currentState):
    sum = 0
    for ch in range(len(currentState.value)):
        icurrent = ch // 3
        jcurrent = ch - (icurrent * 3)
        truePosition = int(currentState.value[ch])
        i = truePosition // 3
        j = truePosition - (i * 3)
        distance = sqrt(abs(icurrent - i) ** 2 + abs(jcurrent - j) ** 2)
        sum = sum + distance
    return sum
