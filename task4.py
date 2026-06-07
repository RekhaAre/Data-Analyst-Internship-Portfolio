import pandas as pd
from scipy import stats

# Load dataset (IMPORTANT: correct file name)
df = pd.read_csv("sales.csv")

print("DATA LOADED SUCCESSFULLY")
print(df.head())

# Check columns
print(df.columns)

# Remove missing values
df = df.dropna()

# Hypothesis:
# H0: Discount has no effect on Sales
# H1: Discount affects Sales

# ⚠️ IMPORTANT: adjust column names if needed after printing df.columns
discount_sales = df[df["Discount"] > 0]["Sales"]
no_discount_sales = df[df["Discount"] == 0]["Sales"]

# T-test
t_stat, p_value = stats.ttest_ind(discount_sales, no_discount_sales)

print("\nT-statistic:", t_stat)
print("P-value:", p_value)

# Decision
if p_value < 0.05:
    print("Reject H0 → Discount affects Sales")
else:
    print("Accept H0 → No significant effect")