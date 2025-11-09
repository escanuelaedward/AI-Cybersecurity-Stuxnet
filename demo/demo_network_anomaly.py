# demo/demo_network_anomaly.py
# This code is to simulate normal network activity and plot it

import numpy as np #imports the NumPy library and gives it the nickname "np"
import matplotlib.pyplot as plt # imports the plotting utilities from Matplotlib and names them "plt"

# we create repeatable random numbers
np.random.seed(42)

# next is our parameters
# loc=100 -> center (mean) of distribution (value around 100)
# scale=5 -> standard deviation (how much values typically vary)
# size=200 -> how many samples to generate
# This will simulate 200 consecutive measurements of a sensor or network traffic that normally fluctuates around 100
normal = np.random.normal(loc=100, scale=5, size=200)

# now we're implementing our attack data
attack=np.random.normal(loc=150, scale=10, size=10)

# stitch the normal + attack into one series
data = np.concatenate([normal[:100], attack, normal[100:]])

# IsolationForest - unsupervised anomaly detector
from sklearn.ensemble import IsolationForest

# prepare data for scikit-learn
X = data.reshape(-1, 1)

# create the model
# contamination - fraction of samples the model should consider anomalous
model = IsolationForest(contamination=0.05, random_state=42)

# train the model on the series (unsupervised)
model.fit(X)

# get predictions: 1 => norma, -1 => anomaly
preds = model.predict(X)

# get indices flagged as anomalies
import numpy as np
anomaly_idx = np.where(preds == -1)[0]

# console feedback
print(f"IsolationForest flagged {len(anomaly_idx)} points as anomalies")

# now we plot the data
plt.figure(figsize=(10,4)) #starts a new plot with the dimensions of 10x4 inches
plt.plot(data, label="Traffic (with injected attack)", color="tab:blue")

#draw red dots where the model flags anomalies
if len(anomaly_idx):
    plt.scatter(
        anomaly_idx,                # x positions
        data[anomaly_idx],          # y values at those indices
        color="red", 
        s=40,
        label="AI-flagged anomalies",
        zorder=3                    # draws on top of the blue line
    )

# highlight where we inserted the attack so we can see it
attack_start = 100
attack_end = attack_start + len(attack)
plt.axvspan(attack_start, attack_end, color="orange", alpha=0.2, label="Injected attack window") # draws a rectangle around the attack

plt.title("Network Traffic with Injected Attack (visualized)")
plt.xlabel("Time(index)")
plt.ylabel("Traffic Intensity")
plt.legend()
plt.tight_layout()

# ensures the assets folder exists (fixing FileNotFoundError on save)
from pathlib import Path
Path("../assets").mkdir(parents=True, exist_ok=True)

# save the image and open
plt.savefig("../assets/step6_ai_detects.png") # saves image to assets folder
plt.show()