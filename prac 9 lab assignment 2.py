class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title):
        self.books.append(Book(title))

    def add_member(self, name):
        self.members.append(Member(name))

    def lend_book(self, title, member_name):
        for b in self.books:
            if b.title == title and b.available:
                for m in self.members:
                    if m.name == member_name:
                        b.available = False
                        m.books.append(title)
                        return

    def return_book(self, title, member_name):
        for b in self.books:
            if b.title == title:
                for m in self.members:
                    if m.name == member_name and title in m.books:
                        b.available = True
                        m.books.remove(title)
                        return

    def display_books(self):
        for b in self.books:
            print(b.title, b.available)


lib = Library()

while True:
    print("1 Add Book")
    print("2 Add Member")
    print("3 Lend Book")
    print("4 Return Book")
    print("5 Display Books")
    print("6 Exit")

    ch = int(input())

    if ch == 1:
        t = input()
        lib.add_book(t)
    elif ch == 2:
        n = input()
        lib.add_member(n)
    elif ch == 3:
        t = input()
        n = input()
        lib.lend_book(t, n)
    elif ch == 4:
        t = input()
        n = input()
        lib.return_book(t, n)
    elif ch == 5:
        lib.display_books()
    elif ch == 6:
        break