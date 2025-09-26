### 2. Python Program to Concatenate Two Dictionaries Into One

def concatinateDicts(dict1,dict2):
    final_dict={}

    for index in dict1:
        final_dict[index]=dict1[index]
    for index in dict2:
        final_dict[index]=dict2[index]
    return final_dict


d1={"a":12,"b":17,"c":71,"d":99,"e":12}
d2={"f":92,"g":77,"h":49,"i":70007,"j":1992}

merge_dict=concatinateDicts(d1,d2)
print(f"""
1st Dictionary : {d1}
2nd Dictionary : {d2}
-------------------------------------------------------------------------------------------------------------------
merged Dictionary : {merge_dict}
-------------------------------------------------------------------------------------------------------------------

""")