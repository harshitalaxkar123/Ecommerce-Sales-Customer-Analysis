USE ecommerce_analysis;

SHOW TABLES;

USE ecommerce_analysis;

SELECT COUNT(*) 
FROM sales_transactions;

SELECT *
FROM sales_transactions
LIMIT 10;

SELECT *
FROM sales_transactions
LIMIT 10;

USE ecommerce_analysis;

-- 1. Total Revenue
SELECT ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM sales_transactions
WHERE IsValidSale = 1;

-- 2. Total Orders
SELECT COUNT(DISTINCT Invoice) AS Total_Orders
FROM sales_transactions
WHERE IsValidSale = 1;

-- 3. Total Customers
SELECT COUNT(DISTINCT CustomerID) AS Total_Customers
FROM sales_transactions
WHERE IsValidSale = 1
AND CustomerID IS NOT NULL;

-- 4. Total Products
SELECT COUNT(DISTINCT StockCode) AS Total_Products
FROM sales_transactions
WHERE IsValidSale = 1;

-- 5. Total Units Sold
SELECT SUM(Quantity) AS Total_Units_Sold
FROM sales_transactions
WHERE IsValidSale = 1;

-- 6. Country-wise Revenue
SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM sales_transactions
WHERE IsValidSale = 1
GROUP BY Country
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 7. Top 10 Products
SELECT
    StockCode,
    Description,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    SUM(Quantity) AS Units_Sold
FROM sales_transactions
WHERE IsValidSale = 1
GROUP BY StockCode, Description
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 8. Monthly Sales Trend
SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS Sales_Month,
    ROUND(SUM(Revenue), 2) AS Monthly_Revenue,
    COUNT(DISTINCT Invoice) AS Total_Orders
FROM sales_transactions
WHERE IsValidSale = 1
GROUP BY Sales_Month
ORDER BY Sales_Month;

-- 9. Repeat vs One-Time Customers
SELECT
    CASE
        WHEN Order_Count = 1 THEN 'One-Time Customers'
        ELSE 'Repeat Customers'
    END AS Customer_Type,
    COUNT(*) AS Total_Customers
FROM (
    SELECT
        CustomerID,
        COUNT(DISTINCT Invoice) AS Order_Count
    FROM sales_transactions
    WHERE IsValidSale = 1
    AND CustomerID IS NOT NULL
    GROUP BY CustomerID
) AS Customer_Orders
GROUP BY Customer_Type;

USE ecommerce_analysis;

-- 1. Average Order Value
SELECT
    ROUND(SUM(Revenue) / COUNT(DISTINCT Invoice), 2) AS Average_Order_Value
FROM sales_transactions
WHERE IsValidSale = 1;

-- 2. Country-wise Customer Count
SELECT
    Country,
    COUNT(DISTINCT CustomerID) AS Total_Customers
FROM sales_transactions
WHERE IsValidSale = 1
AND CustomerID IS NOT NULL
GROUP BY Country
ORDER BY Total_Customers DESC
LIMIT 10;

-- 3. Top 10 Customers by Revenue
SELECT
    CustomerID,
    ROUND(SUM(Revenue), 2) AS Total_Spending,
    COUNT(DISTINCT Invoice) AS Total_Orders
FROM sales_transactions
WHERE IsValidSale = 1
AND CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY Total_Spending DESC
LIMIT 10;

-- 4. Monthly Order Performance
SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS Sales_Month,
    COUNT(DISTINCT Invoice) AS Total_Orders,
    SUM(Quantity) AS Units_Sold
FROM sales_transactions
WHERE IsValidSale = 1
GROUP BY Sales_Month
ORDER BY Sales_Month;

-- 5. Return and Cancellation Summary
SELECT
    SUM(IsReturn = 1) AS Total_Return_Records,
    SUM(IsCancelled = 1) AS Total_Cancelled_Records
FROM sales_transactions;

USE ecommerce_analysis;

CREATE OR REPLACE VIEW monthly_sales_view AS
SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS Sales_Month,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    COUNT(DISTINCT Invoice) AS Total_Orders
FROM sales_transactions
WHERE IsValidSale = 1
GROUP BY Sales_Month;

CREATE OR REPLACE VIEW country_sales_view AS
SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    COUNT(DISTINCT Invoice) AS Total_Orders,
    COUNT(DISTINCT CustomerID) AS Total_Customers
FROM sales_transactions
WHERE IsValidSale = 1
GROUP BY Country;

CREATE OR REPLACE VIEW product_sales_view AS
SELECT
    StockCode,
    Description,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    SUM(Quantity) AS Units_Sold
FROM sales_transactions
WHERE IsValidSale = 1
GROUP BY StockCode, Description;

CREATE OR REPLACE VIEW customer_sales_view AS
SELECT
    CustomerID,
    ROUND(SUM(Revenue), 2) AS Total_Spending,
    COUNT(DISTINCT Invoice) AS Total_Orders
FROM sales_transactions
WHERE IsValidSale = 1
AND CustomerID IS NOT NULL
GROUP BY CustomerID;

SHOW FULL TABLES
WHERE Table_type = 'VIEW';