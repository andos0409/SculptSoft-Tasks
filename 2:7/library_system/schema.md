Book(
    BookID PK,
    Title,
    Author,
    ISBN UNIQUE,
    Genre,
    PublishedYear,
    TotalCopies,
    AvailableCopies
)

Member(
    MemberID PK,
    FullName,
    Email UNIQUE,
    Phone,
    MembershipDate
)

Loan(
    LoanID PK,
    MemberID FK,
    BookID FK,
    BorrowDate,
    DueDate,
    ReturnDate,
    Status
)