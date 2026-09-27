<div align="center">

# 📊 IBM HR Analytics – Data Pipeline & Dashboard

An end-to-end data analysis pipeline processing employee income data—from raw CSV to interactive Power BI report.

<img width="631" height="353" alt="dashboard" src="https://github.com/user-attachments/assets/4b9f5e5c-a7cb-45e2-90e6-f6646444e83f" />

</div>

## 👋 Welcome!

Thank you for taking an interest in my project! This repository contains a full analytical pipeline I created as part of my journey into the world of data analysis. 

The main goal was to take raw HR data, clean and transform it programmatically, store it in a relational database, and build a report providing insight into income levels and pay equity.

---

## 📁 Dataset Overview

* **Dataset Name:** IBM HR Analytics Employee Attrition & Performance
* **Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
* **Domain:** Human Resources / Employee Performance & Income

---

## 🛠️ Pipeline Architecture

The workflow is divided into three structured steps:

Python Script (Data Cleaning) ───► SQL Server (Data View) ───► Power BI (Dashboard)

### 1. 🐍 Python Data Cleaning
* **Goal:** Preprocess raw data before ingestion into SQL Server.
* **Key Tasks:**
  * Deduplication (identifying and removing duplicate rows)
  * String sanitation (stripping leading and trailing whitespace)
  * Missing value analysis (counting NULL instances)
  * Feature encoding (converting `Yes`/`No` binary strings to `1`/`0`)
  * Database ingestion (automated export to SQL Server)

### 2. 🗄️ SQL Transformation
* **Goal:** Filter and structure data for optimized visualization.
* **Key Tasks:**
  * Created an optimized **SQL View** to restrict columns and export only relevant features to Power BI, reducing memory overhead.

### 3. 📊 Power BI Reporting
* **Goal:** Build a final income report for a fictitious company.

---

## 💡 Power BI Highlights

Key Power BI techniques and concepts utilized in this project:

| Category | Features & Techniques Used |
| :--- | :--- |
| **ETL & Data Prep** | Power Query transformations |
| **Data Modeling** | Basic Data Modeling, Table Relationships (Star Schema basics) |
| **Visualizations** | Core charts (Bar, Scatter plots), Tables & Matrices, Cards |
| **DAX & Logic** | Custom Conditional Columns, Measures |
| **UX/UI** | Executive Dashboard layout and UI design
