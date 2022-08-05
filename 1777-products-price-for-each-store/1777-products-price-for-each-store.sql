/* Write your T-SQL query statement below */

select product_id, store1, store2, store3
from Products
pivot
(
    max(price) 
    for store in (store1,store2,store3)
) piv

/*SELECT product_id,
       store1,
       store2,
       store3
FROM   (SELECT product_id,
               store,
               price
        FROM   products) result
       PIVOT (Max(price)
             FOR store IN ([store1],
                           [store2],
                           [store3])) piv 
                           */