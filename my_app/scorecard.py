import numpy as np
import pandas as pd
from scipy.stats import ks_2samp
from scipy.spatial.distance import jensenshannon


class Scorecard:
    def __init__(self, original_dataset, synthetic_dataset):
        self.original_dataset = original_dataset
        self.synthetic_dataset = synthetic_dataset

    def calculate_metrics(self):
        # Calculate Stats metric comparison
        stats_comparison = self.original_dataset.describe() - self.synthetic_dataset.describe()
        stats_comparison = stats_comparison.drop(['count'])  # Remove 'count' row

        # Calculate Kolmogorov-Smirnov test
        ks_test_results = {}
        for column in self.original_dataset.columns:
            ks_stat, ks_p_value = ks_2samp(self.original_dataset[column], self.synthetic_dataset[column])
            ks_test_results[column] = {'KS Statistic': ks_stat, 'KS p-value': ks_p_value}

        # Calculate Jensen-Shannon divergence
        js_divergence = {}
        for column in self.original_dataset.columns:
            p = np.histogram(self.original_dataset[column], bins='auto', density=True)[0]
            q = np.histogram(self.synthetic_dataset[column], bins='auto', density=True)[0]
            js_div = jensenshannon(p, q)
            js_divergence[column] = js_div

        # Return a dictionary of calculated metrics
        metrics = {
            'Stats Comparison': stats_comparison,
            'Kolmogorov-Smirnov Test': ks_test_results,
            'Jensen-Shannon Divergence': js_divergence
        }

        return metrics

    def generate_scorecard(self):
        metrics = self.calculate_metrics()

        print("Scorecard:")
        for metric, value in metrics.items():
            print(metric)
            if isinstance(value, pd.DataFrame):
                print(value.to_string())
            elif isinstance(value, dict):
                for column, result in value.items():
                    print(f"{column}:")
                    print(f"  KS Statistic: {result['KS Statistic']} (Ideal: 0, Poor: >0.1)")
                    print(f"  KS p-value: {result['KS p-value']} (Ideal: >0.05, Poor: <=0.05)")
                    print(f"  JS Divergence: {result} (Ideal: 0, Poor: >0.3)")
            print()


