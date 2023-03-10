import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import sample

#Basic Example
x = np.linspace(0, 5, 11)
y = x ** 2

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r--')  # More on color options later
plt.subplot(1, 2, 2)
plt.plot(y, x, 'g*-')
plt.show()


fig = plt.figure(2)

# Add set of axes to figure
# left, bottom, width, height (range 0 to 1)
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Plot on that set of axes
axes.plot(x, y, 'b')
axes.set_xlabel('Set x Label')  # Notice the use of set_ to begin methods
axes.set_ylabel('Set y Label')
axes.set_title('Set Title')
plt.show()

# Creates blank canvas
fig = plt.figure(3)

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # inset axes

# Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')

# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title')
plt.show()
fig.savefig("filename.png", dpi=200)
fig.savefig("filenome.png", dpi=100)
fig.savefig("filename.pdf", dpi=200)
fig.savefig("fil.jpg", dpi=200)
fig.savefig("file.eps", dpi=200)
fig.savefig("filen.svg", dpi=200)
fig.savefig("filena.pgf", dpi=200)

fig = plt.figure(4)

ax = fig.add_axes([0.1,0.1,0.8,0.8])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend(loc=2)
plt.show()

#Setting colors, linewidths, linetypes
# MATLAB style line color and style
fig, ax = plt.subplots()
ax.plot(x, x**2, 'b.-')  # blue line with dots
ax.plot(x, x**3, 'g--')  # green dashed line
plt.show()

fig, ax = plt.subplots()

ax.plot(x, x+1, color="blue", alpha=0.5)  # half-transparant
ax.plot(x, x+2, color="#8B008B")        # RGB hex code
ax.plot(x, x+3, color="#FF8C00")        # RGB hex code
plt.show()

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# custom dash
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10])  # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x + 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# marker size and color
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-',
        marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")
plt.show()

#Plot range
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range")
plt.show()

#Special Plot Types
plt.scatter(x,y)
plt.show()

data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show()

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# rectangular box plot
plt.boxplot(data,vert=True,patch_artist=True)
plt.grid()
plt.show()
