import sqlite3

try:
    connection = sqlite3.connect ("amrutha_DB.db")
    cursor = connection.cursor()
    insert_data_query = """
         Insert INTO student(name,email,course,cgpa) VALUES (?,?,?,?) 
          """
    student_data = ("Katherene","kat456@gmail.com","BE.agriculture","9.0")
    cursor.execute(insert_data_query,student_data)
    connection.commit();
    print("Student Data Inserted Successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()