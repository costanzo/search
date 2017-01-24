# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import copy
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    state = problem.getStartState()
    queue = util.Stack()
    queue.push([(state, None, 0)])

    while not queue.isEmpty():
        states= queue.pop()
        currentState, action, cost= states[-1]
        if problem.isGoalState(currentState):
            acs = []
            for s, a, c in states:
                if a:
                    acs.append(a)
            return acs

        successors = problem.getSuccessors(currentState)
        su =[]
        for s,a,c in successors:
            if not isVisited(states, s):
                su.append((s,a,c))
        for e in su:
            list = copy.deepcopy(states)
            list.append(e)
            queue.push(list)

def popTheSame(s1, s2):
    e1 = s1.pop()
    e2 = s2.pop()
    while e1 == e2:
        e1 = s1.pop()
        e2 = s2.pop()
    s1.push(e1)
    s2.push(e2)

def stackToList(stack):
    acts = util.Stack()
    while not stack.isEmpty():
        s, a = stack.pop()
        acts.push(a)
    sequence = []
    acts.pop()
    while not acts.isEmpty():
        sequence.append(acts.pop())
    return sequence

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"

    state = problem.getStartState()
    queue = util.Queue()
    queue.push([(state, None, 0)])

    while not queue.isEmpty():
        states= queue.pop()
        currentState, action, cost= states[-1]
        print currentState
        if problem.isGoalState(currentState):
            acs = []
            for s, a, c in states:
                if a:
                    acs.append(a)
            return acs

        successors = problem.getSuccessors(currentState)
        su =[]
        for s,a,c in successors:
            if not isVisited(states, s):
                su.append((s,a,c))
        for e in su:
            list = copy.deepcopy(states)
            list.append(e)
            queue.push(list)

def getActionsFromQueue(queue):
    last = queue.pop()
    acts = []
    for su, action in last:
        if action:
            acts.append(action)
    return acts

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    queue = util.PriorityQueue()
    queue.push([(state, None, 0)], 0)

    while not queue.isEmpty():
        states= queue.pop()
        currentState, action, cost = states[-1]
        if problem.isGoalState(currentState):
            acs = []
            for s, a, c in states:
                if a:
                    acs.append(a)
            return acs

        successors = problem.getSuccessors(currentState)
        su =[]
        for s,a,c in successors:
            if not isVisited(states, s):
                su.append((s,a,c))
        for e in su:
            list = copy.deepcopy(states)
            list.append(e)
            cost = totalCost(list)
            queue.push(list, cost)

def totalCost(list):
    cost = 0
    for s,a,c in list:
        cost += c
    return cost

def isVisited(elements, state):
    for su, ac, co in elements:
        if su == state:
            return True
    return False

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    queue = util.PriorityQueue()
    queue.push([(state, None, 0)], 0)

    while not queue.isEmpty():
        states = queue.pop()
        currentState, action, cost = states[-1]
        if problem.isGoalState(currentState):
            acs = []
            for s, a, c in states:
                if a:
                    acs.append(a)
            return acs

        successors = problem.getSuccessors(currentState)
        su = []
        for s, a, c in successors:
            if not isVisited(states, s):
                su.append((s, a, c))
        for s,a,c in su:
            list = copy.deepcopy(states)
            list.append((s,a,c))
            cost = totalCost(list)
            incr = heuristic(s, problem)
            queue.push(list, cost + incr)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
