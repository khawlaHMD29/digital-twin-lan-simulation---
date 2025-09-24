import random

def generate_delays(nodes):
    return {node: random.randint(1, 15) for node in nodes}

def create_twins(delays, threshold=3):
    twins = {}
    for node, delay in delays.items():
        twins[node] = {
            "device": node,
            "delay": delay,
            "status": "Disk OK",
            "spike": "Yes" if delay > threshold else "No"
        }
    return twins