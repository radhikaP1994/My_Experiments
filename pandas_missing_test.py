# importing pandas as pd
import pandas as pd1

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {'First Score': [100, 90, 0, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98],
        'Fourth Score':[1,2,4,5]}

# creating a dataframe from list
df = pd1.DataFrame(dict)
print(df)
# using isnull() function
df1=df.isnull()
print(df1)

df2=df.notnull()
print(df2)

df3=df.fillna(3)
print(df3)

df4=df.dropna()
print(df4)

df5=df.drop_duplicates()
print(df5)



