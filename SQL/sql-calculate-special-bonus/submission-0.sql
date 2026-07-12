SELECT 
    employee_id,
    salary * ((employee_id % 2 != 0) AND (LEFT(name, 1) != 'M'))::int AS bonus
FROM employees
ORDER BY employee_id;