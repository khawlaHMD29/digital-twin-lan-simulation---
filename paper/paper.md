---
title: 'Digital Twin LAN Simulation – Intelligent Fault Detection'
tags:
  - python
  - digital twin
  - networking
  - fault detection
  - machine learning
authors:
  - name: Khawla Hammouda
    affiliation: 1
affiliations:
 - name: Independent Researcher, Algeria
   index: 1
date: 24 September 2025
bibliography: paper.bib
---

# Summary

`digital-twin-lan-simulation` is an open-source Python project that simulates a Local Area Network (LAN) using a digital twin architecture enhanced with machine learning. Each physical device is mirrored by a digital twin that tracks delay, jitter, and packet loss. Fault detection is performed with both rule-based logic and a trained Random Forest classifier. The framework enables comparative analysis of detection strategies and provides visualizations of network health, supporting reproducible research and education in intelligent network monitoring.

# Statement of need

As modern networks grow in complexity, traditional rule-based monitoring is often insufficient to capture subtle fault dynamics such as jitter and packet loss. There is a need for reproducible, extensible tools that integrate data-driven approaches into fault detection. `digital-twin-lan-simulation` fills this gap by combining digital twin modeling with machine learning classification, offering a platform for exploring hybrid detection strategies. The software is intended for researchers, educators, and practitioners interested in intelligent fault detection, network reliability analysis, and simulation-driven experimentation.

`digital-twin-lan-simulation` provides the following scope:

- **Inputs:** LAN topology parameters, node metrics (delay, jitter, loss).
- **Outputs:** fault classifications (Latency Spike, Jitter, Packet Loss, No Fault), comparative reports of rule-based vs. ML-based detection.
- **Scope:** extensible framework for small-to-medium scale LANs, reproducible experiments in fault detection.
- **Integration:** modular Python codebase, simple API for extensions, visualization tools for temporal and structural analysis.

# Functionality

The simulator models a star network topology with a central server and five computers. Each node has a virtual twin that records metrics and feeds into fault detection modules. Detection is performed using:

- **Rule-based logic:** latency spike detection when delay > 10s.  
- **Machine learning model:** Random Forest classifier trained to distinguish Latency Spike, Jitter, Packet Loss, and No Fault.  

Results are logged and visualized with color-coded graphs, allowing users to observe discrepancies between detection strategies.

## Minimal example

```bash
git clone https://github.com/your-username/digital-twin-lan-simulation.git
cd digital-twin-lan-simulation
pip install -r requirements.txt
python main.py
```

Example output:
```
Computer01 -> Delay: 13s | Jitter: 1.2 | Loss: 2% -> Fault: Latency Spike
Computer02 -> Delay: 4s | Jitter: 4.1 | Loss: 1% -> Fault: Jitter
```

# Acknowledgements

This project was developed independently by the author. The software makes use of open-source libraries including pandas, scikit-learn, matplotlib, and networkx.

# References
