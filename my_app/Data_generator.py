import pandas as pd
import numpy as np


class DataGenerator:
    def __init__(self, original_dataset):
        self.original_dataset = original_dataset
        self.synthetic_dataset = None

    def generate_synthetic_data(self):
        num_rows = int(input("Enter the number of rows for the synthetic dataset: "))

        # Get the column names from the original dataset
        columns = self.original_dataset.columns

        # Print the list of columns
        print("Columns in the dataset:")
        for column in columns:
            print(f"- {column}")

        # Create an empty DataFrame for the synthetic dataset
        self.synthetic_dataset = pd.DataFrame(columns=columns)

        # Generate synthetic data for each column
        for column in columns:
            # Prompt the user to choose SD or distribution adjustment for the column
            print(f"Adjust column: {column}")
            adjustment_type = input("Enter 'sd' to adjust standard deviation or 'dist' to adjust distribution: ")

            if adjustment_type.lower() == 'sd':
                # Adjust the standard deviation of the column
                sd = float(input(f"Enter the desired standard deviation for column '{column}': "))
                synthetic_values = np.random.normal(loc=self.original_dataset[column].mean(), scale=sd, size=num_rows)

            elif adjustment_type.lower() == 'dist':
                # Adjust the distribution of the column
                distribution_type = input(
                    f"Enter the desired distribution for column '{column}' (e.g., 'normal', 'uniform'): ")

                if distribution_type.lower() == 'normal':
                    mean = float(input(f"Enter the desired mean for column '{column}': "))
                    sd = float(input(f"Enter the desired standard deviation for column '{column}': "))
                    synthetic_values = np.random.normal(loc=mean, scale=sd, size=num_rows)

                elif distribution_type.lower() == 'uniform':
                    low = float(input(f"Enter the desired lower bound for column '{column}': "))
                    high = float(input(f"Enter the desired upper bound for column '{column}': "))
                    synthetic_values = np.random.uniform(low=low, high=high, size=num_rows)

                else:
                    raise ValueError(
                        f"Invalid distribution type: {distribution_type}. Supported types are 'normal' and 'uniform'.")

            else:
                raise ValueError(f"Invalid adjustment type: {adjustment_type}. Supported types are 'sd' and 'dist'.")

            # Add the synthetic data to the synthetic dataset
            self.synthetic_dataset[column] = synthetic_values

        return self.synthetic_dataset




