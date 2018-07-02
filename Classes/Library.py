#!/usr/bin/python3.6
#!/usr/bin/env python3.6
#class = > Library
#Layer of abstraction =>display available books, to lend a book, to add a book
#Class => Customer
#Layers of abstraction =>request for a book, return a book
class Library:
    def __init__(self, listofBooks):
        self.availableBooks = listofBooks
    def displayAvailableBooks(self):
         print("Avaiable books in the Library ")
         count = 1
         for book in self.availableBooks:
                print("Book No:",count," = ",book)
                count +=1
    def lendBook(self, requestBook):
         if requestBook in self.availableBooks:
               print("You have now borrowed the book")
               self.availableBooks.remove(requestBook)
         else:
             print("Sorry, the books is not available in our list")        
    def addBook(self, requstedBook):
          self.availableBooks.append(requstedBook)
          print("You have returned the book. Thank you!")

class Customer:
      def requestBook(self):
          self.book = input("Enter the name of a book you would like to borrow")
          return self.book.split()
 
      def returnBook(self):
          self.book = input("Enter the name of the book which you want to return")
          return self.book.split()


books_list = input("Enter book names: ")
print(books_list.split())
library = Library(books_list.split())
#library = Library(['AAAA','BBBB','CCCC','DDDD'])
customer = Customer()
library.displayAvailableBooks()
print()
print("##############")
print()

while True:
#######   Print  #####################
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a books")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
######################################

    userchoice = int(input())
    if userchoice is 1:
         library.displayAvailableBooks()
    elif userchoice is 2:
         requestBook = customer.requestBook()
         library.lendBook(requestBook)
    elif userchoice is 3:
         returnBook = customer.returnBook()
         library.addBook(returnBook)
    elif userchoice is 4:
         quit()



