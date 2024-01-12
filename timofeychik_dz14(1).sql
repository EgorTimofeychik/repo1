-- SQLite
CREATE TABLE Departments (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(50)
);

INSERT INTO Departments (ID, NAME) VALUES (1, 'Managment');
INSERT INTO Departments (ID, NAME) VALUES (2, 'HRs');
INSERT INTO Departments (ID, NAME) VALUES (3, 'Sales');
INSERT INTO Departments (ID, NAME) VALUES (4, 'Software Development');
INSERT INTO Departments (ID, NAME) VALUES (5, 'Support');
INSERT INTO Departments (ID, NAME) VALUES (6, 'RND');

CREATE TABLE Employee (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(50),
    DEPARTMENT_ID INTEGER,
    ROLE VARCHAR(50),
    MANAGER_ID INTEGER
);

INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (1, 'James Smith', 1, 'CEO', NULL);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (2, 'Sarah Goldman', 1, 'CFO', 1);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (3, 'Wayne Ablet', 1, 'CIO', 1);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (4, 'Michelle Carey', 2, 'HR Manager', 1);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (5, 'Chris Matthews', 3, 'Sales Manager', 2);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (6, 'Andrew Judy', 4, 'Development Manager', 3);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (7, 'Daniele McLeon', 5, 'Support Manager', 3);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (8, 'Matthew Swan', 2, 'HR Representative', 4);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (9, 'Stephanie Richardson', 2, 'Salesperson', 5);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (10, 'Tony Stark', 3, 'Salesperson', 5);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (11, 'Jenna Lockett', 4, 'Front-End Developer', 6);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (12, 'Michael Dunstall', 4, 'Back-End Developer', 6);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (13, 'Jane Voss', 4, 'Back-End Developer', 6);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (14, 'Anthony Hird', 5, 'Support', 7);
INSERT INTO Employee (ID, NAME, DEPARTMENT_ID, ROLE, MANAGER_ID) VALUES (15, 'Natalie Rocca', 5, 'Support', 7);

SELECT e.NAME, e.ROLE, d.NAME AS DepartmentName
FROM Employee e
INNER JOIN Departments d ON e.DEPARTMENT_ID = d.ID;

SELECT m.NAME AS ManagerName
FROM Employee e
INNER JOIN Employee m ON e.MANAGER_ID = m.ID
WHERE e.NAME = 'Tony Stark';

SELECT d.NAME AS DepartmentName, e.NAME AS EmployeeName
FROM Departments d
LEFT JOIN Employee e ON d.ID = e.DEPARTMENT_ID;