
#undirected, unweighted graph
graph = []
f = open("inputMatrix.txt",'r')
for line in f:
	line = [int(x) for x in line.split()]
	graph.append(line)
N = len(graph)
print(graph)

start_vertex = 0
end_vertex = 8

visited = []
toExplore = [start_vertex]

while toExplore:
	vertex = toExplore.pop(0)
	visited.append(vertex)
	print(vertex)
	if vertex == end_vertex:
		print("found path!")
		break
	else:
		for i in range(N):
			if graph[vertex][i] == 1 and i not in visited:
				#toExplore.append(i) # BFS
				toExplore = [i]+toExplore # DFS

else:
	print("no path found")
