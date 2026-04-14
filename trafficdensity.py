import pandas as pd
import matplotlib.pyplot as plt
data =[
120, 135, 150, 180, 210, 250, 300, 350, 400, 450,
500, 550, 600, 650, 700, 750, 800, 820, 850, 900,
920, 940, 960, 980, 1000, 1020,
980, 950, 920, 880, 840, 800, 760, 720, 680, 640,
600, 560, 520, 480, 440, 400, 360, 320, 280, 240,
200, 170, 150, 130, 110
]
df = pd.DataFrame(data, columns=["Traffic Density"])

# Add time (seconds)
df["Time"] = range(0, len(df))

# Plot
plt.figure()
plt.plot(df["Time"], df["Traffic Density"])

plt.title("Traffic Density Variation Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Traffic Density (0–1023)")

plt.grid()
plt.show()