import matplotlib.pyplot as plt
import numpy as np

# Data: model names, number of vertices, and times
models = ['Iphi bad (10k)', 'Beetle', 'Cat',  'Hand']
vertices_symmetric = np.array([3487, 4498, 9578,  4310])
vertices_non_symmetric = np.array([5002, 5105, 9447, 3978])
time_symmetric = np.array([5.17379, 9.47354, 8.81313,1.4826]) # in milliseconds
time_symmetric /= 1000  # Convert to seconds
time_non_symmetric = np.array([11.8367, 12.2466, 9.06163, 2.30153])
time_non_symmetric /= 1000  # Convert to seconds

# Multiply time by corresponding vertices
total_time_symmetric = time_symmetric * vertices_symmetric
total_time_non_symmetric = time_non_symmetric * vertices_non_symmetric
avg_error_non_sym = [0.560481, 0.673274, 0.130568, 0.252965]
avg_error_sym = [0.1094, 0.166504, 0.0936139,0.115583]

# Create bar plot
x = np.arange(len(models))  # model indices
plt.rcParams.update({'font.size': 20})

# Width of the bars
bar_width = 0.35

# Plot bars for symmetric and non-symmetric
plt.bar(x - bar_width/2, total_time_symmetric, width=bar_width, color='green', label='Re-meshed')
plt.bar(x + bar_width/2, total_time_non_symmetric, width=bar_width, color='red', label='Original')

# Labels and title
plt.xlabel('Model')
plt.ylabel('Time (sec)')
plt.title('Comparison of Original and Re-meshed Laplcian Inversion Times')

# Adding model names to x-axis
plt.xticks(x, models)

# Add legend
plt.legend()
# Annotate deltas on top of the bars
for i in range(len(models)):
    plt.text(x[i] - bar_width/2, total_time_symmetric[i], f'{avg_error_sym[i]:.0%}', ha='center', va='bottom')
    plt.text(x[i] + bar_width/2, total_time_non_symmetric[i], f'{avg_error_non_sym[i]:.0%}', ha='center', va='bottom')


# Show plot
plt.tight_layout()
plt.show()