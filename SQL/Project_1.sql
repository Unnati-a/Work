create database data_digger;
use data_digger;

create table customers (
Customer_id int primary key,
Name varchar(80),
Email varchar(100),
Address varchar (200));

insert into customers values
(1, 'Rahul Sharma', 'rahul.sharma@gmail.com', 'Mumbai'),
(2, 'Neha Verma', 'neha.verma@gmail.com', 'Delhi'),
(3, 'Amit Patel', 'amit.patel@gmail.com', 'Gujarat'),
(4, 'Pooja Mehta', 'pooja.mehta@gmail.com', 'Mumbai'),
(5, 'Kunal Shah', 'kunal.shah@gmail.com', 'Gujarat');

-- all customer details

select * from customers;

-- update a address

update customers
set address = "Mumbai"
where customer_id = 5;

-- delet customer using id

delete from customers
where customer_id = 4;

-- display all customers using name "Amit Patel"

select * from customers
where name = "Amit Patel";

-- / -- Order Table

create table order_table (
order_id int primary key,
customer_id int,
orderDate date,
totalAmount int,
foreign key (customer_id) references customers (customer_id));

insert into order_table values
(101, 1, '2024-01-10', 2500),
(102, 2, '2024-01-12', 1800),
(103, 3, '2024-01-15', 3200),
(104, 1, '2024-01-20', 1500),
(105, 5, '2024-01-22', 4000);

-- all orders by specific customer "Rahul Sharma"

select * from order_table
where customer_id = 1; 

-- update orders total amount

update order_table
set totalamount = 60000
where order_id = 102;

-- delete order using order_id

delete from order_table
where order_id = 105;

-- all orders placed in last 30 days 
-- today 23-12-2025 (last 30 days = 23-11-2025)

select * from order_table
where orderdate >= 23-11-2025;

-- highest, lowest and average order amount

select avg(totalamount) as Average_order_amount from order_table;

select max(totalamount) as Maximum_order_amount from order_table;

select min(totalamount) as Minimum_order_amount from order_table;

-- / -- Products table

create table products (
product_id int primary key,
productName varchar(80),
price int,
stock int);

insert into products values
(1, 'Power Bank', 150, 300),
(2, 'USB Cable', 200, 500),
(3, 'Bluetooth Speaker', 1200, 150),
(4, 'Wireless Mouse', 800, 250),
(5, 'Keyboard', 1800, 100);

-- all products in price desc order

select * from products
order by price desc;

-- update price of specific product

update products
set price = 1700
where product_id = 3;

-- delete product if out-of-stock

delete from products
where stock = 0;

-- all products who's price between 500 and 2000

select * from products
where price between 500 and 2000;

-- most expensive and cheapest product usinh min and max

select productname as Cheapest_product, price as Lowest_price from products
where price = (select min(price) from products);

select productname as Expensive_product, price as Highest_price from products
where price = (select max(price) from products);

-- / -- Order Details table

create table orderdetail (
orderdetail_id int,
order_id int,
product_id int,
quantity int,
sub_total int,
foreign key (order_id) references order_table (order_id),
foreign key (product_id) references products (product_id));

insert into orderdetail values
(1, 101, 1, 2, 300),    -- Power Bank (150 × 2)
(2, 101, 2, 3, 600),    -- USB Cable (200 × 3)
(3, 102, 4, 1, 800),    -- Wireless Mouse (800 × 1)
(4, 103, 3, 2, 2400),   -- Bluetooth Speaker (1200 × 2)
(5, 104, 5, 1, 1800);

-- all order details for specific order

select * from orderdetail
where order_id = 101;

-- total revenue from all orders

select sum(sub_total) as Total_revenue from orderdetail;

-- top 3 most ordered products

select product_id, sum(quantity) as Total_quantity from orderdetail
group by product_id
order by total_quantity desc
limit 3;

-- how many times specific product have been sold using count

select count(*) from orderdetail
where product_id = 3;


