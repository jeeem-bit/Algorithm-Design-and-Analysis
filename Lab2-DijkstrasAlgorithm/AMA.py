import sys

def dijkstra(adj_matrix, source):
    num_vertices = len(adj_matrix)
    d = [float('inf')] * num_vertices
    d[source] = 0
    priority_queue = list(range(num_vertices))

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

    return d

# Test
if __name__ == "__main__":
    adjacency_matrix = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

    source_vertex = 0
    shortest_distances = dijkstra(adjacency_matrix, source_vertex)
    print("Shortest distances from source vertex:")
    for i, distance in enumerate(shortest_distances):
        print(f"Vertex {i}: {distance}")