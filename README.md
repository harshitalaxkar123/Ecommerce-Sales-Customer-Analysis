# E-commerce Sales & Customer Analysis

## Project Overview

An end-to-end data analytics project that explores online retail transactions, sales performance, and customer purchasing behaviour using Python, SQL, MySQL, and Power BI.

The project transforms raw transaction data into meaningful business insights through data cleaning, exploratory data analysis, customer segmentation, SQL analysis, and interactive dashboard reporting.

## Technologies Used

- **Programming:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Database:** MySQL
- **Query Language:** SQL
- **Integration:** SQLAlchemy, PyMySQL
- **Business Intelligence:** Microsoft Power BI
- **Development Tools:** VS Code, MySQL Workbench, Git & GitHub

## Dataset

**Source:** [UCI Online Retail II Dataset](https://archive.ics.uci.edu/dataset/502/online+retail+ii)

- Dataset period: 2009–2011
- Original records: 1,067,371
- Original columns: 8
- Exact duplicate records removed: 34,335

## Project Workflow

1. Collected and combined the two years of Online Retail II transaction data.
2. Cleaned and preprocessed the data using Python and Pandas.
3. Handled missing values, duplicate records, cancellations, returns, and invalid transactions.
4. Performed Exploratory Data Analysis (EDA).
5. Analyzed monthly revenue, country performance, products, and customers.
6. Performed RFM (Recency, Frequency, Monetary) customer segmentation.
7. Loaded valid sales transactions into MySQL.
8. Created SQL queries and analytical views for business analysis.
9. Integrated Python with MySQL and exported analysis results.
10. Created business visualizations and an interactive Power BI dashboard.
11. Prepared a Business Insights Report with findings and recommendations.

## Key Business Metrics

| Metric | Result |
|---|---:|
| Total Revenue | 20,476,260.45 |
| Total Orders | 40,079 |
| Unique Customers | 5,878 |
| Unique Products | 4,916 |
| Countries | 43 |
| Units Sold | 11,205,148 |

*Revenue represents the total value of filtered valid sales transactions, not audited profit.*

## Customer Segmentation (RFM Analysis)

RFM analysis was used to segment customers based on their purchasing behaviour.

| Customer Segment | Customers |
|---|---:|
| Best Customers | 646 |
| Loyal Customers | 1,405 |
| At Risk Customers | 888 |
| Recent Customers | 888 |
| Others | 2,051 |

This segmentation helps identify valuable customers, loyal buyers, recently active customers, and customers who may need re-engagement.

## Key Analysis

- Monthly revenue and order trends
- Top-performing countries by revenue
- Highest-revenue products
- Top customers by spending
- Customer purchasing behaviour
- Repeat and one-time customer analysis
- RFM-based customer segmentation
- Business performance and sales KPIs

## Power BI Dashboard

An interactive Power BI dashboard was developed to present key business metrics and sales trends.

**Dashboard includes:**
- Revenue, orders, customers, and products KPI cards
- Monthly revenue trend
- Top 10 products by revenue
- Top 10 countries by revenue
- Customer segment distribution

[Open Power BI Dashboard (.pbix)](Ecommerce_Sales_Customer_Dashboard.pbix)

## Visualizations

Python-generated charts are available in:

`outputs/final_charts/`

The charts cover monthly revenue, top countries, top products, and top customers.

## Business Insights Report

The project includes a detailed report containing key findings, customer segmentation insights, business recommendations, and project limitations.

[View Business Insights Report](reports/Business_Insights_Report.md)

## Project Structure

```text
Ecommerce-Sales-Customer-Analysis/
│
├── data/
├── src/
│   ├── analysis.py
│   ├── eda.py
│   ├── rfm_analysis.py
│   ├── load_to_mysql.py
│   ├── sql_analysis.py
│   └── create_visualizations.py
│
├── sql/
│   └── analysis_queries.sql
│
├── outputs/
│   ├── charts/
│   ├── final_charts/
│   └── analysis_results/
│
├── reports/
│   └── Business_Insights_Report.md
│
├── Ecommerce_Sales_Customer_Dashboard.pbix
├── requirements.txt
├── README.md
└── .gitignore
```

*Raw datasets and selected generated files are excluded from GitHub through `.gitignore`.*

## Data Limitations

- Missing Customer IDs were retained in the cleaned master dataset but excluded from customer-level RFM analysis.
- Cancelled transactions and returns were classified separately from valid sales.
- Duplicate records were removed during preprocessing.
- RFM segmentation is descriptive and rule-based; it is not a predictive machine learning model.

## Business Value

This project demonstrates how raw retail transaction data can be transformed into actionable business insights. It combines Python-based data processing, SQL database analysis, customer segmentation, and Power BI reporting to support data-driven business decisions.

## Author

**Harshita Laxkar**  
BCA (AI & Data Science) Student  
Poornima University

[GitHub Profile](https://github.com/harshitalaxkar123)