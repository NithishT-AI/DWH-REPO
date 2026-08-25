# Enterprise Data Warehouse (Banking Domain)

## Overview
A scalable enterprise data warehouse for banking, integrating raw data from multiple systems and delivering trusted insights through a layered architecture: 



## Problem Statement
Banks handle data across branches, customers, employees, loans, accounts, credit cards, payments, and transactions — often arriving in inconsistent formats from multiple sources. This project centralizes and standardizes that data into a single source of truth, preserving history while enabling fast, department-focused insights and KPI tracking.

## Architecture
| Layer          | Purpose                                                |
|----------------|------------------------------------------------------- |
| **Staging**    | Raw data ingestion from source systems                 |
| **ODS**        | Cleansed, de-duplicated, standardized data             |
| **DWH**        | Business rules applied; conformed dimensions and facts |
| **Data Marts** | Department-focused facts and KPI aggregates            |
| **Reporting**  | Dashboards and reports for end users                   |

## Conceptual Data Model - High Level
<img width="1403" height="180" alt="image" src="https://github.com/user-attachments/assets/b1a9eed7-9b36-4bb5-ae8d-dfddb7849538" />

## Logical Data Model - Low Level
<img width="553" height="561" alt="image" src="https://github.com/user-attachments/assets/9138809a-5d05-4c36-94bb-1ab57e2d86f9" />


## Key Domains
Branches, Customers, Employees, Loans, Accounts, Credit Cards, Payments, Transactions

## Key Use Cases
- Branch performance analysis
- Fraud detection
- Customer profiling

## Consumers
Executives, auditors, clients, managers, and outbound/third-party systems

## Key Features
- ✅ Single source of truth with historical data
- ✅ Faster queries via single fact tables per mart
- ✅ KPI tracking through aggregate tables
- ✅ Scalable, layered design

## Project Status
🚧 In progress — tech stack and setup details to be added.
