# CS4630_Group3_Project2

## Organization

### data/raw
This code expects the full dataset to be placed in data/raw under the filename HIGGS.csv

### data/processed

| File | Description | Dimensions | Type |
| :--- | :--- | :--- | :--- |
| **higgs_sample.csv** | Raw subsampled data | 200,001 x 29 | CSV |
| **X_sample.csv** | Feature matrix (input) | 200,000 x 28 | CSV |
| **Y_sample.csv** | Ground truth labels | 200,000 x 1 | CSV |
| **X_pca_2.csv** | PCA Reduced (Low dim) | 200,000 x 2 | CSV |
| **X_pca_5.csv** | PCA Reduced (Mid dim) | 200,000 x 5 | CSV |
| **X_pca_10.csv** | PCA Reduced (High dim) | 200,000 x 10 | CSV |

### results/metrics
Here is only one file: **clustering_summary.csv** which contains training data for each iteration of K-Means for each dataset

### results/visualizations
This folder contains various visualizations to illustrate different stages of our process of using PCA and K-Means through this unsupervised learning process

## Running

All of the code is done in jupiter notebook files in the following order

1. prepare_data.ipynb
2. kmeans_full.ipynb
3. pca_analysis.ipynb
4. kmeans_pca_10.ipynb
5. kmeans_pca_5.ipynb
6. kmeans_pca_2.ipynb
7. calculate_clustering_metrics.ipynb

## Basic Results (further expanded in report)

The following results were produced by running K-Means (`k=2`) on each PCA-reduced dataset.

| Method | Dataset | Features | Training Time (s) | Prediction Time (s) | Iterations | Accuracy (%) |
|---|---|---:|---:|---:|---:|---:|
| KMeans PCA 2 | sample_200k | 2 | 4.2092 | 0.0202 | 18 | 55.6195 |
| KMeans PCA 5 | sample_200k | 5 | 5.9581 | 0.0184 | 14 | 55.6780 |
| KMeans PCA 10 | sample_200k | 10 | 7.9921 | 0.0253 | 6 | 55.6380 |

### Key Findings
- `KMeans PCA 2` was performed on the 2-component PCA projection and reached 55.6195% accuracy.
- `KMeans PCA 5` was performed on the 5-component PCA projection and reached 55.6780% accuracy.
- `KMeans PCA 10` was performed on the 10-component PCA projection and reached 55.6380% accuracy.
- Increasing PCA dimensionality from 2 to 10 components did not produce a meaningful accuracy increase.

### Conclusions
- K-Means performance is effectively stable across full features and PCA-reduced versions for this dataset.
- PCA-5 provided the best result among PCA variants, but the margin is very small.
- The near-identical accuracies suggest strong overlap between classes in feature space, limiting K-Means separation quality.


