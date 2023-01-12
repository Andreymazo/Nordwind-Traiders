--"Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees), когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)"
--Связь условия о перевозчике United Package не нашел. Связь условия о том ,что работник отвечает за конкретный заказ,
--тоже еле нашел в таблице orders, так как в условии задачи его нет. Без условия о перевозчике вроде все работает. C этим условием и без связи, таблица пустая.
SELECT company_name, orders.customer_id, CONCAT(first_name, ' ', last_name) AS SSS
FROM customers
INNER JOIN orders USING(customer_id)
INNER JOIN employees USING (employee_id)
JOIN shippers USING (company_name)
WHERE employees.city ='London'and customers.city='London' and shippers.company_name ='United Package'
--2 вариант - совместное произвосдтво с Семеном: Когда мы искусственно подставляем ключ, которого нет. Вроде читерство, но зато не нули в таблице)
--SELECT customers.company_name, CONCAT(employees.first_name, ' ', employees.last_name) AS full_name, shippers.company_name
--FROM orders
--INNER JOIN customers USING(customer_id)
--INNER JOIN employees USING(employee_id)
--JOIN shippers ON orders.ship_via=shippers.shipper_id
--WHERE employees.city ='London' AND customers.city='London' AND shippers.company_name = 'United Package'

--Наименование продукта, количество товара (product_name и units_in_stock в табл products), имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов, которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments. Отсортировать результат по возрастанию количества оставшегося товара.
SELECT product_name, units_in_stock, suppliers.contact_name, suppliers.phone, discontinued, categories.category_name
FROM products
JOIN suppliers USING(supplier_id)
JOIN categories USING(category_id)
WHERE discontinued <> 1 AND units_in_stock < 25
AND categories.category_name IN ('Dairy Products', 'Condiments')
ORDER BY units_in_stock
--При изменении 25 на другую цифру, выборка меняется, но в таблице products.units_in_stock не меняется, не понял почему, но надо делать следующую задачу
--Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
SELECT Contact_Name
FROM Customers
WHERE NOT EXISTS (SELECT 1 FROM Orders WHERE Customers.Customer_ID = Orders.Customer_ID)

--2. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
SELECT product_name FROM products
WHERE EXISTS (SELECT 1 FROM order_details  WHERE products.product_id = product_id and quantity = 10)