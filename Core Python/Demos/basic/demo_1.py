###
def iterateOnDS(data):
    for item in data:
        if isinstance(item, (list, tuple, set)):
            for ele in item:
                if isinstance(ele, (list,tuple,set)):
                    for val in ele:
                        print(val, end=" ")
                else:
                    print(ele)
        else:
            print(item)

nested = [1, (2, 3), [4, {5, 6}], 7]
iterateOnDS(nested)