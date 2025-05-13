"""
Завдання 2. SOLID
Перед вами спрощена програма для керування бібліотекою книг. Програма має можливість додавання нових книг,
видалення книг та відображення всіх книг у бібліотеці. Користувач має змогу взаємодіяти з програмою через командний рядок,
використовуючи команди add, remove, show та exit.
"""

from abc import ABC, abstractmethod
from log import info


# Щоб виконати принцип єдиної відповідальності (SRP), створіть клас Book, який відповідатиме за зберігання інформації про книгу.
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show(self):
        info(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

    def get_title(self):
        return self.title


# - Щоб забезпечити принцип відкритості/закритості (OCP), зробіть так, щоб клас Library міг бути розширений для нової функціональності
# без зміни його коду.
# - Щоб виконати принцип підстанови Лісков (LSP), переконайтеся, що будь-який клас, який наслідує інтерфейс LibraryInterface, може замінити клас
# Library без порушення роботи програми.
# - Щоб виконати принцип розділення інтерфейсів (ISP), використовуйте інтерфейс LibraryInterface для чіткої специфікації методів, які необхідні
# для роботи з бібліотекою library.
class LibraryInterface(ABC):
    def __init__(self):
        self.books = []

    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def remove_book(self):
        pass


class Library(LibraryInterface):
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            book.show()


class LibraryManager:
    # - Щоб виконати принцип інверсії залежностей (DIP), зробіть так, щоб класи вищого рівня, такі як LibraryManager, залежали від абстракцій
    # (інтерфейсів), а не від конкретних реалізацій класів.
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        self.library.add_book(Book(title, author, year))

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        for book in self.books:
            book.show()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
