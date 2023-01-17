--- Посчитать количество заказчиков
SELECT COUNT(customer_id) FROM customers
--- Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики
SELECT DISTINCT city, region FROM customers
--- Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники из города London, а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.
SELECT customers.company_name, CONCAT(employees.first_name, ' ', employees.last_name) AS full_name, shippers.company_name
FROM orders
INNER JOIN customers USING(customer_id)
INNER JOIN employees USING(employee_id)
JOIN shippers ON orders.ship_via=shippers.shipper_id
WHERE employees.city ='London' AND customers.city='London' AND shippers.company_name = 'Speedy Express'
--- Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
--Видимо опечатка в задании, если нет заказов, то и айди нет
SELECT Contact_Name
FROM Customers
WHERE NOT EXISTS (SELECT 1 FROM Orders WHERE Customers.Customer_ID = Orders.Customer_ID)
