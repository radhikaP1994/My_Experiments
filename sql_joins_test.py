import pandas as pd

df1=pd.DataFrame({"id":["A1","A2","A3","A4","A5"],"name":["Mandy","Josh","Jhon","Robert","Scott"]})
print(df1)
df2=pd.DataFrame({"id":["A1","A4","A6","A7","A8"],"city":["Mandy1","Josh1","Jhon1","Robert1","Scott1"]})
print(df2)
# df=pd.merge(df1,df2,how="inner")
#
# print(df)

# df=pd.merge(df1,df2,how="outer")
#
# print(df)

# df=pd.merge(df1,df2,how="right")
#
# print(df)

# df=pd.merge(df1,df2,how="left")
#
# print(df)

# df=pd.merge(df1,df2,how="full")
#
# print(df)

# df1=pd.DataFrame({"id":["A1","A2","A3","A4","A5"],"name":["Mandy","Josh","Jhon","Robert","Scott"]},index=[0,1,2,3,4])
#
# df2=pd.DataFrame({"id":["A1","A4","A6","A7","A8"],"city":["Mandy1","Josh1","Jhon1","Robert1","Scott1"]},index=[1,2,5,6,7])
#
# df=pd.merge(df1,df2,how="inner",left_index=True,right_index=True)
# print(df)
#




