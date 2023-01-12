--1. "имя контакта" и "город" (contact_name, country) из таблицы customers (только эти две колонки)
--SELECT contact_name, country FROM customers
--2. идентификатор заказа и разницу между датами формирования (order_date) заказа и его отгрузкой (shipped_date) из таблицы orders
--SELECT order_id, (order_date - shipped_date) as differency FROM orders
--3. все города без повторов, в которых зарегестрированы заказчики (customers)
--SELECT DISTINCT city FROM customers
--4.количество заказов (таблица orders)
--SELECT COUNT (*) count_id FROM orders
--5. количество стран, в которые откружался товар (таблица orders, колонка ship_country)
--SELECT COUNT (*) ship_country FROM orders

--1. заказы, доставленные в страны France, Germany, Spain (таблица orders, колонка ship_country)
--SELECT * FROM orders
--WHERE ship_country='France' or ship_country='Germany' or ship_country='Spain'
--2. уникальные города и страны, куда отправлялись заказы, отсортировать по странам и городам (таблица orders, колонки ship_country, ship_city)
--SELECT DISTINCT ship_country, ship_city
--FROM orders
--ORDER BY ship_country, ship_city
--3.сколько дней в среднем уходит на доставку товара в Германию (таблица orders, колонки order_date, shipped_date, ship_country)
--SELECT AVG (shipped_date - order_date)
--FROM orders
--WHERE ship_country = 'Germany'
--4. минимальную и максимальную цену среди продуктов, не снятых с продажи. 1 сняты, 0 не сняты. (таблица products, колонки unit_price, discontinued не равно 1)
--SELECT MAX(unit_price), MIN (unit_price) FROM products
--WHERE discontinued <> 1
--5. минимальную и максимальную цену среди продуктов, не снятых с продажи и которых имеется не меньше 20 (таблица products, колонки unit_price, units_in_stock, discontinued не равно 1)
--SELECT MAX(unit_price), MIN (unit_price) FROM products
--WHERE units_in_stock > 20 AND discontinued <> 1

--1. заказы, отправленные в города, заканчивающиеся на 'burg'. Вывести без повторений две колонки (город, страна) (см. таблица orders, колонки ship_city, ship_country)
--SELECT ship_city, ship_country FROM orders
--WHERE ship_city LIKE '%burg'
--2. из таблицы orders идентификатор заказа, идентификатор заказчика, вес и страну отгузки. Заказ откружен в страны, начинающиеся на 'P'. Результат отсортирован по весу (по убыванию). Вывести первые 10 записей.
--SELECT order_id, customer_id, ship_country, freight FROM orders
--WHERE ship_country LIKE 'P%'
--ORDER BY freight DESC
--LIMIT 10
--3. фамилию и телефон сотрудников, у которых в данных отсутствует регион (см таблицу employees)
--SELECT last_name, home_phone FROM employees
--WHERE region is NULL
--4. количество поставщиков (suppliers) в каждой из стран. Результат отсортировать по убыванию количества поставщиков в стране
--SELECT country, COUNT(*)
--FROM suppliers
--GROUP BY country
--ORDER BY COUNT(*) DESC
--5.суммарный вес заказов (в которых известен регион) по странам, но вывести только те результаты, где суммарный вес на страну больше 2750. Отсортировать по убыванию суммарного веса (см таблицу orders, колонки ship_region, ship_country, freight)
--SELECT  sum(freight)
--FROM orders
--WHERE ship_region IS NOT NULL
--GROUP BY  ship_country, ship_region
--HAVING sum(freight) > 2750
--ORDER BY sum(freight) DESC
--6. страны, в которых зарегистированы и заказчики (customers) и поставщики (suppliers) и работники (employees).
--SELECT country
--FROM suppliers
--INTERSECT
--SELECT country
--FROM customers
--INTERSECT
--SELECT country
--FROM employees
--7. страны, в которых зарегистированы и заказчики (customers) и поставщики (suppliers), но не зарегистрированы работники (employees).
SELECT country
FROM suppliers
INTERSECT
SELECT country
FROM customers



