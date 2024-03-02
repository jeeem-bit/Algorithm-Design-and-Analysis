import math
import random

WEIGHTRANGE = 100


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.list = [AdjacencyList() for i in range(nodes)]
        self.generate()

    def connect(self, node1, node2, weight):
        self.list[node1].addNode(node2, weight)

    def generate(self):
        edgesToGen = self.edges
        while edgesToGen > 0:
            random1 = random.randint(0, self.nodes - 1)
            random2 = random.randint(0, self.nodes - 1)
            if random1 == random2:
                continue
            elif self.list[random1].findNode(random2) == 1:
                continue

            self.list[random1].addNode(random2, random.randint(1, WEIGHTRANGE))
            self.list[random2].addNode(random1, random.randint(1, WEIGHTRANGE))
            edgesToGen -= 1

    def printGraph(self):
        for i in range(self.nodes):
            print("Node ", i, " list: ", end="")
            self.list[i].printList()


class AdjacencyList:
    def __init__(self):
        self.size = 0
        self.head = None

    def addNode(self, value, weight):
        current = self.head
        if current == None:
            self.head = ListNode(value, weight)
            self.size += 1
            return

        while current != None:
            if current.next == None:
                break
            current = current.next

        current.next = ListNode(value, weight)
        self.size += 1

    def removeNode(self, value):
        current = self.head
        previous = None
        if current.value == value:
            self.head = current.next
            current.next = None
            self.size -= 1
            return 1

        while current != None:
            if current.value == value:
                previous.next = current.next
                current.next = None
                self.size -= 1
                return 1
            previous = current
            current = current.next

        return 0

    def findNode(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return 1
            current = current.next

        return 0

    def printList(self):
        current = self.head
        if self.head == None:
            print("Empty List")
            return

        while current != None:
            print(current.value, "(", current.weight, ") ->", end=" ")
            current = current.next

        print()


class ListNode:
    def __init__(self, value, weight):
        self.value = value
        self.next = None
        self.weight = weight


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


def Dijkstra2(graph, source):
    dToSource = [math.inf for i in range(graph.nodes)]
    predecessors = [-1 for i in range(graph.nodes)]
    inTree = [0 for i in range(graph.nodes)]
    H = Heap(graph.nodes)

    dToSource[source] = 0
    predecessors[source] = source
    for i in range(graph.nodes):
        H.enqueue(i, dToSource[i]) 

    while not H.isEmpty():
        current = H.dequeue()
        inTree[current] = 1
        adjacentNode = graph.list[current].head
        while adjacentNode != None:
            if inTree[adjacentNode.value] != 1 and dToSource[adjacentNode.value] > dToSource[current] + adjacentNode.weight:
                H.remove_node(adjacentNode.value)
                dToSource[adjacentNode.value] = dToSource[current] + adjacentNode.weight
                predecessors[adjacentNode.value] = current
                H.enqueue(adjacentNode.value, dToSource[adjacentNode.value])
            adjacentNode = adjacentNode.next


    print("Shortest cost to each node is:")
    for i in range(graph.nodes):
        print("Node: ", i, " Parent: ", predecessors[i], " Cost: ", dToSource[i])


G = Graph(10, 10)
G.printGraph()

Dijkstra2(G, 0)
