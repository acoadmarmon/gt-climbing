import numpy as np
import networkx as nx
from copy import copy

def get_possible_holds(climbing_face, current_configuration):
    possible_configurations = []
    for i in range(len(current_configuration)):
        for j in range(len(climbing_face)):
            current_point = current_configuration[i]
            new_hold = climbing_face[j]

            dist = np.linalg.norm(np.asarray(current_point) - np.asarray(new_hold))
            body_com = np.mean(np.asarray(current_configuration), axis=0)
            dist_from_body = np.linalg.norm(np.asarray(body_com) - np.asarray(new_hold))
            #Later we need to change the dist here to real dynamic constraint
            if dist <= 1.0 and tuple(new_hold) not in [tuple(k) for k in current_configuration]:
                possible_configurations.append((current_point, new_hold))
    return possible_configurations

def shortest_path(climbing_face, initial_holds=[(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0)], goal_hold=(0.0, 0.0, 0.0)):
    current_configuration = initial_holds
    G = nx.Graph()
    G.add_nodes_from(initial_holds)
    ucs(G, climbing_face, initial_holds, goal_hold)
    return min(list(nx.all_simple_paths(G, source=initial_holds[0], target=goal_hold)) + list(nx.all_simple_paths(G, source=initial_holds[1], target=goal_hold)) + 
           list(nx.all_simple_paths(G, source=initial_holds[2], target=goal_hold)) + list(nx.all_simple_paths(G, source=initial_holds[3], target=goal_hold)), key=len)

def ucs(G, climbing_face, initial_holds=[(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0)], goal_hold=(0.0, 0.0, 0.0)):
    if goal_hold in initial_holds:
        return

    possible_configurations = get_possible_holds(climbing_face, initial_holds)
    new_nodes = [i[1] for i in possible_configurations if not G.has_node(i[1])]
    if len(new_nodes) == 0:
        return

    new_edges = [i for i in possible_configurations if not G.has_node(i[1])]
    G.add_nodes_from(new_nodes)
    G.add_edges_from(new_edges)
    for i in new_edges:
        updated_initial_holds = copy(initial_holds)
        updated_initial_holds[updated_initial_holds.index(i[0])] = i[1]
        ucs(G, climbing_face, updated_initial_holds, goal_hold)