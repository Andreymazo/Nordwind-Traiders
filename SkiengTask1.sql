-- DROP TABLE IF EXISTS post;
-- create table post (
--       category_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--       category_name VARCHAR(100) NOT NULL
--    );
DROP TABLE orders CASCADE
create table employee
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);
create table customers(
    customer_id varchar(100) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
    contact_name varchar(100) NOT NULL
    );

create table orders(
    order_id int PRIMARY KEY,
    customer_id varchar(100)  REFERENCES customers(customer_id) NOT NULL,
    employee_id int REFERENCES employee(employee_id) NOT NULL,
    order_date date,
    ship_city varchar(100) NOT NULL
	);


--create table post
--(
--	post_id int PRIMARY KEY,
--	title varchar(100) NOT NULL,
--	content text,
--	author int REFERENCES user_account (user_id) NOT NULL
--);
--create table profile
--(
--	profile_id int PRIMARY KEY,
--	user_id int UNIQUE REFERENCES user_account(user_id),
--	image varchar(255)
--)
--CREATE TABLE user_account
--(
--	user_id int PRIMARY KEY,
--	fullname varchar(100) NOT NULL
--);
INSERT INTO profile VALUES (1,1, 'default.jpg' )


-- create table post
-- (
-- 	post_id int PRIMARY KEY,
-- 	title varchar(100) NOT NULL,
-- 	content text
-- );
INSERT INTO post VALUES (1, 'Happy New Year', '', 2);
INSERT INTO post VALUES 
(2, 'My plans 2023', '', 1),
(3, 'Somth more', '', 1),
(4, 'Haary wears pans', '', 2);
SELECT*FROM post;
SELECT*FROM user_account;
SELECT*FROM profile
SELECT*FROM test;


INSERT INTO user_account VALUES
(1, 'Tom'),
(2, 'Jane');
