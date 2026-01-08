create database smart_library;
use smart_library;


create table authors (
author_id int primary key,
author_name varchar(50),
email varchar(40));

insert into authors values
(111, 'Chetan Bhagat', 'chetan@gmail.com'),
(222, 'Amish Tripathi', 'amish@gmail.com'),
(333, 'Sudha Murthy', 'sudha@gmail.com'),
(444, 'Rujuta Diwekar', 'rujuta@gmail.com'),
(555, 'Anita Desai', 'anita@gmail.com');

create table members (
member_id int primary key,
member_name varchar(30),
member_email varchar(40),
phone_number varchar(10),
membership_date date);

insert into members values
(1, 'Amit Patel', 'amit@gmail.com', 9876543210, '2019-06-10'),
(2, 'Neha Sharma', 'neha@gmail.com', 9876543222, '2019-11-20'),
(3, 'Rahul Mehta', 'rahul@gmail.com', 9876543233, '2020-03-15'),
(4, 'Priya Verma', 'priya@gmail.com', 9876543244, '2020-08-05'),
(5, 'Rohan Shah', 'rohan@gmail.com', 9876543255, '2021-01-12'),
(6, 'Pooja Iyer', 'pooja@gmail.com', 9876543266, '2021-07-30'),
(7, 'Karan Malhotra', 'karan@gmail.com', 9876543277, '2022-04-18'),
(8, 'Sneha Kulkarni', 'sneha@gmail.com', 9876543288, '2022-10-09'),
(9, 'Vikas Jain', 'vikas@gmail.com', 9876543299, '2023-02-14');


create table books (
book_id int primary key,
title varchar(70),
author_id int,
category varchar(30),
isbn int,
published_date date,
price int,
available_copies int,
foreign key (author_id) references authors(author_id));

insert into books values
(101, 'Life Story', 111, 'Novel', 11111, '2020-05-10', 350, 5),
(102, 'Love Journey', 222, 'Novel', 22222, '2013-08-15', 400, 3),
(201, 'Funny Comics', 222, 'Comic', 33333, '2014-02-20', 300, 6),
(202, 'Daily Laughs', 111, 'Comic', 44444, '2015-06-18', 280, 5),
(301, 'Indian Cooking', 444, 'Recipe', 55555, '1999-09-10', 550, 4),
(302, 'Healthy Meals', 444, 'Recipe', 66666, '2017-11-22', 600, 2),
(401, 'Think Positive', 333, 'Motivation', 77777, '2018-03-12', 700, 4),
(402, 'Power of Mind', 333, 'Motivation', 88888, '2019-07-25', 850, 2),
(501, 'Basic Science', 111, 'Science', 99999, '2020-01-05', 650, 3),
(502, 'Advanced Science', 111, 'Science', 90009, '2020-01-05', 850, 3);


create table transactions (
transaction_id int primary key,
member_id int,
book_id int,
borrow_date date,
return_date date,
fine_amount int,
foreign key (book_id) references books(book_id),
foreign key (member_id) references members(member_id));

insert into transactions values
(1, 1, 101, '2021-01-10', '2021-01-20', 0),
(2, 1, 102, '2021-02-05', '2021-02-18', 10),
(3, 1, 201, '2021-03-12', '2021-03-25', 0),
(4, 1, 301, '2021-04-01', '2021-04-15', 5),
(5, 2, 202, '2022-01-11', '2022-01-20', 0),
(6, 5, 302, '2022-02-14', '2022-02-28', 0),
(7, 2, 401, '2022-03-10', '2022-03-24', 15),
(8, 4, 402, '2022-04-05', '2022-04-18', 0),
(9, 5, 501, '2023-01-08', '2023-01-22', 0),
(10, 9, 101, '2023-02-12', '2023-02-25', 0),
(11, 3, 201, '2023-03-15', '2023-03-30', 5);

-- 1. CRUD ===///===
-- insert new books, members and authors (1 each) ===============================================
insert into authors values
(666, 'Robin Sharma', 'robin@gmail.com');
insert into members values
(10, 'Alok Gupta', 'alok@gmail.com', '9876500000', '2023-08-10');
insert into books values
(601, 'Mind Power', 333, 'Motivation', 77770, '2021-05-10', 720, 4);

-- update book availability after book is borrowed or returned ===============================================
-- borrow
update books
set available_copies = available_copies - 1
where book_id = 101;

-- return
update books
set available_copies = available_copies + 1
where book_id = 101;

-- delete members who have not borrowed any books in last year ===============================================
delete from members
where member_id in (
select distinct member_id from transactions
where borrow_date <= date_sub(curdate(), interval 1 year)
);

-- retrive all books with available copies ===============================================
select * from books
where available_copies > 0;



-- 2. SQL Clause ===///===
-- books published after year 2015 ===============================================
select book_id, title, published_date from books
where year(published_date) > 2015;

-- top 5 most expensive books ===============================================
select book_id, title, price from books
order by price desc
limit 5;

-- members who joined before 2022 ===============================================
select member_id, member_name, membership_date from members
where year(membership_date) < 2022;



-- 3. SQL Operators ===///===
-- books where category = 'Science' AND price < 500 (here < 700) ===============================================
select book_id, title, category, price from books
where category = 'Science' and price < 700;

-- books not available for borrowing ===================================================================
select * from books
where available_copies = 0;

-- member who joined after 2020 OR borrowed more than 3 books ===============================================
select members.member_id, count(*) as total_borrowed, member_name, membership_date from transactions
left join members on
transactions.member_id = members.member_id
group by member_id
having count(*) > 3 or year(membership_date) > 2020;



-- 4. Sorting and Grouping ===///===
-- books sorted by title in alphabetical order ===============================================
select book_id, title from books
order by title;

-- number of book borrowed by each member ===============================================
select members.member_id, member_name, count(book_id) as number_of_books_borrowed from members
join transactions on
members.member_id = transactions.member_id
group by member_id;

-- group books by category and show the total count ===============================================
select category, count(*) as total_count from books
group by category;



-- 5. Use Aggregate Functions ===///===
-- find total number of books in each category ===============================================
select category, count(*) as total_number_of_books from books
group by category;

-- calculate average price of books in library ===============================================
select avg(price) as average_price from books;

-- identify most borrowed book ===============================================
select books.book_id, title, count(*) as borrow_count from transactions
join books on
transactions.book_id = books.book_id
group by book_id
order by borrow_count desc
limit 1;

-- calculate total fines collected ===============================================
select sum(fine_amount) as total_fines_collected from transactions;



-- 6. Primary and Foreign key relationl ===///===
-- relation and table linking is already done while creation of tables


-- 7. Implement Joins ===///===
-- Inner joins, books and author name ===============================================
select title, author_name from books
inner join authors on
books.author_id = authors.author_id;

-- Left join, details of members (who have borrowed book) ===============================================
select book_id, member_name, members.member_id, member_email, phone_number, membership_date from transactions
left join members on
transactions.member_id = members.member_id; -- only members who have borrowed book

-- Right Join, books that have not been borrowed ===============================================
select transaction_id, member_id, borrow_date, title from transactions
right join books on
transactions.book_id = books.book_id; -- books all (even though not borrowed)

-- Full outer join, show members who have never borrowed a book ===============================================
select member_name, book_id from transactions
left join members on 
transactions.member_id = members.member_id
union
select member_name, book_id from transactions
right join members on 
transactions.member_id = members.member_id;



-- 8. Sub-query ===///===
-- books that were borrowed by members who registered after 2022 ===============================================
select members.member_id, membership_date, member_name, count(transaction_id) from members
join transactions on 
members.member_id=transactions.member_id
group by members.member_id
having year(membership_date) > 2020 or count(transaction_id) > 3;

-- most borrowed book ===============================================
select books.book_id, count(*) as borrow_count, title from transactions
join books on
transactions.book_id = books.book_id
group by book_id
order by borrow_count desc
limit 1;

-- members who have never borrowed a book ===============================================
select * from members
where member_id not in (select distinct member_id from transactions);


-- 9. Date and Time Function ===///===
-- extract year from published date ===============================================
select published_date, year(published_date) as Just_Year from books;

-- difference between borrow date and return date ===============================================
select borrow_date, return_date, datediff(borrow_date, return_date) as difference_in_days from transactions;

-- format borrow date as D-M-Y ===============================================
select borrow_date, date_format(borrow_date, '%d-%m-%Y') as formatted_date from transactions;


-- 10. String Manipulation ===///===
-- convert all book titles to uppercase ===============================================
select title, upper(title) as upper_case from books;

-- trim white space from author name ===============================================
select author_name, trim(author_name) as trimed_names from authors;

-- replace missing emails with "not provided" (all have provided mails) ===============================================
select ifnull(member_email, 'Not Provided' ) from members;



-- 11. Implement Windows Function ===///===
-- rank books based on number of times they have been borrowed ===============================================
select book_id, count(*) as borrow_count, rank() over
(order by count(*) desc) as rank_number
from transactions
group by book_id;

-- cummulicatve number of books borrowed per member ===============================================
select member_id, count(*) over 
(partition by member_id order by borrow_date) as cumulative_total
from transactions;

-- moving average of books borrowed in last 3 months ===============================================
select member_id, borrow_date, count(*) over
(partition by member_id order by borrow_date 
rows between 2 preceding and current row) as moving_avg
from transactions;


-- 12. CASE Expression ===///===
-- "ACTIVE" if member has borrowed book in last 6 months or else "INACTIVE" ===============================================
select member_id, borrow_date,
case
	when borrow_date >= date_sub(curdate(), interval 6 month) then 'ACTIVE'
    else 'INACTIVE'
    end as status_of_members
from transactions;

-- "New" after 2020, "classic" before 2000 and rest "regular" ===============================================
select title, published_date,
case
  when year(published_date) > 2020 then 'New'
  when year(published_date) < 2000 then 'Classic'
  else 'Regular'
end as book_type
from books;




