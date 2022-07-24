/* Write your T-SQL query statement below */
SELECT id, 
CASE WHEN p_id IS NULL THEN 'Root' WHEN NOT EXISTS (
    SELECT id FROM tree WHERE p_id = t0.id) 
    THEN 'Leaf' ELSE 'Inner' END as type from tree t0 order by id