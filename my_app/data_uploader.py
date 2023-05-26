import pandas as pd


class DataUploader:
    def __init__(self):
        self.original_dataset = None

    def upload_file(self, file_path):
        file_path = input("Enter the file path of the CSV file: ")
        try:
            self.original_dataset = pd.read_csv(file_path)
            print("File uploaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred during file upload:", str(e))

    def validate_file(self):
        if self.original_dataset is None:
            print("No dataset uploaded. Please upload a file.")
        else:
            print("Dataset is valid.")

