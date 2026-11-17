import pandas as pd
import math

data = {
    "X" : [[1,4],[2,6],[3,5],[4,7],[5,6],[6,8],[5,4],[2,8]],
    "Y" : ["Fail","Fail","Fail","Pass","Pass","Pass","Fail","Fail"],
    "dist" : []
    }

q =[4,6]

dist = []

for v in data["X"]:
    x1,y1=v
    d = math.sqrt((q[0] - x1) **2 + (q[1] - y1) **2)
    dist.append(d)
print(dist)

data["dist"]=dist


df = pd.DataFrame(data)

df = df.sort_values("dist")
print(df)

k = 3
print(df.head())

pass_no = 0
fail_no = 0

for i in range(k):

    if df["Y"].iloc[i] == "Pass":
        pass_no += 1
    else:
        fail_no += 1
print("PASS :",pass_no)
print("FAIL :",fail_no)

if pass_no > fail_no:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")

