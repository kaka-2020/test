

# 人口行为模型项目

## 项目概述

本项目旨在通过HDBSCAN聚类算法分析人口行为模式。项目包括数据生成、数据预处理、特征工程、模型训练和结果评估等步骤。

## 目录结构

**代码结构：

population_behavior_model/
├── data/
│   └── raw_data.csv
├── src/
│   ├── generate_data.py
│   ├── data_preparation.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── evaluation.py
├── requirements.txt
└── README.md


## 依赖项

项目依赖于以下Python库：
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `hdbscan`

安装依赖项：

pip install -r requirements.txt

运行项目

1. 生成样例数据
运行 generate_data.py 脚本生成样例数据并保存为 raw_data.csv 文件。

python src/generate_data.py
2. 数据预处理
运行 data_preparation.py 脚本读取并预处理生成的数据。


python src/data_preparation.py
3. 特征工程
运行 feature_engineering.py 脚本创建新的特征。


python src/feature_engineering.py
4. 模型训练
运行 model_training.py 脚本使用HDBSCAN进行聚类。


python src/model_training.py
5. 结果评估
运行 evaluation.py 脚本评估聚类效果并可视化结果。
python src/evaluation.py


**项目说明

generate_data.py
功能: 生成样例数据并保存为CSV文件。
输入: 无
输出: data/raw_data.csv
data_preparation.py
功能: 读取并预处理生成的数据。
输入: data/raw_data.csv
输出: data/prepared_data.csv
feature_engineering.py
功能: 创建新的特征。
输入: data/prepared_data.csv
输出: data/data_with_features.csv
model_training.py
功能: 使用HDBSCAN进行聚类。
输入: data/data_with_features.csv
输出: data/clustered_data.csv
evaluation.py
功能: 评估聚类效果并可视化结果。
输入: data/clustered_data.csv
输出: 控制台输出和可视化图表




