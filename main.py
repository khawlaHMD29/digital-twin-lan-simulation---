from network import create_lan
from ml_model import train_fault_classifier
import random
import pandas as pd
from visualize import draw_network
from collections import defaultdict
import matplotlib.pyplot as plt

total = 0
agree = 0
disagree_log = []

# Créer le réseau
G, nodes = create_lan()

# Entraîner le modèle ML
model = train_fault_classifier()
for round_num in range(10):
    print(f"\n--- Round {round_num + 1} ---")
    for node in nodes:
        delay = random.randint(1, 15)
        jitter = round(random.uniform(0, 5), 2)
        packet_loss = random.randint(0, 10)

        sample = pd.DataFrame([{
            "delay": delay,
            "jitter": jitter,
            "packet_loss": packet_loss
        }])
        ml_fault = model.predict(sample)[0]
        rule_fault = "Latency Spike" if delay > 10 else "No Fault"

        total += 1
        if ml_fault == rule_fault:
            agree += 1
        else:
            disagree_log.append({
                "node": node,
                "delay": delay,
                "jitter": jitter,
                "packet_loss": packet_loss,
                "ml_fault": ml_fault,
                "rule_fault": rule_fault
            })

        print(f"{node} -> Delay: {delay}s | Rule: {rule_fault} | ML: {ml_fault}")
# Simuler les métriques réseau pour chaque nœud
twins = {}
for node in nodes:
    delay = random.randint(1, 15)
    jitter = round(random.uniform(0, 5), 2)
    packet_loss = random.randint(0, 10)

    # Prédire le type de faute
    sample = pd.DataFrame([{
        "delay": delay,
        "jitter": jitter,
        "packet_loss": packet_loss
    }])
    fault_type = model.predict(sample)[0]

    # Créer le jumeau numérique enrichi
    twins[node] = {
        "device": node,
        "delay": delay,
        "jitter": jitter,
        "packet_loss": packet_loss,
        "fault_type": fault_type
    }

# Afficher les résultats
print("\nFault Detector (ML-based):")
for twin in twins.values():
    print(f"{twin['device']} -> Delay: {twin['delay']}s | Jitter: {twin['jitter']} | Loss: {twin['packet_loss']}% -> Fault: {twin['fault_type']}")

# visualisation
draw_network(G, nodes, twins)

fault_history = defaultdict(list)

for round_num in range(10):
    print(f"\n--- Round {round_num + 1} ---")
    for node in nodes:
        delay = random.randint(1, 15)
        jitter = round(random.uniform(0, 5), 2)
        packet_loss = random.randint(0, 10)

        sample = pd.DataFrame([{
            "delay": delay,
            "jitter": jitter,
            "packet_loss": packet_loss
        }])
        fault_type = model.predict(sample)[0]
        fault_history[node].append(fault_type)
        print(f"{node} -> Fault: {fault_type}")
        
# Résumé final de la comparaison
print(f"\nAgreement Rate: {agree}/{total} = {round(agree / total * 100, 2)}%")

if disagree_log:
    print("\nWARNING: Discrepancies:")
    for entry in disagree_log:
        print(f"{entry['node']} -> Delay: {entry['delay']}s | Jitter: {entry['jitter']} | Loss: {entry['packet_loss']}% | Rule: {entry['rule_fault']} | ML: {entry['ml_fault']}")
        
def plot_fault_frequency(fault_history):
    fault_counts = defaultdict(lambda: defaultdict(int))
    for node, faults in fault_history.items():
        for fault in faults:
            fault_counts[node][fault] += 1

    for node, counts in fault_counts.items():
        plt.figure()
        color_map = {
        "Latency Spike": "red",
        "Packet Loss": "yellow",
        "Jitter": "purple",
        "No Fault": "green"
        }
        colors = [color_map.get(fault, "gray") for fault in counts.keys()]
        plt.bar(counts.keys(), counts.values(), color=colors)
        plt.title(f"Fault Frequency for {node}")
        plt.xlabel("Fault Type")
        plt.ylabel("Occurrences")
        plt.show()

plot_fault_frequency(fault_history)
