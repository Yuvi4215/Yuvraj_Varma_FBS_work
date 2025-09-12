### Slicing

li=[42,6,8,74,77,22,3,66,87,52]

print("Printing from 0 to 2 index ::",li[0:3])
print("Printing from 2 to 5 index ::",li[2:6])
print("Printing from 2 to last index ::",li[2:])
print("Printing from first to 8 index ::",li[:9])
print("Printing from first to last index ::",li[:])
print("Printing from first to last index with default step '1' ::",li[::])
print("Printing from 3 to 1 index with step '-1' ::",li[3:0:-1])
print("Printing from last to first index with default step '-1' ::",li[::-1])