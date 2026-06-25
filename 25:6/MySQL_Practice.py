import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "H2.p1r8st",
    database = "business_db"
)

cursor = connection.cursor()

# Listing every employee working on 'Customer Churn Predictor'
cursor.execute("""
               SELECT E.EmpName
               FROM EmployeeProject EP 
               INNER JOIN Employee E 
               ON E.EmployeeID = EP.EmployeeID
               INNER JOIN Project P
               ON P.ProjectID = EP.ProjectID
               WHERE P.ProjectName = 'Customer Churn Prediction';
               """)

rows = cursor.fetchall()

for row in rows:
    print(row[0])

# Listing highest-paid employee based on their latest salary record

cursor.execute("""
            SELECT E.EmpName
            FROM Employee E
            INNER JOIN SalaryRecord SR
                ON E.EmployeeID = SR.EmployeeID
            WHERE SR.SalaryDate = (
                SELECT MAX(SR2.SalaryDate)
                FROM SalaryRecord SR2
                WHERE SR2.EmployeeID = SR.EmployeeID
            )
            AND SR.Amount = (
                SELECT MAX(SR1.Amount)
                FROM SalaryRecord SR1
                WHERE SR1.SalaryDate = (
                    SELECT MAX(SR3.SalaryDate)
                    FROM SalaryRecord SR3
                    WHERE SR3.EmployeeID = SR1.EmployeeID
                )
            );
               """)

rows = cursor.fetchall()

print('Highest Salary Employee:')
for row in rows:
    print(row[0])

cursor.close()
connection.close()