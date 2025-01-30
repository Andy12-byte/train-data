import pandas as pd
import os

for i in range(12, 13):
    train_file = f"train{i}.csv"
    predict_file = f"predict{i}.csv"
    final_file = f"final{i}.csv"
    
    # 1. 读取 train{i}.csv, predict{i}.csv
    if not os.path.exists(train_file) or not os.path.exists(predict_file):
        print(f"跳过 {train_file} 或 {predict_file}：文件不存在")
        continue

    # 分别读入 train/predict
    df_train = pd.read_csv(train_file)
    df_predict = pd.read_csv(predict_file)

    # 2. 分别排序
    #    先对 df_train 根据 (country, store, product, date, id) 排序
    df_train.sort_values(by=["country", "store", "product", "date", "id"], 
                         ascending=[True, True, True, True, True],
                         inplace=True)

    #    再对 df_predict 根据 (country, store, product, date, id) 排序
    df_predict.sort_values(by=["country", "store", "product", "date", "id"], 
                           ascending=[True, True, True, True, True],
                           inplace=True)

    # 3. 合并：train 在前, predict 在后
    df_final = pd.concat([df_train, df_predict], ignore_index=True)

    # 4. 导出结果
    df_final.to_csv(final_file, index=False)
    print(f"已生成 {final_file}")
