""" Script for the citation graph analysis of scientific papers. This project is part of the
Algorithmic Thinking (part 1) course of Coursera.
Author: Laura Misrachi
"""
import logging
import os
import time

import matplotlib.pyplot as plt

from collections import defaultdict
from datetime import timedelta
from urllib.request import urlopen

from dpa import DPATrial
from graph_functions import in_degree_distribution, compute_average_out_degree

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"
RESULT_FOLDER = os.path.join(os.getcwd(), "results")


def create_result_folder():
    """ Create the results folder. """
    if not os.path.exists(RESULT_FOLDER):
        os.mkdir(RESULT_FOLDER)


def parse_url(url):
    """ Parse the .txt URL and generate the related graph dictionnary.

    Arguments:
        url (str): path to the .txt URL

    Returns:
        graph_dict (dict): citation graph dictionnary with the following shape
        {'node': set_of_neighbours, ... }
    """

    data = urlopen(url)
    graph = data.readlines()
    logging.info('Loading graph with %d nodes' % len(graph))
    graph_dict = defaultdict(set)

    for file in graph:
        decoded_string = file.decode().split('\r\n')[0].split(' ')
        node = int(decoded_string[0])

        for i in range(1, len(decoded_string) - 1):
            if decoded_string[i]:
                graph_dict[node].add(int(decoded_string[i]))
            else:
                graph_dict[node] = {}

    return dict(graph_dict)


def plot_in_degree_normalized_distribution(graph_dict, save=True, filename=None):
    """ Plot the in degree normalized distribution for a given graph described
    by its neighbours."""

    if save and not filename:
        raise ValueError("A filename should be provided when 'save' is set to True")

    in_degree_distribution_dict = in_degree_distribution(graph_dict)
    norm_in_degree_distribution_dict = {k : v/sum(list(in_degree_distribution_dict.values()))
                                        for k, v in in_degree_distribution_dict.items()}

    plt.figure()
    plt.loglog(list(norm_in_degree_distribution_dict.keys()),
               list(norm_in_degree_distribution_dict.values()), "o")
    plt.xlabel("in-degree")
    plt.ylabel("fraction of nodes")
    plt.title("In-degree distribution of the citation graph")

    if save:
        plt.savefig(os.path.join(RESULT_FOLDER, filename))
    else:
        plt.show()


def run_dpa(num_nodes, num_connected_nodes):
    """ Run the DPA algorithm and return the grown directed graph. """

    dpa_trial = DPATrial(num_nodes, num_connected_nodes)
    graph_dict = dpa_trial.grow_graph()

    return graph_dict


def run_assignment():
    """ Run the assignment by answering all the provided questions."""

    create_result_folder()
    print("The results folder was created.")

    start = time.time()
    citation_graph = parse_url(CITATION_URL)
    print("Time elapsed to read url and construct graph: %f" %
          timedelta(seconds=time.time() - start).total_seconds())

    filename = "citation_graph_in_degree_distribution.png"
    plot_in_degree_normalized_distribution(citation_graph, save=True,
                                           filename=filename)
    print("In-degree distribution for the citation graph saved")

    avg_out_degree = compute_average_out_degree(citation_graph)
    print("Average out degree of the citation graph: %d" % avg_out_degree)

    start = time.time()
    num_nodes = len(citation_graph)
    num_connected_nodes = avg_out_degree
    dpa_graph = run_dpa(num_nodes, num_connected_nodes)
    print("Time elapsed to construct graph with DPA algorithm: %f" %
          timedelta(seconds=time.time() - start).total_seconds())

    filename = "dpa_graph_in_degree_distribution.png"
    plot_in_degree_normalized_distribution(dpa_graph, save=True,
                                           filename=filename)
    print("In-degree distribution for the dpa graph was saved.")


if __name__ == '__main__':
    run_assignment()
