def DFS(graph,src,visited):
    print(src,end=" ")
    visited.add(src)
    for i in graph[src]:
        if i not in visited:
            DFS(graph,i,visited)

def DFS2(graph,src):
    visited=set()
    stack=set()
    stack.add(src)
    while stack:
        # print(stack)
        data = stack.pop()
        visited.add(data)
        print(data,end=" ")
        for i in graph[data]:
            if i not in visited:
                stack.add(i)
graph = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B", "D", "E"],
    "D": ["A", "C", "E"],
    "E": ["C", "D"]
}
src = 'A'
visited=set()
# DFS(graph,src,visited)
DFS2(graph,src)

# def DFS(graph, start, visited=None):

#     if visited == None:

#         visited = set()

#     visited.add(start)

#     print(start)

#     for i in graph[start]:

#         if i not in visited:

#             visited.add(i)

#             DFS(graph, i, visited)

# graph = {

#     "A": ["B", "D"],

#     "B": ["A", "C"],

#     "C": ["B", "D", "E"],

#     "D": ["A", "C", "E"],

#     "E": ["C", "D"]

# }

# # BFS(graph, "A")

# DFS(graph, "C")




