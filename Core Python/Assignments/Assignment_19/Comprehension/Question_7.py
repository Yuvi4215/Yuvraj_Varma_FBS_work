### 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.
# li=[div for div in [ele for ele in range(1,1001)] if div%2==0 or div%3==0 or div%5==0 or div%7==0]
li=[num for num in range(1,1001) if any(num%div ==0 for div in(2,10))]
print(f"""List of numbers from 1–1000 that are divisible by any single digit : 
{li}""")