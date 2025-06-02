# 4.1
import pandas as pd
df = pd.read_csv('titanic.csv')
avg_survival_by_gender = df.groupby('Sex')['Survived'].mean()
print(avg_survival_by_gender)

# 4.2
filtered_df = df[(df['Sex'] == 'female') & (df['Age'] > 30) & (df['Survived'] == 1)]
print(filtered_df.head())

# 4.3
df_cleaned = df.dropna()
df_cleaned = df_cleaned.drop_duplicates()
print(f"Original shape: {df.shape}")
print(f"After cleaning: {df_cleaned.shape}")
