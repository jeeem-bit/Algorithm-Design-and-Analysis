import math
import random
import sys
import heapq
import time


# Adjacency Matrix and Array
def dijkstra(adj_matrix, source):
    num_vertices = len(adj_matrix)
    d = [float('inf')] * num_vertices
    d[source] = 0
    priority_queue = list(range(num_vertices))

    time_start = time.time_ns()
    while priority_queue:
        # Find vertex with minimum distance in the priority queue
        min_distance_vertex = min(priority_queue, key=lambda v: d[v])
        priority_queue.remove(min_distance_vertex)

        # Update distances for neighbors
        for neighbor in range(num_vertices):
            if adj_matrix[min_distance_vertex][neighbor] != 0:
                new_distance = d[min_distance_vertex] + adj_matrix[min_distance_vertex][neighbor]
                if new_distance < d[neighbor]:
                    d[neighbor] = new_distance

    time_end = time.time_ns()
    time_taken = time_end - time_start
    print(f"Time taken: {time_taken}")
    return d


def generate_matrix(nodes, edges):
    edges_generated = 0
    MAXWEIGHT = 10

    matrix = [[0 for i in range(nodes)] for j in range(nodes)]

    while edges_generated != edges:
        random_x = random.randint(0, nodes - 1)
        random_y = random.randint(0, nodes - 1)
        if random_x == random_y:
            continue
        if matrix[random_x][random_y] >= 1 or matrix[random_y][random_x] >= 1:
            continue
        random_weight = random.randint(1, MAXWEIGHT)
        matrix[random_x][random_y] = random_weight
        matrix[random_y][random_x] = random_weight
        edges_generated += 1

    return matrix


def cal_max_edges(nodes):
    return math.floor(((nodes - 2)*(nodes + 1)) / 2)


# Test
if __name__ == "__main__":
    print("Testing Matrix/Array")
    num_nodes = [1000, 10000]
    for i in num_nodes:
        nodes = i
        max_edges = cal_max_edges(nodes)
        adjacency_matrix = generate_matrix(nodes, nodes-1)
        print(f"Nodes: {i}, Edges: {nodes-1}")
        source_vertex = 0
        shortest_distances = dijkstra(adjacency_matrix, source_vertex)





# Adjacency List and Heap
def dijkstra2(adj_list, source):
    num_vertices = len(adj_list)
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    priority_queue = [(0, source)]  # (distance, vertex)

    time_start = time.time_ns()
    while priority_queue:
        # Pop vertex with smallest distance from the min-heap
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If already processed vertex w smaller distance, skip
        if current_distance > distances[current_vertex]:
            continue

        # Update distances for neighbors
        for neighbor, edge_weight in adj_list[current_vertex]:
            new_distance = distances[current_vertex] + edge_weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # Push the updated distance and neighbor into the min-heap
                heapq.heappush(priority_queue, (new_distance, neighbor))

    time_end = time.time_ns()
    time_taken = time_end - time_start
    print(f"Time Taken: {time_taken}")
    return distances

def isConnected(node1, node2, list):
    for vertex, edge_weight in list[node1]:
        if vertex == node2:
            return 1
    return 0

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

    return list

# Test
if __name__ == "__main__":
    print("Testing List/Heap")
    num_nodes = [1000, 10000, 100000]
    for i in num_nodes:
        nodes = i
        edges = cal_max_edges(nodes)
        adjacency_list = generate_list(nodes, nodes - 1)
        print(f"Nodes: {nodes}, Edges: {nodes-1}")
        source_vertex = 0
        shortest_distances = dijkstra2(adjacency_list, source_vertex)

    #print("Shortest distances from source vertex:")
    #for i, distance in enumerate(shortest_distances):
        #print(f"Vertex {i}: {distance}")


 #print("Shortest distances from source vertex:")
    #for i, distance in enumerate(shortest_distances):
        #print(f"Vertex {i}: {distance}")