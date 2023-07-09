import pandas as pd


def display_dataframe_info(df):
    print("DataFrame Info:")
    print(df.info())


def preprocess_dataset(dataset):
    # Perform data preprocessing tasks on the dataset using pandas
    df = pd.DataFrame(dataset)  # Convert dataset to a DataFrame

    # Print the first 10 rows of the DataFrame
    print(df.head(10))

    display_dataframe_info(df)  # Display DataFrame info

    # Prompt user for dropping non-numeric columns
    drop_non_numeric = input("Do you want to drop non-numeric columns? (y/n): ")
    if drop_non_numeric.lower() == "y":
        non_numeric_columns = df.select_dtypes(exclude=["number"]).columns
        df = df.drop(columns=non_numeric_columns)
        print("Non-numeric columns dropped.")
        print("Updated DataFrame:")
        print(df.head(10))

    # Prompt user to select columns to drop
    drop_columns_option = input("Do you want to drop any specific columns? (y/n): ")
    while drop_columns_option.lower() == "y":
        print("Columns in the DataFrame:")
        print(df.columns)

        # Prompt user to enter column numbers to drop
        columns_to_drop = input("Enter the column numbers to drop (comma-separated): ").split(",")
        columns_to_drop = [int(col) for col in columns_to_drop]

        # Drop the specified columns
        df = df.drop(df.columns[columns_to_drop], axis=1)

        print("Columns dropped:")
        print("Updated DataFrame:")
        print(df.head(10))

        # Prompt user if they want to drop more columns
        drop_columns_option = input("Do you want to drop any other columns? (y/n): ")

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

    return df
