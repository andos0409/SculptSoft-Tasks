CREATE DATABASE librarysystem_db;
USE librarysystem_db;

CREATE TABLE Book (
	BookID INT NOT NULL,
    Title VARCHAR(50) NOT NULL,
    Author VARCHAR (40) NOT NULL,
    ISBN CHAR(13) UNIQUE NOT NULL,
    Genre ENUM("Fiction", "Non-Fiction", "Fantasy", "Science Fiction", "Mystery", "Thriller", "Romance"),
    PublishedYear YEAR,
    TotalCopies INT NOT NULL,
    AvailableCopies INT NOT NULL,
    PRIMARY KEY (BookID)
);

CREATE TABLE LibMember (
	MemberID INT NOT NULL,
    FullName VARCHAR(40) NOT NULL,
    Email VARCHAR(40) UNIQUE NOT NULL,
    Phone CHAR(8) NOT NULL,
    MembershipDate DATE NOT NULL,
    PRIMARY KEY (MemberID)
);

CREATE TABLE Loan(
    LoanID INT NOT NULL,
    MemberID INT NOT NULL,
    BookID INT NOT NULL,
    BorrowDate DATE NOT NULL,
    DueDate DATE NOT NULL,
    ReturnDate DATE,
    LoanStatus ENUM('Not Due Yet', 'Due Today', 'Overdue', 'Returned By Due', 'Returned After Due') NOT NULL,
    PRIMARY KEY (LoanID),
    FOREIGN KEY (MemberID) REFERENCES LibMember(MemberID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID)
);