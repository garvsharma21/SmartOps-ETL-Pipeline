from extract import extract_data

def transform_data(data):
    data = data.dropna()

    data = data[data['age'] > 18]

    return data

data = extract_data('data/daily_gym_attendance_workout_data.csv')

transformed_data = transform_data(data)

if __name__== "__main__":
    print(transformed_data.head())