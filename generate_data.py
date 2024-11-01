import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 设置随机种子以确保结果可重复
np.random.seed(42)

# 生成日期时间范围
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start_date, end_date, freq='1H')

# 生成样例数据
n_samples = len(date_range)
data = {
    'date': date_range,
    'latitude': np.random.uniform(39.9, 40.1, n_samples),  # 经度范围
    'longitude': np.random.uniform(116.2, 116.4, n_samples),  # 纬度范围
    'activity_type': np.random.choice(['work', 'home', 'leisure', 'shopping'], n_samples),
    'duration_minutes': np.random.randint(10, 120, n_samples)
}

# 创建DataFrame
df = pd.DataFrame(data)

# 保存为CSV文件
df.to_csv('../data/raw_data.csv', index=False)

