SELECT max(salary) as SecondHighestSalary from Employee
where salary<(SELECT max(salary) from Employee)