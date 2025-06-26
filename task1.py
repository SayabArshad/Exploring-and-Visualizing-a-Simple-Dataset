# Task 1 : Exploring and Visualizing a Simple Dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')  # or use pd.read_csv("iris.csv")

# Inspect structure
print("Shape:", iris.shape)
print("Columns:", iris.columns)
print(iris.head())

# Scatter plot
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
plt.title("Sepal Length vs Width")
plt.show()

# Histogram
iris.hist(figsize=(10, 6))
plt.suptitle("Histograms of Iris Features")
plt.show()

# Box plot
sns.boxplot(data=iris)
plt.title("Box Plot of Iris Features")
plt.show()
