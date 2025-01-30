import pandas as pd

def merge_csv_files(num_files=90, output_file='final.csv'):
    # create empty list, store all data 
    df_list = []

    #read train1.csv ~ train90.csv
    for i in range(1, num_files + 1):
        filename = f'train{i}.csv'
        df = pd.read_csv(filename)
        df_list.append(df)

    #merge and sort
    merged_df = pd.concat(df_list, ignore_index=True)

    merged_df.sort_values('id', inplace=True)
    merged_df[['id', 'num_sold']].to_csv(output_file, index=False)      #merge into final file and keep 'id' and 'num_sold' columns
    print(f"已成功生成 {output_file}")

if __name__ == "__main__":
    merge_csv_files()
