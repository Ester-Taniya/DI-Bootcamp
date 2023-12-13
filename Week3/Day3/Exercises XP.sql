
------Exercise 1: DVD Rental------


--1
SELECT * FROM language;

--2
SELECT film.title, film.description, language.name
FROM film
JOIN language ON film.language_id = language.language_id;

--3
SELECT film.title, film.description ,language.name
FROM language
LEFT JOIN film ON language.language_id = film.language_id;


--4
CREATE TABLE new_film (id SERIAL PRIMARY KEY,name VARCHAR(255));

INSERT INTO new_film (name) VALUES
('Back to the Future'),
('Back to the Future Part II'),
('Back to the Future Part III');


--5
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY NOT NULL,
   film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP);


--6
INSERT INTO customer_review (film_id, language_id, title, score, review_text) VALUES
(1, 1, 'Great movie', 9, 'the movie was great'),
(2, 2, 'Good', 8, 'second part of "Back to the future" , still good');


--7
DELETE FROM new_film WHERE id = 2;

--SELECT * FROM customer_review;









-------------------------------------------------------------------------------------------------------------------------











------Exercise 2 : DVD Rental--------

--1
UPDATE film
SET language_id = 2
WHERE film_id <10;''
--select * from film where film_id <10;

--2
--foreign keys (references) are defined for the customer table : 
-- stote_id(f_key to connection with STORE table ), address_id f_key to connection with ADDRESS table )
-- and customer_id  is a f_key in tables : Rrental, payment
-- f_key it's connection/relationship between  different tables 
--f_key in 1 st table must be exsist as prymery key in 2nd tabel



--3


-- f. key chekker :
SELECT
    conname AS foreign_key_name,
    conrelid::regclass AS table_name,
    a.attname AS column_name
FROM
    pg_constraint AS c
JOIN
    pg_attribute AS a ON a.attnum = ANY(c.conkey)
WHERE
    confrelid = 'customer_review'::regclass;
-- if prymery key in this table == f key in other tables we can't dropp the table 

-- avoid an error if the table doesn't exist
DROP TABLE IF EXISTS customer_review;


--4
SELECT COUNT(rental_id) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;


--5
SELECT film.title
---,film.rental_rate,inventory.inventory_id,rental.return_date 
--(if this columns are nead)
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE rental.return_date IS NULL
ORDER BY film.rental_rate DESC
LIMIT 30;


--6

SELECT title
FROM film
WHERE description ILIKE '%sumo%' 
AND film_id IN 
(   SELECT film_id 
    FROM film_actor
    WHERE actor_id = (SELECT actor_id FROM actor
    WHERE first_name = 'Penelope' AND last_name = 'Monroe'));

--
SELECT title
FROM film
WHERE length < 60 AND rating = 'R';

 -- 
 SELECT title
FROM film
where rental_rate >4.00 and film_id in (
	SELECT inventory.film_id
    FROM rental  
	JOIN inventory ON rental.inventory_id = inventory.inventory_id
    JOIN customer ON rental.customer_id = customer.customer_id
	WHERE customer.first_name = 'Matthew'AND customer.last_name = 'Mahan' 
	AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01' )

--
SELECT title
FROM film
WHERE description ILIKE '%boat%' OR title ILIKE '%boat%'
and film_id in (
	SELECT inventory.film_id
    FROM rental  
	JOIN inventory ON rental.inventory_id = inventory.inventory_id
    JOIN customer ON rental.customer_id = customer.customer_id
	WHERE customer.first_name = 'Matthew'AND customer.last_name = 'Mahan') 
	order by film.replacement_cost DESC
	LIMIT 1;
 
 




























