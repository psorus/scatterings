import numpy as np

q1=np.load("../01/out.npz")["q"]
q2=np.load("../02/out.npz")["q"]


print("Maximum Difference:",np.max(np.abs(q1-q2)))
#0.00122
print("Mean Difference:",np.mean(np.abs(q1-q2)))
#4.55e-5
print("Comparison Scale:",np.mean(np.abs(q1)))
#1616.7

