import pandas as pd
from matplotlib import pyplot as plt

edge = 'edge.pwr'
slab = 'slab.pwr'
step_edge = 'step-edge.pwr'

# with open('slab.pwr', 'r') as file:
#     lines = [next(file) for _ in range(10)]
# headers = lines[2].strip().split()

data_edge = pd.read_table(edge, delimiter=r'\s+', header=None, skiprows=3, engine='python')
y1 = data_edge.iloc[18891:19799,27]
y1_max = y1.max()
y1 = y1/y1_max
x = data_edge.iloc[18891:19799,0]

data_slab = pd.read_table(slab, delimiter=r'\s+', header=None, skiprows=3, engine='python')
y2 = data_slab.iloc[18891:19799,27]
y2_max = y2.max()
y2 = y2/y2_max

data_step_edge = pd.read_table(step_edge, delimiter=r'\s+', header=None, skiprows=3, engine='python')
y3 = data_step_edge.iloc[18891:19799,27]
y3_max = y3.max()
y3 = y3/y3_max

# Create main figure and axis
fig, ax1 = plt.subplots(figsize=(10, 3))

# First y-axis
ax1.plot(x, y1, 'r-', label='edge')
ax1.set_xlabel('X (cm-1)')
ax1.set_ylabel('edge', color='r')
ax1.tick_params(axis='y', labelcolor='r')

# Second y-axis (twin of the first)
ax2 = ax1.twinx()
ax2.plot(x, y2, 'g-', label='slab')
ax2.set_ylabel('slab', color='g')
ax2.tick_params(axis='y', labelcolor='g')

# Third y-axis (make a twin of the first again)
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Offset the right spine of ax3
ax3.plot(x, y3, 'b-', label='step-edge')
ax3.set_ylabel('step-edge', color='b')
ax3.tick_params(axis='y', labelcolor='b')

# Titles and legends
plt.title('Multiple Y-Axes for Different Scales')
fig.tight_layout()  # Adjust layout to make room for the third y-axis

# Adding legends (combining)
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax2.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc='upper left')

plt.show()

print(y1)

# data.columns = headers
