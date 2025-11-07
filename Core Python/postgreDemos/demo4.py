import psycopg2


conn_str="host='localhost' dbname='myappdb' user='postgres' password='root123' port='5432'"

conn=psycopg2.connect(conn_str)
cursor=conn.cursor()


sql="SELECT * FROM employee"
cursor.execute(sql)

for row in cursor.fetchall():
    print(row)