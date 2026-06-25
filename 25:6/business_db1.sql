CREATE DATABASE business_db;
USE business_db;

CREATE TABLE Department (
	DeptID INT NOT NULL,
    DeptName VARCHAR(40) NOT NULL,
    Location VARCHAR(40),
    PhoneNumber CHAR(12) NOT NULL,
    ManagerID INT,
    PRIMARY KEY (DeptID)
);

CREATE TABLE Employee (
	EmployeeID INT AUTO_INCREMENT NOT NULL,
    EmpName VARCHAR(40) NOT NULL,
    Email VARCHAR(40) NOT NULL UNIQUE,
    DOB DATE NOT NULL,
    HireDate DATE NOT NULL,
    JobTitle VARCHAR(40) NOT NULL,
    DeptID INT NOT NULL,
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);

CREATE TABLE SalaryRecord (
	SalaryDate DATE NOT NULL,
    EmployeeID INT NOT NULL,
    PayGrade ENUM('A', 'B', 'C', 'D') NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (EmployeeID, SalaryDate),
    FOREIGN KEY (EmployeeID) REFERENCES Employee (EmployeeID)
);

CREATE TABLE Project (
	ProjectID INT NOT NULL,
    ProjectName VARCHAR(50) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Budget DECIMAL(14, 2),
    PRIMARY KEY (ProjectID)
);

CREATE TABLE EmployeeProject (
	ProjectID INT NOT NULL,
    EmployeeID INT NOT NULL,
    HoursWorked INT NOT NULL,
    EmployeeRole VARCHAR(40) NOT NULL,
    PRIMARY KEY (ProjectID, EmployeeID),
    FOREIGN KEY (ProjectID) REFERENCES Project (ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee (EmployeeID)
);

ALTER TABLE Department
ADD FOREIGN KEY (ManagerID) REFERENCES Employee(EmployeeID);

INSERT INTO Department (DeptID, DeptName, Location, PhoneNumber)
VALUES 
	(101, 'AI', 'Delhi', '+9119383889'),
	(102, 'Advisory', 'Mumbai', '+9119383880'),
    (103, 'Banking', 'Kolkata', '+9119383810');

INSERT INTO Project (ProjectID, ProjectName, StartDate, EndDate, Budget)
VALUES
	(1, 'Customer Churn Prediction', '2025-01-10', '2025-06-30', 120000.00),
	(2, 'Employee Portal Upgrade', '2025-03-01', NULL, 200000.00),
	(3, 'Budget Forecasting System', '2025-02-15', '2025-09-30', 150000.00);
    
INSERT INTO Employee (EmpName, Email, DOB, HireDate, JobTitle, DeptID)
VALUES
('Maya Chen', 'maya.chen@company.com', '1995-04-12', '2022-01-15', 'Data Analyst', 102),
('Liam Patel', 'liam.patel@company.com', '1992-08-20', '2021-03-10', 'Software Engineer', 101),
('Noah Smith', 'noah.smith@company.com', '1988-11-05', '2019-07-01', 'Finance Manager', 103),
('Ava Wilson', 'ava.wilson@company.com', '1997-02-17', '2023-02-01', 'ML Engineer', 101),
('Ethan Brown', 'ethan.brown@company.com', '1994-06-30', '2020-09-12', 'Backend Developer', 103),
('Pranav Gandham', 'raj.gandham@company.com', '1993-09-29', '2022-09-29', 'Manager', '103'),
('Andy Singh', 'and.s@company.com', '1993-09-29', '2022-09-29', 'Manager', '102'),
('Paul Joseph', 'paul.j@company.com', '1993-09-29', '2022-09-29', 'Manager', '101');

UPDATE Department
SET ManagerID = 13
WHERE DeptID = 101;

UPDATE Department
SET ManagerID = 12
WHERE DeptID = 102;

UPDATE Department
SET ManagerID = 11
WHERE DeptID = 103;

INSERT INTO EmployeeProject (ProjectID, EmployeeID, HoursWorked, EmployeeRole)
VALUES
(1, 6, 120, 'Data Analyst'),
(1, 9, 160, 'ML Engineer'),
(1, 13, 40, 'Project Manager'),
(2, 7, 180, 'Software Engineer'),
(2, 10, 140, 'Backend Developer'),
(2, 12, 50, 'Project Manager'),
(3, 8, 130, 'Finance Manager'),
(3, 11, 60, 'Project Manager'),
(3, 6, 80, 'Data Analyst');

INSERT INTO SalaryRecord (SalaryDate, EmployeeID, PayGrade, Amount)
VALUES
('2024-01-01', 6, 'B', 85000.00),
('2025-01-01', 6, 'A', 92000.00),
('2024-01-01', 7, 'A', 105000.00),
('2025-01-01', 7, 'A', 112000.00),
('2024-01-01', 8, 'A', 115000.00),
('2025-02-01', 9, 'B', 90000.00),
('2024-07-01', 10, 'B', 95000.00),
('2024-01-01', 11, 'A', 125000.00),
('2024-01-01', 12, 'A', 120000.00),
('2024-01-01', 13, 'A', 122000.00);
