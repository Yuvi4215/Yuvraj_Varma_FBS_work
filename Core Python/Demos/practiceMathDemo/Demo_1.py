### math module

import math


## 1. Loan Payment Calculator
principal = 25000      # loan amount
annual_rate = 5.5 / 100
years = 5

monthly_rate = annual_rate / 12
n = years * 12

print(monthly_rate)

monthly_payment = principal * (monthly_rate * math.pow(1 + monthly_rate, n)) / (math.pow(1 + monthly_rate, n) - 1)
print(f"Monthly Payment: ${monthly_payment:.2f}")