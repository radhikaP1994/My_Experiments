import pandas as pd
import numpy as np
l={"name":["radhi","asd","dgy","shh"],
   "age":[25,24,63,65],
   "salary":[1,2,3,45]}
df1=pd.DataFrame(l)
dict = {'name': ["radhi1", "asd1", "dgy1", "shh1"],
        'age': [30, 45, 56, 34],
        'salary': [56, 40, 80, 98]
        }
df2=pd.DataFrame(dict)
df=pd.concat([df1,df2])
print(df)



