import numpy as np
#NOTE:The reference value are illustrative and may vary by laboratory.
report = np.array([['Total protein',6,8],
                   ['Albumin',3.5,5]])
Total_protein = float(input("""Enter your measured protein value(in g/dl): """))
Total_albumin = float(input("""Enter your measured albumin value(in g/dl): """))
if (Total_protein >= float(report[0][1]) and Total_protein <= float(report[0][2])):
    Total_protein_check = "Normal"
else:
    Total_protein_check = "Abnormal"
    
if (Total_albumin>= float(report[1][1]) and Total_albumin <= float(report[1][2])):
    Total_albumin_check = "Normal"
else:
    Total_albumin_check = "Abnormal"
print("Total protein:" + Total_protein_check)
print("Total albumin:" +Total_albumin_check)

