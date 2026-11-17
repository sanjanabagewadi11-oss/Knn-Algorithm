'''
Problem: Will bank give loan? 

 Given Dataset: 

 Income		Credit Score	Loan Approved 

(Lakhs)		( 0 - 10)	( 0 - No / 1 - Yes ) 

2		    3		    No 

3		    4		    No 

5		    7		    Yes 

8		    8	    	Yes 

 Query: Income = 4L, Score = 6	Loan =? 
'''
import pandas as pd
import math

 
data = {
    "X": [[2,3], [3,4], [5,7], [8,8]],
    "Y": ["No", "No", "Yes", "Yes"],
    "dist": []
}
 
#q = [72, 66, 62]
q = [4,6]


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
yes_no = (z["Y"] == "Yes").sum()
no_no = (z["Y"] == "No").sum()
 
print("\nYES :", yes_no)
print("NO  :", no_no)
 
# Prediction
if yes_no > no_no:
    print("Prediction: YES - Loan Approved")
else:
    print("Prediction: NO - Loan Not Approved")