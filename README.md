# Digital Twin LAN Simulation – Intelligent Fault Detection

This project simulates a Local Area Network (LAN) using a digital twin architecture enhanced with machine learning to detect multiple fault types. It serves as a foundational step toward intelligent, data-driven fault detection in networked systems.

---

## 🧠 Project Objective

To build a modular and extensible simulation of a LAN where each physical device is mirrored by a digital twin. The system monitors delay, jitter, and packet loss, and classifies faults using both rule-based logic and a trained ML model

---

## 🧱 Architecture Overview

- LAN Topology: Star network with 5 computers connected to a central server
- Digital Twins: Each node has a virtual twin that tracks delay, jitter, and packet loss
- Fault Detector:
- Rule-Based: Flags latency spikes when delay > 10s
- ML-Based: Classifies faults as Latency Spike, Jitter, Packet Loss, or No Fault using a trained Random Forest model


---

## 🧪 Features

- Simulates realistic network metrics (delay, jitter, packet loss)
- Detects faults using both rule-based and ML-based strategies
- Logs fault history over multiple rounds for temporal analysis
- Visualizes fault types per node using color-coded graphs
- Compares detection strategies and highlights discrepancies
- Modular codebase for clarity, scalability, and research extension

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/digital-twin-lan-simulation.git
   cd digital-twin-lan-simulation

2. Install dependencies:

pip install pandas scikit-learn matplotlib networkx

3. Run the simulation:
python main.py

## 📊 Example Output

1. Fault Detector (ML-based):

Computer01 -> Delay: 13s | Jitter: 1.2 | Loss: 2% -> Fault: Latency Spike
Computer02 -> Delay: 4s  | Jitter: 4.1 | Loss: 1% -> Fault: Jitter
Computer03 -> Delay: 3s  | Jitter: 2.0 | Loss: 6% -> Fault: Packet Loss

2. Network Graph:
- 🔴 Latency Spike
- 🟡 Packet Loss
- 🟣 Jitter
- 🟢 No Fault
- 🔵 Server

## 📈 Comparative Analysis
- Agreement Rate: 46% between ML and rule-based detection
- Discrepancies: ML detects faults missed by rule-based logic
- Conclusion: ML-based classification provides richer and more accurate fault detection, especially for jitter and packet loss scenarios


