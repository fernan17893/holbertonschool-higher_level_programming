-- lists all cities contained in database hbtn_0d_usa
-- results should be in acending order by cities.id
SELECT c.id, c.name, s.name
FROM cities as c
INNER JOIN cities AS s
ON c.state_id = s.id
ORDER BY c.id ASC;
