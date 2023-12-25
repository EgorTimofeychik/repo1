class Publication:
    publisher = "Издательство"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"Заголовок: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год выпуска: {self.year}")
        print(f"Издательство: {self.publisher}")


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f"ISBN: {self.isbn}")


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        super().display()
        print(f"Номер выпуска: {self.issue_number}")


publication = Publication("Название публикации", "Автор публикации", 2022)
book = Book("Название книги", "Автор книги", 2021, "ISBN-123456")
magazine = Magazine("Название журнала", "Автор журнала", 2022, "№1")

publication.display()
print()
book.display()
print()
magazine.display()