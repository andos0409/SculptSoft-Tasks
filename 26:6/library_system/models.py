class Book:

    def __init__(self, BookID, Title, Author, 
                 ISBN, Genre, PublishedYear, TotalCopies=1,
                 AvailableCopies=1):
        self.BookID = BookID
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN
        self.Genre = Genre
        self.PublishedYear = PublishedYear
        self.TotalCopies = TotalCopies
        self.AvailableCopies = AvailableCopies
    
    def new_book(self, connection):

        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO Book
            (BookID, Title, Author, ISBN, Genre, PublishedYear, TotalCopies, AvailableCopies)
        VALUES 
            (%s, %s, %s, 
            %s, %s, %s, 
            %s, %s)
        """, (self.BookID, self.Title, self.Author, self.ISBN,
                self.Genre, self.PublishedYear, self.TotalCopies, self.AvailableCopies)
        )

        connection.commit()
    
    def add_copy(self, connection):

        self.AvailableCopies += 1
        self.TotalCopies += 1

        cursor = connection.cursor()

        cursor.execute(
        """
        UPDATE Book
        SET TotalCopies = %s, AvailableCopies = %s
        WHERE BookID = %s
        """, (self.TotalCopies, self.AvailableCopies, self.BookID)
        )

        connection.commit()

        
        

class LibMember:
    
    def __init__(self, MemberID, FullName, Email,
                 Phone, MembershipDate):
        self.MemberID = MemberID
        self.FullName = FullName
        self.Email = Email
        self.Phone = Phone
        self.MembershipDate = MembershipDate
    
    def add_member(self, connection):

        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO LibMember
            (MemberID, FullName, Email, Phone, MembershipDate)
        VALUES 
            (%s, %s, %s, 
            %s, %s)
        """, (self.MemberID, self.FullName, self.Email, self.Phone, self.MembershipDate)
        )

        connection.commit()

        


class Loan:

    def __init__(self, LoanID, MemberID, BookID,
                 BorrowDate, DueDate, ReturnDate, book, 
                 libmember, LoanStatus='Not Due Yet'):
        
        self.LoanID = LoanID
        self.MemberID = MemberID
        self.BookID = BookID
        self.BorrowDate = BorrowDate
        self.DueDate = DueDate
        self.ReturnDate = ReturnDate
        self.LoanStatus = LoanStatus
        self.book = book
        self.libmember = libmember
        
    def issue_loan(self, connection):
        self.book.AvailableCopies -= 1

        cursor = connection.cursor()

        cursor.execute(
        """
        INSERT INTO Loan 
            (LoanID, MemberID, BookID, BorrowDate, DueDate, ReturnDate, LoanStatus)
        VALUES 
            (%s, %s, %s, 
            %s, %s, %s, 
            %s)
        """, (self.LoanID, self.MemberID, self.BookID, 
            self.BorrowDate, self.DueDate, self.ReturnDate, 
            self.LoanStatus)
        )

        cursor.execute(
        """
        UPDATE Book
        SET AvailableCopies = %s
        WHERE BookID = %s
        """, (self.book.AvailableCopies, self.BookID)
        )

        connection.commit()
    


    def return_book(self, connection, return_date):
        self.book.AvailableCopies += 1

        if return_date <= self.DueDate:
            self.LoanStatus = 'Returned By Due'
        else: 
            self.LoanStatus = 'Returned After Due'

        self.ReturnDate = return_date

        cursor = connection.cursor()

        cursor.execute(
        """
        UPDATE Loan
        SET LoanStatus = %s,
            ReturnDate = %s
        WHERE LoanID = %s
        """,
        (self.LoanStatus, self.ReturnDate, self.LoanID)
        )

        cursor.execute(
        """
        UPDATE Book
        SET AvailableCopies = %s
        WHERE BookID = %s
        """, (self.book.AvailableCopies, self.BookID)
        )

        connection.commit()