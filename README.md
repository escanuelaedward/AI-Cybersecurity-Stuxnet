# AI in Cybersecurity: Detecting Anomalies like Stuxnet

This project demonstrates how Artificial Intelligence (AI) can detect unusual patterns in network activity, similar to how modern cybersecurity systems might spot threats like the Stuxnet Worm before they cause damage.

---

## Overview

The demo simulates network traffic using Python and applies an AI model called an Isolation Forest to automatically detect suspicious behavior.

**Core idea:**  
AI learns what "normal" behavior looks like and flags activity that doesn’t fit the pattern—just like how anomaly detection systems help identify potential cyberattacks.

---

## How It Works

1. **Normal Activity Simulation:**  
   Generates typical network data centered around normal traffic values.

2. **Attack Injection:**  
   Introduces a short burst of abnormal traffic to mimic a Stuxnet-like anomaly.

3. **AI Detection (Isolation Forest):**  
   The model learns the normal pattern and highlights the anomalies automatically.

4. **Visualization:**  
   A Matplotlib plot shows:  
   - Blue line = normal network activity  
   - Orange area = simulated attack window  
   - Red dots = AI-flagged anomalies  

---

## Example Output

![AI Detection Demo](assets/step6_ai_detects.png)

---

## Tech Stack

| Component | Purpose |
|------------|----------|
| Python 3.13 | Programming language |
| NumPy | Data simulation and math |
| Matplotlib | Data visualization |
| Scikit-learn | Isolation Forest model |

---

## How to Run

### 1. Create a virtual environment
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # For Windows PowerShell
```
## Install Dependencies
python -m pip install numpy matplotlib scikit-learn

python demo/demo_network_anomaly.py
