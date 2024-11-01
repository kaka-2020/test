import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_clusters(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='longitude', y='latitude', hue='cluster_label', data=df, palette='viridis')
    plt.title('Population Behavior Clusters')
    plt.show()

def evaluate_clusters(df):
    # 打印每个聚类的数量
    print(df['cluster_label'].value_counts())
    
    # 可视化聚类结果
    visualize_clusters(df)

if __name__ == "__main__":
    df = pd.read_csv('../data/clustered_data.csv')
    evaluate_clusters(df)