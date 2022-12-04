# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:43:06 2022

@author: yered
"""

from collections import defaultdict

# Generate adjacency list for undirected graph
def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList

edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'H'], ['D', 'I'], ['E', 'J'], ['E', 'K'], ['F', 'L'], ['F', 'M']]
adjacencyList = generateAdjacencyLst(edges)
print(adjacencyList)