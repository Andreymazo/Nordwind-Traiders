--- Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
select*from orders
GROUP BY required_date DESC, shipped_date ASC
--- Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
select AVG (shipped_date-order_date) from orders
WHERE orders.ship_country = 'USA'
--- Найти сумму, на которую имеется товаров (количество * цену) причём таких, которые не сняты с продажи (см. на поле discontinued)
select SUM (unit_price*units_in_stock) AS SSS from products
WHERE discontinued <> 1