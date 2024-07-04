from heapq import heapify, heappush, heappop

def adjacencyList(v, list):
    dict = {}

    for x in range(v + 1):
        dict[x] = [[], 0]

    for z in list:
        dict[z[0]][0].append(z[1])

    return dict

def modified_topology_dfs(graph, source, stack, visited):
    if source not in stack:
        visited.append(source)
        for x in graph[source][0]:
            if x not in visited:
                modified_topology_dfs(graph, x, stack, visited)
        stack.append(source)

def transposed_topology_dfs(graph, source, stack, visited, group):
    if source not in stack:
        visited.append(source)
        for x in graph[source][0]:
            if x not in visited:
                transposed_topology_dfs(graph, x, stack, visited, group)
        stack.append(source)
        group.append(source)


read_list = [["input3a.txt", "output3a.txt"], ["input3b.txt", "output3b.txt"], ["input3c.txt", "output3c.txt"]]

for num in read_list:
    r = open(num[0], 'r')
    w = open(num[1], 'w')

    first = r.readline().split()
    list = []
    list2 = []

    for x in range(int(first[1])):
        second = r.readline().split()
        second = [int(x) for x in second]
        list.append(second)
        second = second[::-1]
        list2.append(second)

    store = adjacencyList(int(first[0]), list)
    store2 = adjacencyList(int(first[0]), list2)
    stack = []
    visited = []

    for y in range(1, int(first[0]) + 1):
        modified_topology_dfs(store, y, stack, visited)

    stack = stack[::-1]
    stack2 = []
    visited2 = []
    final = []

    for z in stack:
        group = []
        transposed_topology_dfs(store2, z, stack2, visited2, group)
        if group not in final and len(group) != 0:
            final.append(group)


    output = ""

    for i in final:
        for j in range(len(i)):
            heapify(i)
            vertex = heappop(i)
            output += f"{vertex} "
        output += "\n"

    w.write(output)
    w.close()




