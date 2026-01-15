import pandas as pd
sales_report = [
    {"date": "2026-01-01", "product": "Laptop", "category": "Electronics", "quantity": 2, "price": 55000, "salesperson": "Anil"},
    {"date": "2026-01-01", "product": "Mouse", "category": "Electronics", "quantity": 5, "price": 500, "salesperson": "Meera"},
    {"date": "2026-01-02", "product": "Chair", "category": "Furniture", "quantity": None, "price": 3500, "salesperson": "Rahul"},
    {"date": "2026-01-02", "product": "Desk", "category": "Furniture", "quantity": 1, "price": None, "salesperson": "Rahul"},
    {"date": "2026-01-03", "product": "Pen", "category": "Stationery", "quantity": 20, "price": 10, "salesperson": None},
    {"date": "2026-01-03", "product": "Notebook", "category": "Stationery", "quantity": 10, "price": 50, "salesperson": "Anil"},
    {"date": None, "product": "Printer", "category": "Electronics", "quantity": 1, "price": 12000, "salesperson": "Meera"},
    {"date": "2026-01-04", "product": "Monitor", "category": "Electronics", "quantity": 2, "price": None, "salesperson": "Anil"},
    {"date": "2026-01-05", "product": None, "category": "Furniture", "quantity": 1, "price": 8000, "salesperson": "Rahul"},
    {"date": "2026-01-05", "product": "Table Lamp", "category": None, "quantity": 3, "price": 1500, "salesperson": "Meera"}
]
df=pd.DataFrame(sales_report)
print(df.shape)
print(df.columns)
print(df.info())
print(df.head())
print(df.tail())
print(df.isnull())
print(df.isnull().sum())
most_frequent_date=df["date"].mode()[0]
print(most_frequent_date)
df["date"].fillna(most_frequent_date,inplace=True)
print(df)
print(df.isnull().sum())
df["product"].fillna("unknown",inplace=True)
print(df)
most_frequent_category=df["category"].mode()[0]
df["category"].fillna(most_frequent_category,inplace=True)
print(df)
print(df.isnull().sum())
average_quantity=df["quantity"].mean()
print(average_quantity)
df["quantity"].fillna(average_quantity,inplace=True)
print(df)
price=df["price"].mean()
df["price"].fillna(price,inplace=True)
print(df)
df.dropna(subset=["salesperson"],inplace=True)
print(df)
print(df.isnull().sum())

# sales count by category
print(df["category"].value_counts())
# sales count by sales_person
print(df["salesperson"].value_counts())
# category electronics and quantity >2
print(df[((df["category"]=="Electronics").value_counts())&(df["quantity"]>2)])
print(df.groupby("category")["quantity"].sum())
print(df.groupby("category")["price"].sum())
print(df.sort_values(by="price",ascending=False))
print(df.loc[2])
print(df.iloc[2])
# costly product details
print(df.iloc[df["price"].idxmax()])

print(df.loc[df["price"].idxmin()])
print(df)
df["revenue"]=df["price"]*df["quantity"]
print(df.loc[0,["price","quantity"]])

"""
fillna() fill null values
dropna(subset=["colname"])  drop rows
isnull()  check that column is null or not
isnull().sum() null content
groupby()    to group
values_count()   return count of unique value
sort_values(by="colname",ascending=False)  to sort
df.loc[] to get rows
df.iloc[] to get rows
"""