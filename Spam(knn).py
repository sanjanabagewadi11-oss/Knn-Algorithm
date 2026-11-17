''''
Problem: Email is a Spam or not Spam 

 Features: 

X1 = Number of Times word FREE appears 

X2 = Number of ‘!!!’ marks 

 Given Dataset: 

X1 (FREE)	X2 (!!!)		Spam 

0		    0		    Not Spam 

1		    0		    Not Spam 

3		    2		    Spam 

5		    3		    Spam 

 
Query: Email has FREE 2 Times, and ‘!!!’  1 Time
'''
import pandas as pd
import math

 
data = {
    "X": [[0,0], [1,0], [3,2], [5,8]],
    "Y": ["NotSpam", "NotSpam", "Spam", "NotSpam"],
    "dist": []
}
 
#q = [72, 66, 62]
q = [2,1]


dist = []
 
for v in data["X"]:
    x1,y1=v
    d = math.sqrt((q[0] - x1) **2 + (q[1] - y1) **2)
    dist.append(d)
print(dist)
 
 
data["dist"] = dist
 
 
df = pd.DataFrame(data)
 
 
df = df.sort_values("dist")
 
print(df)
 
k = 3
 
z = df.head(k)
 
# Count Yes and No
Spam_no = (z["Y"] == "Spam").sum()
NotSpam_no = (z["Y"] == "NotSpam").sum()
 
print("\nSpam :", Spam_no)
print("NotSpam  :", NotSpam_no)
 
# Prediction
if Spam_no > NotSpam_no:
    print("Prediction: Spam")
else:
    print("Prediction: NotSpam")