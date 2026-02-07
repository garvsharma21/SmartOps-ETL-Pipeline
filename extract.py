import pandas as pd

def extract_data(file_path):
    data = pd.read_csv(file_path)
    return data

data = extract_data('data/daily_gym_attendance_workout_data.csv')

if __name__== "__main__":
    print(data.head())