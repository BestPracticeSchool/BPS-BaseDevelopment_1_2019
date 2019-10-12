class Book:
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    def get_pages(self):
        return "There are " + str(self.page) + " in the book"

    @classmethod
    def new_book(cls, new_title, new_author, new_page):
        return cls(new_title, new_author, new_page)


class Magazine(Book):
    pass




my_book = Book("LOTR", "Lol Kek", 1200)
my_new_book = my_book.new_book("Warcraft", "Blizzard", 1450)
print(type(my_new_book))
my_magazine = Magazine("FORBES", "Jhon Forbes", 100)
print(my_book.get_pages())
print(my_new_book.get_pages())
print(my_magazine.get_pages())

my_new_magazine = my_magazine.new_book("asd","asd", 12321)
print(type(my_new_magazine))
