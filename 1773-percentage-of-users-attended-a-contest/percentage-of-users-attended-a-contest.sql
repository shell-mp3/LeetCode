# Write your MySQL query statement below
SELECT r.contest_id, ROUND((count(distinct(r.user_id))*100/count(distinct(u.user_id))), 2) as percentage
FROM Users as u, Register as r
GROUP BY r.contest_id
ORDER by percentage DESC, r.contest_id ASC