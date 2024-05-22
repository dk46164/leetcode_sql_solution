# Write your MySQL query statement below
SELECT 
    machine_id,
    ROUND(
        SUM(CASE WHEN ACTIVITY_TYPE = 'end' then timestamp else -1*timestamp end )/
        COUNT(DISTINCT PROCESS_ID),
    3) as processing_time
FROM
    ACTIVITY
GROUP BY
    machine_id
;
