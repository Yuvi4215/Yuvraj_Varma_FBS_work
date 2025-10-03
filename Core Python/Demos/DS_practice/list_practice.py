### list methods

li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#append(ele)
li.append(69)

#extend(iterables)
li.extend([1,1,2,2,3,3,4,4])

#insert(index,ele)----> NO Error if index out of range
li.insert(99,999)

#index(ele)----> value Error
li.index(7)

#count(ele)--->NO Error in if ele not present
li.count(6969)

#sort()--same list will bes sort---> erroe
li.sort()

#remove(ele)---> value Error
li.remove(12)

li2=[1]
#pop()--last ele--->Index Error
li2.pop()
#pop(index)-- ele at index
li.pop(7)

#reverse()--same list reverse
li.reverse()

#copy()--shallow copy
li.copy()

#clear()
li.clear()



