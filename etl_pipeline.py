import os
from extract import extract_data
from transform import transform_data
from load import load_data
from dotenv import load_dotenv

load_dotenv()

def run_pipeline():
    data = extract_data(os.getenv("SOURCE-FILE-PATH"))
    data = transform_data(data)
    load_data(data, os.getenv("SINK-FILE-PATH"))

if __name__ == "__main__":
    run_pipeline()