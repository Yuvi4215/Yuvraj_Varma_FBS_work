import psycopg2

#   id - int 
#   name- varchar(20)
#   dept- varchar(15)
#   salary- int

conn_str="host='localhost' dbname='myappdb' user='postgres' password='root123' port='5432'"

conn=psycopg2.connect(conn_str)
# sql="CREATE TABLE employee(id SERIAL, name VARCHAR(40), age INT, dept VARCHAR(20), salary NUMERIC(10,2))"

cursor=conn.cursor()
# cursor.execute(sql)

sql="INSERT INTO employee(name, age, dept, salary) values('Yuvraj', 28, 'Data science', 69000.00)"
cursor.execute(sql)
conn.commit()