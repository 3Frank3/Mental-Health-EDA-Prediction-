import pandas as pd

Data1 = pd.read_csv("/Users/xuzhiwei/Mental Health (EDA + Prediction)/Dataset/Mental Illnesses Prevalence.csv")
Data2 = pd.read_csv("/Users/xuzhiwei/Mental Health (EDA + Prediction)/Dataset/Mental Health Adult Population Data.csv")
Data3 = pd.read_csv("/Users/xuzhiwei/Mental Health (EDA + Prediction)/Dataset/Depressive Symptoms US Population.csv")
Data4 = pd.read_csv("/Users/xuzhiwei/Mental Health (EDA + Prediction)/Dataset/Mental Health Countries Data.csv")

df1 = pd.DataFrame(Data1)
df2 = pd.DataFrame(Data2)
df3 = pd.DataFrame(Data3)
df4 = pd.DataFrame(Data4)


print(df1)