### 6. Write a Python program to find the two numbers whose product is maximum among all the pairs 
#      in a given list of numbers. Use the Python set.

def maxProductPair(nums):
    unique_nums = []
    for n in nums:
        if n not in unique_nums:
            unique_nums.append(n)

    max_prod = float('-inf')
    # print(max_prod)
    
    pair = 0
    for i in range(len(unique_nums)):
        for j in range(i+1, len(unique_nums)):
            prod = unique_nums[i] * unique_nums[j]
            if prod > max_prod:
                max_prod = prod
                pair = (unique_nums[i], unique_nums[j])
    return pair, max_prod


num_li = [1, 20, -5, 4, 5]
pair,max_prod=maxProductPair(num_li)
print(f"Pair : {pair} and Max product : {max_prod}" )