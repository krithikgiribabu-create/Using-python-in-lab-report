# Using Python in Lab Reports 

A clinical informatics prototype exploring how computational logic can support clinicians and prevent human fatigue errors in high-volume laboratory environments.

# What is albumin?
Albumin is the most abundant plasma protein, synthesized by the liver. It helps maintain plasma colloid osmotic pressure and transports various substances, including hormones, fatty acids, and drugs. Serum albumin is commonly measured as part of liver function and nutritional assessment.

##  Liver Function Test (LFT) Analyzer
This script uses array-based logic to evaluate a patient's custom laboratory values against standardized test reference intervals. 

### Why This Tool Matters:
- **Reduces Cognitive Load:** On heavy outpatient shifts, reviewing hundreds of panels manually can occasionally lead to oversight of minor clinical elevations. This script flags anomalies automatically.
- **Scalable Framework:** By managing parameters within a core matrix, the script can easily expand from basic liver markers to whole metabolic or chemical panels.

### Expected System Output:
Enter your measured protein value(in g/dl): 5.4
Enter your measured albumin value(in g/dl): 4.2

[System Analysis Results]
Total protein: Abnormal
Total albumin: Normal
