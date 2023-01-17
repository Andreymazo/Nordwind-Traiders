import sqlite3
import os
import psycopg2
import csv
import json

import dup

import sort_qwck_sort

conn = psycopg2.connect(database="Nordwind Taders", user="postgres", password="12345",
                        host="localhost")  # , port="5432"

path = 'suppliers.json'
cur = conn.cursor()
# cur.execute('select * from student')
# rows = cur.fetchall()

conn.autocommit = True
with open('suppliers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    data_ = []
    # print(type(data))
    # data_sppl = csv.DictReader(f);
    # index = 1
    # supl_country_lst=[]
    # # supl_country_lst.append
# def str_lst():
#
# str_lst(lst)

    for i in data:##Zapoliaem suppliers
        # index = 0
        # ii = ', '.join(i.get("products"))
        # print(ii)

        cur.execute(
            'INSERT INTO suppliers(company_name, contact, address, phone, fax, homepage, products, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (i.get('company_name'), i.get('contact'), i.get('address'), i.get('phone'), i.get('fax'), i.get("homepage"),
             ', '.join(i.get("products")), i.get('address').split(';')[0]))


        # with open('products.csv', 'r', encoding='utf-8') as f1:  # Пока не решил, что делать, просто открыл
        #     with open('suppliers.csv', 'r', encoding='utf-8') as f2:  # Скачать наверное без заголовка надо
        #         data1 = csv.reader(f1, delimiter=',')  # products
        #         data2 = csv.reader(f2, delimiter=',')  # suppliers
        #         data_supl = []
        #         data_prod = []
        #         # prod = set()
        #         prod = []  # Spisok productov
        #         for ii in data1:
        #             data_prod.append(ii)
        #         for i in data2:
        #             data_supl.append(i)
    # #     #     row = cur.fetchone()[0]
    # #     #     Supl_index.append(row)
    #     index += 1
    # # with open('suppliers.json', 'r', encoding='utf-8') as f:
    # #     data = json.load(f)
    # index = 0
    # for i in data:
    #     if index < 29:
    #         r.append(i)
    #         qq = next(q)[index]
    #         # print(type(qq))
    #         # qqq = qq.split()
    #         rr.append(qq)
    #         # print(type(r))
    #
    #         index += 1
    # print(rr)

    # for i in rr:
    #     # print(i)
    #     cur.execute(f'INSERT INTO suppliers(country) VALUES (%s)', (i,))
    # f'UPDATE suppliers SET country = %s', (i,))#INSERT INTO suppliers(country) VALUES (country)""",(i))

    # cur.executemany(f'UPDATE suppliers SET country = %s', (rr,))#INSERT INTO suppliers(country) VALUES (country)', rr)
    # print(r)
    # rrr = zip(r, rr)
    # ff = []
    # fff = []
    # index = 0
    # for i in enumerate(rrr):
    #     ff.append(i)
    # # print(ff)
    # index = 0
    # for i in ff:
    #     # print(i)
    #     fff.append(i[1])
        # del i[index]
    # print(fff)

    # print(len(fff))

    #
    # print(ff[0][1][0].get('company_name'))#Exotic Liquids
    # print(ff[0][1][0].get('contact'))#Charlotte Cooper, Purchasing Manager
    # print(ff[1][1][0].get('contact'))#Shelley Burke, Order Administrator
    # print(ff[0][1][1])#['UK']
    # print(ff[1][1][1])#['USA']
    # print(ff[2][1][1])#['USA']
    # print(ff[2][1][0].get('contact'))#Regina Murphy, Sales Representative
    # print(ff[1][1][0].get('company_name'))#New Orleans Cajun Delights
    #     print(ff[2][0])
    #     print(i[1][0].get('address'))
    #     print(i[1][0].get('company_name'))
    #     print(i[0])
    #     print(i[1][1])
    # index = 0####################Isert ito suppliers##########################
    # for i in fff:
    # #     # print(i[0])
    #     cur.execute('INSERT INTO suppliers( company_name, contact, address, phone, fax, homepage, products, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    #         (i[0].get('company_name'), i[0].get('contact'), i[0].get('address'), i[0].get('phone'),
    #          i[0].get('fax'),
    #          i[0].get("homepage"), i[0].get("products")[0:], i[1]))

    # cur.execute(
    #     "INSERT INTO suppliers(company_name, contact_name, contact_title, country, region, postal_code, city, address, phone, fax, homepage, products) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    #     (row.get("company_name"), row.get("contact").split(',')[0], row.get("contact").split(',')[1],
    #      row.get("address").split(';')[0], row.get("address").split(';')[1],
    #      row.get("address").split(';')[2], row.get("address").split(';')[3],
    #      row.get("address").split(';')[4],
    #      row.get("phone"), row.get("fax"), row.get("homepage"),
    #      row.get("products")[0:]))
