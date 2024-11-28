import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
#check number of rows
print("number of rows",pd.options.display.max_rows)