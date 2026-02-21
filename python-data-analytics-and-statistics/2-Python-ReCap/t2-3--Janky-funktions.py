# Check which list is correct
def add_to_list(item, lst=[]):
    lst.append(item)
    return lst

list1 = add_to_list(1)
list2 = add_to_list(2, [])
list3 = add_to_list(3)
print(list1, list2, list3)