### Описание данных
<u> Таблица products: </u>
- product_id - id товара
- level1 - категория
- level2 - подкатегория
- name - наименование товара

<u> Таблица orders: </u>
- order_id - номер чека
- accepted_at - дата и время чека
- product_id - id товара
- quantity - кол-во товара в чеке
- regular_price - регулярная цена
- price - текущая цена
- cost_price - закупочная цена
<br>

## Задания
### Самая ходовая товарная группа
- По какой категории товаров продано больше всего позиций? Подкрепите свой ответ таблицей, в которой рассчитано количество проданных штук товара в каждой товарной категории.

<i> Дополнительно постройте на основании этой таблицы barchart.
Проверьте, чтобы все подписи на вашем графике выглядели читаемо и понятно. Этот график должен быть сходу понятен стороннему наблюдателю. </i>
<br>
### Распределение продаж по подкатегориям
- Оцените распределение количества проданных позиций в каждой товарной категории (<i><b> level1 </b></i>) по подкатегориям (<i><b> level2 </b></i>). Проиллюстрируйте свой результат расчетной таблицей.
<br>
### Найти средний чек в заданную дату
- Какой средний чек был 13.01.2022?
<br>
### Доля промо в заданной категории
- Вам необходимо посчитать, какую долю от общих продаж категории <i><b> Сыры </b></i> занимают промо (в штуках).

<i>Построить пайчарт, который это проиллюстрирует. На графике должны быть видны группы, соответствующие доли и понятные подписи к ним.</i>
<br>

### Посчитать маржу по категориям
- Нужно посчитать маржу в рублях и %.

<i>Сделать это нужно по всем категориям level1 и отобразить с помощью 2 горизонтальных барчартов. Все подписи должны быть читаемыми и понятными.</i>
<br>

#### ABC анализ
- Сделайте ABC-анализ продаж по количеству;
- Сделайте ABC-анализ по сумме продаж.

<i>Сделайте новый столбец, в котором будет итоговая группа на основании двух анализов. Например, A C.</i>
