import numpy as np

print("Input the names of all the nodes : ")
titles = [input("enter name {} : ".format(i + 1)) for i in range(int(input("no. of nodes : ")))]
n = len(titles)
graph_dict = {}
for i in titles:
    graph_dict[i] = list(map(int, input("outlinks from {} : ".format(i)).split()))

graph = ([graph_dict[i] for i in graph_dict])

# print(f'{graph}')
"""
0 1 0 0 0 1
0 0 0 0 0 1
0 1 0 0 0 0
0 1 0 0 0 1
0 1 0 1 0 0
1 1 1 1 1 0
"""

def A_val(graph):
    built_graph = []
    for i in graph:
        link_weight = []
        for j in i:
            if j == 1:
                link_weight.append(1/i.count(1))
            else:
                link_weight.append(0)
        built_graph.append(link_weight)
    return np.array(built_graph)

Adjacency_Matrix = A_val(graph)

print(f'\nAdjacency Matrix\n{Adjacency_Matrix}\n\n')


P_new = np.divide((np.array([1 for i in range(n)]).T), n)
P_old = 0

E = np.divide(np.ones(((n, n))), n)

ε = float(input("Enter the stopping Criteria : "))
d = float(input("Enter the damping factor : "))

def checker(P_new, P_old, ε):
    P = np.abs(P_new - P_old)
    flag = True
    for i in range(len(P)):
        if P[i] > ε:
            flag = False
    return flag
count = 0
while not checker(P_new, P_old, ε):
    P_old = P_new
    P_new = np.dot(np.add(np.multiply((1 - d), E), np.multiply(d, Adjacency_Matrix.T)), P_old)
    count += 1
    print("\n\n[INFO] Ran {} iterations...\n".format(count))
    for i in range(len(P_new)):
        print("Page Rank for {}, is {}".format(titles[i], round(P_new[i], 5)))