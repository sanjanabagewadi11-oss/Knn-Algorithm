'''
Problem 1: Predicting Student result as PASS / FAIL 
Given : Predict PASS (A), FAIL (B) based on 3 Subject marks: 

Student	Math (X)	Science (Y) 	English (Z)	     Result 

S1		70		        65		        60		     PASS A 

S2		75		        70		        65		     PASS A 

S3		80		        68		        70		     PASS A 

S4		40		        45		        50		     FAIL B 

S5		45		        50		        55		     FAIL B 

 

Query q:	72		66		62		?
'''
import pandas as pd
import math

data = {
    "X" : [[70,65,60],[75,70,65],[80,68,70],[40,45,50] ,[45, 50, 55]],
    "Y" : ["PASS", "PASS", "PASS", "FAIL", "FAIL"],
    "dist" : []
    }

q = [72, 66, 62]

dist = []

for v in data["X"]:
    x1, y1, z1 = v
    d =math.sqrt((q[0] - x1) ** 2 + (q[1] - y1) ** 2 + (q[2] - z1) ** 2)
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

z = df.head(k)
pass_no = (z["Y"] == "Pass").sum()
fail_no = (z["Y"] == "Fail").sum()
print("PASS :",pass_no)
print("FAIL:",fail_no)

if pass_no > fail_no:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")