import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

df = df.drop_duplicates()
df = df.dropna(subset=['age', 'embarked', 'embark_town', 'fare', 'deck'])

df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])

print("Dataset shape:", df.shape)
print("Column info:")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

print("\nAverage survival rate by gender:")
print(df.groupby('sex')['survived'].mean())

print("\nSurvival rate by class:")
print(df.groupby('pclass')['survived'].mean())

print("\nAverage fare by class:")
print(df.groupby('pclass')['fare'].mean())

print("\nSurvival rate by embarkation town:")
print(df.groupby('embark_town')['survived'].mean())

print("\nAverage age by survival status:")
print(df.groupby('survived')['age'].mean())

sns.countplot(data=df, x='sex', hue='survived')
plt.title('Survival Count by Gender')
plt.show()

sns.boxplot(data=df, x='pclass', y='fare')
plt.title('Fare Distribution by Class')
plt.show()

sns.histplot(data=df, x='age', hue='survived', kde=True, bins=30)
plt.title('Age Distribution by Survival Status')
plt.show()

sns.barplot(data=df, x='embark_town', y='survived')
plt.title('Survival Rate by Embarkation Town')
plt.show()

sns.countplot(data=df, x='pclass', hue='survived')
plt.title('Survival Count by Passenger Class')
plt.show()
