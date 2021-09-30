graph = {
  '1' : ['4', '2'],
  '2' : ['1', '3', '8', '7', '5'],
  '3' : ['10', '9', '4', '2'],
  '4' : ['1','3'],
  '5' : ['2', '7', '6'],
  '6' : ['5'],
  '7' : ['5', '2', '8'],
  '8' : ['2', '7'],
  '9' : ['3'],
  '10' : ['3']
}

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, graph, '1')