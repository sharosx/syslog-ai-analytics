import os
import pandas as pd

def process_data():
    raw_data_path = 'data/raw/'
    processed_data_path = 'data/processed/'

    logs = []
    for file_name in os.listdir(raw_data_path):
        if file_name.endswith('.log'):
            with open(os.path.join(raw_data_path, file_name), 'r') as file:
                logs.extend(file.readlines())

    df = pd.DataFrame(logs, columns=['log'])
    df.to_csv(os.path.join(processed_data_path, 'logs.csv'), index=False)

if __name__ == "__main__":
    process_data()
