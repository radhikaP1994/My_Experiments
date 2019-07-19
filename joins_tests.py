import pandas as pd

df1=pd.DataFrame({"id1":["A1","A2","A3","A4","A5"],"name":["Mandy","Josh","Jhon","Robert","Scott"],"salary":[10000,20000,30000,50000,60000]})
print(df1)
df2=pd.DataFrame({"id1":["A1","A4","A6","A7","A8"],"city":["Mandy1","Josh1","Jhon1","Robert1","Scott1"]})
print(df2)

# df=pd.merge(df1,df2, on=['id1'],how='inner')
# print(df)
#
# df=pd.merge(df1,df2, on=['id1'],how='left')
# print(df)
#
# df=pd.merge(df1,df2, on=['id1'],how='right')
# print(df)
#
# df=pd.merge(df1,df2, on=['id1'],how='outer',indicater="indicator_col")
# print(df)
#
# df=df1.join(df2,rsuffix='_salary')
#
# print(df)
# #
# df=df1.join(df2,lsuffix='_salary')

# print(df)

