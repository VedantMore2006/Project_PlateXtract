import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.get_dataset_names()
try:
    print(sns.get_dataset_names())
except Exception as e:
    print("Error fetching datasets:", e)
peng = sns.load_dataset("penguins")
print(peng.head(5))
sns.set_style("whitegrid")
sns.set_context("poster")
sns.scatterplot(
    data=peng, x="flipper_length_mm", y="body_mass_g", hue="sex", palette="Dark2"
)

plt.show()
plt.savefig("penguins_scatterplot.png")

