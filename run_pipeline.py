import logging

from etl.extract import extract
from etl.transform import transform
from etl.load import load


# Enable logging output in terminal
logging.basicConfig(level=logging.INFO)


def main():
    print("\n🚀 PIPELINE STARTED\n")

    # Input file from your data folder
    input_file = "data/input.xlsx"

    # Step 1: Extract
    extracted_file = extract(
        input_file,
        "data/raw/extracted.csv"
    )
    print("✅ Extract Step Completed")

    # Step 2: Transform
    transformed_file = transform(
        extracted_file,
        "data/raw/transformed.csv"
    )
    print("✅ Transform Step Completed")

    # Step 3: Load
    load(
        transformed_file,
        "data/final/final_output.csv"
    )
    print("✅ Load Step Completed")

    print("\n🎉 PIPELINE FINISHED SUCCESSFULLY!\n")


if __name__ == "__main__":
    main()