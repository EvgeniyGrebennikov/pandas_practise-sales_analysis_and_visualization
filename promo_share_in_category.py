#Доля промо в заданной категории
#Когда товар продается по промо-акции, его базовая цена не совпадает с фактической ценой.

#Вам необходимо:
#Посчитать, какую долю от общих продаж категории Сыры занимают промо (в штуках)

#Построить пайчарт, который это проиллюстрирует. На графике должны быть видны группы, соответствующие доли и понятные подписи к ним.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

orders_df = pd.read_excel('orders.xlsx')
products_df = pd.read_excel('products.xlsx')
df = orders_df.merge(products_df, how='inner', on='product_id')

category = df[df['level1'] == 'Сыры']
promo_share = (category[category['regular_price'] > category['price']]['quantity'].sum() / category['quantity'].sum() * 100).round()

sales_shares = pd.DataFrame({
    'Категория': ['Промо', 'Общие'],
    'Доля': [promo_share, 100 - promo_share]
})

plt.pie(sales_shares['Доля'], labels=sales_shares['Категория'], explode=[0, 0.1], autopct='%0.f%%');
plt.title('Доля промо от общих продаж (сыры):')
plt.show()