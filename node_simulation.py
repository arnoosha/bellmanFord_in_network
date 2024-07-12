from DV import DistanceVectorNode, INFINITY
import numpy as np

NUM_NODES = 4

topology = np.array([
    [0, 1, INFINITY, 7],
    [1, 0, 2, 3],
    [INFINITY, 2, 0, 3],
    [7, 3, 3, 0]
])

nodes = [DistanceVectorNode(i, NUM_NODES, topology) for i in range(NUM_NODES)]

def simulate_routing_protocol():
    for node in nodes:
        node.rtinit()

    iteration = 0
    while True:
        updated = False
        print(f"Iteration {iteration}:")

        # Sending updates
        messages = []
        for node in nodes:
            messages.extend(node.send_update())

        # Receiving updates
        for sender, receiver, vector in messages:
            print(f"Node {sender} sends distance vector to Node {receiver}: {vector}")
            if nodes[receiver].rtupdate(sender, vector):
                updated = True

        if not updated:
            break
        iteration += 1

    print("Final Distance Tables:")
    for node in nodes:
        node.print_distance_table()

simulate_routing_protocol()
