import numpy as np

INFINITY = float('inf')

class DistanceVectorNode:
    def __init__(self, node_id, num_nodes, topology):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.topology = topology
        self.distance_table = np.full((num_nodes, num_nodes), INFINITY) #First mark all as infinity

        self.distance_table[node_id, :] = topology[node_id, :] #then mark those who are adjacent
                                                               # with their own distance
        self.distance_table[:, node_id] = topology[:, node_id]

        self.neighbors = [i for i in range(num_nodes) if topology[node_id, i] < INFINITY and i != node_id]

    def rtinit(self):
        print(f"Node {self.node_id} initialization:")
        self.print_distance_table()
        print()

    def rtupdate(self, received_node, received_vector):
        updated = False
        for i in range(self.num_nodes):
            new_distance = self.topology[self.node_id, received_node] + received_vector[i]
            if new_distance < self.distance_table[self.node_id, i]:
                self.distance_table[self.node_id, i] = new_distance
                updated = True
        if updated:
            print(f"Node {self.node_id} updated distance table from Node {received_node}:")
            self.print_distance_table()
            print()
        return updated

    def print_distance_table(self):
        print(f"Distance table for Node {self.node_id}:")
        print(self.distance_table[self.node_id])

    def send_update(self):
        messages = []
        for neighbor in self.neighbors:
            messages.append((self.node_id, neighbor, self.distance_table[self.node_id].copy()))
        return messages
