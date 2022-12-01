import sqlite3 # import package
db = sqlite3.connect('student_db') # connect to database
c = db.cursor() # create cursor
 # create table
c.execute('''CREATE TABLE python_programming(
                                                  id INTEGER, 
                                                  name TEXT, 
                                                  grade INTEGER)''')


 # insert all values into table
c.execute("INSERT INTO python_programming VALUES (55,'Carl Davis',61)")
c.execute("INSERT INTO python_programming VALUES (66,'Dennis Fredrickson',88)")
c.execute("INSERT INTO python_programming VALUES (77,'Jane Richards',78)")
c.execute("INSERT INTO python_programming VALUES (12,'Peyton Sawyer',45)")
c.execute("INSERT INTO python_programming VALUES (2,'Lucas Brooke',99)")

 # select all records with grades between 60 and 80
c.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
print(c.fetchall())

 # change Carl's grade to 65
c.execute('''UPDATE python_programming SET grade = 65 WHERE id = 55 ''')

# delete Dennis' row
id=66
c.execute('''DELETE FROM python_programming WHERE id = ? ''',(id,))

 # change grade if id < 55
c.execute('''UPDATE python_programming SET grade = 100 WHERE id < 55 ''')

 # print all rows
c.execute("SELECT * FROM python_programming")
print(c.fetchall())
db.commit() # commit
db.close() # close db
