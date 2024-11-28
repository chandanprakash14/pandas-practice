import pandas as pd
a=pd.read_json('data.json')
print(a.to_string())

#check number of rows

print(pd.options.display.max_rows)