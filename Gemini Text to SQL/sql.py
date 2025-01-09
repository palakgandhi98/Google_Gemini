import sqlite3

##connect sqlite3
connection = sqlite3.connect("student.db")

## Create a cursor object to insernt record, create a talble and retrive
cursor = connection.cursor()

##create a table
table_info= """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

##Insert some records

cursor.execute('''Insert Into STUDENT values('Palak', 'Data Scoence','A', 90)''')
cursor.execute('''Insert Into STUDENT values('Shubham', 'Machine Learnining','B', 92)''')
cursor.execute('''Insert Into STUDENT values('Ashu', 'Arts','A', 75)''')
cursor.execute('''Insert Into STUDENT values('Akash', 'DS','B', 85)''')
cursor.execute('''Insert Into STUDENT values('Renu', 'Commerce','A', 93)''')

##Display all the records
print("The inserted records are:")

data = cursor.execute('''Select * From STUDENT ''')

for row in data:
    print(row)
    
## Close Connection
connection.commit()
connection.close()