import pandas as pd

def display_dataframe_info(df):
    print("DataFrame Info:")
    print(df.info())

def preprocess_dataset(dataset):
    # Perform data preprocessing tasks on the dataset using pandas
    df = pd.DataFrame(dataset)  # Convert dataset to a DataFrame

    display_dataframe_info(df)  # Display DataFrame info

    # Prompt user for column dropping option
    drop_columns_option = input("Do you want to drop any columns? (y/n): ")

    if drop_columns_option.lower() == "y":
        print("Columns in the DataFrame:")
        print(df.columns)

        # Prompt user to enter column names to drop
        columns_to_drop = input("Enter the column names to drop (comma-separated): ").split(",")

        # Drop the specified columns
        df = df.drop(columns=columns_to_drop)

        display_dataframe_info(df)  # Display DataFrame info after column dropping

    # Check for duplicate rows
    duplicate_rows = df.duplicated()
    if duplicate_rows.any():
        print("Duplicate rows detected.")
        handle_duplicates = input("How do you want to handle duplicate rows? (1. Remove, 2. Keep): ")
        if handle_duplicates == "1":
            print("Removing duplicate rows.")
            df = df[~duplicate_rows]
        else:
            print("Keeping duplicate rows.")

    display_dataframe_info(df)  # Display DataFrame info after handling duplicates

    # Check for blank/null values
    blank_values = df.isnull().sum()
    if blank_values.any():
        print("Blank/Null values detected.")
        handle_blanks = input("How do you want to handle blank/null values? (1. Remove rows, 2. Fill with values): ")
        if handle_blanks == "1":
            print("Removing rows with blank/null values.")
            df = df.dropna()
        else:
            print("Filling blank/null values with appropriate values.")
            # Fill blank/null values using suitable techniques

    display_dataframe_info(df)  # Display DataFrame info after handling blanks

    # Example preprocessing tasks
    # ...

    return df
