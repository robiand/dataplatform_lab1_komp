import pandas as pd

# Create a dataframe from csv to be able to manipulate data
df = pd.read_csv("lab 1 - csv.csv", sep=";")
print(df, "\n") # test print before cleanup

# Clean up some "dirty" data
df["id"] = df["id"].str.strip() # Remove spaces before/after strings for price...
df["name"] = df["name"].str.strip() # ...name...
df["currency"] = df["currency"].str.strip() # ...and currency

df["price"] = pd.to_numeric(df["price"],errors= "coerce") # Set invalid prices to NaN
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce") # Set invalid datetimes to NaT

print(df, "\n") # test print after cleanup

# Collect products with missing currency value
missing_currency = df[df["currency"].isna()]
print(missing_currency, "\n")

# Collect producs with invalid prices
rejected_price_products = df[df["price"] < 0]

# Collect valid products where prices are correct
valid_products = df[df["price"] >= 0]

# Collect products with high prices (over 1000)
luxury_products = valid_products[valid_products["price"] > 1000]
print(luxury_products.head(5))

# Export a csv into output
df.to_csv("output/analytics_summary.csv", index=False)