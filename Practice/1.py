import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Create some sample data (or load a dataset)
data = {
    'X_values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y_values': [2, 3, 5, 7, 6, 8, 9, 10, 12, 11]
}
df = pd.DataFrame(data)

# 2. Create the plot using seaborn's scatterplot function
sns.scatterplot(x='X_values', y='Y_values', data=df)

# 3. Add a title and labels (optional, but good practice)
plt.title('Simple Scatter Plot with Seaborn')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# 4. Display the plot
plt.show()
