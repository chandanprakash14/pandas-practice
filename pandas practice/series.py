import pandas as pd
calories={ 
    "Day 1":420,
    "Day 2":380,
    "Day 3":390
}
y=pd.Series(calories)
print(y)
#change index values
x=pd.Series(calories,index=['a','b','c'])
print(x)

#list
a=[12,23,34,56]
x=pd.Series(a)
print(x)
#update
x=x.replace(23,45)
print(x)
