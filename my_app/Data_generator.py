import anvil.server
from anvil import *

class PreprocessingForm(PreprocessingFormTemplate):

    def __init__(self, data_table):
        self.data_table = data_table

    def show_data(self, data):
        self.data_table.items = data.to_dict(orient="records")

    def drop_non_numeric_columns(self):
        data = self.data_table.items
        for col in data.columns:
            if not pd.api.types.is_numeric_dtype(data[col]):
                data = data.drop(columns=[col])

        self.show_data(data)

    def drop_selected_columns(self, columns_to_drop):
        data = self.data_table.items
        data = data.drop(columns=columns_to_drop)
        self.show_data(data)

    def handle_duplicates(self, remove_duplicates):
        data = self.data_table.items
        if remove_duplicates:
            data = data.drop_duplicates()
        self.show_data(data)

    def handle_blank_values(self, remove_blanks):
        data = self.data_table.items
        if remove_blanks:
            data = data.dropna()
        self.show_data(data)
