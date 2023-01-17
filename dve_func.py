import psycopg2
import json

conn = psycopg2.connect(database="Nordwind Taders", user="postgres", password="12345",
                        host="localhost")


def get_product_by_id(id):  # id продукта
    conn.autocommit = True
    cur = conn.cursor()
    with open('suppliers.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for row in data:
            print(row.get("company_name"))
            # cur.execute(
            #     "INSERT INTO suppliers(company_name, contact_name, contact_title, country, region, postal_code, city, address, phone, fax, homepage, products) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            #     (row.get("company_name"), row.get("contact").split(',')[0], row.get("contact").split(',')[1],
            #      row.get("address").split(';')[0], row.get("address").split(';')[1],
            #      row.get("address").split(';')[2], row.get("address").split(';')[3],
            #      row.get("address").split(';')[4],
            #      row.get("phone"), row.get("fax"), row.get("homepage"),
            #      row.get("products")[0:]))
    # cur.execute(
    #     f'SELECT product_name, categories.category_name, unit_price FROM products Join categories using(category_id) where product_id = {id}')
    d = cur.fetchall()
    # print(d)
    # return {product_id, product_name, category_name, unit_price}
    # pass
    cur.close()
    conn.close()
    # print(type(d[0]))
    # print(d[0])
    l = json.dumps(d[0])
    # print(type(l))
    print(f"Вывод данных о товаре с id номером {id}: {l}")


# get_product_by_id(29)


# mycursor = db.cursor()
# query_1 = "ALTER TABLE person ADD salary int(20);"
# query_2 = "UPDATE persons SET salary = '145000' where Emp_Id=12;"
#
# # execute the queries
# mycursor.execute(query_1)
# mycursor.execute(query_2)
#
# mycursor.execute("select * from persons;")
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)
#
# db.commit()
#
# # close the Connection
# db.close()

def get_category_by_id(id):
    conn.autocommit = True

    cur = conn.cursor()
    cur.execute(
        f'SELECT categories.category_name, product_name, suppliers.products FROM products Join categories using(category_id) join suppliers ON suppliers.products=products.product_name where category_id = {id}')
    d = cur.fetchall()
    # print(d)

    cur.close()
    conn.close()
    # print(type(d[0]))
    # print(d[0])
    l = json.dumps(d[0])
    # print(type(l))
    print(f"Вывод данных о товаре с id номером {id}: {l}")
get_category_by_id(8)  # id категории
# Модуль содержит две функции, которые вызываются, когда пользователь запрашивает данные по продукту и данные по категории
# продуктов. Функции принимают словарь с данными для подключения к БД и id запрашиваемого объекта
# Функции возвращают данные в виде json-строки.
