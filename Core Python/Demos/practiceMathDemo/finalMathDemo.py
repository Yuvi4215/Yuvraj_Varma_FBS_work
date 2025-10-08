import math
import random

print("\n=== 🧮 MATH MODULE EXAMPLES ===")

# ---- Basic Arithmetic ----
print("\n-- Basic Arithmetic --")
print("ceil(4.1):", math.ceil(4.1))
print("floor(4.9):", math.floor(4.9))
print("trunc(3.99):", math.trunc(3.99))
print("fabs(-3.5):", math.fabs(-3.5))
print("factorial(5):", math.factorial(5))
print("fmod(10, 3):", math.fmod(10, 3))
print("remainder(10, 3):", math.remainder(10, 3))

# ---- Power & Roots ----
print("\n-- Power & Roots --")
print("pow(2, 3):", math.pow(2, 3))
print("sqrt(16):", math.sqrt(16))
print("isqrt(16):", math.isqrt(16))
print("exp(1):", math.exp(1))
print("log(100, 10):", math.log(100, 10))
print("log10(1000):", math.log10(1000))
print("log2(8):", math.log2(8))

# ---- Trigonometry ----
print("\n-- Trigonometry --")
print("sin(pi/2):", math.sin(math.pi/2))
print("cos(0):", math.cos(0))
print("tan(pi/4):", math.tan(math.pi/4))
print("asin(1):", math.asin(1))
print("acos(0):", math.acos(0))
print("atan(1):", math.atan(1))
print("atan2(1, 1):", math.atan2(1, 1))
print("degrees(pi):", math.degrees(math.pi))
print("radians(180):", math.radians(180))

# ---- Constants ----
print("\n-- Constants --")
print("pi:", math.pi)
print("e:", math.e)
print("tau:", math.tau)
print("inf:", math.inf)
print("nan:", math.nan)

# ---- Distance, Combinatorics, Misc ----
print("\n-- Miscellaneous --")
print("dist((0,0),(3,4)):", math.dist((0,0),(3,4)))
print("hypot(3,4):", math.hypot(3,4))
print("comb(5,2):", math.comb(5,2))
print("perm(5,2):", math.perm(5,2))
print("isfinite(5):", math.isfinite(5))
print("isnan(math.nan):", math.isnan(math.nan))