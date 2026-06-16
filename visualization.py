import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("employee_salary.csv")

# Salary Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Salary"], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/salary_distribution.png")
plt.show()

# Department-wise Average Salary
plt.figure(figsize=(8,5))
df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("charts/department_salary.png")
plt.show()

# Experience vs Salary
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Experience", y="Salary")
plt.title("Experience vs Salary")
plt.tight_layout()
plt.savefig("charts/experience_vs_salary.png")
plt.show()

# Gender Distribution
plt.figure(figsize=(6,6))
df["Gender"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("charts/gender_distribution.png")
plt.show()

# Performance Rating
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Performance_Rating")
plt.title("Performance Rating Distribution")
plt.tight_layout()
plt.savefig("charts/performance_distribution.png")
plt.show()

# Correlation Heatmap
numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(8,5))
sns.heatmap(numeric_df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png")
plt.show()

print("All charts generated successfully!")