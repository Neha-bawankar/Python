import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load a sample dataset
data = sns.load_dataset("penguins")

# Display the first few rows of the dataset
print("Dataset Preview:")

print(data.head())

# Function to create a scatter plot with regression line
def scatter_plot(data):
    plt.figure(figsize=(8, 5))
    sns.regplot(x="bill_length_mm", y="bill_depth_mm", data=data, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
    plt.title("Bill Length vs. Bill Depth with Regression Line")
    plt.show()

# Function to create a categorical boxplot
def box_plot(data):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="species", y="body_mass_g", data=data, palette="pastel")
    plt.title("Boxplot of Body Mass by Species")
    plt.show()

# Function to create a pair plot
def pair_plot(data):
    sns.pairplot(data, hue="species", palette="dark")
    plt.suptitle("Pair Plot of Penguin Data", y=1.02)
    plt.show()

# Function to create a heatmap
def heatmap(data):
    plt.figure(figsize=(8, 5))
    correlation = data.corr(numeric_only=True)
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Heatmap of Correlation Matrix")
    plt.show()

# Ask the user for the type of plot they want to create
print("Choose the type of plot to create:")
print("1. Scatter Plot with Regression Line")
print("2. Box Plot")
print("3. Pair Plot")
print("4. Heatmap")
choice = input("Enter the number corresponding to your choice: ")

# Create the chosen plot
if choice == "1":
    scatter_plot(data)
elif choice == "2":
    box_plot(data)
elif choice == "3":
    pair_plot(data)
elif choice == "4":
    heatmap(data)
else:
    print("Invalid choice. Please enter a number between 1 and 4.")