from collections import deque
def bfs(graph, start, goal):
 visited = set()
 queue = deque([[start]]) # queue holds paths, not just nodes
 visited.add(start)
 while queue:
 path = queue.popleft()
 node = path[-1]
 print("Visiting:", node)
 if node == goal:
 return path
 for neighbour in graph[node]:
 if neighbour not in visited:
 visited.add(neighbour)
 newpath = list(path)
 newpath.append(neighbour) queue.append(newpath)
 return None
graph = {
 'You': ['B', 'C', 'D'],
 'B': ['You', 'E', 'F'],
 'C': ['You', 'G'],
 'D': ['You', 'H'],
 'E': ['B'],
 'F': ['B'],
 'G': ['C'],
 'H': ['D']
}
startnode = 'You'
goalnode = 'G'
resultpath = bfs(graph, startnode, goalnode)
if resultpath:
 print("\nGoal found!")
 print("Path from", startnode, "to", goalnode, ":", " -> ".join(resultpath))
else:
 print("\nGoal not found.")
