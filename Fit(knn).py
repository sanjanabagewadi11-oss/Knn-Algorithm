'''
Problem Predict if person is Fit or Unfit based on Height (cm), Weight (kg), Age(years) 

Given Data: 

Sno	Height		Weight		Age	    Class 

1	170		    65		    25	    Fit 

2	165		    80		    30	    Unfit 

3	180		    70		    22	    Fit 

4	160		    75		    35	    Unfit 

5	175		    68		    28	    Fit 

 

Query:	168		70		26	? 
'''
import pandas as pd
import math

 
data = {
    "X": [[170, 65, 25],[165, 80, 30],[180, 70,22],[160, 75, 35],[175, 68, 28]],
    "Y": ["Fit", "Unfit", "Fit", "Unfit", "Fit"],
    "dist": []
}
 
#q = [72, 66, 62]
q = [168, 70, 26]


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
Fit_no = 0
Unfit_no = 0
 
z = df.head(k)
Fit_no = (z["Y"] == "Fit").sum()
Unfit_no = (z["Y"] == "Unfit").sum()
 
print("Fit :",Fit_no)
print("Unfit:",Unfit_no)
 
if Fit_no > Unfit_no:
    print("Prediction: Fit")
else:
    print("Prediction: Unfit")