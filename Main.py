from my_app.data_uploader import DataUploader
from my_app.correlation import Correlation
from my_app.preprocessing import preprocess_dataset


def main():
    data_uploader = DataUploader()
    data_uploader.upload_file('dataset.csv')
    data_uploader.validate_file()

    preprocessed_dataset = preprocess_dataset(data_uploader.original_dataset)

    correlation = Correlation(preprocessed_dataset)

    # Continue with other operations using the preprocessed dataset and correlation object
    # ...


if __name__ == '__main__':
    main()
