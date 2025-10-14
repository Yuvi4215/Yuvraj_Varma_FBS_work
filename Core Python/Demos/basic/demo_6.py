from collections import defaultdict

squre= lambda x,y,z=2,a=2: x*y*z*a
print(squre(1,1))

dd = defaultdict(int)
print(dd["banana"])



nums = [1, 2, 3, 4]
print(list(map(lambda x: x*2, nums)))

# filter()
print(list(filter(lambda x: x%2==0, nums)))

# sorted()
print(sorted(nums, reverse=True))