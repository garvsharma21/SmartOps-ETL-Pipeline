def load_data(df, output_csv_path):
    df.to_csv(output_csv_path, index=False)