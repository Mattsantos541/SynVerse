# DataUploader.py

import pandas as pd
# Comment out Anvil-related imports
# import anvil.server
# from anvil import FileLoader

class DataUploader:
    def __init__(self):
        self.original_dataset = None

    def upload_file(self, file_path):
        try:
            # Read the uploaded file as a Pandas DataFrame
            self.original_dataset = pd.read_csv(file_path)
            return True, "File uploaded successfully."
        except Exception as e:
            return False, f"An error occurred during file upload: {str(e)}"

    def validate_file(self):
        if self.original_dataset is None:
            return False, "No dataset uploaded. Please upload a file."
        else:
            return True, "Dataset is valid."

# Create an instance of DataUploader
data_uploader = DataUploader()

# Comment out Anvil server functions for local testing
# @anvil.server.callable
# def upload_csv(file_path):
#     success, message = data_uploader.upload_file(file_path)
#     return success, message
#
# @anvil.server.callable
# def validate_file():
#     success, message = data_uploader.validate_file()
#     return success, message


