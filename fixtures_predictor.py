import pandas as pd

# Exploratory Data Analysis (EDA)
fixtures = pd.read_csv("./data/fixtures_merged_statistics_df.csv")
num_of_columns = len(fixtures.columns)
print(num_of_columns)

fixtures.describe().to_csv("./data/fixtures_description.csv")

print(fixtures.isnull().sum())  # Check for missing values

# Feature Selection and Data Preparation
fixtures = fixtures.sort_values(by='start_date', ascending=False)

# Need to extract last game stats...
# Then turn columns to numerical...
