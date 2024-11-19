import pandas as pd

# Data for the DataFrame
data = {
    "Americano": [562, 623],
    "Latte": [812, 925],
    "Espresso": [426, 384],
    "Cappuccino": [852, 756],
}
# Set the index
index = ["2021 Sales", "2022 Sales"]

# Create the DataFrame
coffee_sales = pd.DataFrame(data, index=index)

# Print the DataFrame
print("Initial DataFrame:")
print(coffee_sales)

# Calculate the total sales for each beverage across the two years
coffee_sales.loc["Total Sales"] = coffee_sales.sum()

# Calculate the year-over-year growth rate for each beverage type
coffee_sales.loc["YoY Growth (%)"] = (
    ((coffee_sales.loc["2022 Sales"] - coffee_sales.loc["2021 Sales"]) / coffee_sales.loc["2021 Sales"]) * 100).round(2
)

# Print the updated DataFrame
print("\nUpdated DataFrame with Total Sales and YoY Growth:")
print(coffee_sales)

# Identify the best-selling and least-selling beverage for each year
best_selling_2021 = coffee_sales.loc["2021 Sales"].idxmax()
least_selling_2021 = coffee_sales.loc["2021 Sales"].idxmin()

best_selling_2022 = coffee_sales.loc["2022 Sales"].idxmax()
least_selling_2022 = coffee_sales.loc["2022 Sales"].idxmin()

print(f"\nIn 2021, the best-selling beverage was {best_selling_2021}, and the least-selling beverage was {least_selling_2021}.")
print(f"In 2022, the best-selling beverage was {best_selling_2022}, and the least-selling beverage was {least_selling_2022}.")
