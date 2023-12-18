import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture

class DataGenerator:
    def __init__(self, original_dataset):
        self.original_dataset = original_dataset
        self.synthetic_dataset = None

    def generate_synthetic_data(self, num_rows=1000):
        # Get the column names from the original dataset
        columns = self.original_dataset.columns

        # Create an empty DataFrame for the synthetic dataset
        self.synthetic_dataset = pd.DataFrame(columns=columns)

        # Generate synthetic data for each column using Gaussian Mixture Model (GMM)
        for column in columns:
            # Fit a GMM to the original data for the current column
            gmm = GaussianMixture(n_components=2, random_state=0)  # You can customize n_components
            gmm.fit(self.original_dataset[column].values.reshape(-1, 1))

            # Generate synthetic data points
            synthetic_values = gmm.sample(num_rows)[0]

            # Add the synthetic data to the synthetic dataset
            self.synthetic_dataset[column] = synthetic_values.flatten()

        return self.synthetic_dataset

