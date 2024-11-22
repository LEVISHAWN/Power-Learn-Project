# Base class Book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading the book '{self.title}' by {self.author}.")

    def book_info(self):
        print(f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}")


# class Ebook inheriting from Book
class Ebook(Book):
    def __init__(self, title, author, year, file_size, file_format):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.file_format = file_format

    def download(self):
        print(f"Downloading the Ebook '{self.title}'.")

    def book_info(self):
        super().book_info()
        print(f"File Size: {self.file_size} MB, File Format: {self.file_format}")
