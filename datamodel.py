import pandas as pd
df=pd.read_csv("C:/Users/Ch. Hamza/Downloads/dirty_cafe_sales.csv")
df.head()
df.info()
print(df.isnull().sum())
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")
print(df.head(10))
important_cols = ["Item", "Quantity", "Price Per Unit", "Total Spent", "Payment Method", "Location", "Transaction Date"]

df = df.dropna(subset=important_cols)

print(df.isnull().sum())
df = df[~df["Item"].isin(["UNKNOWN", "ERROR"])]
df = df[~df["Payment Method"].isin(["UNKNOWN", "ERROR"])]
df = df[~df["Location"].isin(["UNKNOWN", "ERROR"])]
df = df[~df["Transaction Date"].isin(["UNKNOWN", "ERROR"])]
# Drop rows where these columns are still empty
df = df.dropna(subset=["Item", "Payment Method", "Location"])
print(df.isnull().sum())
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")
df = df.dropna(subset=["Transaction Date"])
print(df["Transaction Date"].head())
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())
df.to_csv("cleaned_cafe_sales.csv", index=False)

print("✅ Cleaned dataset saved as cleaned_cafe_sales.csv")

