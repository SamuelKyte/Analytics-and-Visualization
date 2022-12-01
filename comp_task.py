''' got help here: https://www.youtube.com/watch?v=pd-0G0MigUA'''

import sqlite3 # import package
from books import Book # imports class from py file
conn=sqlite3.connect('book.db') # create a database and connect
c = conn.cursor() # create a cursor

 # create a table
c.execute("""CREATE TABLE books (
            id integer,
            title text,
            author text,
            qty integer
            )""")
 # create function to insert book
def insert_book(b):
  with conn: # connect to db
      c.execute("INSERT INTO books VALUES (:id, :title, :author, :qty)", {'id': b.id, 'title':  b.title, 'author':  b.author, 'qty':  b.qty}) # insert values

def update_bid(title, id): # create function to update book's id
  with conn: # connect to db
    c.execute("""UPDATE books SET id = :id
                WHERE title = :title""", {'title': title, 'id': id}) # update id
    
def update_btitle(id, title): # create function to update book's title
  with conn: # connect to db
    c.execute("""UPDATE books SET title = :title
                WHERE id = :id""", {'id': id, 'title': title}) # update title
    
def update_bauth(id, author): # create function to update book's author
  with conn: # connect to db
    c.execute("""UPDATE books SET author = :author
                WHERE id = :id""", {'id': id, 'author': author}) # update author
    
def update_bqty(id, qty): # create function to update qty
  with conn: # connect to db
    c.execute("""UPDATE books SET qty = :qty
                WHERE id = :id""", {'id': id, 'qty': qty}) # update qty

def del_book(id): # create function to delete book
  with conn: # connect to db
    c.execute("""DELETE FROM books WHERE id = :id""", {'id': id}) # delete entry

def search_book(id): # create function to search for book by id
    c.execute("SELECT * FROM books WHERE id = :id", {'id': id})
    print(c.fetchall()) # print entries with id

 # task listed book values
 # run books through class from py file
b_1 = Book(3001, 'A Tale of Two Cities', 'Charles Dickens', 30)
b_2 = Book(3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40)
b_3 = Book(3003, 'The Lion, the Witch, and the Wardrobe', 'C. S. Lewis', 25)
b_4 = Book(3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37)
b_5 = Book(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)

 # insert books into db
insert_book(b_1)
insert_book(b_2)
insert_book(b_3)
insert_book(b_4)
insert_book(b_5)

menu = 0 # give menu a value

 # create a while loop for menu
while menu != -1:
   # generate menu
  menu = int(input("""
Menu Selection
==============
1. Enter Book
2. Update Book
3. Delete Book
4. Search Book
0. Exit

Selection: """))
   # enter a new book function
  if menu == 1:
       # create variables for new class object
      id = int(input("Enter book's id number: "))
      title = input("What is the book's title: ")
      author = input("What is the book's author: ")
      qty = int(input("What is the qty in stock: "))
      new_book = Book(id, title, author, qty) # create class object
      insert_book(new_book) # insert class object into db
      print(search_book(id)) # print object
      pass
  elif menu == 2: # update menu
      up_menu = 0
      while up_menu != -1: # while loop for update menu
          up_menu = int(input("""
Menu Selection
==============
1. Update ID
2. Update Title
3. Update Author
4. Update Qty
0. Exit

Selection: """))
          if up_menu == 1: # update id num
              title = input("What is the book's title: ")
              id = int(input("Enter book's new id number: "))
              update_bid(title, id)
              pass
          elif up_menu == 2: # update title
              id = int(input("Enter book's id number: "))
              title = input("What is the book's new title: ")
              update_btitle(id, title)
              pass
          elif up_menu == 3: # update author
              id = int(input("Enter book's id number: "))  
              author = input("What is the book's author: ")
              update_bauth(id, author)
              pass
          elif up_menu == 4: # update qty
              id = int(input("Enter book's id number: "))
              qty = int(input("What is the new qty in stock: "))
              update_bqty(id, qty)
              pass
          elif up_menu == 0: # return to main menu
            up_menu -=1
  elif menu == 3: # delete option
      id = int(input("Enter book's id number: "))
      del_book(id) # delete book
      c.execute("SELECT * FROM books") # select table
      print(c.fetchall()) # print all non-deleted entries
      pass
  elif menu == 4: # search for book
      id = int(input("What is the book's ID number: "))
      search_book(id)
      pass
  
  elif menu == 0: # exit
      print("Goodbye")
      menu -= 1

'''Please check dropbox folder if you do not have books.py file. This is my imported class; program will not work without it.'''