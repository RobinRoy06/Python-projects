first_list = [1,2,3]
second_list = [3,4,1]

if first_list == second_list:
    print("They are the same list.")
else:
    common_elements = set(first_list) & set(second_list)
    if common_elements:
        print("The common elements are", common_elements)
    else:
        print("There are no common elements.")