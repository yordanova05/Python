class LibraryBook:
    def __init__(self, id:int, title, author, price:float, copies:int):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies
        self.available = True
        
    def book_info(self):
        return (f"ID: {self.id}, title: {self.title}, author: {self.author}\
price: {self.price}, copies: {self.copies}, avaialbe: {self.available}")
           
    def __str__(self):
        return self.book_info() 
       
    def update_price(self):
        new_price = float(input("New price: "))  
        if new_price >= 0:
            self.price = new_price
        else:
            return ("The price can't be negative number!")
            
    def update_copies(self):
        new_copies = int(input("New copies:"))
        if new_copies > 0:
            self.copies = new_copies
            
        elif new_copies == 0:
            self.available = False
         
        else:
            return ("The copies can't be negative number!")

def find_book_by_id(books_list, id):
    if books_list:
        for book in books_list:
            if book.id == id:
                return book.book_info()
    else:
        return "Not defined book in the library!"
            
def find_by_author(book_list, author):
    matches = [a for a in book_list if a.author == author]
    if matches:
        for x in matches:
            print(x)
        return len(matches)
    else:
        return "Not books with this author was founded!"
    
def borrow_book(book_list, id, count):
    for book in book_list:
        if book.id == id:
            if book.copies >= count:
                book.copies -= count
                if book.copies == 0:
                    book.available = False
                return f"You succesfully borrowed this book!"
            else:
                return "The book doesn't have this much copies!"
    return "This book isn't in our library!"
    
                
book1 = LibraryBook(123, "Rekata", "Ïvan Klinch", 13.99, 1200)
book2 = LibraryBook(333, "It", "Steven King", 24.99, 3500)
book3 = LibraryBook(948, "Pod Igoto", "Steven King", 19.99, 1000)

booklist = [book1, book2, book3]

print(book1.book_info())
print(book2.book_info())
print(book3.book_info())

# book2.update_copies()
# book1.update_price()
print(book1.book_info())
print(book2.book_info())
print("_____----------------____")

print(find_book_by_id(booklist, 123))
print(find_by_author(booklist, "Steven King"))
print(borrow_book(booklist, 948, 1000))
print(book3.book_info())