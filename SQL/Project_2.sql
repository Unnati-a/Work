create database project_2;
use project_2;

create table customers (
customer_id int primary key,
first_name varchar(50),
last_name varchar(50),
email varchar(70),
resigtration_date date);

insert into customers values
(1, 'Mickey', 'Mouse', 'mickey@toonmail.com', '2023-01-15'),
(2, 'Donald', 'Duck', 'donald@toonmail.com', '2023-07-20'),
(3, 'Tom', 'Cat', 'tom@toonmail.com', '2024-02-10'),
(4, 'Jerry', 'Mouse', 'jerry@toonmail.com', '2024-11-05'),
(5, 'Scooby', 'Doo', 'scooby@toonmail.com', '2025-03-18');

create table orders (
order_id int primary key,
customer_id int,
order_date date,
total_amount int,
foreign key (customer_id) references customers(customer_id));

insert into orders values
(101, 1, '2023-02-01', 450),
(102, 2, '2023-08-05', 1200),
(103, 1, '2024-01-12', 1800),
(104, 2, '2024-03-22', 700),
(105, 4, '2024-12-01', 950),
(106, 5, '2025-04-02', 1600),
(107, 2, '2025-06-10', 2000);

create table employees (
employee_id int primary key,
first_name varchar(80),
last_name varchar(60),
department varchar(30),
hire_date date,
salary int);

insert into employees values
(111, 'Amit', 'Patel', 'Management', '2023-03-10', 22000),
(222, 'Neha', 'Sharma', 'Design', '2023-09-18', 28000),
(333, 'Rohit', 'Verma', 'HR', '2024-01-25', 45000),
(444, 'Pooja', 'Mehta', 'Marketing', '2024-08-14', 38000),
(555, 'Suresh', 'Iyer', 'Management', '2025-02-05', 60000);

-- inner join -- get all matching rows
select * from customers
inner join orders on
customers.customer_id = orders.customer_id;

-- left join -- will show all customers even if no order placed by them
select first_name, order_id from customers c
left join orders o on
c.customer_id = o.customer_id;

-- right join -- will show all orders not all customers
select first_name, order_id from customers c
right join orders o on
c.customer_id = o.customer_id;

-- full outer join -- shows everything
select first_name, order_id, total_amount, order_date from customers c
right join orders o on
c.customer_id = o.customer_id
union
select first_name, order_id, total_amount, order_date from customers c
left join orders o on
c.customer_id = o.customer_id;

-- customers who placed order more than average amount
select first_name, order_id, total_amount from customers c
join orders o on
c.customer_id = o.customer_id
where total_amount > (select avg(total_amount) from orders);

-- to find employees with salary more than average salary
select * from employees
where salary > (select avg(salary) from employees);

-- extract year and month from order date (orders table)
select order_date, year(order_date) as Just_Year, month(order_date) as Just_Month from orders;

-- difference between (order date AND current date)
select order_date, datediff(order_date, curdate()) as Difference from orders;

-- format order date to (d-m-y)
select order_date, date_format(order_date, '%d-%m-%Y')  as Formatted_date from orders;

-- concat first and last name as full name
select first_name, last_name, concat(first_name, " ", last_name) as Full_Name from customers;

-- replace part of string from duck ==> duckling
select last_name, replace(last_name, "Duck", "Duckling") as updated_name from customers;

-- convert first name to upper and last name to lower case
select upper(first_name) as Upper_case, lower(last_name) as Lower_case from customers;

-- trim extra spaces from email field
select trim(email) as Trimmed from customers;

-- running total for total_amount for each order
select order_date, total_amount, sum(total_amount)
over (order by order_date) as Running_total
from orders;

-- rank orders based on total_amount
select order_id, total_amount, rank()
over (order by total_amount desc)
from orders;

-- discount based on total amount > 1000 = 10% >500 = 5%
select order_id, total_amount,
case
	when total_amount > 1000 then total_amount*0.10
    when total_amount > 500 then total_amount*0.05
    else 0
    end
    as Discount_given
from orders;

-- categorize employees salary as high medium and low
select first_name, salary,
case
	when salary >= 50000 then "High"
    when salary >= 30000 then "Medium"
    else "Low"
    end
    as Categorised_salary
from employees;
