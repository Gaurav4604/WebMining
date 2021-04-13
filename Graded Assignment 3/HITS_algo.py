import numpy as np

print("Input the names of all the nodes : ")
titles = [input("enter name {} : ".format(i + 1)) for i in range(int(input("no. of nodes : ")))]
n = len(titles)
graph_dict = {}
for i in titles:
    graph_dict[i] = list(map(int, input("outlinks from {} : ".format(i)).split()))

graph = np.array([graph_dict[i] for i in graph_dict]) #also the adjacency matrix

a_new = h_new = np.array([1 for i in range(n)], dtype="float")

def hub_checker(h_new, h_old, eps_hub):
    h = np.abs(h_new - h_old)
    # print(h, h_old, h_new)
    for i in h:
        if i > eps_hub:
            return False
    return True

def auth_checker(a_new, a_old, eps_auth):
    a = np.abs(a_new - a_old)
    for i in a:
        if i > eps_auth:
            return False
    return True

a_old = h_old = 0

eps_hub = float(input("Enter the stopping criteria for Hub : "))
eps_auth = float(input("Enter the stopping criteria for Authority : "))

count = 0

while not (hub_checker(h_new, h_old, eps_hub) and auth_checker(a_new, a_old, eps_auth)):
    h_old = h_new
    a_old = a_new

    a_new = np.dot(np.dot(graph.T, graph), a_old)
    h_new = np.dot(np.dot(graph, graph.T), h_old)

    a_new /= np.sum(a_new)
    h_new /= np.sum(h_new)
    count += 1
    
    print("\n[INFO] Ran {} iterations...\n".format(count))
    for i in range(len(titles)):
        print("Name -> {}, Auth rank -> {}, Hub rak -> {}".format(titles[i], round(a_new[i], 5), round(h_new[i], 5)))

