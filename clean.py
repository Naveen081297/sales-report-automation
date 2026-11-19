import pandas as pd
pd.set_option("display.max_columns",None)

df = pd.read_csv("sales_raw.csv")
print("Row at start: ", len(df))

dupes = df[df.duplicated()]
print("duplicate row found:")
print(dupes)

df = df.drop_duplicates()
print("Rows after removing duplicates:", len(df)) 

print("Branches before:", df["branch"].unique())
df["branch"] = df["branch"].str.strip().str.title()
df["product"] = df["product"].str.strip().str.title()
print("Branches after:", df["branch"].unique())

d1 = pd.to_datetime(df["date"],format="%d-%m-%Y",errors="coerce")
d2=pd.to_datetime(df["date"],format="%Y/%m/%d",errors="coerce")
df["date"]=d1.fillna(d2)
print(df["date"])
