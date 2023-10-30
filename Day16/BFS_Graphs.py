def BFS(graph, start):
    visited = [start]
    queue = [start]
    while len(queue) != 0:
        ele = queue.pop(0)
        print(ele, end=", ")
        for i in graph[ele]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
graph = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B", "D", "E"],
    "D": ["A", "C", "E"],
    "E": ["C", "D"]
}
BFS(graph, "A")