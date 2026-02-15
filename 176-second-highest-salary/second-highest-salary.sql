# Write your MySQL query statement below
select(
    select max(salary)
    from Employee
    where salary < (select max(salary) from Employee)
) as SecondHighestSalary