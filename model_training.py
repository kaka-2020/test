import pandas as pd
import hdbscan

def train_hdbscan_model(data, min_cluster_size=5):
    # 训练HDBSCAN模型
    clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size)
    cluster_labels = clusterer.fit_predict(data)
    
    return cluster_labels

if __name__ == "__main__":
    df = pd.read_csv('../data/data_with_features.csv')
    features = df[['day_of_week', 'hour_of_day', 'latitude', 'longitude']]  # 选择用于聚类的特征
    cluster_labels = train_hdbscan_model(features)
    df['cluster_label'] = cluster_labels
    df.to_csv('../data/clustered_data.csv', index=False)