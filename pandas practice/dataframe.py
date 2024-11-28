import pandas as pd
data={
    "cars":['kia','bmw','tata','audi'],
    'ranks':[5,4,3,2],
    "user":['chandan','basha','gokul','dinesh']
            }
x=pd.DataFrame(data,index=['a','b','c','d'])
print(x)


#dictionary
mydictionary={"player name":["kohli","maxwell","rohit"],"rank":[1,2,3],"country":['ind','aus','ind'],}
z=pd.Series(mydictionary)
print(z)