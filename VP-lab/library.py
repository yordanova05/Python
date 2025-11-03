class Book:
    def __init__(self, name, author, year):
        self.name = name 
        self.author = author
        self.year = year
        self.is_available = True
        self.times_borrowd = 0
        
    def information(self):
        print(f"Заглавие: {self.name}, Автор: {self.author}, Година: {self.year}")
        
    def rent_the_book(self):
        if self.is_available == True:
            print(f"Вие наехте книгата: {self.name}")
            self.is_available = False
            self.times_borrowd+=1
        else:
            print(f"Книгата {self.name} е вече заета")
            
    def return_the_book(self):
        if self.is_available == True:
            print(f"Няма как да върнете {self.name} като вече е върната!")
        else:
            print(f"Вие върнахте книфгата {self.name}")
            self.is_available = True
            
    def times_borrowed_book(self):
        print(f"{self.name} е наемана вече {self.times_borrowd} пъти!")
            
class Library:
    def __init__(self):
        self.library = []
        self.avaliable_books = []
        self.library_user = {}
        
    def add_book(self,book):
        self.library.append(book)
        if book.is_available:
            self.avaliable_books.append(book) 
    
    def show_available_books(self):
        for name in self.avaliable_books:
            print(name, end = " ")
        return ""
    
    def rent_book(self, user, name):
        if not user in self.library_user:
            self.library_user[user] = []
            
        if len(self.library_user[user]) >= 3:
            print(f"Потребителят '{user}' не може да наеме повече от 3 книги наведнъж.")
            return
        
        for book in self.library:
            if book.name == name:
                if book.is_available:
                    book.rent_the_book()
                    self.library_user[user].append(book)
                else:
                    print(f"Книгата '{name}' вече е заета.")
                return

        print(f"Книга със заглавие '{name}' не беше намерена в библиотеката.")
        
    def return_book(self,user,title):
        if user in self.library_user:
            for book in self.library:
                if book.name == title: 
                    book.return_the_book()
                    self.library_user[user].remove(book)
                    return
            print(f"Потребителят '{user}' не е наемал книгата '{title}'.")
        else:
            print(f"Book with title ({title}) was not found in the library")
            
    def borrowed_books(self):
        borrowed = [book for book in self.library if not book.is_available]
        if borrowed:
            print("Заети книги:")
            for book in borrowed:
                print(book.name)
        else:
            print("Вмомента няма заети книги!")
            
    def find_by(self,keyword):
        matches = [book for book in self.library if keyword.lower() in book.name.lower() or keyword.lower() in book.author.lower()]
        if matches:
            print("Matches: ")
            for book in matches:
                book.information()
        else:
            print("Няма намерени книги по зададения критерий!")
            
            
            
            
library = Library()
book1 = Book("The new neighbor", "Steven King", 2003)
book2 = Book("Story", "Adam Gary", 1977)
book3 = Book("It", "Steven King", 1999)
book4 = Book("The great wall", "Jennifer Grose", 2020)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.show_available_books()

library.rent_book("Ivan","It")
library.rent_book("Ivan","Story")
library.rent_book("Ivan","The new neighbor")

library.rent_book("Ivan","The great wall")

library.return_book("Ivan","It")

library.borrowed_books()

library.find_by("wall")
library.find_by("King")
library.find_by("The")

# library.show_available_books()

book1.times_borrowed_book()
            
        