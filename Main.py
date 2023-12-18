import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from my_app.data_uploader import DataUploader
from my_app.preprocessing import preprocess_dataset
from my_app.correlation import Correlation
from my_app.data_generator import DataGenerator
from my_app.scorecard import Scorecard
from my_app.finish import Finish


def main():
    # Step 1: Upload the CSV file
    uploader = DataUploader()
    uploader.upload_file()
    uploader.validate_file()

    # Step 2: Preprocess the dataset
    if uploader.original_dataset is not None:
        processed_data = preprocess_dataset(uploader.original_dataset)

        # Proceed only if the preprocessing step is successful
        if processed_data is not None:
            # Print the first 10 rows of the preprocessed dataset
            print("First 10 rows of the preprocessed dataset:")
            print(processed_data.head(10))
            # Step 3: Perform correlation analysis
            correlation = Correlation(processed_data)
            correlation.generate_heatmap()

        # Step 4: Generate synthetic data
        generator = DataGenerator(processed_data)
        synthetic_data = generator.generate_synthetic_data()

        # Step 5: Generate scorecard
        scorecard = Scorecard(processed_data, synthetic_data)
        scorecard.generate_scorecard()

        # Step 6: Finish and send email
        satisfied = input("Are you satisfied with the synthetic dataset? (y/n): ")
        if satisfied.lower() == "y":
            filename = input("Enter the filename for the synthetic dataset CSV: ")
            scorecard_results = scorecard.calculate_metrics()
            finish = Finish(synthetic_data, scorecard_results)
            finish.generate_csv(filename)

            # Prompt user for email details
            sender_email = input("Enter your email address: ")
            receiver_email = input("Enter the recipient's email address: ")
            subject = "Synthetic Dataset for the Original CSV"
            body = "This is your synthetic dataset for the original CSV."


if __name__ == '__main__':
    main()

