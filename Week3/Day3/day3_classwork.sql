

CREATE FUNCTION get_film_count(len_from INT, len_to INT)
RETURNS INT
LANGUAGE plpgsql
AS
$$
DECLARE 
    film_count INT;
BEGIN
    SELECT COUNT(*) INTO film_count
    FROM film 
    WHERE length BETWEEN len_from AND len_to;

    RETURN film_count;
END;
$$;