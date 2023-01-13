--Создаем таблицу
create table student
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
)
--2. Добавить в таблицу после создания колонку `middle_name varchar`
--3. Удалить колонку `middle_name`
--4. Переименовать колонку `birthday` в `birth_date`
--5. Изменить тип данных колонки `phone` на `varchar(32)`
--6. Вставить три любых записи с автогенерацией идентификатора
--7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние

alter table student rename column birthday to bith_day
alter table student alter column phone set data type varchar(32)
insert into student (first_name) VALUES ('Mariya'), ('Anton'), ('Else')
truncate table student restart identity

--2
--1. добавить ограничение на поле `unit_price` таблицы `products` (цена должна быть больше `0`)
--2. добавить ограничение, что поле `discontinued` таблицы `products` может содержать только значения `0` или `1`
--3.  Создать новую таблицу, содержащую все продукты, снятые с продажи (`discontinued = 1`)
--4. Удалить из `products` товары, снятые с продажи (`discontinued = 1`)
alter table products add constraint unit_price check (unit_price > 0)
alter table products add constraint discontinued check (discontinued in (0, 1))
select * into new_product_new_1 from products where discontinued = 1

--Сбрасываем ограничения, удаляем и восстанавливаем обратно. Каскадом скорее всего целиком
--удалится таблица и все связи с ней тоже. Там даже условие where скорее всего не сработает
-- delete деликатнее
Alter table products DISABLE TRIGGER ALL;
delete from products where discontinued = 1
ALTER TABLE products ENABLE TRIGGER ALL;