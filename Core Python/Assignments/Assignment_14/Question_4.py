### 4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

def pairSum(nums, target):
    seen = []
    pairs = []
    for num in nums:
        # print(num)
        diff = target - num
        if diff in seen:
            pair_val = (min(num, diff), max(num, diff))
            if pair_val not in pairs:
                pairs.append(pair_val)
        if num not in seen:
            seen.append(num)
    return pairs

nums = [1, 5, 7, -1, 5]
target = 6
print("Pairs:", pairSum(nums, target))