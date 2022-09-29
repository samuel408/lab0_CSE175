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
    if startNode == problem.goal:
        return startNode
    #add startNode to frontier,initializing a queue
    Frontier(startNode, True)
    #reached set must contain startNode
    path = set((startNode))
    #while frontier is not empty
    check = Frontier.is_empty()
    while check != 0:
        #node that has just been removed
        removedNode = Frontier.pop()
        #return if goal
        if removedNode == problem.goal:
            return removedNode
     #expand removedNode then iterate
        for i in removedNode.expand(problem):
            #add child to  frontier
          #  if repeat_check == False:
              #  Frontier.add(i)
            #temp variable to check if child is in set
            temp = 0
            for j in path:
                if i == j:
                    temp = 1
            if temp == 0 and repeat_check == False:
                Frontier.add(i)
                path.add(i)




        check = Frontier.is_empty()# loop condition


    return None #none is failure
