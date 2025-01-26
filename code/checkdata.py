import os
import pandas as pd


path = "./" 


def count_missing_values():
    missing_values = {}


    for i in range(1, 91):
        filename = f"train{i}.csv"
        file_path = os.path.join(path, filename)


        if os.path.exists(file_path):

            df = pd.read_csv(file_path)


            if 'num_sold' in df.columns:
                missing_count = df['num_sold'].isna().sum()
                missing_values[filename] = missing_count
            else:
                missing_values[filename] = "Column 'num_sold' not found"
        else:
            missing_values[filename] = "File not found"

    
    for file, count in missing_values.items():
        print(f"{file}: {count}")


if __name__ == "__main__":
    count_missing_values()
