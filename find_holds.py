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

            current_point_4x3 = np.zeros((4, 3))
            current_point_4x3[i] = current_point
            new_point_4x3 = np.zeros((4, 3))
            new_point_4x3[i] = new_hold
            new_body_com = np.mean(np.asarray(current_configuration) - current_point_4x3 + new_point_4x3, axis=0)
            is_valid_com = all([np.linalg.norm(new_body_com - current_configuration[j]) < 2.0 for j in range(len(current_configuration)) if j != i])
            
            if is_valid_com and tuple(new_hold) not in [tuple(k) for k in current_configuration]:
                possible_configurations.append((current_point, tuple(new_hold), i))
    return possible_configurations


def shortest_path(climbing_face, initial_holds=[(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0)], goal_hold=(0.0, 0.0, 0.0)):
    current_configuration = initial_holds
    G = nx.Graph()
    G.add_nodes_from(initial_holds)
    ucs(G, climbing_face, initial_holds, goal_hold)
    return G

def ucs(G, climbing_face, initial_holds=[(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0)], goal_hold=(0.0, 0.0, 0.0), max_depth=25, curr_depth=0):
    def get_4x3_of_3_vector(vec, index):
        current_point_4x3 = np.zeros((4, 3))
        current_point_4x3[index] = vec
        return current_point_4x3

    if goal_hold in initial_holds or curr_depth >= max_depth:
        return
    
    possible_configurations = get_possible_holds(climbing_face, initial_holds)
    configuration_change = [(np.asarray(initial_holds), np.asarray(initial_holds) - get_4x3_of_3_vector(i[0], i[2]) + get_4x3_of_3_vector(i[1], i[2])) for i in possible_configurations]
    new_nodes = [i[1].tostring() for i in configuration_change if not G.has_node(i[1].tostring())]
    new_possible_configurations = [possible_configurations[i] for i in range(len(possible_configurations)) if not G.has_node(configuration_change[i][1].tostring())]

    if len(new_nodes) == 0:
        return

    new_edges = [(i[0].tostring(), i[1].tostring()) for i in configuration_change if not G.has_node(i[1].tostring())]
    edge_attrs = {new_edges[i]: {'point_change': new_possible_configurations[i]} for i in range(len(new_edges))}
    G.add_nodes_from(new_nodes)
    G.add_edges_from(new_edges)
    nx.set_edge_attributes(G, edge_attrs)
    for i in configuration_change:
        updated_initial_holds = list(map(tuple, i[1]))
        ucs(G, climbing_face, updated_initial_holds, goal_hold, curr_depth=curr_depth + 1)