SELECT co.Continent, FLOOR((AVG(c.Population)))
FROM CITY AS c
JOIN
COUNTRY co
ON
c.CountryCode = co.code
GROUP BY co.Continent
