import pandas as pd

# Create a dataframe from csv to be able to manipulate data
df = pd.read_csv("lab 1 - csv.csv", sep=";")

# Clean up some "dirty" data
df["id"] = df["id"].str.strip() # Remove spaces before/after strings for price...
df["name"] = df["name"].str.strip() # ...name...
df["currency"] = df["currency"].str.strip() # ...and currency

df["price"] = pd.to_numeric(df["price"],errors= "coerce") # Set invalid prices to NaN
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce") # Set invalid datetimes to NaT

# Collect products with missing id value
missing_id = df[df["id"].isna()]
print(missing_id, "\n")

# Collect products with missing name value
missing_name = df[df["name"].isna()]
print(missing_name, "\n")

# Collect products with missing currency value
missing_currency = df[df["currency"].isna()]
print(missing_currency, "\n")

# Collect products with invalid prices such as 0 or -50 (free products should be invalid)
invalid_prices = df[df["price"] <= 0]
print(invalid_prices, "\n")

# Rejected products (has any incorrect value)
rejected_products = df[
    (df["price"] <= 0) |
    (df["id"].isna()) |
    (df["name"].isna())
]
# Export rejected products
rejected_products.to_csv("output/rejected_products.csv", index=False)

# Collect valid products where name, price, currency values are correct (after cleaning)
valid_products = df[
    (df["name"].notna()) &
    (df["price"] > 0) &
    (df["currency"].notna())
]
print(valid_products, "\n")

# Collect products with high prices (over 1000)
luxury_products = valid_products[valid_products["price"] > 1000]
print(luxury_products.head(5))

# Collect some values to use for analytics df and csv
average_price = valid_products["price"].mean()
median_price = valid_products["price"].median()
product_count = len(valid_products)
missing_price_count = df["price"].isna().sum()
# Missing prices counted from original df as valid products do not have any

# Assemble data into new dataframe
analytics_summary = pd.DataFrame({
    "average_price": [average_price],
    "median_price": [median_price],
    "product_count": [product_count],
    "missing_price_count": [missing_price_count]
})

# Export a csv into output
analytics_summary.to_csv("output/analytics_summary.csv", index=False)