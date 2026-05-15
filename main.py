import numpy as np
Marks=input("Enter the marks separated by space:")
Marks= np.array(Marks.split(), dtype= int)

Mean= np.mean(Marks)
print("Mean of marks :",Mean)

Maximum= np.max(Marks)
print("Maximum of marks :",Maximum)

Minimum = np.min(Marks)
print("Minimum of marks :",Minimum)

print("Topper Marks:",Maximum)

Above_avg = Marks[Marks > Mean]
print("Above average marks:",Above_avg)
