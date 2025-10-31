list_string=["thermodynamics","fluid mechanics","heat and mass transfer","refrigeration and air conditioning"]

list_output=[ele.upper() for ele in list_string]
# print(list_output)
print(f"Original List of String :: {list_string}")
print(f"Output List-Comprehension:: {list_output}")