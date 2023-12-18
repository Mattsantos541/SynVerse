import anvil.server


class Finish:
    def __init__(self, synthetic_dataset):
        self.synthetic_dataset = synthetic_dataset

    def generate_csv(self, filename):
        # Save the synthetic dataset as a CSV file in Anvil's built-in data storage
        synthetic_data_table = anvil.server.tables.get_table('SyntheticData')  # Adjust table name
        new_row = synthetic_data_table.add_row(SyntheticData=anvil.server.serialise(self.synthetic_dataset))
        synthetic_data_table.update_data()

        # Return a download link for the user
        download_link = anvil.server.call('generate_download_link', new_row['SyntheticData'], filename)
        return download_link


# Anvil server function to generate a download link for the CSV file
@anvil.server.callable
def generate_download_link(synthetic_data, filename):
    synthetic_data = anvil.server.deserialise(synthetic_data)

    # Save the DataFrame as a CSV file
    synthetic_data.to_csv(filename, index=False)

    # Return the download link for the user
    return anvil.BlobMedia("text/csv", open(filename, "rb").read(), name=filename)
