import psycopg2


conn_str="host='localhost' dbname='myappdb' user='postgres' password='root123' port='5432'"

conn=psycopg2.connect(conn_str)
cursor=conn.cursor()

sql="INSERT INTO employee(name, age, dept, salary) values('Sunny', 21, 'Sales ', 78000.00)" # single insert

sql="INSERT INTO employee(name, age, dept, salary) values('Abhi', 21, 'Sales ', 47000.00), ('Vijay', 40, 'Transport', 48000.00)" # Multi insert
cursor.execute(sql)

conn.commit()