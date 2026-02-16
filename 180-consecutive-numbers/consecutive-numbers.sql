# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from 
(select num, lag(num,1) over(order by id) as p1,
lag(num,2) over(order by id) as p2
from Logs) as t
where (p1 = num
and p2 = num)
