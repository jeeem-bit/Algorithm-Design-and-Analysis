import random

def generate_list(nodes, edges):
    edges_generated = 0
    MAXWEIGHT = 10

    list = [[] for i in range(nodes)]

    while edges_generated != edges:
        random_x = random.randint(0, nodes-1)
        random_y = random.randint(0, nodes-1)
        if random_x == random_y:
            continue
        elif isConnected(random_x, random_y, list) == 1:
            continue
        else:
            random_weight = random.randint(1, MAXWEIGHT)
            list[random_x].append((random_y, random_weight))
            list[random_y].append((random_x, random_weight))
            edges_generated += 1

    for i in list:
        print(i)

def isConnected(node1, node2, list):
    for vertex, edge_weight in list[node1]:
        if vertex == node2:
            return 1
    return 0

generate_list(10,10)
