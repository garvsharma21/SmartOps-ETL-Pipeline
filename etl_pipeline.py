from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    data = extract_data("data/daily_gym_attendance_workout_data.csv")
    data = transform_data(data)
    load_data(data, "data/output.csv")

if __name__ == "__main__":
    run_pipeline()