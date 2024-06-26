/* Write your T-SQL query statement below */
SELECT
T.REQUEST_AT AS Day,
ROUND(SUM(CASE WHEN T.STATUS IN ('cancelled_by_driver','cancelled_by_client') THEN 1.0 ELSE 0.0 END)/COUNT(STATUS),2) AS "Cancellation Rate"
FROM 
    TRIPS  T
    JOIN USERS UC ON UC.USERS_ID = T.CLIENT_ID  AND UC.BANNED = 'No'
    JOIN USERS UD ON  T.DRIVER_ID = UD.USERS_ID  AND UD.BANNED = 'No'
WHERE T.REQUEST_AT BETWEEN CAST('2013-10-01' AS DATE) AND CAST('2013-10-03' AS DATE) 
GROUP BY
   T.REQUEST_AT
;