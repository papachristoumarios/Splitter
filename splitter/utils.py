import pandas as pd
import networkx as nx
from texttable import Texttable
import collections

def tab_printer(args):
    """
    Function to print the logs in a nice tabular format.
    :param args: Parameters used for the model.
    """
    args = vars(args)
    keys = sorted(args.keys())
    t = Texttable() 
    t.add_rows([["Parameter", "Value"]] +  [[k.replace("_"," ").capitalize(),args[k]] for k in keys])
    print(t.draw())

def graph_reader(path):
    """
    Function to read the graph from the path.
    :param path: Path to the edge list.
    :return graph: NetworkX object returned.
    """
    with open(path) as f:
        lines = f.read().splitlines()

    edgelist = []
    node2idx = collections.defaultdict(lambda: -1)
    idx2node = collections.defaultdict(str)
    counter = 0
    for line in lines:
        u, v = line.split()
        if node2idx[u] == -1:
            node2idx[u] = counter
            idx2node[counter] = u
            counter += 1
        if node2idx[v] == -1:
            node2idx[v] = counter
            idx2node[counter] = u
            counter += 1
        edgelist.append((node2idx[u], node2idx[v]))
    graph = nx.from_edgelist(edgelist)
    graph.remove_edges_from(graph.selfloop_edges())
    #import pdb; pdb.set_trace()
    
    print('Graph Nodes: {}, Graph Edges: {}'.format(len(graph), len(graph.edges())))
    
    return graph, node2idx, idx2node
