def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list

# Taking input from the user for the first list
list1 = int(input("Enter elements of the first list separated by spaces: ")).split()
list1 = [int(element) for element in list1]

# Taking input from the user for the second list
list2 = int(input("Enter elements of the second list separated by spaces: ")).split()
list2 = [int(element) for element in list2]

# Merging the two lists
merged_list = merge_lists(list1, list2)
print("Merged List:", merged_list)

