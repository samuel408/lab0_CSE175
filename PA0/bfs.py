#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
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


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""
    # PLACE YOUR CODE HERE
    #  node containing initial state of the problem
    startNode = Node(problem.start)
    #return  Node if it contains goal node
    if problem.is_goal(startNode):
        return startNode
    #add startNode to frontier,initializing a queue
    queue = Frontier(startNode, True)
    #reached set must contain startNode
    path = set()
    if repeat_check:
        path.add(startNode.loc)

    #while frontier is not empty
    while not queue.is_empty():

        #node that has just been removed
        removedNode = queue.pop()
        #return if goald
        if problem.is_goal(removedNode):
            return removedNode
         #expand removedNode then iterate

        location = removedNode.expand(problem)
    for i in location :
            # add child to  frontier
        if repeat_check:
            if i not in path:
                 path.add(i.loc)#adds to reached set
                 queue.add(i)
        else:
             queue.add(i)

    return None#none is failure
