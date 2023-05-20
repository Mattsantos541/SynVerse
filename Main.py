from my_app.data_uploader import DataUploader
from my_app.correlation import Correlation

def main():
    # Construct objects and perform operations
    data_uploader = DataUploader()
    data_uploader.upload_file('dataset.csv')
    data_uploader.validate_file()

    correlation = Correlation(data_uploader.original_dataset)
    correlation.generate_heatmap()
    correlation.compare_histograms('column_name')

    # Continue with other operations using the created objects
    # ...

if __name__ == '__main__':
    main()

