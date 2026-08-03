/*
Enter your query here.
*/
SELECT 
    CASE 
        WHEN Grades.Grade < 8 THEN 'NULL' 
        ELSE Students.Name 
    END AS StudentName,
    Grades.Grade,
    Students.Marks
FROM 
    Students, Grades 
WHERE 
    Students.Marks >= Grades.Min_mark AND Students.Marks <= Grades.Max_mark 
ORDER BY 
    Grades.Grade DESC, Students.Name;
