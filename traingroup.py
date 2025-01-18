import pandas as pd
# Read the train.csv file
df = pd.read_csv('train.csv')
# Group by country, store, and product
grouped = df.groupby(['country','store','product'])
# Initialize file counter
file_counter= 1
# Iterate over the grouped data and $each aroup to a separate csV file
# Iterate over the grouped data and save each group to a separate
for(country, store, product),group in grouped:
    # Create a file name based on the group
    file_name = f'train{file_counter}.csv'
    # Save the group to the csV file
    group.to_csv(file_name, index=False)
    # Increment the counter
    file_counter += 1
print("Files saved successfully!")
