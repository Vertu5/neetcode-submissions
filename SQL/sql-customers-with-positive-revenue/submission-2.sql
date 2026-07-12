SELECT customer_id
FROM customers
GROUP BY customer_id
HAVING SUM(revenue) FILTER (WHERE year = 2020) > 0;