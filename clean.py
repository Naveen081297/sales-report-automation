import pandas as pd
pd.set_option("display.max_columns",None)

df = pd.read_csv("sales_raw.csv")
print("Row at start: ", len(df))

dupes = df[df.duplicated()]
print("duplicate row found:")
print(dupes)

df = df.drop_duplicates()
print("Rows after removing duplicates:", len(df))