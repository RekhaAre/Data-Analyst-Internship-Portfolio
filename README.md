# Task 1 - Data Immersion & Wrangling

## Objective

Clean and prepare the sales dataset for analysis.

## Tasks Performed

* Loaded the dataset using Python and Pandas.
* Identified and handled missing values.
* Removed duplicate records.
* Converted the "Order Date" column to datetime format.
* Created a new "Year" column from the Order Date.
* Generated a cleaned dataset for further analysis.

## Files Included

* dataset/sales.csv
* scripts/cleaning.py
* output/cleaned_data.csv

## Tools Used

* Python
* Pandas
* VS Code

## Outcome

Successfully cleaned and transformed the dataset into an analysis-ready format.

# Task 2 - Exploratory Data Analysis (EDA)

## Objective

Perform Exploratory Data Analysis on the cleaned sales dataset and generate business insights.

## Tasks Performed

* Analyzed sales, profit, and order trends
* Identified top-performing products
* Performed region-wise sales analysis
* Performed category-wise sales analysis
* Created visualizations using Matplotlib
* Generated business insights

## Files Included

* cleaning.py
* eda.py
* cleaned_data.csv
* EDA_Report.txt
* region_sales.png
* category_sales.png
* monthly_sales_trend.png

## Tools Used

* Python
* Pandas
* Matplotlib
* VS Code

## Outcome

Successfully performed Exploratory Data Analysis and extracted meaningful insights from the dataset.


# Task 3 - Deep Dive Analysis Dashboard

## Objective
Built an interactive Power BI dashboard for business insights.

## Pages
1. Overview Dashboard
2. Product Analysis

## KPIs
- Total Sales
- Total Profit
- Quantity Sold
- Average Order Value

## Analysis
- Region-wise sales
- Category-wise performance
- Top product analysis

## Tools Used
- Power BI
- Excel/CSV

## Outcome
Interactive dashboard for business decision-making.

# Task 4 - Data Storytelling & Statistical Validation

## 📊 Project Title
Superstore Sales Analysis & Hypothesis Testing

---

## 🎯 Objective
To analyze sales data and validate business assumptions using statistical hypothesis testing.

---

## 📁 Dataset
- Dataset used: Superstore Sales Dataset (sales.csv)
- Contains information about:
  - Orders
  - Customers
  - Sales
  - Profit
  - Discount
  - Region
  - Categories

---

## 🧪 Hypothesis

### Null Hypothesis (H0):
Discount has no effect on Sales.

### Alternative Hypothesis (H1):
Discount has a significant effect on Sales.

---

## ⚙️ Methodology

- Data loaded using Pandas
- Data cleaning performed (handling missing values)
- Grouped data into:
  - Discount sales
  - No discount sales
- Applied Independent T-Test using SciPy

---

## 💻 Tools Used
- Python
- Pandas
- SciPy
- VS Code

---

## 📊 Results

- T-statistic: 0.5975  
- P-value: 0.5501  

---

## 📌 Conclusion

Since the p-value is greater than 0.05, we **accept the null hypothesis**.

👉 There is no statistically significant impact of discount on sales.

---

## 📁 Files Included

- task4.py (Python code)
- sales.csv (dataset)
- PPT presentation


## 🚀 Key Learning

- Hypothesis testing using Python
- Business decision validation using statistics
- Data-driven insights generation

---

##  Acknowledgement

Thanks to **ApexPlanet Software Pvt. Ltd.** for providing this internship opportunity and guiding through real-world data analytics tasks.
