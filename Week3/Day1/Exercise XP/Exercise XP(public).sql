-- create schema publik


CREATE TABLE items (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    price INTEGER NOT NULL
);
CREATE TABLE customers (
    id SERIAL PRIMARY KEY NOT NULL unique,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

insert into items (id, name, price) 
values 
(1,'Small Desk', 100),
(2 ,'Large desk', 300),
(3, 'Fan', 80);

insert into customers (first_name, last_name)
values 

('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

select * from items;
select * from items where price >80;
select * from items where price <300 or price=300;
select * from customers where last_name='Smith';
select * from customers where last_name='Jones';
select * from customers where last_name !='Scott';



  
 
 
