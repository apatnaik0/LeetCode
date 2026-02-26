# Write your MySQL query statement below
with new_table as
(select d.name as Department, e.name as Employee, e.salary as Salary, 
dense_rank() over (partition by d.id order by e.salary desc) as rnk
from Employee e
join Department d
on e.departmentId = d.id)
select Department, Employee, Salary
from new_table
where rnk <= 3