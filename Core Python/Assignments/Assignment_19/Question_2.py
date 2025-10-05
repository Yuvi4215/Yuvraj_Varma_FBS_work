### 2. Find all of the numbers from 1–1000 that have a 6 in them

li = [ele for ele in range(1, 1001) if "6" in str(ele)]
print(f"""List element that have 6 in them : 
{li}""")