import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# 读取数据
data = pd.read_csv('train50.csv')

# 确保时间列是正确的类型，假设时间列为 'date'，如果需要，替换列名
data['date'] = pd.to_datetime(data['date'])

# 提取年份信息
data['year'] = data['date'].dt.year

# 按年分组处理每年的数据
def fill_missing_data(group):
    # 获取该年数据中缺失的索引
    missing = group['num_sold'].isna()

    # 如果缺失值存在，则进行插值处理
    if missing.any():
        # 提取非缺失值
        valid_data = group.dropna(subset=['num_sold'])
        
        # 生成时间和销售数量的数组
        time_values = valid_data['date'].map(lambda x: x.toordinal())
        num_sold_values = valid_data['num_sold']
        
        # 使用线性插值方法
        linear_interp = interp1d(time_values, num_sold_values, kind='linear', fill_value="extrapolate")
        
        # 对缺失值进行插值填补
        group.loc[missing, 'num_sold'] = linear_interp(group.loc[missing, 'date'].map(lambda x: x.toordinal()))
    
    return group

# 使用groupby按年分组并填补缺失值
data_filled = data.groupby('year').apply(fill_missing_data)

# 保存填补后的数据
data_filled.to_csv('train50fill.csv', index=False)

print("数据填补完成，结果已保存为 'train50fill.csv'")
