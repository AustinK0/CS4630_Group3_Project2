import pandas as pd
import os
import time
import json

# ----------------------------
# Configuration
# ----------------------------

raw_file = "data/raw/HIGGS.csv.gz"
output_directory = "data/processed"

sample_size = 200000
random_seed = 42

os.makedirs(output_directory, exist_ok = True)


# ----------------------------
# Load Dataset
# ----------------------------

print("Loading Dataset...")

start_time = time.time()

df = pd.read_csv(raw_file, header = None)

print("Original dataset shape:", df.shape)


# ----------------------------
# Sample Dataset (for scalability)
# ----------------------------

df = df.sample(n=sample_size, random_state = random_seed)

print("Sampled dataset shape:", df.shape)


# ----------------------------
# Assign Column Names (since HIGGS does not have column names)
# ----------------------------

columns = ["label"] + [f"feature_{i}" for i in range(1,29)]
df.columns = columns


# ----------------------------
# Split features and target
# ----------------------------

X = df.drop(columns="label")
y = df["label"]


# ----------------------------
# Save processed files
# ----------------------------

df.to_csv(f"{output_directory}/higgs_sample.csv", index = False)
X.to_csv(f"{output_directory}/X_sample.csv", index = False)
y.to_csv(f"{output_directory}/y_sample.csv", index = False)

# ----------------------------
# Runtime
# ----------------------------

runtime = time.time() - start_time

print("Data preparation complete.")
print("Runtime:", runtime, "seconds")
