from etl.extract import extract
from etl.transform import transform
from etl.load import load

def main():

    input_file = "data/input.xlsx"  # <-- put your file name here

    extracted = extract(
        input_file,
        "data/raw/extracted.csv"
    )

    monthly, customers = transform(
        extracted,
        "data/reports"
    )

    load(monthly, customers)

    print("✅ Reports Generated Successfully!")


if __name__ == "__main__":
    main()
