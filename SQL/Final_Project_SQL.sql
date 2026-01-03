create database Final_Project;
use Final_Project;


create table students (
student_id int primary key,
first_name varchar(50),
last_name varchar(50),
email varchar(70),
birth_date date,
enrollment_date date);

insert into students values
(1, 'Judy', 'Hopps', 'judy@toon.com', '2002-05-10', '2020-06-15'),
(2, 'Nick', 'Wilde', 'nick@toon.com', '2001-09-18', '2021-07-20'),
(3, 'Mickey', 'Mouse', 'mickey@toon.com', '2000-11-11', '2022-01-10'),
(4, 'Donald', 'Duck', 'donald@toon.com', '2001-03-22', '2022-08-05'),
(5, 'Tom', 'Cat', 'tom@toon.com', '2002-12-01', '2023-02-12'),
(6, 'Jerry', 'Mouse', 'jerry@toon.com', '2003-04-14', '2023-09-01'),
(7, 'Scooby', 'Doo', 'scooby@toon.com', '2000-07-07', '2024-01-18'),
(8, 'Bugs', 'Bunny', 'bugs@toon.com', '2001-10-30', '2024-03-10'),
(9, 'Daffy', 'Duck', 'daffy@toon.com', '2002-06-06', '2024-07-25');


create table departments (
department_id int primary key,
department_name varchar(40));

insert into departments values
(11, 'Data and AI'),
(22, 'Mathematics'),
(33, 'Science'),
(44, 'Design');

create table courses (
course_id int primary key,
course_name varchar(40),
department_id int,
credits int,
foreign key (department_id) references departments(department_id));

insert into courses values
(1001, 'Machine Learning', 11, 4),
(1002, 'Data Analytics', 11, 3),
(1003, 'Linear Algebra', 22, 4),
(1004, 'Dentist', 33, 3);

create table instructors (
instructor_id int primary key,
first_name varchar(50),
last_name varchar(50),
email varchar(70),
department_id int,
foreign key (department_id) references departments(department_id));

insert into instructors values
(908, 'Amit', 'Patel', 'amit@college.com', 11),
(708, 'Neha', 'Sharma', 'neha@college.com', 22),
(608, 'Rohit', 'Verma', 'rohit@college.com', 33);

create table enrollments (
enrollment_id int primary key,
student_id int,
course_id int,
enrollment_date date,
foreign key (student_id) references students(student_id),
foreign key (course_id) references courses(course_id));

insert into enrollments values
(1, 1, 1001, '2020-06-20'),
(2, 1, 1002, '2020-06-21'),
(3, 1, 1003, '2020-06-22'),
(4, 2, 1001, '2021-07-25'),
(5, 3, 1002, '2022-01-15'),
(6, 4, 1003, '2022-08-10'),
(7, 5, 1004, '2023-02-18'),
(8, 6, 1001, '2023-09-05'),
(9, 7, 1004, '2024-01-20'),
(10, 3, 1001, '2024-01-20'),
(11, 8, 1003, '2024-03-15');



-- 1. perform crud on all table
-- Table 1 Students ===========================================
-- create 
insert into students values
(10, 'Harry', 'Pot', 'daffy@toon.com', '2002-06-06', '2024-07-25');

-- read
select * from students;

-- update
update students
set last_name = 'Potter'
where student_id = 10;

-- delete
delete from students
where student_id = 10;

-- Table 2 Departments =================================
-- create
insert into departments values
(55, 'Physics');

-- read
select * from departments;

-- update [and to &]
update departments
set department_name = 'Data & AI'
where department_id = 11;

-- delete
delete from departments
where department_id = 55;

-- Table 3 Courses =================================
-- create
insert into courses values
(1005, 'Statistics', 22, 4);

-- read
select * from courses;

-- update
update courses
set course_name = 'Data & Statistics'
where course_id = 1005;

-- delete
delete from courses
where course_id = 1005;

-- Table 4 Instructors ========================
-- create
insert into instructors values
(508, 'Kiran', 'Mehta', 'kiran@college.com', 44);

-- read
select * from instructors;

-- update
update instructors
set last_name = 'Sharma'
where instructor_id = 508;

-- delete
delete from instructors
where instructor_id = 508;

-- Table 5 Enrollments ===============
-- create
insert into enrollments values
(12, 2, 1002, '2024-08-05');

-- read
select * from enrollments;

-- update
update enrollments
set course_id = 1001
where enrollment_id = 12;

-- delete
delete from enrollments
where enrollment_id = 12;

-- 2. students who enrolled after 2022 ============
select * from students
where year(enrollment_date) > '2022';

-- 3. courses offered by "Data & AI" with limit of 5  ============
select * from courses
where department_id = 11
limit 5;
-- OR
select department_name, course_name from courses c
join departments d on
c.department_id = d.department_id
where department_name = "Data & AI"
limit 5;

-- 4. no of students for each course filter course with more than 5 [for now (2)] students  ============
select count(student_id), course_name from enrollments
join courses on 
enrollments.course_id = courses.course_id
group by course_name
having count(student_id) > 2;

-- 5. students enrolled in BOTH courses [ Machine Learning & Data Analytics ]  ============
select student_id from enrollments
join courses on
enrollments.course_id = courses.course_id
where course_name in ('Machine Learning', 'Data Analytics')
group by student_id
having count(distinct course_name) = 2;
-- -------------- student_id 1 and 3 are enrolled for BOTH courses -------------

-- 6. students enrolled in EITHER courses [ Machine Learning & Data Analytics ]  ============
select student_id, course_name from enrollments
join courses on
enrollments.course_id = courses.course_id
where course_name = 'Machine learning' or course_name = 'data analytics';

-- 7. average number of credits for all courses  ============
select course_name, avg(credits) as average_credits from courses
group by course_name;

-- 8. maximum salary of instructors in the Computer Science department
-- ========== [no salary field] ==============
select first_name, max(salary) from instructors
join departments on
instructors.department_id = departments.department_id
where department_name = 'Data & AI';

-- 9. number of students enrolled in each department  ============
select department_name, count(distinct student_id) from courses
join enrollments on
courses.course_id = enrollments.course_id
join departments on
departments.department_id = courses.department_id
group by department_name;

-- 10. students and their corresponding courses  ============
select first_name, last_name, course_name from students
inner join enrollments on
students.student_id = enrollments.student_id
inner join courses on
courses.course_id = enrollments.course_id;

-- 11. all students and their courses___HENCE all students will come  ============
select first_name, last_name, course_name from students
left join enrollments on
students.student_id = enrollments.student_id
left join courses on
courses.course_id = enrollments.course_id;

-- 12. students enrolled in courses with more than 2 students  ============
/* 
==== split query in two ============== this will find courses with > 2 students
select course_id from enrollments
group by course_id
having count(student_id) > 2; */

select enrollments.student_id, first_name, course_name from students
join enrollments on
students.student_id = enrollments.student_id
join courses on
courses.course_id = enrollments.course_id
where enrollments.course_id in (select course_id from enrollments
							group by course_id
							having count(student_id) > 2);

-- 13. extract the year from the EnrollmentDate of students  ============
select student_id, first_name, enrollment_date, year(enrollment_date) as enrollment_year from students;

-- 14. concat instructor’s first and last name  ============
select first_name, last_name, concat(first_name, " ", last_name) as full_name from instructors;

-- 15. running total of students enrolled in courses  ============
select enrollment_date, count(student_id), sum(count(student_id))
over (order by enrollment_date) 
from enrollments
group by enrollment_date;

-- 16. label students as ‘Senior’ or ‘Junior’  ============
select first_name, enrollment_date,
case
	when enrollment_date <= date_sub(curdate(), interval 4 year) then 'Senior'
    else 'Junior'
    end
    as Classification
from students;

