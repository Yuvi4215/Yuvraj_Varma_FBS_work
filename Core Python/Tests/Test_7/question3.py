
list_odd_number=[ele for ele in range(1,51) if ele%2!=0]
print(list_odd_number)

list_even_number=list(filter(lambda x : x%2==0,[ele for ele in range(1,51)]))
print(list_even_number)