import random
import math
import time

class Heap:
    def __init__(self, size):
        self.size = size
        self.numElements = 0
        self.array = [HeapNode(-1, math.inf) for i in range(self.size)]

    def leftChild(self, index):
        return 2 * index

    def rightChild(self, index):
        return 2 * index + 1

    def isLeaf(self, index):
        return 2 * index > self.size

    def parent(self, index):
        if index == 1:
            return 1
        return math.floor(index / 2)

    def enqueue(self, node, distance):
        self.array[self.numElements].value = self.array[0].value
        self.array[self.numElements].distance = self.array[0].distance
        self.array[0].value = node
        self.array[0].distance = distance
        self.numElements += 1
        self.minHeapify(self.parent(self.numElements), True)

    def remove_node(self, node):
        nodeIndex = self.findNode(node)
        # switch last and element to delete
        self.array[nodeIndex].value = self.array[self.numElements-1].value
        self.array[nodeIndex].distance = self.array[self.numElements-1].distance
        self.array[self.numElements-1].value = -1
        self.array[self.numElements-1].distance = math.inf
        # heapify from position of element deleted
        self.numElements -= 1
        self.minHeapify(nodeIndex + 1, True)

    def dequeue(self):
        minValue = self.array[0].value
        self.array[0].value = self.array[self.numElements-1].value
        self.array[0].distance = self.array[self.numElements-1].distance
        self.array[self.numElements-1].value = -1
        self.array[self.numElements-1].distance = math.inf
        self.numElements -= 1
        self.minHeapify(1, False)
        return minValue

    def findNode(self, node):
        for i in range(self.numElements):
            if self.array[i].value == node:
                return i

        return -1

    def isEmpty(self):
        return self.numElements == 0

    def minHeapify(self, root, bottomUp):
        left = self.leftChild(root)
        right = self.rightChild(root)

        smallest = root

        if left <= self.numElements and self.array[left - 1].distance < self.array[smallest - 1].distance:
            smallest = left

        if right <= self.numElements and self.array[right - 1].distance < self.array[smallest - 1].distance:
            smallest = right

        if smallest != root:
            self.array[smallest - 1].value, self.array[root - 1].value = self.array[root - 1].value, self.array[
                smallest - 1].value
            self.array[smallest - 1].distance, self.array[root - 1].distance = self.array[root - 1].distance, \
            self.array[smallest - 1].distance
            if bottomUp:
                self.minHeapify(self.parent(root), True)
            else:
                self.minHeapify(smallest, False)

class HeapNode:
    def __init__(self, value, distance):
        self.value = value
        self.distance = distance
    
def dijkstra(adjacency_list, source):
    num_vertices = len(adjacency_list)

    # Initialize the priority queue (min-heap)
    heap = Heap(num_vertices)

    # Initialize lists to store distances and previous vertices
    distances = [math.inf] * num_vertices
    previous_vertices = [None] * num_vertices

    # Set the distance for the source vertex to 0 and enqueue it
    distances[source] = 0
    heap.enqueue(source, 0)

    time_start = time.time_ns()
    while not heap.isEmpty():
        # Dequeue the vertex with the minimum distance
        current_vertex = heap.dequeue()

        # Explore neighbors of the current vertex
        for neighbor, weight in adjacency_list[current_vertex]:
            distance = distances[current_vertex] + weight

            # If a shorter path to the neighbor is found, update the distance and previous vertex
            if distance < distances[neighbor]
                previous_vertices[neighbor] = current_vertex
                heap.enqueue(neighbor, distance)

    time_end = time.time_ns()
    time_taken = time_end - time_start
    print(f"Time Taken: {time_taken}")
    return distances, previous_vertices

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
        
def isConnected(node1, node2, list):
    for vertex, edge_weight in list[node1]:
        if vertex == node2:
            return 1
    return 0

def cal_max_edges(nodes):
    return math.floor(((nodes - 2)*(nodes + 1)) / 2) 

if __name__ == "__main__":
    print("Testing List/Heap")
    num_nodes = [1000, 10000, 100000]
    for num_node in num_nodes:
        edges = cal_max_edges(num_node)
        adjacency_list = generate_list(num_node, num_node - 1)
        source_vertex = 0
        print(f"Nodes: {num_node}, Edges: {num_node-1}")
        distances, previous_vertices = dijkstra(adjacency_list, source_vertex)
