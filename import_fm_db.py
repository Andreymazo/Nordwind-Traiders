import os
import psycopg2
#############################Import from DB Import OS ###################################
conn = psycopg2.connect(database="Nordwind Taders", user="postgres", password="12345",
                        host="localhost")  # , port="5432"

path = 'suppliers.json'
cur = conn.cursor()
sql1 = "SELECT * FROM products"
sql2 = "select suppliers.supplier_id from suppliers join products on products.product_name=suppliers.products order by (products.product_name=products)"
sql3 = "select*from suppliers"
# cmd1 = " Your SQL to csv Command"
# os.system(cmd1)
query = f""" {sql3}"""
outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
with open(f"suppliers.csv", "w+", encoding='utf-8') as file:
    cur.copy_expert(outputquery, file)
#     ######################################Zapisali v csv files######################
# ###################    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
# ##########################psycopg2.OperationalError
import psycopg2
# from psycopg2.extras import DictCursor
#
# with psycopg2.connect(
#         host='localhost',
#         database='Northwind Traders',
#         user='postgres',
#         password='8071',
# ) as conn:
#     with conn.cursor(cursor_factory=DictCursor) as cur:
#         cur.execute("SELECT product_id, product_name FROM products")
#         r = [dict((cur.description[i][0], value) \
#                   for i, value in enumerate(row)) for row in cur.fetchall()]
# conn.close()
#
# print(r)
######################
# import json
# def db(database_name='Northwind Traders'):
#     return psycopg2.connect(host='localhost',
#         database='Northwind Traders',
#         user='postgres',
#         password='8071'
# )
#
# def query_db(query):
#     cur = db().cursor()
#     cur.execute(query)
#     r = [dict((cur.description[i][0], value) \
#                for i, value in enumerate(row)) for row in cur.fetchall()]
#     cur.connection.close()
#     return (r[0] if r else None)
#
# my_query = query_db("select product_id, product_name from products")
#
# json_output = json.dumps(my_query)
#
# print(my_query)