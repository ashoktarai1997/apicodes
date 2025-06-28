import pandas as pd

data = pd.read_csv("Data1.csv")
data.columns = data.columns.str.strip().str.lower()  # Normalize column names
print(data.loc[3, ['open','symbol']])  # Now this works with lowercase
print(data)
print(data.iloc [[1,3,4],0])

# print(data.loc[[3,"OPEN"]])
print(data.head(4).tail(1))

print(data.shape)
print(data.dtypes)
print(data.info)
dict = {
    "empno" :   ["01","02","03","04"],
    "name"  :   ["ashok","Akshaya","Baba","Maa"],
    "role"  :   ["it","Business","job","housewife"]
}

print(dict)
df = pd.DataFrame(dict)
print(df)
















