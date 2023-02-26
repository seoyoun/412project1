# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    ## keeping track of whether a position is visited or not 
    positionsVisited = {}
    ## add ((4,5), [n,s,w])
    from util import Stack
    
    ## stack to push and pop nodes that we need to traverse at the moment
    stack = Stack()
    
    ## get the starting position
    startingPosition = problem.getStartState()

    ## push it into the stack
    stack.push((startingPosition, [], 0))

    while not stack.isEmpty: 
        currentPositionInformation = stack.pop()

        currentPosition = currentPositionInformation[0]
        
        if not currentPosition in positionsVisited :
            ## if we have not visted the position we just popped, we
            ## add it to the list of positions
            
            positionsVisited[currentPosition] = (currentPositionInformation[1], currentPositionInformation[2])
        
        ## getting the successors of the current position, verify if they
        ## have not been visited, then add to the node
        successors = problem.getSuccessors(currentPosition)

        for (coordinate, direction, length) in successors: 
            if coordinate not in positionsVisited: 
                appendedDirection = currentPositionInformation[1].append(direction)
                appendedLength = currentPositionInformation[2] + length
                stack.push((coordinate, appendedDirection, appendedLength))

      
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    from game import Directions


    ## code is adapted from the graph_search psuedocode from Project 1 instructions

    startState = problem.getStartState()

    ## initializing the priority queue
    frontier = Queue()
    frontier.push((startState, []))
    
    ## initializing a dictionary of the expanded states
    expanded = {}
    
    ## since this is a priority queue, will pop the value of the smallest depth
    while not frontier.isEmpty() :
        nodeCoordinate, coordinatePath = frontier.pop()

        if problem.isGoalState(nodeCoordinate):
            return coordinatePath
        if nodeCoordinate not in expanded:
            expanded.append(nodeCoordinate)
            
            ## getting the list of successors and appending it to the queue
            successors = problem.getSuccessors(nodeCoordinate)

            for coordinate, direction, length in successors:
                updatedDirectionPath = coordinatePath
                if direction is 'North':
                    updatedDirectionPath.append(Directions.NORTH)
                elif direction is 'South':
                    updatedDirectionPath.append(Directions.SOUTH)
                elif direction is 'East':
                    updatedDirectionPath.append(Directions.EAST)
                elif direction is 'West':
                    updatedDirectionPath.append(Directions.WEST)
                frontier.push((coordinate, updatedDirectionPath))

    


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
