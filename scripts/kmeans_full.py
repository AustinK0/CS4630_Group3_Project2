import pandas as pd

X = pd.read_csv("data/processed/X_sample.csv")

print("X Shape:", X.shape)
print("\nFirst rows of X:")
print(X.head())
