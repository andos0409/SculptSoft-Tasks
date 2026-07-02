from db import get_connection
from models import Book, LibMember, Loan
from datetime import date

connection = get_connection()

book1 = Book(1, "Dune", "Frank Herbert", "9780441172719", "Fiction", 1965, 3, 3)
book2 = Book(2, "1984", "George Orwell", "9780451524935", "Fiction", 1949, 2, 2)

member1 = LibMember(101, "Tom Andrew", "tom@example.com", "04000001", date(2026, 6, 1))
member2 = LibMember(102, "John Smith", "john@example.com", "04000002", date(2026, 6, 3))

book1.new_book(connection)
book2.new_book(connection)

member1.add_member(connection)
member2.add_member(connection)

loan1 = Loan(
    1001,
    member1.MemberID,
    book1.BookID,
    date(2026, 6, 10),
    date(2026, 6, 24),
    None,
    book1,
    member1
)

loan1.issue_loan(connection)

loan1.return_book(connection, date(2026, 6, 22))