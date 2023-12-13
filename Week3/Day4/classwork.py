import psycopg2


import os

from dotenv import load_dotenv

load_dotenv()


db_name = os.getenv('DB_name')
db_user = os.getenv('DB_user')
db_password = os.getenv('DB_password')
db_host = os.getenv('DB_host')
db_port = os.getenv('DB_port')



conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,)

 
"""
conn = psycopg2.connect(
    dbname='esncjsmy',
    user='esncjsmy',
    password='T9AsUvRYHz1765d_shU6DY9jY8hYu6QX',
    host='bubble.db.elephantsql.com',
    port='5432'
)

"""

cur=conn.cursor()

# Execute a SELECT query
cur.execute('SELECT * FROM public_items')
rows = cur.fetchall()

for row in rows:
    print(row)


cur.close()
conn.close()





"""





# Establish a connection
conn = psycopg2.connect(
    dbname='esncjsmy',
    user='esncjsmy',
    password='T9AsUvRYHz1765d_shU6DY9jY8hYu6QX',
    host='bubble.db.elephantsql.com',
    port='5432'
)

# Create a cursur object to execute SQL queries
cur = conn.cursor()

# CRUD  - Create (insert) Read (select) Update (update) Delete (delete)

# Insert query
# insert_query = 'INSERT INTO products (name, price) VALUES (%s, %s)'
# data_to_insert = ('iKey', 750)
# # cur.execute(insert_query, data_to_insert)
# cur.execute('INSERT INTO products (name, price) VALUES (%s, %s)', ('iKey', 750))



# Update query
# update_query = 'UPDATE products SET name=%s, price=%s WHERE id= %s'
# new_value = ('iCar2024', 9999, 8)
# cur.execute(update_query, new_value)



# Delete query
#cur.execute('DELETE FROM products WHERE id=%s', ('8'))

# Commit the transaction
#conn.commit()



# Execute a SELECT query
cur.execute('SELECT * FROM public_items')
rows = cur.fetchall()

for row in rows:
    print(row)


insert_qury='INSERT INTO public_items (id, name, price) VALUES (%s,%s,%s)'
data_to_insert = (6,'iPhone',1000)
cur.execute(insert_qury,data_to_insert)


conn.commit() 

cur.execute('SELECT * FROM public_items')
rows = cur.fetchall()
for row in rows:
    print(row)

#
# Close the cursur and the connection
#cur.close()
#conn.close()


insert_qury='INSERT INTO public_items (id, name, price) VALUES (%s,%s,%s)'
data_to_insert = (4,'iKey',750)
#cur.execute('INSERT INTO public_items (name, price) VALUES (%s,%s)', ('iKey',750))
cur.execute(insert_qury,data_to_insert)
"""


