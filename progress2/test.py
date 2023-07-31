import matplotlib.pyplot as plt
import numpy as np

# Define the color map
cmap = plt.cm.get_cmap('RdYlBu', 2)  # 2 colors: red and blue

# Define the matrix
matrix = [[0, 0, 1], [0, 0, 0], [1, 1, 0]]

# Create the plot
fig, ax = plt.subplots()
im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=1)

# Add color bar
cbar = ax.figure.colorbar(im, ax=ax)

# Show the plot
plt.show()