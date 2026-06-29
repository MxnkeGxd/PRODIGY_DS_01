import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_282912.csv",
    skiprows=4
)

# Get 2024 population data
population = df["2024"].dropna()

# Create histogram
plt.figure(figsize=(12,6))

sns.histplot(
    population,
    bins=30,
    log_scale=True
)

plt.title("Distribution of Population Across Countries (2024)")

plt.xlabel("Population (Log Scale)")

plt.ylabel("Number of Countries")

plt.tight_layout()

plt.savefig("population_histogram.png")

plt.show()