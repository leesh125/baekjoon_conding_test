-- 코드를 입력하세요
SELECT branch_id as 'BRANCH_ID', sum(salary) as 'TOTAL'
from employees
group by branch_id
order by branch_id;