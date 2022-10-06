#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# YOUR COMMENTS INCLUDING CITATIONS
#
# Samuel Saldivar- 09/22/2022
# 


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    #  node containing initial state of the problem
    startNode = Node(problem.start)
    # return  Node if it contains goal node
    if problem.is_goal(startNode):
        return startNode
    # add startNode to frontier,initializing a stack
    stack = Frontier(startNode, True)
    # reached set must contain startNode
    path = set()
    if repeat_check:
        path.add(startNode.loc)

    # while frontier is not empty
    while not stack.is_empty():
        # node that has just been removed
        startNode = stack.pop()
        # return if goal node
        if problem.is_goal(startNode.loc):
            return startNode
        # expand removedNode then iterate

        for i in startNode.expand(problem):
            # add child to  frontier
            if repeat_check:
                current = i.loc
                if current not in path:
                    path.add(current)  # adds to reached set
                    stack.add(i)

            else:
                stack.add(i)

    return None  # none is failure
