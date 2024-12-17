from imblearn.over_sampling import SMOTE 
from sklearn.datasets import make_classification
import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset (X = independent features, y = dependent feature)
X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0,
                           n_clusters_per_class=1, weights=[0.90], random_state=1)

# Create a DataFrame from the generated data
df1 = pd.DataFrame(X, columns=['f1', 'f2'])
df2 = pd.DataFrame(y, columns=['target'])
final_df = pd.concat([df1, df2], axis=1)

# Apply SMOTE to balance the dataset
oversample = SMOTE()
X_resampled, y_resampled = oversample.fit_resample(final_df[['f1', 'f2']], final_df['target'])

# Create DataFrames for resampled data
df1_resampled = pd.DataFrame(X_resampled, columns=['f1', 'f2'])
df2_resampled = pd.DataFrame(y_resampled, columns=['target'])
final_df_resampled = pd.concat([df1_resampled, df2_resampled], axis=1)

# Plot the resampled data
plt.scatter(final_df_resampled['f1'], final_df_resampled['f2'], c=final_df_resampled['target'])
plt.title("SMOTE Resampled Data")
plt.show()
