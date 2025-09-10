### keyword variable length/number of argument.
# 1.
# 2.
# 3.


def emp(**data):
    for i, j in data.items():
        print(f"key:{i}---value:{j}")
    
emp(id="142", name="mohit", sal=5566)
print("-------------------------------------")
emp(age=45, name="Iron man", dept="Avengers", is_alive=False, wealth=7584623)