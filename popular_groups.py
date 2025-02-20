#Самая ходовая товарная группа
#По какой категории товаров продано больше всего позиций?

#Подкрепите свой ответ таблицей, в которой рассчитано количество проданных штук товара в каждой товарной категории.
#Дополнительно постройте на основании этой таблицы barchart.

#Проверьте, чтобы все подписи на вашем графике выглядели читаемо и понятно. Этот график должен быть сходу понятен стороннему наблюдателю.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

orders_df = pd.read_excel('orders.xlsx')
products_df = pd.read_excel('products.xlsx')
df = orders_df.merge(products_df, how='inner', on='product_id')

categories_quantity = df.groupby('level1', as_index=False)['quantity'].sum()
categories_quantity.sort_values('quantity', ascending=True, inplace=True)

plt.rcParams['figure.figsize'] = (8, 8)

bars = plt.barh(categories_quantity['level1'], categories_quantity['quantity']);
plt.title('График кол-ва продаж по категории товаров');
plt.xlabel('Кол-во продаж');
plt.ylabel('Категория');
plt.bar_label(bars, fontsize=8);

plt.show()