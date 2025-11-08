import sqlite3

try:
    connection = sqlite3.connect ("amrutha_DB.db")
    cursor = connection.cursor()
    insert_data_query = """
         Insert INTO student(name,email,course,cgpa) VALUES (?,?,?,?) 
          """
    student_records = [
        ("Bennet","bennetbennet6@gmail.com","BE.AI&DS","9.5"),
        ("Rosaline", "rosaline55@gmail.com", "BE.agriculture", "7.0"),
        ("Edward", "edwardhawking@gmail.com", "AI&ML", "8.6"),
        ("Howard", "howardhawking@gmail.com", "BE.CSE", "7.8"),
        ("Alice", "alicebennet56@gmail.com", "BE.agriculture", "5.1"),
        ]
    cursor.executemany(insert_data_query,student_records)
    connection.commit()
    print("All Student Records Inserted Successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()