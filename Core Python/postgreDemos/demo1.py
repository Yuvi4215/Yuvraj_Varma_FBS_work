import psycopg2

conn_string="host='localhost' dbname='myappdb' user='postgres' password='root123' port='5432'"
conn=psycopg2.connect(conn_string)

    