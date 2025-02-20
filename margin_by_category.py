#Посчитать маржу по категориям

#Нужно посчитать маржу в рублях и %
#Сделать это нужно по всем категориям level1 и отобразить с помощью 2 горизонтальных барчартов. Все подписи должны быть читаемыми и понятными.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

orders_df = pd.read_excel('orders.xlsx')
products_df = pd.read_excel('products.xlsx')
df = orders_df.merge(products_df, how='inner', on='product_id')

categories_revenue = df.groupby('level1', as_index=False).apply(lambda ser: sum(ser['price'] * ser['quantity']), include_groups=False)
categories_revenue.columns = ['category', 'revenue']

categories_cost = df.groupby('level1', as_index=False).apply(lambda ser: sum(ser['cost_price'] * ser['quantity']), include_groups=False)
categories_cost.columns = ['category', 'cost']

categories = categories_revenue.merge(categories_cost, on='category')
categories['margin'] = categories['revenue'] - categories['cost']
categories['marginality'] = (categories['margin'] / categories['revenue'] * 100).round(2)
categories.drop(['revenue', 'cost'], axis=1, inplace=True)

plt.rcParams['figure.figsize'] = (10, 12)

fig, ax = plt.subplots(2, 1)
fig.tight_layout(pad=4);

# Строим горизонтальный барчарт по марже, руб.
categories.sort_values('margin', inplace=True)

ax[0].set_title('Маржа по категории продуктов');
ax[0].set_xlabel('Маржа, руб.');
ax[0].set_ylabel('Категория');

bars1 = ax[0].barh(categories['category'], categories['margin']);
ax[0].bar_label(bars1, fontsize=8);

# Строим горизонтальный барчарт по маржинальности, %
categories.sort_values('marginality', inplace=True)

ax[1].set_title('Маржинальность по категории продуктов')
ax[1].set_xlabel('Маржинальность, %.')
ax[1].set_ylabel('Категория')

bars2 = ax[1].barh(categories['category'], categories['marginality'], color='orange');
ax[1].bar_label(bars2, fontsize=8);

plt.show()