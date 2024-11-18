import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("risk.csv")
print("Summary Statistics:")
print(df.describe())

# 2. Correlation matrix
print("\nCorrelation Matrix:")
corr_matrix = df.corr()
print(corr_matrix)

# 3. Heatmap for correlations
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 4. Box plots to check for outliers
for column in df.columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df[column])
    plt.title(f'Boxplot for {column}')
    plt.show()
