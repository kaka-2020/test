import pandas as pd

def load_and_prepare_data(file_path):
    # 读取数据
    df = pd.read_csv(file_path)
    
    # 数据清洗
    df.dropna(inplace=True)  # 删除空值
    df['date'] = pd.to_datetime(df['date'])  # 转换日期格式
    
    return df

if __name__ == "__main__":
    file_path = '../data/raw_data.csv'
    prepared_data = load_and_prepare_data(file_path)
    prepared_data.to_csv('../data/prepared_data.csv', index=False)