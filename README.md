# Large-Scale Unsupervised Structure Discovery on UCI HIGGS Dataset

## 1. Key Problems Studied
High energy physics studies fundamental particles and forces through high energy collisions. The UCI HIGGS dataset captures simulated collision events where class `1` is signal and class `0` is background. The core challenge is that these classes overlap strongly in feature space, making separation difficult.

This project studies unsupervised structure discovery on HIGGS with K-Means clustering. A major systems challenge is scale: the dataset has about 11 million rows and 29 columns, so some quality metrics and modeling steps become expensive at full size.

## 2. Solutions Proposed for Theory, Algorithms, and Systems

### 2.1 Theoretical Framework
- Unsupervised learning with K-Means clustering (`k=2`) to reflect signal vs background structure.
- Objective: minimize within-cluster squared distance to centroids.
- PCA used for dimensionality reduction (2, 5, and 10 components) to improve efficiency and potentially improve cluster structure.
- Evaluation metrics: accuracy (via post-hoc label mapping), silhouette score, Davies-Bouldin index, compactness, separation, plus runtime metrics.

### 2.2 System Architecture
Pipeline stages:
1. Data ingestion from UCI HIGGS source.
2. Preprocessing and data quality checks.
3. K-Means modeling on full and PCA-reduced datasets.
4. Metric calculation and visualization generation.

### 2.3 Model Configuration
K-Means parameters used:
- `n_clusters=2`
- `init='k-means++'`
- `random_state=42`
- `n_init=20`

Accuracy is computed by mapping each cluster to the majority true label in that cluster, then comparing mapped predictions to true labels.

## 3. Implementation Details

### 3.1 Programming Environment
- Language: Python
- Core libraries: pandas, numpy, scikit-learn, matplotlib, scipy, time
- Collaboration: Git/GitHub

### 3.2 Dataset and Schema
- Dataset: UCI HIGGS
- Total size: ~11,000,000 rows and 29 columns
- Column 1: class label (`1` signal, `0` background)
- Remaining 28 columns: feature set (low-level and high-level physics-derived features)

### 3.3 Data Cleaning and Preparation
- Assigned column names from UCI metadata.
- Verified no missing values.
- Kept duplicate rows because identical recorded measurements can represent distinct physical events.
- Evaluated outliers with IQR; retained outliers to avoid removing potentially meaningful rare events.
- Created a 200,000 row sample to keep PCA and clustering metrics computationally practical while preserving class proportions.

### 3.4 PCA Workflow
- Applied `StandardScaler` before PCA.
- Generated reduced datasets with 2, 5, and 10 components.
- Saved outputs in `data/processed`.

PCA summary (from project analysis):

| Components | Variance Explained | Runtime |
|---:|---:|---:|
| 2 | 21.58% | 0.04s |
| 5 | 37.84% | 0.04s |
| 10 | 59.73% | 0.04s |

## 4. Key Experimental Results - Effectiveness and Efficiency

### 4.1 K-Means Metrics Summary
Results from `results/metrics/clustering_summary.csv`:

| Method | Dataset | Features | Train (s) | Predict (s) | Iterations | Accuracy (%) | Silhouette | Davies-Bouldin | Compactness | Separation | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KMeans Full 28 | HIGGS.csv.gz(full) | 28 | 32.7565 | 3.9917 | 13 | 54.8023 | - | - | - | - | not_evaluated_due_to_scale |
| KMeans Full 28 | sample_200k | 28 | 1.6321 | 0.0243 | 6 | 55.6385 | 0.1160 | 2.7150 | 17.5120 | 2.1100 | evaluated_sampled_silhouette |
| KMeans PCA 5 | sample_200k | 5 | 5.9581 | 0.0184 | 14 | 55.6780 | 0.3498 | 1.4701 | 8.1801 | 2.4178 | evaluated_sampled_silhouette |
| KMeans PCA 10 | sample_200k | 10 | 7.9921 | 0.0253 | 6 | 55.6380 | 0.2651 | 1.9814 | 14.3063 | 2.4230 | evaluated_sampled_silhouette |
| KMeans PCA 2 | sample_200k | 2 | 6.8643 | 0.0156 | 18 | 55.6195 | 0.4868 | 0.8775 | 3.6302 | 2.4218 | evaluated_sampled_silhouette |

### 4.2 Main Findings
- Accuracy is very similar across all sampled variants (about 55.6%).
- PCA-2 has the strongest internal clustering quality:
	- highest silhouette
	- lowest Davies-Bouldin
	- lowest compactness
- Full 28-feature clustering on the sample has weaker internal structure than PCA-reduced versions.
- Full 11M-row runtime is much slower than sampled runtime, while accuracy remains close, supporting use of the 200k sample for practical experimentation.

### 4.3 Metric Interpretation
- Accuracy (mapped): higher is better.
- Silhouette: higher is better.
- Davies-Bouldin: lower is better.
- Compactness: lower is better.
- Separation: higher is better.

## 5. Repository Organization and Run Order

### 5.1 Data Files (`data/processed`)

| File | Description | Dimensions | Type |
| :--- | :--- | :--- | :--- |
| `higgs_sample.csv` | Raw subsampled data | 200,001 x 29 | CSV |
| `X_sample.csv` | Feature matrix (input) | 200,000 x 28 | CSV |
| `y_sample.csv` | Ground truth labels | 200,000 x 1 | CSV |
| `X_pca_2.csv` | PCA-reduced features (low dimension) | 200,000 x 2 | CSV |
| `X_pca_5.csv` | PCA-reduced features (mid dimension) | 200,000 x 5 | CSV |
| `X_pca_10.csv` | PCA-reduced features (higher dimension) | 200,000 x 10 | CSV |

### 5.2 Notebook Execution Order
1. `notebooks/prepare_data.ipynb`
2. `notebooks/kmeans_full.ipynb`
3. `notebooks/pca_analysis.ipynb`
4. `notebooks/kmeans_pca_10.ipynb`
5. `notebooks/kmeans_pca_5.ipynb`
6. `notebooks/kmeans_pca_2.ipynb`
7. `notebooks/calculate_clustering_metrics.ipynb`

### 5.3 Output Artifacts
- Metrics table: `results/metrics/clustering_summary.csv`
- Visualizations:
	- `results/visualizations/clustering_metrics_comparison.png`
	- `results/visualizations/dataset_balance.png`
	- `results/visualizations/kmeans_accuracy_comparison.png`
	- `results/visualizations/kmeans_pca10_cluster_scatter.png`
	- `results/visualizations/kmeans_pca2_cluster_scatter.png`
	- `results/visualizations/kmeans_pca5_cluster_scatter.png`
	- `results/visualizations/kmeans_pca_combined_scatter.png`
	- `results/visualizations/kmeans_runtime_comparison.png`
	- `results/visualizations/metrics_summary_table.png`
	- `results/visualizations/pca_2d_scatter.png`
	- `results/visualizations/variance_explained.png`

## 6. Limitations and Future Work

### 6.1 Limitations
- Primary analysis uses a 200k sample, not full 11M rows for all quality metrics.
- K-Means assumes roughly spherical clusters and may not capture complex structure.

### 6.2 Future Work
- Identify the smallest sample size that preserves clustering quality.
- Compare against other unsupervised methods (for example, GMM).
- Evaluate additional dimensionality reduction approaches (for example, UMAP or t-SNE).
- Run repeated trials and report average metrics/variance.
- Compare against supervised baselines that use labels directly.

## 7. Conclusion
K-Means on UCI HIGGS shows stable mapped accuracy across full and PCA-reduced representations, while internal quality metrics strongly favor PCA-2 on the sampled dataset. The project demonstrates a practical workflow for large-scale unsupervised analysis where sampling and dimensionality reduction improve tractability without materially changing top-level label agreement.

## 8. References
- HIGGS - UCI Machine Learning Repository
- https://arxiv.org/abs/1402.4735

## Appendix: Team Contributions

| Name | Contribution | Percentage |
|---|---|---:|
| Hailey | PCA analysis | 20% |
| Lavender | K-Means on PCA datasets | 20% |
| Amelia | Data ingestion and cleaning; K-Means on full features | 20% |
| Austin | Result analysis and visualizations | 20% |
| Jim | Clustering metric calculation | 20% |



