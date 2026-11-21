RevenueX — Enterprise E-Commerce Intelligence Platform
Product Requirements Document (PRD)

Version: 1.0
Status: Project Specification
Project Type: End-to-End Data Analytics & Business Intelligence
Primary Audience: Data Analyst Recruiters, Hiring Managers, Business Stakeholders
Estimated Development Time: 8 Weeks
Daily Development Commitment: 2–3 Hours
Technology Stack: PostgreSQL, Python, Pandas, NumPy, Scikit-learn, Power BI, GitHub

1. Executive Summary

RevenueX is an end-to-end e-commerce analytics and business intelligence platform designed to transform raw transactional data into actionable business insights.

The platform will analyze historical e-commerce transactions, customer behavior, product performance, seller performance, payment patterns, customer satisfaction, and delivery operations.

The primary objective is to demonstrate how a Data Analyst can use SQL, Python, statistical analysis, predictive modeling, and Power BI to solve real-world business problems.

RevenueX will provide:

Executive-level business performance monitoring.
Customer segmentation and retention analysis.
Sales and product performance analysis.
Delivery and operational performance analysis.
Seller performance evaluation.
Customer churn risk modeling.
Revenue forecasting.
Data-driven business recommendations.

The project will use the Olist Brazilian E-Commerce Public Dataset as its primary data source.

The final product will include a structured PostgreSQL database, reusable SQL analytical queries, Python analytical notebooks, a multi-page Power BI dashboard, and professional technical documentation.

2. Problem Statement

E-commerce companies generate large amounts of transactional data but often struggle to convert that data into useful business decisions.

Common business challenges include:

Lack of visibility into revenue trends.
Difficulty identifying high-value customers.
Poor understanding of customer retention.
Limited visibility into delivery delays.
Difficulty identifying underperforming sellers.
Inadequate understanding of product category performance.
Inability to identify customers at risk of not returning.
Difficulty forecasting future sales.
Lack of centralized business reporting.

RevenueX addresses these challenges through an integrated analytical solution.

3. Product Vision

Build a professional, reproducible, data-driven business intelligence system that simulates the analytical workflow of an enterprise Data Analyst.

The platform should transform:

Raw Data → Clean Data → Structured Database → Analytical Insights → Interactive Dashboards → Business Recommendations

The project must demonstrate technical competency and business understanding rather than simply visualizing datasets.

4. Project Objectives
4.1 Primary Objectives
Build an end-to-end analytics pipeline.
Design a relational PostgreSQL database.
Demonstrate intermediate-to-advanced SQL skills.
Perform exploratory data analysis using Python.
Implement customer segmentation.
Develop a carefully validated churn prediction model.
Develop a revenue forecasting model.
Create interactive Power BI dashboards.
Generate evidence-based business recommendations.
Publish the complete project on GitHub.
4.2 Learning Objectives

The project should demonstrate proficiency in:

Skill	Expected Competency
SQL	Advanced querying, CTEs, window functions
Python	Data cleaning, analysis and modeling
Pandas	Data manipulation
NumPy	Numerical operations
Statistics	Hypothesis testing and interpretation
Scikit-learn	Clustering and classification
PostgreSQL	Database design and querying
Power BI	Data modeling, DAX and visualization
Git/GitHub	Version control and documentation
Business Analytics	KPI design and recommendations
5. Target Users
5.1 Primary User: Business Executive

Needs:

Understand business performance.
Monitor revenue and order trends.
Identify business risks.
Make strategic decisions.
5.2 Secondary User: Operations Manager

Needs:

Monitor delivery performance.
Identify delayed shipments.
Evaluate seller performance.
Improve operational efficiency.
5.3 Secondary User: Marketing and Customer Manager

Needs:

Understand customer segments.
Identify high-value customers.
Monitor retention.
Identify customers at risk of not returning.
5.4 Secondary User: Data Analyst

Needs:

Explore transactional data.
Investigate business questions.
Generate reports.
Validate analytical findings.
6. Dataset Requirements
6.1 Primary Dataset

Dataset: Brazilian E-Commerce Public Dataset by Olist

Source:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Dataset characteristics:

Approximately 100,000 orders.
Nine primary CSV files.
Historical data from 2016–2018.
Multiple related transactional tables.
Anonymized customer and seller identifiers.
6.2 Dataset Components
Dataset	Description
customers	Customer information
orders	Order lifecycle information
order_items	Products and order item details
order_payments	Payment information
order_reviews	Customer reviews
products	Product attributes
sellers	Seller information
geolocation	Geographic information
category_translation	Product category translations
6.3 Optional Dataset

Olist Marketing Funnel Dataset:

https://www.kaggle.com/datasets/olistbr/marketing-funnel-olist

This dataset may be used as a separate marketing and lead-acquisition analysis extension.

It must not be treated as direct consumer advertising campaign spend or joined to consumer transactions without a valid relationship.

6.4 Data Handling Requirements
Preserve original raw datasets.
Never modify raw data directly.
Maintain separate raw and processed layers.
Document missing values.
Identify duplicate records.
Validate primary and foreign keys.
Record data transformation logic.
Document dataset limitations.
7. Scope of the Project
7.1 In Scope
Data ingestion.
Database design.
Data quality assessment.
SQL analytics.
Python exploratory analysis.
Customer segmentation.
Cohort retention analysis.
Churn prediction.
Revenue forecasting.
Power BI dashboard development.
Business recommendations.
GitHub documentation.
7.2 Out of Scope

The following are not part of the initial implementation:

Real-time transaction processing.
Live payment gateway integration.
Actual e-commerce order management.
Production customer notification systems.
Real-world marketing campaign execution.
Automated business decision execution.
Guaranteed financial impact.
Enterprise cloud deployment.
8. Technical Architecture
8.1 High-Level Architecture
text
                DATA SOURCES
                     |
                     v
              RAW CSV FILES
                     |
                     v
             DATA INGESTION
                     |
                     v
             POSTGRESQL DB
                     |
              DATA QUALITY
                     |
                     v
            ANALYTICAL VIEWS
                     |
             +-------+-------+
             |               |
             v               v
        PYTHON ANALYSIS   POWER BI
             |               |
             v               v
       ML MODEL OUTPUTS  DASHBOARDS
             |               |
             +-------+-------+
                     |
                     v
             BUSINESS INSIGHTS
                     |
                     v
             RECOMMENDATIONS

8.2 Technology Stack
Layer	Technology
Data source	CSV
Database	PostgreSQL
Database client	DBeaver
Data analysis	Python
Data manipulation	Pandas, NumPy
Visualization	Matplotlib, Seaborn, Plotly
Machine learning	Scikit-learn
Statistical modeling	Statsmodels
Business intelligence	Power BI
Version control	Git
Repository	GitHub
Documentation	Markdown
9. Database Requirements
9.1 Database Name

revenuex

9.2 Database Schemas

The database should contain:

raw
staging
analytics
Raw Schema

Contains imported source data without business transformations.

Staging Schema

Contains cleaned, standardized and validated data.

Analytics Schema

Contains analytical tables, dimensional models and reusable business views.

9.3 Dimensional Model

The project should implement a star-schema-inspired analytical model.

Fact Tables
Table	Grain
fact_orders	One row per order
fact_order_items	One row per order item
fact_payments	One row per payment record
fact_reviews	One row per review record
Dimension Tables
Table	Grain
dim_customers	One row per customer identity
dim_products	One row per product
dim_sellers	One row per seller
dim_date	One row per calendar date
dim_geography	One row per geographic location
9.4 Database Requirements
Use primary keys.
Use foreign keys wherever appropriate.
Define appropriate data types.
Use indexes on frequently queried keys.
Maintain referential integrity.
Document table grain.
Avoid unnecessary duplication.
Create reusable analytical views.
9.5 Analytical Views

The following views must be implemented:

text
vw_monthly_sales
vw_customer_rfm
vw_customer_cohorts
vw_delivery_performance
vw_seller_scorecard
vw_category_performance
vw_payment_analysis
vw_order_status_analysis


All views must use clearly documented business definitions.

10. Functional Requirements
FR-01: Data Ingestion

Description: Import all primary CSV datasets into PostgreSQL.

Requirements:

Import all nine datasets.
Preserve source columns.
Validate record counts.
Handle date and numeric data types.
Log ingestion errors.
Record source filenames.

Acceptance criteria:

All required datasets are imported.
Imported row counts are documented.
Failed imports are identified.
Primary key constraints are validated.
FR-02: Data Quality Assessment

Description: Identify and document data quality issues.

Requirements:

Identify missing values.
Identify duplicate records.
Validate relationships.
Identify orphan records.
Validate timestamps.
Identify invalid numeric values.
Document cleaning decisions.

Acceptance criteria:

Data quality report exists.
Major issues are documented.
Cleaning logic is reproducible.
FR-03: Sales Analytics

Description: Analyze sales and order performance.

Required metrics:

Total GMV.
Total orders.
Average order value.
Monthly GMV.
Monthly growth.
Product category performance.
Geographic performance.
Payment method distribution.

Acceptance criteria:

Metrics are calculated using documented definitions.
Results are validated against source data.
Monthly trends can be analyzed.
FR-04: Customer Analytics

Description: Understand customer behavior and value.

Required metrics:

Total unique customers.
Repeat customers.
Customer order frequency.
Customer lifetime revenue.
RFM segmentation.
Customer cohort retention.
Customer geographic distribution.

Acceptance criteria:

RFM segments are generated.
Cohort retention is calculated.
Customer identity is handled using customer_unique_id.
FR-05: Delivery Analytics

Description: Evaluate order delivery performance.

Required metrics:

Average delivery duration.
Estimated versus actual delivery.
Late delivery percentage.
Delivery performance by state.
Seller delivery performance.
Delivery time versus review score.

Acceptance criteria:

Delivery duration is calculated consistently.
Late delivery definitions are documented.
Undelivered orders are handled separately.
FR-06: Seller Analytics

Description: Evaluate seller performance.

Required metrics:

Seller order volume.
Seller GMV.
Average review score.
Delivery delay percentage.
Seller ranking.
Category distribution.

Acceptance criteria:

Seller scorecards are generated.
Ranking calculations are reproducible.
Low-volume sellers are interpreted cautiously.
FR-07: Customer Segmentation

Description: Group customers based on purchasing behavior.

Requirements:

Calculate recency.
Calculate frequency.
Calculate monetary value.
Scale features.
Implement K-means clustering.
Evaluate cluster quality.
Interpret customer segments.

Expected segments:

Champions.
Loyal Customers.
Potential Loyalists.
At-Risk Customers.
Lost Customers.
New Customers.

Acceptance criteria:

Cluster assignments are generated.
Silhouette score is evaluated.
Business interpretation is documented.
FR-08: Churn Prediction

Description: Develop a model to identify customers unlikely to return within a defined future period.

Requirements:

Define observation and prediction windows.
Define a measurable churn proxy.
Engineer historical customer features.
Prevent temporal leakage.
Train Logistic Regression.
Train Random Forest.
Compare model performance.

Evaluation metrics:

Precision.
Recall.
F1 Score.
PR-AUC.
Confusion Matrix.

Acceptance criteria:

Churn definition is documented.
Features contain no information from the prediction period.
Baseline and trained models are compared.
Model limitations are documented.

Important: A customer with only one recorded order must not automatically be classified as permanently churned. The historical dataset has a limited observation window.

FR-09: Revenue Forecasting

Description: Forecast monthly GMV.

Requirements:

Prepare monthly time series.
Analyze seasonality.
Establish a seasonal naïve baseline.
Evaluate exponential smoothing.
Evaluate ARIMA where appropriate.
Compare models.
Generate forecast intervals.

Evaluation metrics:

MAE.
RMSE.
MAPE where appropriate.

Acceptance criteria:

Forecasting uses chronological validation.
Actual and predicted values are compared.
Forecast limitations are documented.
FR-10: Power BI Reporting

Description: Create an interactive business intelligence dashboard.

Requirements:

Connect Power BI to analytical data.
Implement relationships.
Create DAX measures.
Create interactive visualizations.
Add filters and slicers.
Add drill-through where useful.
Maintain consistent visual design.

Acceptance criteria:

Six report pages are completed.
KPIs are validated.
Interactions work correctly.
Report screenshots are documented.
11. SQL Requirements

The SQL module must demonstrate the following capabilities.

ID	Requirement	SQL Concept
SQL-01	Monthly GMV	GROUP BY
SQL-02	Revenue growth	LAG
SQL-03	Top categories	Aggregation
SQL-04	Top products per category	DENSE_RANK
SQL-05	Customer purchase frequency	COUNT
SQL-06	Customer ranking	ROW_NUMBER
SQL-07	RFM analysis	CTE
SQL-08	Customer cohorts	DATE_TRUNC
SQL-09	Retention analysis	Window functions
SQL-10	Seller scorecard	RANK
SQL-11	Delivery analysis	CASE
SQL-12	Payment analysis	Aggregation
SQL-13	Product combinations	Self JOIN
SQL-14	Repeat purchase intervals	LEAD
SQL-15	Data validation	Constraints and queries

Target: 30–40 meaningful SQL queries.

Each query should contain:

Business question.
SQL implementation.
Explanation.
Expected output.
Business interpretation.
12. Python Requirements
12.1 Exploratory Data Analysis

Perform:

Dataset inspection.
Missing value analysis.
Duplicate analysis.
Distribution analysis.
Outlier analysis.
Correlation analysis.
Time-series analysis.
Category analysis.
Geographic analysis.

Deliverable: 02_eda.ipynb

12.2 Customer Segmentation

Implement:

RFM calculation.
Feature scaling.
Outlier treatment.
K-means clustering.
Cluster evaluation.
Segment interpretation.

Deliverable: 03_rfm_analysis.ipynb

12.3 Churn Prediction

Implement:

Churn proxy definition.
Feature engineering.
Chronological data splitting.
Logistic Regression.
Random Forest.
Model evaluation.
Feature importance analysis.

Deliverable: 04_churn_prediction.ipynb

12.4 Revenue Forecasting

Implement:

Time-series aggregation.
Trend analysis.
Seasonality analysis.
Baseline forecasting.
Exponential smoothing.
ARIMA where appropriate.
Forecast evaluation.

Deliverable: 05_sales_forecasting.ipynb

12.5 Statistical Analysis

Investigate:

Relationship between delivery delays and review scores.
Differences in average order value across categories.
Freight cost differences across regions.
Customer purchasing patterns.

Use appropriate statistical tests, confidence intervals and effect sizes.

Deliverable: 06_statistical_analysis.ipynb

13. Power BI Dashboard Requirements

The Power BI report must contain six pages.

Page 1: Executive Overview

Purpose: Provide an overview of overall business performance.

KPIs:

Total GMV.
Total Orders.
Unique Customers.
Average Order Value.
Repeat Customer Rate.
Late Delivery Rate.

Visualizations:

Monthly GMV trend.
Orders by month.
Category contribution.
Geographic distribution.
Order status distribution.
Page 2: Sales Intelligence

Purpose: Investigate sales performance.

Visualizations:

Monthly GMV.
Top categories.
Top products.
Revenue by state.
Payment method distribution.
Average order value.
Page 3: Customer Intelligence

Purpose: Understand customer purchasing behavior.

Visualizations:

Customer segmentation.
RFM distribution.
Repeat customer rate.
Customer cohort retention.
Customer lifetime revenue.
Customer purchase frequency.
Page 4: Delivery and Operations

Purpose: Monitor fulfillment and delivery performance.

Visualizations:

Average delivery time.
Late delivery percentage.
Delayed orders.
Delivery performance by state.
Seller delivery performance.
Review score versus delivery duration.
Page 5: Seller and Product Performance

Purpose: Compare seller and product performance.

Visualizations:

Seller ranking.
Seller GMV.
Product category performance.
Average review score.
Delivery reliability.
Seller order volume.
Page 6: Predictive Analytics

Purpose: Display analytical model outputs.

Visualizations:

Actual versus forecast GMV.
Forecast intervals.
At-risk customer segments.
Churn prediction performance.
Model evaluation metrics.

All model outputs must include appropriate validation and context.

14. KPI Definitions

All business metrics must have documented definitions.

KPI	Definition
GMV	Sum of order item prices for qualifying orders
Total Orders	Distinct qualifying order IDs
Average Order Value	GMV / qualifying orders
Repeat Customer Rate	Customers with multiple qualifying purchases / eligible customers
Average Delivery Time	Average delivered timestamp minus purchase timestamp
Late Delivery Rate	Orders delivered after estimated delivery date / delivered orders with valid dates
Customer Lifetime Revenue	Historical qualifying revenue per customer
Freight Value	Sum of recorded freight charges
Review Score	Average available review score

Important business rules:

Revenue calculations must avoid duplicated order-item values.
Order eligibility must be documented.
Cancelled and unavailable orders must be handled consistently.
Customer-level analysis must use the correct customer identity.
Missing delivery timestamps must not be treated as zero.
Actual profit must not be claimed without actual cost data.
Repeat customer calculations must account for the dataset observation window.
15. Business Intelligence Requirements

The platform must produce evidence-based recommendations.

Examples of possible findings:

Certain product categories contribute disproportionately to GMV.
Some customer cohorts exhibit lower repeat purchasing.
Certain geographic regions experience longer delivery durations.
Seller performance varies significantly.
Delivery delays may be associated with lower review scores.
Customer segments demonstrate different purchasing behaviors.

Recommendations must be based on actual analytical results.

Every recommendation should include:

Identified problem.
Supporting evidence.
Proposed action.
Expected direction of impact.
Metric to monitor.
Limitations.

No financial impact or savings should be presented as realized unless independently measured.

16. Non-Functional Requirements
Performance
Queries should use appropriate indexes.
Analytical queries should avoid unnecessary full-table operations.
Power BI visuals should remain responsive.
Python processing should be memory-conscious.
Reliability
Data transformations should be reproducible.
Database relationships should be validated.
Model results should be reproducible using documented settings.
KPI calculations should be consistent across tools.
Maintainability
Use modular SQL files.
Use reusable Python functions where appropriate.
Maintain clear folder structures.
Document assumptions.
Use meaningful Git commits.
Security
Never commit credentials.
Use environment variables for sensitive configuration.
Keep private information out of the repository.
Use only the anonymized public dataset.
Reproducibility

A new user should be able to:

Download the dataset.
Configure PostgreSQL.
Execute database scripts.
Run Python notebooks.
Open the Power BI report.
Reproduce the documented analytical findings.
17. GitHub Repository Structure
text
revenuex-ecommerce-intelligence/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_data_quality.sql
│   ├── 03_sales_analysis.sql
│   ├── 04_customer_analysis.sql
│   ├── 05_cohort_analysis.sql
│   ├── 06_delivery_analysis.sql
│   └── 07_seller_analysis.sql
│
├── python/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_rfm_analysis.ipynb
│   ├── 04_churn_prediction.ipynb
│   ├── 05_sales_forecasting.ipynb
│   └── 06_statistical_analysis.ipynb
│
├── powerbi/
│   ├── RevenueX.pbix
│   └── screenshots/
│
├── reports/
│   ├── executive_summary.pdf
│   ├── business_recommendations.md
│   └── data_dictionary.md
│
├── docs/
│   ├── architecture.png
│   ├── methodology.md
│   └── KPI_definitions.md
│
├── requirements.txt
├── .gitignore
├── PRD.md
└── README.md


Large raw datasets should not be committed unnecessarily.

18. Development Timeline

Total duration: 8 Weeks.

Week	Development Phase	Deliverable
1	Dataset exploration and database setup	PostgreSQL database
2	Advanced SQL analysis	SQL query collection
3	Python EDA	EDA notebook
4	RFM, cohorts and churn analysis	Customer intelligence
5	Forecasting and statistics	Predictive analysis
6	Power BI foundations and dashboards	First three pages
7	Complete Power BI reporting	Six-page dashboard
8	Documentation and portfolio	Final GitHub repository

Estimated effort: 100–130 focused hours.

19. Project Acceptance Criteria

The project will be considered complete when all critical deliverables are met.

Data Engineering
Nine source datasets imported.
Raw, staging and analytics layers established.
Data quality checks implemented.
Relationships documented.
Analytical model created.
SQL
30–40 meaningful SQL queries.
Window functions demonstrated.
CTEs demonstrated.
Cohort analysis implemented.
RFM calculations implemented.
Analytical views created.
Python
Data cleaning completed.
EDA completed.
RFM segmentation implemented.
Cohort analysis implemented.
Churn model evaluated.
Forecasting model evaluated.
Statistical analysis documented.
Power BI
Six dashboard pages completed.
KPI measures validated.
Relationships checked.
Slicers implemented.
Navigation and drill-through tested.
Screenshots captured.
Portfolio
Professional README.
Complete PRD.
Architecture documentation.
Executive summary.
Business recommendations.
Requirements file.
Reproducibility instructions.
No credentials or sensitive information committed.
20. Risks and Mitigation
Risk	Mitigation
Missing data	Document and apply justified handling rules
Duplicate revenue	Respect fact-table grain
Data leakage	Use temporal validation
Weak churn labels	Define a clear prediction horizon
Limited historical data	Document forecasting limitations
Incorrect KPI calculations	Reconcile SQL and Power BI
Dashboard performance	Use efficient models and measures
Overcomplicated scope	Prioritize core deliverables
Dataset licensing issues	Preserve attribution and comply with licence
Unsupported business claims	Separate measured results from hypotheses
21. Future Enhancements

Potential future improvements:

Automated ETL pipelines.
Scheduled data refresh.
Cloud database deployment.
Streamlit analytics application.
Automated data quality reporting.
Advanced customer lifetime value modeling.
Product recommendation analysis.
More robust forecasting models.
Business alerting and monitoring.
CI/CD for analytical validation.

These enhancements are optional and should not delay the core deliverables.

22. Final Deliverables

At project completion, RevenueX should contain:

A PostgreSQL database with structured data.
A documented SQL analytical query collection.
Python EDA notebooks.
RFM customer segmentation.
A validated churn prediction experiment.
A revenue forecasting experiment.
A six-page Power BI dashboard.
A business insights report.
A professional GitHub repository.
A project presentation suitable for interviews.
23. Success Metrics

The project will be evaluated based on:

Evaluation Area	Success Criteria
Data Engineering	Reproducible and validated data pipeline
SQL	Correct and efficient analytical queries
Python	Clear, reproducible analytical methodology
Statistics	Appropriate tests and interpretation
Predictive Analytics	Leakage-free evaluation
Power BI	Accurate, usable dashboards
Business Thinking	Evidence-based recommendations
Documentation	Clear project explanation
Communication	Ability to defend analytical decisions

The objective is not to maximize the number of technologies or charts.

The objective is to demonstrate the ability to transform raw data into reliable business intelligence.

24. Project Mission

RevenueX is designed to demonstrate the complete analytical journey of a professional Data Analyst.

From understanding raw data to writing complex SQL queries, developing Python models, designing executive dashboards, and communicating business recommendations, every component should demonstrate analytical thinking and practical problem-solving.

The final project should be detailed enough that a hiring manager can inspect the methodology, reproduce the analysis, understand the findings, and evaluate the developer's technical competency.

Project Motto:

"Don't just analyze the data. Understand the business, discover the problem, and deliver the decision."

End of Product Requirements Document