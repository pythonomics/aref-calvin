# import librairies
import numpy as np
import matplotlib.pyplot as plt

# Choose the height of the bars
height = [3, 12 ,5 ,18, 45]

# Bar lables
bars = ('group1', 'group2', 'group3', 'group4', 'group5')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create axis labels
plt.xticks(y_pos, bars, color='orange')
plt.yticks(color='orange')

plt.show() 
