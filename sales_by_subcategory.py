#Распределение продаж по подкатегориям

#Оцените распределение количества проданных позиций в каждой товарной категории (level1) по подкатегориям (level2). 
#Проиллюстрируйте свой результат расчетной таблицей.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

orders_df = pd.read_excel('orders.xlsx')
products_df = pd.read_excel('products.xlsx')
df = orders_df.merge(products_df, how='inner', on='product_id')

subcategories_sales = df.groupby(['level1', 'level2'], as_index=False)['quantity'].sum()
subcategories_sales.sort_values('quantity', ascending=False, inplace=True)
subcategories_sales.reset_index(drop=True, inplace=True)

subcategories_sales.columns = ['Категория', 'Подкатегория', 'Кол-во продаж']

plt.rcParams['figure.figsize'] = (15, 20)
plt.axis('off')

tb = plt.table(cellText=subcategories_sales.values, colLabels=subcategories_sales.columns, cellLoc='center', loc='center', colColours=["green"] * 3);

tb.auto_set_font_size(False)
tb.set_fontsize(12)
tb.scale(1.5, 1.5)

plt.show()