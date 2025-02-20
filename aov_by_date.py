#Найти средний чек в заданную дату
#Какой средний чек был 13.01.2022?

import numpy as np
import pandas as pd

orders_df = pd.read_excel('orders.xlsx')
products_df = pd.read_excel('products.xlsx')
df = orders_df.merge(products_df, how='inner', on='product_id')

df['date'] = pd.to_datetime(df['accepted_at']).dt.strftime('%Y-%m-%d')
revenue_by_check = df[df['date'] == '2022-01-13'].groupby('order_id', as_index=False).apply(lambda x: sum(x['price'] * x['quantity']), include_groups=False)

revenue_by_check.columns = ['receipt', 'revenue']
aov = revenue_by_check['revenue'].mean().round(2)

print(aov)