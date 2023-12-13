
-------Daily Challenge: Tables Relationships-------

--Part I--

CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INT REFERENCES Customer(id)
);


INSERT INTO Customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');




INSERT INTO CustomerProfile (isLoggedIn, customer_id) VALUES
(true, (SELECT id FROM Customer WHERE first_name = 'John')),
(false, (SELECT id FROM Customer WHERE first_name = 'Jerome'));



--The first_name of the LoggedIn customers
SELECT Customer.first_name
FROM Customer
JOIN CustomerProfile  ON Customer.id = CustomerProfile.customer_id
WHERE CustomerProfile.isLoggedIn = true;

--All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT Customer.first_name, CustomerProfile.isLoggedIn
FROM Customer
LEFT JOIN CustomerProfile  ON Customer.id = CustomerProfile.customer_id;

--The number of customers that are not LoggedIn
SELECT COUNT (*) AS num_not_LoggedIn
FROM CustomerProfile 
 WHERE CustomerProfile.isLoggedIn = false;


-- even the customers those who don’t have a profile.
-SELECT COUNT(*) AS num_not_logged_in
FROM Customer 
LEFT JOIN CustomerProfile ON Customer.id = CustomerProfile.customer_id
WHERE CustomerProfile.isLoggedIn IS NULL 
OR CustomerProfile.isLoggedIn = false;


 --Part II--


--1
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL);
--2
INSERT INTO Book (title, author) 
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
		('Harry Potter', 'J.K Rowling'),
		('To Kill a Mockingbird', 'Harper Lee');

--3
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    age INT CHECK (age <= 15));

--4
INSERT INTO Student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

--5
CREATE TABLE Library (
    book_fk_id INT REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id));


--6
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date) VALUES
((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');


--7
SELECT * FROM Library;

SELECT Student.name, Book.title
FROM Library 
JOIN Student ON Library.student_fk_id = Student.student_id
JOIN Book  ON Library.book_fk_id = Book.book_id;



SELECT AVG(Student.age) AS average_age
FROM Library 
JOIN Student  ON Library.student_fk_id = Student.student_id
JOIN Book ON Library.book_fk_id = Book.book_id
WHERE Book.title = 'Alice In Wonderland';


DELETE FROM Student WHERE name = 'Bob';
-- delited row where student_fk_id == Student.student_id where Name "Bob"