# E-commerce Sales & Customer Analysis
## Business Insights Report

**Project Period:** 2009–2011  
**Tools Used:** Python, Pandas, SQL, MySQL, Power BI

### 1. Project Overview
This project analyzes e-commerce sales transactions to understand revenue performance, product demand, geographical sales distribution, and customer purchasing behavior.

### 2. Key Business Performance
- **Total Revenue:** 20.48M
- **Total Orders:** Approximately 40.08K
- **Unique Customers:** Approximately 5.88K
- **Unique Products:** Approximately 4.92K

### 3. Key Findings

**Sales Performance**
- The business generated approximately 20.48M in sales revenue during the analyzed period.
- Monthly revenue analysis shows variations in sales performance over time.
- Monitoring monthly trends can help identify high-performing and low-performing periods.

**Product Performance**
- Manual was the highest-revenue product in the displayed Top 10 Products chart.
- Regency Cakestand 3 Tier and Dotcom Postage were also among the leading revenue contributors.
- Product-level analysis can help prioritize inventory and promotional decisions.

**Country Performance**
- United Kingdom was the leading market by revenue in the Top 10 Countries chart.
- Other contributing markets included EIRE, Netherlands, Germany, and France.
- The business should monitor country-wise performance to identify opportunities for expansion.

**Customer Segmentation**
The RFM analysis identified five customer segments:

| Segment | Customers |
|---|---:|
| Best Customers | 646 |
| Loyal Customers | 1,405 |
| Recent Customers | 888 |
| At Risk Customers | 888 |
| Others | 2,051 |

Best Customers generated approximately 9.32M in revenue, making them an important group for customer retention strategies.

### 4. Business Recommendations

1. **Customer Retention:** Introduce loyalty rewards and exclusive offers for Best Customers.
2. **At-Risk Customers:** Use personalized discounts and re-engagement campaigns to encourage repeat purchases.
3. **Product Strategy:** Maintain sufficient inventory of high-revenue products.
4. **Market Expansion:** Study customer demand in countries beyond the leading UK market.
5. **Sales Monitoring:** Track monthly revenue and order trends to improve business planning.

### 5. Data Quality & Limitations

- The original dataset contained 1,067,371 records.
- 34,335 duplicate records were removed.
- Missing customer IDs were retained in the cleaned master dataset but excluded from customer-level RFM analysis.
- Cancelled transactions and returns were classified separately from valid sales.
- RFM segments are based on relative scoring and business rules; they are descriptive, not predictive.

### 6. Conclusion

The analysis provides insights into e-commerce revenue, product performance, geographical markets, and customer behavior. Python and SQL were used for data processing and analysis, while Power BI was used to present the results through an interactive business dashboard.

**Project Outcome:** An end-to-end e-commerce sales and customer analytics project supporting data-driven business decisions.