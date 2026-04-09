# CS4630_Group3_Project2

## Notes
- Sample dataset with 200k rows is saved in data/processed.

- X_sample.csv and y_sample.csv is saved in data/processed and can be read in to run models with `X = pd.read_csv("data/processed/X_sample.csv")` and `y = pd.read_csv("data/processed/y_sample.csv")`

- Add results to results table to keep all results in one place. Read in with `df_summary = pd.read_csv("results/metrics/clustering_summary.csv")` and update when more metrics are calculated

## Step 3 Results: K-Means on PCA-Reduced Data

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


