''''
EV Vehicle Breakdown Prediction 

 
Engine	Vibration	KM since service	Breakdown 

90	    20		    1000			    No 

120	    80		    8000			    Yes 

110	    70		    7500			    Yes 

Temp = 115 

Vibration = 75 

KM = 700 

Breakdown = ? 
'''
import math
import pandas as pd
 
data = {
    "X": [[90, 20, 1000],[120, 80, 8000],[110, 70, 7500]],
    "Y": ["No", "Yes", "Yes"],
    "dist": []
}
 
q = [115, 75, 700]
 
dist = []
 
for v in data["X"]:
    x1, x2, x3 = v
    d = math.sqrt((q[0] - x1) ** 2 +(q[1] - x2) ** 2 +(q[2] - x3) ** 2 )
    dist.append(d)
print("Distances:")
print(dist)
 
data["dist"] = dist
 
df = pd.DataFrame(data)
 
df = df.sort_values("dist")
 
print("\nSorted Data:")
print(df)
 
k = 3
 
z = df.head(k)
 
yes_no = (z["Y"] == "Yes").sum()
no_no = (z["Y"] == "No").sum()
 
print("\nYES:", yes_no)
print("NO :", no_no)
 
if yes_no > no_no:
    print("Prediction: Breakdown YES")
else:
    print("Prediction: Breakdown NO")