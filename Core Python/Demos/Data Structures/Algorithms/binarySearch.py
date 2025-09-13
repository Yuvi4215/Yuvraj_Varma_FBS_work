### binary search


def binarySearch(li, ele):
    begin = 0
    end = len(li) - 1

    while begin <= end:
        mid = (begin + end) // 2
        if ele == li[mid]:
            return mid
        elif ele > li[mid]:
            begin = mid + 1
        elif ele < li[mid]:
            end = mid - 1
    else:
        return None


li = [10, 20, 30, 40, 50, 60, 70, 80]
search_ele = int(input("Enter the element to search :: "))

result = binarySearch(li, search_ele)

if result != None:
    print(f"{search_ele} is found at index :: {result}")
else:
    print(f"{search_ele} is not present in List!")
