import random
from graph_functions import make_complete_graph

class DPATrial(object):
    """ Class to generate random directed graph using the DPA algorithm.

    Arguments:
        num_nodes (int): number of nodes to grow in the graph
        num_connected_nodes (int): number of connections to add at each
        node adding step
        verbose (bool): whether or not to allow verbosity
    """

    def __init__(self,
                 num_nodes,
                 num_connected_nodes,
                 verbose=1):

        self._num_nodes = num_nodes
        self._num_connected_nodes = num_connected_nodes
        self._verbose_print = print if verbose else lambda *a, **k: None

        self._complete_graph = make_complete_graph(num_connected_nodes)
        self._verbose_print("The initial complete graph with %d nodes "
                            "was grown" % num_connected_nodes)
        self._cnt_nodes = [node for node in range(self._num_connected_nodes)
                           for _ in range(self._num_connected_nodes)]

    def add_node(self, i):
        """ Add node i to the complete graph and connect it to
        num_connected_nodes randomly selected neighbors."""

        neighbors = set()
        for _ in range(self._num_connected_nodes):
            neighbors.add(random.choice(self._cnt_nodes))

        self._cnt_nodes.append(i)
        self._cnt_nodes.extend(list(neighbors))
        self._complete_graph[i] = neighbors

    def grow_graph(self):
        """ Grow the full directed graph. """

        for i in range(self._num_connected_nodes, self._num_nodes):
            self.add_node(i)

        return self._complete_graph
