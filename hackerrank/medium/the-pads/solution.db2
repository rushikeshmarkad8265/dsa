
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
-- Query 1: Format name and first letter of occupation
-- Query 1: Format name and first letter of occupation
SELECT NAME || '(' || SUBSTR(OCCUPATION, 1, 1) || ')'
FROM OCCUPATIONS
ORDER BY NAME;

-- Query 2: Count occupations and format the summary text
SELECT 'There are a total of ' || CHAR(COUNT(OCCUPATION)) || ' ' || LOWER(OCCUPATION) || 's.'
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION) ASC, OCCUPATION ASC;

