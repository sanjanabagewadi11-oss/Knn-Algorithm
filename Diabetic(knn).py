'''
Predict Diabetes Yes / No 

 Given Dataset: 

Glucose		BMI	    Age	    Diabetes 

120		    25	    25	    No 

140		    30	    35	    Yes 

130		    28	    30	    No 

180		    32	    45	    Yes 

110		    22	    20	    No 

 
Query: Glucose = 150, BMI = 51, Age 38 
'''
import pandas as pd
import math

 
data = {
    "X": [[120, 25, 25],[140, 30, 35],[130,28,30],[180,32,45],[110,22,20]],
    "Y": ["No", "Yes", "No", "Yes", "No"],
    "dist": []
}
 
#q = [72, 66, 62]
q = [150,51,38]


dist = []
 
for v in data["X"]:
    x1,y1,z1=v
    d = math.sqrt((q[0] - x1) **2 + (q[1] - y1) **2+ (q[2] - z1)**2)
    dist.append(d)
print(dist)
 
 
data["dist"] = dist
 
 
df = pd.DataFrame(data)
 
 
df = df.sort_values("dist")
 
print(df)
 
k = 5
print(df.head())
Yes_no = 0
No_no = 0
 
z = df.head(k)
Yes_no = (z["Y"] == "Yes").sum()
No_no = (z["Y"] == "No").sum()
 
print("Yes :",Yes_no)
print("No:",No_no)
 
if Yes_no > No_no:
    print("Prediction: Yes")
else:
    print("Prediction: No")