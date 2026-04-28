use project_1;

-- Total Numbers --

SELECT COUNT(*) AS total_customers FROM customers;
SELECT COUNT(*) AS total_products FROM products;
SELECT COUNT(*) AS total_orders FROM orders;

-- Most frequently ordered products --

SELECT product_id, COUNT(*) AS order_count
FROM order_items
GROUP BY product_id
ORDER BY order_count DESC;

-- Average Order Value --
-- 1st without discount 2nd with discount

SELECT AVG(total_amount) AS avg_order_value
FROM (
  SELECT order_id, SUM(quantity * (1 - discount)) AS total_amount
  FROM order_items
  GROUP BY order_id
) AS order_totals;

SELECT AVG(total_amount) AS avg_order_value
FROM (
  SELECT order_id, SUM(quantity) AS total_amount
  FROM order_items
  GROUP BY order_id
) AS order_totals;

-- Revenue over time --

SELECT 
  DATE_FORMAT(order_date, '%Y-%m') AS month,
  SUM(quantity * (1 - discount)) AS revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY month;

-- Top 5 states by revenue --

SELECT c.state, SUM(oi.quantity * (1 - oi.discount)) AS revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.state
ORDER BY revenue DESC
LIMIT 5;

-- New vs Returning customers monthly --

SELECT 
  MONTH(order_date) AS month,
  COUNT(DISTINCT customer_id) AS customers
FROM orders
GROUP BY MONTH(order_date);

-- Top 10 customers by lifetime value --

SELECT c.first_name, c.last_name,
       SUM(oi.quantity * (1 - oi.discount)) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.first_name, c.last_name
ORDER BY total_spent DESC
LIMIT 10;

-- Gender-wise spending distribution --
SELECT c.gender, 
       SUM(oi.quantity * (1 - oi.discount)) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.gender;

-- Churn prediction (based on last order date) --

SELECT 
  customer_id,
  MAX(order_date) AS last_order_date,
  CASE 
    WHEN MAX(order_date) < CURDATE() - INTERVAL 90 DAY THEN 'Churned'
    ELSE 'Active'
  END AS status
FROM orders
GROUP BY customer_id;

-- Best-selling products (by quantity) --

SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

-- Best-selling products (by revenue) --

SELECT p.product_name,
       SUM(oi.quantity * (1 - oi.discount)) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;

-- Product category-wise revenue --

SELECT p.category,
       SUM(oi.quantity * (1 - oi.discount)) AS revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category;

-- Profit margin analysis --
-- Profit = unit_price - cost_price --

SELECT product_name,
       unit_price - cost_price AS profit_per_unit
FROM Products;

-- Underperforming products --

SELECT product_id, SUM(quantity) AS total_sold
FROM order_items
GROUP BY product_id
HAVING total_sold < 10;

-- Average shipping time --

SELECT AVG(DATEDIFF(shipping_date, order_date)) AS avg_shipping_days
FROM orders o
JOIN shipping s ON o.order_id = s.order_id;

-- Delayed vs On-time delivery --

SELECT 
  CASE 
    WHEN shipping_status = 'Delivered' THEN 'On Time'
    ELSE 'Delayed'
  END AS delivery_type,
  COUNT(*) AS total
FROM Shipping
GROUP BY delivery_type;

-- CASE WHEN (customer segmentation) --

SELECT customer_id,
       CASE 
         WHEN COUNT(order_id) = 1 THEN 'New'
         ELSE 'Returning'
       END AS type
FROM orders
GROUP BY customer_id;

-- Joins across multiple tables --

SELECT c.first_name, SUM(oi.quantity) AS total_items
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.first_name;

