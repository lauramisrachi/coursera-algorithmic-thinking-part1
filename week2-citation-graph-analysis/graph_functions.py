""" Script for the Project # 1 : Degree Distributions for Graph for the Coursera
course Algorithmic Thinking (part1) """

from collections import defaultdict
import numpy as np

# Graph constants
EX_GRAPH0 = {0: {1, 2},
             1: {},
             2: {}}

EX_GRAPH1 = {0: {1, 4, 5},
             1: {2, 6},
             2: {3},
             3: {0},
             4: {1},
             5: {2},
             6: {}}

EX_GRAPH2 = {0: {1, 4, 5},
             1: {2, 6},
             2: {3, 7},
             3: {7},
             4: {1},
             5: {2},
             6: {},
             7: {3},
             8: {1, 2},
             9: {0, 3, 4, 5, 6, 7}}


def make_complete_graph(num_nodes):
    """ Build a complete graph and returns it as an adjacency dictionnary
    representation. A complete graph contains all possible edges subject
    to the restriction that self-loops are not allowed.

    Arguments:
        num_nodes (int): number of nodes in the directed graph.

    Returns:
        graph_dict (dict): graph dictionnary with the following shape
        {'node_idx': adjacency_set,  ... }
    """

    graph_dict = defaultdict(set)
    all_nodes = set(range(num_nodes))

    if num_nodes > 0:
        for node_index in range(num_nodes):
            graph_dict[node_index] = all_nodes - {node_index}

    return dict(graph_dict)


def compute_in_degrees(digraph):
    """ Computes the in-degrees for the nodes in a directed graph.

    Arguments::
        digraph (dict): graph dictionnary with the following shape
        {'node_idx': adjacency_set,  ... }

    Returns:
        in_degree_dict (dict): dict with the graph nodes as keys
        and their corresponding in-degrees as values.
    """

    in_degree_dict = defaultdict(int)
    for _, values in digraph.items():
        for node in values:
            in_degree_dict[node] += 1

    return dict(in_degree_dict)


def compute_out_degrees(digraph):
    """ Compute the out-degrees for the nodes in a directed graph.

    Arguments:
        digraph (dict): graph dictionnary with the following shape
        {'node_idx': adjacency_set, ... }

    Returns:
        dict with the graph nodes as keys and their corresponding
         out-degrees as values.
    """

    return {node: len(values) for node, values in digraph.items()}


def compute_average_out_degree(digraph):
    """ Compute the average out degree of a directed graph. """

    out_degrees = compute_out_degrees(digraph)

    return int(np.mean(list(out_degrees.values())))


def in_degree_distribution(digraph):
    """ Computes the unnormalized distribution of the in-degrees of the
    provided graph digraph.

    Arguments:
        digraph (dict): graph dictionnary with the following shape
        {'node_idx': adjacency_set,  ... }

    Returns:
        in_degree_distribution (dict): dictionnary with the graph
        in-degrees values as keys and their unnormalized occurences
        as values.
    """

    in_degree_distribution_dict = defaultdict(int)
    in_degree_dict = compute_in_degrees(digraph)

    for _, value in in_degree_dict.items():
        in_degree_distribution_dict[value] += 1

    return dict(in_degree_distribution_dict)
