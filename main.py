import psycopg2
import csv
with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='12345'
) as conn:
    with conn.cursor() as cur:
        with open('north_data/employees_data.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            next(file_reader, None)
            for row in file_reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", row)

        with open('north_data/customers_data.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            next(file_reader, None)
            for row in file_reader:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)

        with open('north_data/orders_data.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            next(file_reader, None)
            for row in file_reader:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)




