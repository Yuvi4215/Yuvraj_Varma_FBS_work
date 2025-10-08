### 2. Body Mass Index (BMI) Calculator

import math

weight_kg = 85
height_cm = 169

height_m = height_cm / 100
bmi = weight_kg / math.pow(height_m, 2)

print(f"Your BMI is: {bmi:.2f}")