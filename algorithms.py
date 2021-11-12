import time
import math
from queue import PriorityQueue


class State:
    value = ""
    zeroIndex = 0
    zeroIndexI = 0
    zeroIndexJ = 0
    cost = 0
    total_cost = 0

    def __init__(self, value, zeroIndex):
        self.value = value
        self.zeroIndex = zeroIndex
        self.zeroIndexI = zeroIndex // 3
        self.zeroIndexJ = zeroIndex - (self.zeroIndexI * 3)

    def __eq__(self, other):
        if isinstance(other, State):
            return self.total_cost == other.total_cost

    def findElementIndex(self, indexI, indexJ):
        return (indexI * 3) + indexJ

    def isGoalState(self, goal):
        return self.value == goal.value

    def isGoalState(self, goal):
        return self.value == goal.value


goal_state = State("012345678", 0)
movements = ['up', 'down', 'right', 'left']


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


def construct_path(state, initial_state, start_time, parent_set):
    timeOfExecution = (time.time() - start_time)
    path = []
    costOfPath = state.cost
    # starting from goal until the root of the path
    while state.value != initial_state.value:
        path.append(state.value)
        state = parent_set[state.value]
    path.append(state.value)
    path.reverse()
    return [True, timeOfExecution, path, costOfPath]


def BFS(initial_state):
    frontier_queue = [initial_state]
    parent_set = {initial_state.value: initial_state}
    explored = []
    maxDepth = 0
    start_time = time.time()

    while len(frontier_queue) != 0:
        state = frontier_queue.pop(0)
        if state.cost > maxDepth:
          maxDepth = state.cost
        explored.append(state.value)

        if state.isGoalState(goal_state):
            return construct_path(state, initial_state, start_time, parent_set) + [explored, maxDepth + 1]
        for move in movements:
            newState = constructNextState(state, move)
            if newState is not None and parent_set.get(newState.value) is None:
                # search if not in frontier or explored = not in parent set
                parent_set[newState.value] = state
                frontier_queue.append(newState)
    timeOfExecution = (time.time() - start_time)
    return [False, timeOfExecution, explored, maxDepth + 1]


def DFS(initialState):
    frontierStack = [initialState]
    parentSet = {initialState.value: initialState}
    explored = []
    maxDepth = 0
    start_time = time.time()
    while len(frontierStack) != 0:
        state = frontierStack.pop()
        if state.cost > maxDepth:
          maxDepth = state.cost
        explored.append(state.value)

        if state.isGoalState(goal_state):
            return construct_path(state, initialState, start_time, parentSet) + [explored, maxDepth + 1]

        # adding state childern up down right left
        for move in movements:
            newState = constructNextState(state, move)
            # search if not in frontier or explored = not in parent set
            if newState is not None and parentSet.get(newState.value) is None:
                newState.cost = state.cost + 1
                parentSet[newState.value] = state
                frontierStack.append(newState)
    timeOfExecution = (time.time() - start_time)
    return [False, timeOfExecution, explored, maxDepth + 1]


def AStarEuclidean(initial_state):
    return AStarSearch(initial_state, euclideanHeuristics)

def AStarManhattan(initial_state):
    return AStarSearch(initial_state, manhattanHeuristics)


# A* Search:
def AStarSearch(initialState, heuristicsFunction):
    frontier = PriorityQueue()
    initHeuristics = heuristicsFunction(initialState)  # heuristics in initial state
    frontier.put((initHeuristics, initialState))  # initialize priority queue
    parentSet = {initialState.value: initialState}  # parent set to track the parent of the state
    costSet = {
        initialState.value: initHeuristics}  # hashmap for mapping the cost to the state value, helps search with cost = theta(1)
    explored = []  # list for visited states
    maxDepth = 0
    start_time = time.time()

    while not frontier.empty():
        theCost = frontier.queue[0][0]  # the cost of the min element in the priority queue
        if theCost == costSet[frontier.queue[0][
            1].value]:  # if the cost of the min state equals the cost for the updated state, visit that state
            state = frontier.get()[1]
            explored.append(state.value)
            if(state.cost > maxDepth):
              maxDepth = state.cost
            if state.isGoalState(goal_state):  # check if the state is a goal state
                return construct_path(state, initialState, start_time, parentSet) + [explored, maxDepth+1]

            for i in ['up', 'down', 'right', 'left']:
                newState = constructNextState(state, i)
                if newState is not None:
                    newCost = state.cost + 1
                    newState.cost = newCost
                    totalCost = newCost + heuristicsFunction(newState)  # calculate the new cost

                    if parentSet.get(newState.value) is None:  # the state is not visited or in the priority queue
                        parentSet[newState.value] = state
                        frontier.put((totalCost, newState))
                        costSet[newState.value] = totalCost

                    elif costSet[
                        newState.value] > totalCost:  # state has been put in the priority queue before and now has a lower cost
                        parentSet[newState.value] = state
                        frontier.put((totalCost, newState))  # add to the queue again
                        costSet[newState.value] = totalCost  # decrease key
        else:
            frontier.get()
    timeOfExecution = (time.time() - start_time)
    return [False, timeOfExecution, explored, maxDepth + 1]


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
        distance = math.sqrt(abs(icurrent - i) ** 2 + abs(jcurrent - j) ** 2)
        sum = sum + distance
    return sum
