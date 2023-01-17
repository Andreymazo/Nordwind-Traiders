--Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, которых в продаже менее 20 единиц.
--Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер.
select * from products
join categories on products.category_id=categories.category_id
where discontinued <> 1 and units_in_stock < 20
AND category_name in ('Beverages', 'Seafood')