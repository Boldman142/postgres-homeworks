"""Скрипт для заполнения данными таблиц в БД Postgres."""
import pathlib
import csv
import psycopg2


class DataWrite:
    def __init__(self, file_name):
        self.path = pathlib.Path(
            pathlib.Path(__file__).parent, "north_data", file_name)

    def data_emp(self):
        with open(self.path, encoding='utf-8', newline='') as data:
            data = csv.DictReader(data)
            with conn:
                with conn.cursor() as cur:
                    for i in data:
                        cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                    (int(i['employee_id']), i['first_name'],
                                     i['last_name'], i['title'],
                                     i['birth_date'], i['notes']))

    def data_cust(self):
        with open(self.path, encoding='utf-8', newline='') as data:
            data = csv.DictReader(data)
            with conn:
                with conn.cursor() as cur:
                    for i in data:
                        cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                    (i['customer_id'], i['company_name'],
                                     i['contact_name']))

    def data_orders(self):
        with open(self.path, encoding='utf-8', newline='') as data:
            data = csv.DictReader(data)
            with conn:
                with conn.cursor() as cur:
                    for i in data:
                        cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                    (int(i['order_id']), i['customer_id'],
                                     int(i['employee_id']), i['order_date'],
                                     i['ship_city']))

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="JutsU#69"
)
try:
    DataWrite('employees_data.csv').data_emp()
    DataWrite('customers_data.csv').data_cust()
    DataWrite('orders_data.csv').data_orders()
finally:
    conn.close()
