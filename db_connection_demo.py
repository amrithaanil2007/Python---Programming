import sqlite3

try:
    #connect to the database
    connection = sqlite3.connect('amrutha_DB.db')
    cursor = connection.cursor()
    #select and print data
    cursor.execute("SELECT*FROM book")
    print("BOOKS IN THE DATABASE")
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"SQLITE error:{e}")
finally:
    if  connection:
        connection.close()
