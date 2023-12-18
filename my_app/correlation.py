import anvil.server
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import pandas as pd

class Correlation:
    def __init__(self):
        self.dataset = None

    def set_dataset(self, dataframe):
        self.dataset = dataframe

    def generate_heatmap(self):
        if self.dataset is None:
            return None  # No dataset to analyze

        # Create a correlation matrix
        correlation_matrix = self.dataset.corr()

        # Generate a heatmap plot
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title("Correlation Heat Map")

        # Save the heatmap plot to a BytesIO object
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Encode the plot as base64 to display in Anvil
        plot_base64 = base64.b64encode(buffer.read()).decode()
        buffer.close()

        return plot_base64

# Create an instance of the Correlation module
correlation_anvil = Correlation()

# Define an Anvil server callable function to set the dataset
@anvil.server.callable
def set_correlation_dataset(dataframe_json):
    dataframe = pd.read_json(dataframe_json)
    correlation_anvil.set_dataset(dataframe)

# Define an Anvil server callable function to generate the heatmap
@anvil.server.callable
def generate_correlation_heatmap():
    heatmap_base64 = correlation_anvil.generate_heatmap()
    return heatmap_base64

