# Write your MySQL query statement below
select name as Employee from
(select e1.id, e1.name, e1.salary, e1.managerId, e2.salary as manSal
from Employee e1
left join Employee e2
on e1.managerId = e2.id) t
where manSal < salary