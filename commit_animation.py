import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Get commit dates from git log
log = subprocess.check_output(["git", "log", "--pretty=format:%ad", "--date=short"]).decode().splitlines()
dates = pd.to_datetime(log)
commits_per_day = dates.value_counts().sort_index()

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    ax.bar(commits_per_day.index[:frame], commits_per_day.values[:frame])
    ax.set_title("Commits Over Time")
    ax.tick_params(axis='x', rotation=45)

ani = FuncAnimation(fig, update, frames=len(commits_per_day), repeat=False)

plt.show()  # ✅ Display animation instead of saving
