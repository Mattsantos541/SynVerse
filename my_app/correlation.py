import matplotlib.pyplot as plt
import seaborn as sns

class Correlation:
    def __init__(self, dataset):
        self.dataset = dataset

    def generate_heatmap(self):
        correlation_matrix = self.dataset.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title("Correlation Heat Map")
        plt.show()

    def compare_histograms(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.dataset[column], label='Original', kde=True)
        sns.histplot(self.dataset[column], label='Synthetic', kde=True)
        plt.title(f"Histogram Comparison for {column}")
        plt.legend()
        plt.show()

