--Exercise 1 : Items And Customers
SELECT * FROM  public_items ORDER BY price;
SELECT * FROM public_items WHERE price > 80 OR price = 80 ORDER BY price DESC;
SELECT * FROM  public_customers ORDER BY first_name LIMIT 3;
SELECT last_name FROM  public_customers ORDER BY last_name DESC;



--Exercise 1 : Items And Customers
SELECT * FROM customer;
SELECT first_name || ' ' || last_name AS full_name FROM customer;
SELECT DISTINCT create_date FROM customer;
SELECT * FROM customer ORDER BY first_name DESC;
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;
SELECT address, phone  FROM address WHERE district ='Texas' ;
SELECT * FROM film WHERE film_id = 15 or film_id=150;
SELECT film_id, title, description, length, rental_rate FROM film  WHERE title like 'Back to the future%';
SELECT film_id, title, description, length, rental_rate FROM film  WHERE title like 'Ba%';
SELECT * FROM film ORDER BY replacement_cost LIMIT 10;
SELECT * FROM film ORDER BY replacement_cost OFFSET 10 LIMIT 10;
SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date 
FROM customer JOIN payment ON customer.customer_id = payment.customer_id ORDER BY customer.customer_id;
SELECT film.* FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id WHERE inventory.film_id IS NULL;
SELECT DISTINCT city.city,country.country from city LEFT JOIN country ON  city.country_id = country.country_id;
SELECT DISTINCT payment.staff_id, payment.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
FROM payment LEFT JOIN customer ON payment.customer_id = customer.customer_id;



