import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with multiple subplots

fig, axs = plt.subplots(2, 2, figsize=(10, 6))

# First subplot: Line plot with customization
axs[0, 0].plot(x, y1, label="Sine Wave", color="blue", linestyle="--", linewidth=2)
axs[0, 0].plot(x, y2, label="Cosine Wave", color="green", linestyle="-", linewidth=2)
axs[0, 0].set_title("Sine and Cosine Waves")
axs[0, 0].set_xlabel("X-axis")
axs[0, 0].set_ylabel("Y-axis")
axs[0, 0].legend()
axs[0, 0].grid(True)

# Second subplot: Scatter plot
scatter_x = np.random.rand(50) * 10
scatter_y = np.random.rand(50)
axs[0, 1].scatter(scatter_x, scatter_y, color="purple", marker="o")
axs[0, 1].set_title("Scatter Plot")
axs[0, 1].set_xlabel("Random X")
axs[0, 1].set_ylabel("Random Y")

# Third subplot: Bar plot
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 20]
axs[1, 0].bar(categories, values, color="orange")
axs[1, 0].set_title("Bar Chart")
axs[1, 0].set_xlabel("Categories")
axs[1, 0].set_ylabel("Values")

# Fourth subplot: Annotated plot
axs[1, 1].plot(x, y1, label="Sine Wave", color="red")
axs[1, 1].annotate('Peak', xy=(np.pi/2, 1), xytext=(2, 1.2),
                   arrowprops=dict(facecolor='black', arrowstyle="->"))
axs[1, 1].set_title("Annotated Plot")
axs[1, 1].set_xlabel("X-axis")
axs[1, 1].set_ylabel("Y-axis")

# Adjust layout
plt.tight_layout()
plt.show()