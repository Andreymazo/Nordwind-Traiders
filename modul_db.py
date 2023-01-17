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


# index=0
# for i in q:
#
#     qq.append(next(q)[index])
#     index +=1
#     print(qq)
# print(next(q))
conn.autocommit = True
with open('suppliers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    # data_ = []
    # print(type(data))
    # data_sppl = csv.DictReader(f);
    # index = 1
    # supl_country_lst=[]
    # # supl_country_lst.append
    # index = 0
    # r = []
    # rr = []
    # for i in data:##Zapoliaem suppliers
    #     index = 0
    #
    #     cur.execute(
    #         'INSERT INTO suppliers(company_name, contact, address, phone, fax, homepage, products) VALUES (%s, %s, %s, %s, %s, %s, %s)',
    #         (i.get('company_name'), i.get('contact'), i.get('address'), i.get('phone'), i.get('fax'), i.get("homepage"),
    #          i.get("products")[index]))
    #     #     row = cur.fetchone()[0]
    #     #     Supl_index.append(row)
    #     index += 1
    # with open('suppliers.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)
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
    #          i[0].get("homepage"), i[0].get("products")[0:], i[1]))#i[index],
    #     index += 1########################################################
    #############################Import from DB Import OS ###################################

    # sql1 = "SELECT * FROM products"
    # sql2 = "select suppliers.supplier_id from suppliers join products on products.product_name=suppliers.products order by (products.product_name=products)"
    # sql3 = "select*from suppliers"
    # # cmd1 = " Your SQL to csv Command"
    # # os.system(cmd1)
    # query = f""" {sql3}"""
    # outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
    # with open(f"suppliers.csv", "w+", encoding='utf-8') as file:
    #     cur.copy_expert(outputquery, file)
    #     ######################################Zapisali v csv files######################

    with open('products.csv', 'r', encoding='utf-8') as f1:  # Пока не решил, что делать, просто открыл
        with open('suppliers.csv', 'r', encoding='utf-8') as f2:  # Скачать наверное без заголовка надо
            data1 = csv.reader(f1, delimiter=',')  # products
            data2 = csv.reader(f2, delimiter=',')  # suppliers
            data_supl = []
            data_prod = []
            # prod = set()
            prod = []  # Spisok productov
            for ii in data1:
                data_prod.append(ii)
            for i in data2:
                data_supl.append(i)
            # for i in data_prod: #data_supl
            #     print(i)
            # print(data_prod[1:])
            # Nado ubirat lishnie zagolovki ili srazu bez zagolovlov skachivat
            # print(prod)############################Spisok produktov is table products
            # d = str(input())
            # if d in prod:
            for i in data_prod[1:]:
                # print(type(i[1]))
                # i[1] = i[1].split(',')
                # print(i[1])
                prod.append(i[1])
            # print(prod)
                # ww = i[1].split(' ')
                # prod=i[0].get('products')
            # Сравниваем на совпадение продукта в 8 колонке data_supl и 2 колонка data_prod
            # print(prod[1:])
            # print(len(data_prod))
            # print(len(data_supl))
            new_prod = []
            index = 1

        while len(new_prod) <= 77:
            for ii in data_prod[1:]:
                # if index < 77:
                #     index += 1
                # print(ii[1])
                # index=0
                for i in data_supl[1:]:
                    # index += 1
                    # if index < 29:
                    # print(i[7])
                    # print(ii[1])
                    # if i[7] in prod and ii[1] in prod:
                    if ii[1] in i[7]:
                        # print('iiiiiiiiiiii')
                        iii = ii[:-1]
                        iii.append(i[0])
                        # print(iii)
                        new_prod.append(iii)
                        # if i[7] != ii[1]:
                        #     iii = ii[:-1]
                        #     iii.append(0)
                        #     new_prod.append(iii)
                    # elif i[7] != ii[1]:
                    #      iii = ii[:-1]
                    #      iii.append('----')
                    #      new_prod.append(iii)
        # new_prod_finish = []#################Nado iz 2 spiskov sdelat 1 77 strok#####################
        for i in new_prod:
            print(i)
        with open('result_products.csv', 'w+', encoding='utf-8', newline='') as f:#
            # f.writelines(new_prod)
            www = csv.writer(f, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for h in new_prod:
                www.writerow(h)
        # for i in data_prod:
        #     print(i)

        # for ii in data_prod:
        # new_prod_fin=[]
        # print(len(data_prod))
        # print(len(new_prod))

        # while len(new_prod_finish)<78:
        #     for i in data_prod:
        #         for j in new_prod:
        #             if i[0][0] == j[0][0]:
        #                 new_prod_finish.append(j)
        #     print(new_prod_finish)
        #     print(len(new_prod_finish))
        # tt={}
        # while len(new_prod_finish) <= 77:
        #     # for p,pp in tt.items():
        #     #     print('dffffffffff')
        #     for k in data_prod[1:]:
        #         for j in new_prod:
        #             print(k[0])
        #             if j[0] == k[0]:
        #                 # print(j[0][0])
        #                 # j[0][0]=list(j[0][0])#.split(' ')
        #                 # tt.setdefault(j)
        #                 new_prod_finish.append(j)
        #             if j[0] != k[0] and :
        #                 new_prod_finish.append(k)
        # # print(len(new_prod_finish))
        # f = dup.dupl(new_prod_finish)
        #         # print(tt)
        # for tt in f:
        #     print(tt)
        # print(len(tt))
        # fin_sort = sorted(tt, key=lambda x: x[0])
        # print(fin_sort)

                #             if j[0][0] != k[0][0]:
                # new_prod_fin.append(k)
        # print(type(new_prod_finish[0][0]))#[1:])
        # new_prod_finish1=[int(x) for x in new_prod_finish]
        # for t in new_prod_finish[1:]:
        #     # print(type(t[0]))
        #     # try:
        #         #t = t.strip('\'')
        #         #t=t.split('\'')
        #     t[0]=t[0].split(' ')
            # except AttributeError as e:
            #     print(e)
            # print(type(t[0]))
        #     nn=[]
        #     nn.append(t)
        #
        # # # ffff = dup.dupl(fin_sort)
        # for ig in fin_sort:
        #     print(ig)


                # print(ffff)
        # ffff=sort_qwck_sort.quick_sort(new_prod_finish, 0)
        # print(len(ffff))
        # for l in new_prod_finish:
        #     print(l)

        # for l in new_prod_finish:
        #     print(l)

        # new_prod_lst=[list(i[0]) for i[0] in new_prod or 0 if i[0] is None]
        # print(new_prod)
        # for i in new_prod:
        #     print(i)
        #     print(type(i[0]))
        #     if i[0] is not list:
        #         i[0] = i[0].split(' ')
        #         print(type(i[0]))
        #         print(i)
        #         new_prod_lst.append(i)
        # print(len(new_prod_lst))
        # print(data_prod[1][0])
    ###########Otsortiruem po id############

    # print(new_prod)
    # print(len(new_prod))
    # print(type(new_prod))
    # new_prod_sort = sort_qwck_sort.quick_sort(new_prod, 0)
    # for i in new_prod_sort:
    #     print(i)
    # print(new_prod_sort)

    # def dupl(da):  ##Ubiraem duplikati v new_prod_
    #     index = 0
    #     index2 = 0
    #     data_finish = []
    #     while index < len(da):
    #         # print(da[0][0])
    #         # print(index)
    #         while index < len(da) - 1 and da[index][0] == da[index + 1][0]:
    #             index += 1
    #
    #         da[index2] = da[index]
    #         data_finish.append(da[index2])
    #         index2 += 1
    #         index += 1
    #
    #     return data_finish

    # z = data_finish = dupl(new_prod)
    # for i in z:
    #     print(i)
    #     print(iii)
    # for j in new_prod:
    #     print(i)

    # print(len(data_supl))
    # print(data_supl[:-1])

    # for i in data_supl:
    #     print(i)
    # for i in data_prod:
    #     print(i)
    # prod=set()
    # for i in data_prod:#Sformiruem massiv  produktov dliya proverki
    #     prod.update(i[1])
    # print(prod)
    # print(len(data_prod))
    # print(ii[1])
    # print(i[7])
    # if ii[1] == i[7]:
    #     data_prod.append(ii[:-1])
    #     print(ii[:-1])
    #     print(i[7])

    # header = next(f)
    # data = [header]
    # for i in f:
    #     print(f)
    # [['supplier_id'], ['8'], ['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['9'], ['10'], ['11'], ['12'], ['13'],
    #          ['14'], ['15'], ['16'], ['17'], ['18'], ['19'], ['20'], ['21'], ['22'], ['23'], ['24'], ['25'], ['26'], ['27'],
    #          ['28'], ['29']]

    # print(sql2)
    # print
    # cur.execute(sql1)
    # a=cur.fetchall()
    # print(len(a))

    # fieldnames = ['product_id', 'product_name', 'category_id', 'quantity_per_unit', 'unit_price', 'units_in_stock', 'units_on_order', 'reorder_level', 'discontinued', 'supplier_id']
    # writer = csv.DictWriter(file, fieldnames=fieldnames)
    # a.writelines(file)
    # for i in a:
    #     writer.writerow(i)

    #     print(i)
    # cur.copy_expert(sql1, file)
    # print(file)

    # [(0, ({'company_name': 'Exotic Liquids', 'contact': 'Charlotte Cooper, Purchasing Manager',
    #        'address': 'UK; ; EC1 4SD; London; 49 Gilbert St.', 'phone': '(171) 555-2222', 'fax': '', 'homepage': '',
    #        'products': ['Chang', 'Aniseed Syrup']}, ['UK'])), (1, (
    # {'company_name': 'New Orleans Cajun Delights', 'contact': 'Shelley Burke, Order Administrator',
    #  'address': 'USA; LA; 70117; New Orleans; P.O. Box 78934', 'phone': '(100) 555-4822', 'fax': '',
    #  'homepage': '#CAJUN.HTM#',
    #  'products': ["Chef Anton's Cajun Seasoning", "Chef Anton's Gumbo Mix", 'Louisiana Fiery Hot Pepper Sauce',
    #               'Louisiana Hot Spiced Okra']}, ['USA'])),
    #  (2, ({'company_name': "Grandma Kelly's Homestead", 'contact': 'Regina Murphy,
    # (i[index].get('company_name'), i[index].get('contact'), i[index].get('address'), i[index].get('phone'), i[index].get('fax'),
    #  i[index].get("homepage"), i[index].get("products")[index]), i[index])
    # if index < 28:
    #     ff.append(next(rrr))
    #     index += 1
    #     print(ff)
    # conn.autocommit = True
    # for i in ff:
    #     try:
    #         cur.execute('INSERT INTO suppliers(company_name, contact, address, phone, fax, homepage, products, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    #                     (i[index].get('company_name'), i[index].get('contact'), i[index].get('address'), i[index].get('phone'), i[index].get('fax'),
    #                      i[index].get("homepage"), i[index].get("products")[index]), i[index])
    #         index += 1
    #     except IndexError and TypeError as e:
    #         print(e)

    # index =0
    # for i in r:
    #     i.update(rr[index], index)
    #     index += 1
    #     print(i)

    # for i in data:#{'company_name': 'Bigfoot Breweries', 'contact': 'Cheryl Saylor, Regional Account Rep.', 'address': 'USA; OR; 97101; Bend; 3400 - 8th Avenue Suite 210', 'phone': '(503) 555-9931', 'fax': '', 'homepage': '', 'products': ['Sasquatch Ale', 'Steeleye Stout', 'Laughing Lumberjack Lager']}
    #     # if index < 5:
    #     #     print(i.get('company_name'), i.get('contact'), i.get('address'), i.get('phone'),i.get('fax'), i.get("homepage"), i.get("products"))
    #     # index = 0
    #
    #     row = cur.fetchone()[0]
    #     Supl_index.append(row)
    #     index +=1
    # index = 0
    # for i in r:
    #     print(type(i))
    # print(i)
    # print(i.get('company_name'), i.get('contact'), i.get('address'), i.get('phone'), i.get('fax'),
    #       i.get("homepage"), i.get("products")[index], i[:-1])
    # index += 1
    # cur.execute('insert into suppliers(country) VALUES (%s)', (
    #     get_sup_reg.get_sup_aderss(path)))

    #     print(row)
    # print(Supl_index)
    # cur.execute('select*from suppliers')
    # rows = cur.fetchall()
    # cur.execute('select company_name from suppliers JOIN products on products.product_name=suppliers.products')
    # index = 1
    # for row in rows:
    #     print(row)
    #     index +=1
    # print("Operation done successfully")

    # [(0, {'company_name': 'Exotic Liquids', 'contact': 'Charlotte Cooper, Purchasing Manager',
    #       'address': 'UK; ; EC1 4SD; London; 49 Gilbert St.', 'phone': '(171) 555-2222', 'fax': '', 'homepage': '',
    #       'products': ['Chang', 'Aniseed Syrup']}), (1, {'company_name': 'New Orleans Cajun Delights',
    # index = 0
    # def fun_videl(d):
    #     dd=[]
    #     for i in d:
    #         for ii in i:
    #             if ii =='company_name':
    #                 dd.append(i.get('company_name'))
    #                 # cur.execute('INSERT INTO products (supplier) VALUES (%s)', (i.get('company_name')))
    #             cur.executemany('UPDATE products SET supplier = (%s)', dd)#ne prosto vstavliat nado a pod usloviem
    #                 # print(i)
    #             # cur.executemany('INSERT INTO products.supplier VALUES (%s)', dd)
    #             # INSERT INTO target_table[(< column-list >)] SELECT...FROM...;
    #
    #             # print(dd)
    # fun_videl(data_)

    # def poisk(dat, r):
    #     # print(len(dat))
    #     # print(r)
    #     for i in dat:
    #         if i.get('name') == r:
    #             return i.get('id'), print(i.get('id'))
    #         for ii in i.get('areas'):
    #             if ii.get('name') == r:
    #                 return ii.get('id'), print(ii.get('id'))
    #             for iii in ii.get('areas'):
    #                 if iii.get('name') == r:
    #                     return iii.get('id'), print(iii.get('id'), iii)
    #

    #     with open('regions.json', 'r', encoding='utf-8') as f:
    #         t = 'Санкт-Петербург'
    #         g = []
    #         data = json.load(f)
    #         index = 0
    #         poisk(data, t)
    #     d = [i for i in enumerate(data_) if i.get('company_name') is True]
    #     print(d)
    #         index += 1
    # with open('orders_data.csv', 'r', encoding='utf-8') as f:#Zapasoi variant copy_from
    #     next(f)  # Skip the header row.
    #     #      #f , <database name>, Comma-Seperated
    #     cur.copy_from(f, 'orders', sep=',')
    #
    # for row in rows:
    #     print(f'name:{row[0]}\nid:{row[1]}')
    cur.close()
conn.close()
# import mysql.connector
#
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="geeks"
# )
#
# # getting the cursor by cursor() method
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
# cur.execute(
#                     "INSERT INTO suppliers(company_name, contact_name, contact_title, country, region, postal_code, city, address, phone, fax, homepage, products) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#                     (row.get("company_name"), row.get("contact").split(',')[0], row.get("contact").split(',')[1],
#                      row.get("address").split(';')[0], row.get("address").split(';')[1],
#                      row.get("address").split(';')[2], row.get("address").split(';')[3],
#                      row.get("address").split(';')[4],
#                      row.get("phone"), row.get("fax"), row.get("homepage"),
#                      row.get("products")[0:]))
