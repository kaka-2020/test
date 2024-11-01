import pandas as pd

def create_features(df):
    # 创建新特征
    df['day_of_week'] = df['date'].dt.dayofweek
    df['hour_of_day'] = df['date'].dt.hour
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/prepared_data.csv')
    df_with_features = create_features(df)
    df_with_features.to_csv('../data/data_with_features.csv', index=False)