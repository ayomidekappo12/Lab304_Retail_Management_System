# Design and Implementation of a Scalable Information Management System for a Retail Business

## DTS 304 – Data Management I


## Student Information

**Student Name:** Ayomide Israel Kappo

**Course:** DTS 304 – Data Management I


# Table of Contents

1. Introduction
2. Project Objectives
3. System Overview
4. Data Collection and Representation
5. Dataset Design
6. Database Design and Implementation
7. Database Indexing
8. SQL Retrieval Queries
9. Search Simulation Implementation
10. Performance Analysis
11. Screenshots
12. Challenges Encountered
13. Lessons Learned
14. Conclusion
15. References


# 1. Introduction

Modern retail businesses generate large volumes of customer transaction data daily. Efficient management, storage, retrieval, and analysis of this information are important for improving business decision-making and customer service.

This project presents the design and partial implementation of a retail information management system similar to a real-world retail company such as TIMA Corporation.

The system demonstrates important data management concepts including:

- Data collection
- Structured data representation
- Relational database design
- Database indexing
- Data retrieval
- Searching algorithms
- Performance comparison

The project uses a retail customer purchase dataset collected through Google Forms and represented in CSV format. The dataset is then imported into a relational database where indexing techniques are applied to improve data retrieval efficiency.

A Python search simulation is also implemented to compare Sequential Search and Binary Search algorithms.


# 2. Project Objectives

The objectives of this project are:

- To design a customer purchase data collection form.
- To capture retail transaction information.
- To represent collected data in structured CSV format.
- To design a relational database system.
- To implement database indexing techniques.
- To create SQL queries for data retrieval.
- To implement search algorithms using Python.
- To compare Sequential Search and Binary Search performance.
- To analyze the importance of indexing and efficient retrieval methods.


# 3. System Overview

The Retail Management System consists of three major components:

## 1. Data Collection Layer

Responsible for collecting customer purchase information.

Tools:

- Google Forms
- CSV spreadsheet


## 2. Database Management Layer

Responsible for storing and retrieving structured retail data.

Technology:

- MySQL/PostgreSQL

Implemented features:

- Database creation
- Table creation
- Primary key
- Indexing
- SQL queries


## 3. Search Simulation Layer

Responsible for testing retrieval algorithms.

Technology:

- Python

Algorithms implemented:

- Sequential Search
- Binary Search


# 4. Data Collection and Representation

A Google Form was designed to collect customer purchase information.

The form included the following fields:

| Field | Description |
|-|-|
| Customer ID | Unique customer identifier |
| Customer Name | Customer full name |
| Purchase Date | Date transaction occurred |
| Product ID | Unique product identifier |
| Product Name | Purchased product |
| Product Category | Product classification |
| Quantity | Number of items purchased |
| Unit Price | Cost per item |
| Total Amount | Total transaction value |


## Google Form Design

The Google Form was designed with simple and structured questions to ensure accurate data collection.


# 5. Dataset Design

The captured dataset was represented in CSV format.

File:

customer_purchases.csv

The dataset contains more than 30 retail transaction records.

Example structure:

| Customer ID | Customer Name | Purchase Date | Product ID | Product Name | Category | Quantity | Price | Amount |
|-|-|-|-|-|-|-|-|-|
|1001|John Doe|2026-05-01|P001|Laptop|Electronics|1|850|850|


## Dataset Purpose

The dataset supports:

- Customer transaction storage
- Sales analysis
- Category analysis
- Search operations
- Database indexing


# 6. Database Design and Implementation

A relational database was created using SQL.

Database Name:

retail_management

Table Name:

customer_purchases


## Table Structure
sql
CREATE TABLE customer_purchases(

customer_id INT PRIMARY KEY,

customer_name VARCHAR(100),

purchase_date DATE,

product_id VARCHAR(20),

product_name VARCHAR(100),

product_category VARCHAR(50),

quantity INT,

unit_price DECIMAL(10,2),

total_amount DECIMAL(10,2)

);


# 7. Database Indexing

Indexes were implemented to improve retrieval performance.

The following indexes were created:


## Primary Index

The primary index was created on:

customer_id

Purpose:

- Ensures unique customer identification.
- Improves customer record retrieval.

Example:
sql
CREATE INDEX idx_customer
ON customer_purchases(customer_id);


## Secondary Index

Created on:

product_category

Purpose:

- Improves category-based searches.

Example:
sql
CREATE INDEX idx_category
ON customer_purchases(product_category);


## Non-Clustered Index

Created on:

purchase_date

Purpose:

- Improves date range queries.

Example:
sql
CREATE INDEX idx_purchase_date
ON customer_purchases(purchase_date);


# 8. SQL Retrieval Queries

## Retrieve Purchases Between Two Dates
sql
SELECT *
FROM customer_purchases
WHERE purchase_date
BETWEEN
'2026-05-01'
AND
'2026-05-31';

Purpose:

Retrieves all purchases made within a specified date range.


## Retrieve Purchases By Category
sql
SELECT *
FROM customer_purchases
WHERE product_category='Electronics';

Purpose:

Retrieves all products belonging to a category.


## Retrieve Customer Purchase History
sql
SELECT *
FROM customer_purchases
WHERE customer_id=1001;

Purpose:

Displays all purchases made by a customer.


## Total Sales By Category
sql
SELECT product_category,
SUM(total_amount)

FROM customer_purchases

GROUP BY product_category;


## Total Sales By Date
sql
SELECT purchase_date,
SUM(total_amount)

FROM customer_purchases

GROUP BY purchase_date;


# 9. Search Simulation Implementation

A Python program was created to compare two searching techniques.

File:

search_simulation.py


## Sequential Search

Sequential Search checks each record one by one until the required product is found.

Characteristics:

- Simple implementation
- Works on unsorted data
- Time complexity:

O(n)


## Binary Search

Binary Search repeatedly divides the search space into halves.

Requirements:

- Data must be sorted.

Characteristics:

- Faster searching
- Suitable for indexed datasets
- Time complexity:

O(log n)


# 10. Performance Analysis

The search algorithms were tested using execution time measurement.

Python timing function:
python
time.perf_counter()


## Performance Comparison

| Algorithm | Data Type | Complexity |
|-|-|-|
| Sequential Search | Unindexed Data | O(n) |
| Binary Search | Sorted Data | O(log n) |


## Result Analysis

Binary Search generally performed faster because it reduces the search space by half during each iteration.

Sequential Search becomes slower as dataset size increases because every record may need to be checked.

Database indexing follows a similar principle by improving retrieval speed.


# 11. Screenshots

The following screenshots should be included:


## Google Form

Insert Screenshot


## CSV Dataset

Insert Screenshot


## Database Table Creation

Insert Screenshot


## Database Indexes

Insert Screenshot


## SQL Query Results

Insert Screenshot


## Python Search Execution

Insert Screenshot


# 12. Challenges Encountered

Several challenges were encountered during development.

## Data Collection

Ensuring consistent data formats for dates, prices, and categories required careful validation.


## Database Design

Selecting appropriate indexes required understanding how database retrieval works.


## Search Algorithm Implementation

Binary Search required sorting the dataset before execution.


## Performance Measurement

Execution times were very small, requiring accurate timing functions.


# 13. Lessons Learned

This project provided practical experience in:

- Database design
- Data organization
- SQL programming
- Index implementation
- Algorithm analysis
- Performance evaluation

Important lessons include:

- Structured data improves management efficiency.
- Indexes improve database retrieval speed.
- Binary Search is more efficient for large sorted datasets.
- Data quality affects system performance.


# 14. Conclusion

This project successfully demonstrated the design and implementation of a scalable retail information management system.

The project covered the complete data management process, including:

- Data collection
- Data representation
- Database implementation
- Indexing
- Retrieval
- Searching algorithms

The relational database provided efficient storage and retrieval capabilities, while the Python search simulation demonstrated the performance advantages of efficient search techniques.

The implementation shows how proper data organization, indexing, and algorithm selection contribute to improved information management systems.


# 15. References

- DTS 304 Data Management I Course Materials
- PostgreSQL/MySQL Documentation
- Python Documentation
- Database Management System Concepts