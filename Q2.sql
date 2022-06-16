SELECT t1.accaveragespend, t2.rejaveragespend
FROM
(
SELECT AVG(totalSpent) AS accaveragespend
FROM Receipts
WHERE rewardsReceiptStatus = 'Accepted'
) t1,
(
SELECT AVG(totalSpent) AS rejaveragespend
FROM Receipts
WHERE rewardsReceiptStatus = 'Rejected'
) t2;

SELECT t1.acctotalnum, t2.rejtotalnum
FROM
(
SELECT SUM(l.quantityPurchased) AS acctotalnum
FROM Receipts r, RewardsReceiptItemList l
WHERE r.id=l.receiptId AND rewardsReceiptStatus = 'Accepted'
) t1,
(
SELECT SUM(l.quantityPurchased) AS rejtotalnum
FROM Receipts r, RewardsReceiptItemList l
WHERE r.id=l.receiptId AND rewardsReceiptStatus = 'Rejected'
) t2;

