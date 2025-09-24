import random
import pandas as pd

def generate_training_data(n_samples=200):
    data = []
    for _ in range(n_samples):
        delay = random.randint(1, 15)
        jitter = random.uniform(0, 5)
        packet_loss = random.randint(0, 10)

        # Simple rule-based labeling
        if delay > 10:
            fault = "Latency Spike"
        elif jitter > 3:
            fault = "Jitter"
        elif packet_loss > 5:
            fault = "Packet Loss"
        else:
            fault = "No Fault"

        data.append({
            "delay": delay,
            "jitter": jitter,
            "packet_loss": packet_loss,
            "fault_type": fault
        })

    return pd.DataFrame(data)