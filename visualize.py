import matplotlib.pyplot as plt
import networkx as nx

def draw_network(G, nodes, twins):
    pos = nx.spring_layout(G)

    # Map fault types to colors
    fault_colors = {
        "Latency Spike": "red",
        "Packet Loss": "yellow",
        "Jitter": "purple",
        "No Fault": "green"
    }

    node_colors = [fault_colors.get(twins[node]["fault_type"], "gray") for node in nodes]
    node_colors.append("blue")  # Server

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=10, font_weight='bold')
    plt.title("LAN Topology with Fault Classification")
    plt.show()
