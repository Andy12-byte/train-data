import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('train6.csv')


if 'num_sold' not in data.columns or 'date' not in data.columns:
    raise ValueError("The required columns 'num_sold' and 'date' do not exist in the CSV file.")


data['date'] = pd.to_datetime(data['date'])


start_date = '2010-01-01'
end_date = '2011-2-01'
filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]


filtered_data = filtered_data.sort_values(by='date')

plt.figure(figsize=(12, 6))
plt.plot(filtered_data['date'], filtered_data['num_sold'], marker='o', linestyle='-', color='blue', alpha=0.7)
plt.title('num_sold Trend (Jan 1, 2010 - Jul 1, 2010)')
plt.xlabel('Date')
plt.ylabel('num_sold')
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()
