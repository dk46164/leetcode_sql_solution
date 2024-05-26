WITH LatestPrices AS (
    SELECT 
        product_id, 
        new_price,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM 
        Products
    WHERE 
        change_date <= '2019-08-16'
)

SELECT 
    P.product_id, 
    COALESCE(LP.new_price, 10) AS price
FROM 
    (SELECT DISTINCT product_id FROM Products) P
LEFT JOIN 
    (SELECT product_id, new_price FROM LatestPrices WHERE rn = 1) LP
ON 
    P.product_id = LP.product_id;
