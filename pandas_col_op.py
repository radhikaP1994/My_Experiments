import pandas as pd
import numpy as np
l={"name":["radhi","asd","dgy"],
   "age":[25,24,63],
   "salary":[1,2,3,]}
df=pd.DataFrame(l)
print(df)
df1=df[["name"]]
print(df1)
