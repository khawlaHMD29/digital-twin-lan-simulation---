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
    orcid: 0009-0002-1350-0912
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

As computer networks become increasingly complex, traditional rule-based monitoring approaches are often inadequate for capturing subtle fault dynamics such as jitter and packet loss. This creates a clear need for reproducible and extensible tools that integrate data-driven methods into fault detection.  

`digital-twin-lan-simulation` addresses this challenge by combining digital twin modeling with machine learning classification, providing a unified framework for exploring hybrid fault detection strategies. The software is designed for researchers, educators, and practitioners interested in intelligent fault detection, network reliability analysis, and simulation-driven experimentation.  

Beyond a proof-of-concept, this framework is conceived as a **modular and extensible platform**. Users can incorporate new machine learning models, simulate alternative network topologies, or extend monitoring metrics, making it suitable for both scientific research and educational use.  

The project offers the following scope:

- **Inputs:** LAN topology parameters, node-level metrics (delay, jitter, packet loss).  
- **Outputs:** fault classifications (Latency Spike, Jitter, Packet Loss, No Fault) and comparative analyses of rule-based vs. ML-based detection.  
- **Scope:** extensible framework for small-to-medium scale LANs, supporting reproducible experiments in fault detection.  
- **Integration:** modular Python codebase with a simple API for extensions and visualization tools for temporal and structural analysis.  


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
