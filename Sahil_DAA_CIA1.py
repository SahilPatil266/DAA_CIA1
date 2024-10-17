def addEdge(u, v, w):
	graph.append([u, v, w])

def printArr(dist):
	print("Vertex Distance from Source S")
	for i in range(V):
		print("{0}\t\t{1}".format(i, dist[i]))

def BellmanFord(src):
	dist = [float("Inf")] * V
	dist[src] = 0

	for _ in range(V - 1):
		for u, v, w in graph:
			if dist[u] != float("Inf") and dist[u] + w < dist[v]:
				dist[v] = dist[u] + w

	for u, v, w in graph:
		if dist[u] != float("Inf") and dist[u] + w < dist[v]:
			print("This graph contains negative weight cycle.")
			return

	printArr(dist)

if __name__ == '__main__':
    V=6 
    graph=[]
    addEdge(0, 1, 10)
    addEdge(0, 5, 8)
    addEdge(1, 3, 2)
    addEdge(2, 1, 1)
    addEdge(3, 2, -2)
    addEdge(4, 1, -4)
    addEdge(4, 3, -1)
    addEdge(5, 4, 1)

    BellmanFord(0)   bye

