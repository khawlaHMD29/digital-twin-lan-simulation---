import networkx as nx

def create_lan(num_nodes=5):
    G = nx.Graph()
    nodes = [f"Computer0{i+1}" for i in range(num_nodes)]
    G.add_nodes_from(nodes)
    G.add_node("Server")
    for node in nodes:
        G.add_edge(node, "Server")
    return G, nodes