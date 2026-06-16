import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("quotes.csv")

print("="*50)
print("FIRST 5 ROWS")
print(df.head())

print("\n" + "="*50)
print("DATASET INFORMATION")
print(df.info())

print("\n" + "="*50)
print("SHAPE OF DATASET")
print(df.shape)

print("\n" + "="*50)
print("MISSING VALUES")
print(df.isnull().sum())

print("\n" + "="*50)
print("DUPLICATE VALUES")
print(df.duplicated().sum())

print("\n" + "="*50)
print("UNIQUE AUTHORS")
print(df["Author"].nunique())

# Create a new column
df["Quote_Length"] = df["Quote"].apply(len)

print("\n" + "="*50)
print("STATISTICAL SUMMARY")
print(df["Quote_Length"].describe())

print("\n" + "="*50)
print("TOP AUTHORS")
print(df["Author"].value_counts())

# Visualization 1
author_count = df["Author"].value_counts()

plt.figure(figsize=(10,5))
author_count.plot(kind="bar")
plt.title("Quotes by Author")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 2
plt.figure(figsize=(8,5))
sns.histplot(df["Quote_Length"], bins=10)
plt.title("Distribution of Quote Length")
plt.xlabel("Quote Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()