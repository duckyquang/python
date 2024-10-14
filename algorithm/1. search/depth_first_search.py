# DFS - Depth First Search
# Tracks down a single branch 'til its deepest point
# Backtracks to another untouched branch if there are yet to a be a result

import time

graph = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}

def DFS(graph, node, visited = None):
    delay = 1
    
    if visited == None:
        visited = set()
    
    visited.add(node)
    print(f"Visiting {node}...")
    time.sleep(delay)
    print(f"Visited: {visited}")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)
            time.sleep(delay)


DFS(graph, 'A')
