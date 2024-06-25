import random

class library:
      def __init__(self):
          self.no_of_books = 0
          self.books = [] 
          self.boookno = 0

      def add_books(self, book):
          bookid = random.randint(100000000, 200000000)
          while self.boookno != bookid:
              self.boookno = bookid
              break

          with open("library_data.txt", "a") as file:
              file.write(f"{book},{bookid}\n")
          print(f"Book {book} added with book id {bookid}")

      def show_info(self):
          print(f"The library has {self.no_of_books} books. The books are:")
          with open("library_data.txt", "r") as file:
            print(f"Book ID:,            Title:\n    v                   v")
            for line in file:
                  book, bookid = line.strip().split(",")
                  print(f"{bookid}:      {book}")

      def search_book(self, search_term):
          with open("library_data.txt", "r") as file:
              for line in file:
                  book, bookid = line.strip().split(",")
                  if search_term == book or search_term == bookid:
                      print(f"Book ID: {bookid}, Title: {book}")
                      return
              print("Book not found.")

my_library = library()

inp = input("Do you want to add a book, view the library or search a specified book? (a,s,v): ").upper()
if inp == "A":
      book = input("Enter the name of the book you want to add: ")
      my_library.add_books(book)
elif inp == "S":
      search_term = input("Enter book name or ID to search: ")
      my_library.search_book(search_term)
elif inp == "V":
      my_library.show_info()