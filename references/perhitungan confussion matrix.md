### Confusion Matrix
```plaintext
[[ 6  0  0  2  0]
 [ 0 12  0  1  0]
 [ 0  0 13  1  0]
 [ 0  0  0 13  0]
 [ 0  0  0  4  3]]
```

### Step-by-Step Calculation

#### Step 1: Calculate Precision and Recall for Each Class
1. **Class 0**:
   - **Precision**: \( \frac{TP_0}{TP_0 + FP_0} = \frac{6}{6 + 0} = 1.0 \)
   - **Recall**: \( \frac{TP_0}{TP_0 + FN_0} = \frac{6}{6 + 2} = 0.75 \)

2. **Class 1**:
   - **Precision**: \( \frac{TP_1}{TP_1 + FP_1} = \frac{12}{12 + 0} = 1.0 \)
   - **Recall**: \( \frac{TP_1}{TP_1 + FN_1} = \frac{12}{12 + 1} = 0.923 \)

3. **Class 2**:
   - **Precision**: \( \frac{TP_2}{TP_2 + FP_2} = \frac{13}{13 + 0} = 1.0 \)
   - **Recall**: \( \frac{TP_2}{TP_2 + FN_2} = \frac{13}{13 + 1} = 0.929 \)

4. **Class 3**:
   - **Precision**: \( \frac{TP_3}{TP_3 + FP_3} = \frac{13}{13 + 8} = 0.62 \)
   - **Recall**: \( \frac{TP_3}{TP_3 + FN_3} = \frac{13}{13 + 0} = 1.0 \)

5. **Class 4**:
   - **Precision**: \( \frac{TP_4}{TP_4 + FP_4} = \frac{3}{3 + 0} = 1.0 \)
   - **Recall**: \( \frac{TP_4}{TP_4 + FN_4} = \frac{3}{3 + 4} = 0.429 \)

#### Step 2: Calculate Weighted Precision and Recall
To calculate weighted precision and recall, multiply the precision and recall of each class by the number of true instances (support) of that class, then divide by the total number of instances.

- **Support for each class**:
  - Class 0: 8 (6 + 2)
  - Class 1: 13 (12 + 1)
  - Class 2: 14 (13 + 1)
  - Class 3: 13 (13 + 0)
  - Class 4: 7 (3 + 4)

- **Total number of instances**: \( 8 + 13 + 14 + 13 + 7 = 55 \)

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

These calculations give us a more balanced understanding of the classifier's performance across all classes, taking into account the number of instances for each class.