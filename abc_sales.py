# ABC анализ
#Сделайте ABC-анализ продаж по количеству
#Сделайте ABC-анализ по сумме продаж
#Сделайте новый столбец, в котором будет итоговая группа на основании двух анализов. Например: A C.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

orders_df = pd.read_excel('orders.xlsx')
products_df = pd.read_excel('products.xlsx')
df = orders_df.merge(products_df, how='inner', on='product_id')

# Находим кол-во продаж каждого товара и его долю в общих продажах
products_sales = df.groupby('name').agg({'quantity': 'sum'})
products_sales['rel_quantity'] = products_sales['quantity'] / sum(products_sales['quantity'])

# Сортируем данные по убыванию доли продаж товаров и находим накопительную сумму
products_sales.sort_values('rel_quantity', ascending=False)
products_sales['cum_quantity'] = products_sales['rel_quantity'].cumsum()

# Присваиваем ABC значения в зависимости от вклада продаж 
products_sales['abc_sales'] = np.where(products_sales['cum_quantity'] < 0.8, 'A', np.where(products_sales['cum_quantity'] < 0.95, 'B', 'C'))
products_sales.reset_index(inplace=True)


# Находим выручку от продаж каждого товара и его долю в общей выручке
products_revenue = df.groupby('name').apply(lambda ser: sum(ser['cost_price'] * ser['quantity']), include_groups=False).reset_index()
products_revenue.columns = ['name', 'revenue']

products_revenue['rel_revenue'] = products_revenue['revenue'] / sum(products_revenue['revenue'])

# Сортируем данные по убыванию доли выручки товаров и находим накопительную сумму
products_revenue.sort_values('rel_revenue', ascending=False)
products_revenue['cum_revenue'] = products_revenue['rel_revenue'].cumsum()

# Присваиваем ABC значения в зависимости от вклада выручки 
products_revenue['abc_revenue'] = np.where(products_revenue['cum_revenue'] < 0.8, 'A', np.where(products_revenue['cum_revenue'] < 0.95, 'B', 'C'))

# Объединяем данные по ABC-анализам продаж и выручки в один датафрейм
abc_analysis = products_sales.merge(products_revenue, on='name')[['name', 'abc_sales', 'abc_revenue']]
abc_analysis['abc'] = abc_analysis['abc_sales'] + ' ' + abc_analysis['abc_revenue']
abc_analysis = abc_analysis[['name', 'abc']]
abc_analysis