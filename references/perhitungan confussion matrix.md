### Formulas

1. **Precision for Class \(i\)**:
   \[
   \text{Precision}_i = \frac{TP_i}{TP_i + FP_i}
   \]

2. **Recall for Class \(i\)**:
   \[
   \text{Recall}_i = \frac{TP_i}{TP_i + FN_i}
   \]

3. **Weighted Precision**:
   \[
   \text{Weighted Precision} = \frac{\sum_{i} (\text{Precision}_i \times \text{Support}_i)}{\text{Total Instances}}
   \]

4. **Weighted Recall**:
   \[
   \text{Weighted Recall} = \frac{\sum_{i} (\text{Recall}_i \times \text{Support}_i)}{\text{Total Instances}}
   \]

Where:
- \(TP_i\) = True Positives for class \(i\)
- \(FP_i\) = False Positives for class \(i\)
- \(FN_i\) = False Negatives for class \(i\)
- \(\text{Support}_i\) = Number of true instances for class \(i\)
- \(\text{Total Instances}\) = Sum of instances for all classes

### Step-by-Step Calculation

#### Step 1: Calculate Precision and Recall for Each Class

1. **Class 0**:
   - **Precision**: 
     \[
     \text{Precision}_0 = \frac{TP_0}{TP_0 + FP_0} = \frac{6}{6 + 0} = 1.0
     \]
   - **Recall**: 
     \[
     \text{Recall}_0 = \frac{TP_0}{TP_0 + FN_0} = \frac{6}{6 + 2} = 0.75
     \]

2. **Class 1**:
   - **Precision**: 
     \[
     \text{Precision}_1 = \frac{TP_1}{TP_1 + FP_1} = \frac{12}{12 + 0} = 1.0
     \]
   - **Recall**: 
     \[
     \text{Recall}_1 = \frac{TP_1}{TP_1 + FN_1} = \frac{12}{12 + 1} = 0.923
     \]

3. **Class 2**:
   - **Precision**: 
     \[
     \text{Precision}_2 = \frac{TP_2}{TP_2 + FP_2} = \frac{13}{13 + 0} = 1.0
     \]
   - **Recall**: 
     \[
     \text{Recall}_2 = \frac{TP_2}{TP_2 + FN_2} = \frac{13}{13 + 1} = 0.929
     \]

4. **Class 3**:
   - **Precision**: 
     \[
     \text{Precision}_3 = \frac{TP_3}{TP_3 + FP_3} = \frac{13}{13 + 8} = 0.62
     \]
   - **Recall**: 
     \[
     \text{Recall}_3 = \frac{TP_3}{TP_3 + FN_3} = \frac{13}{13 + 0} = 1.0
     \]

5. **Class 4**:
   - **Precision**: 
     \[
     \text{Precision}_4 = \frac{TP_4}{TP_4 + FP_4} = \frac{3}{3 + 0} = 1.0
     \]
   - **Recall**: 
     \[
     \text{Recall}_4 = \frac{TP_4}{TP_4 + FN_4} = \frac{3}{3 + 4} = 0.429
     \]

#### Step 2: Calculate Weighted Precision and Recall

To calculate weighted precision and recall, multiply the precision and recall of each class by the number of true instances (support) of that class, then divide by the total number of instances.

- **Support for each class**:
  - Class 0: \(8 \, (\text{6 true positive} + \text{2 false negative})\)
  - Class 1: \(13 \, (\text{12 true positive} + \text{1 false negative})\)
  - Class 2: \(14 \, (\text{13 true positive} + \text{1 false negative})\)
  - Class 3: \(13 \, (\text{13 true positive} + \text{0 false negative})\)
  - Class 4: \(7 \, (\text{3 true positive} + \text{4 false negative})\)

- **Total number of instances**: 
  \[
  8 + 13 + 14 + 13 + 7 = 55
  \]

1. **Weighted Precision**:
   \[
   \text{Weighted Precision} = \frac{(1.0 \times 8) + (1.0 \times 13) + (1.0 \times 14) + (0.62 \times 13) + (1.0 \times 7)}{55}
   \]
   \[
   = \frac{8 + 13 + 14 + 8.06 + 7}{55}
   = \frac{50.06}{55} \approx 0.91
   \]

2. **Weighted Recall**:
   \[
   \text{Weighted Recall} = \frac{(0.75 \times 8) + (0.923 \times 13) + (0.929 \times 14) + (1.0 \times 13) + (0.429 \times 7)}{55}
   \]
   \[
   = \frac{6 + 11.999 + 13.006 + 13 + 3.003}{55}
   = \frac{47.008}{55} \approx 0.85
   \]

### Summary
- **Weighted Precision**: \( 0.91 \)
- **Weighted Recall**: \( 0.85 \)