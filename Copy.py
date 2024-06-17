# shallow copy
import copy

# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = copy.copy(old_list)

# print("Old list:", old_list)
# print('ID of Old List:', id(old_list))


# print("New list:", new_list)
# print('ID of new List:', id(new_list))




# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)

# old_list.append([4, 4, 4])

# print("Old list:", old_list)
# print('ID of Old List:', id(old_list))

# print("New list:", new_list)
# print('ID of new List:', id(new_list))



# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)

# old_list[1][1] = 'AA'

# print("Old list:", old_list)
# print("New list:", new_list)

#Deep copy
# creates new object and adds object recursively


# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.deepcopy(old_list)

# print("Old list:", old_list)
# print('ID of Old List:', id(old_list))

# print("New list:", new_list)
# print('ID of new List:', id(new_list))



old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print('ID of Old List:', id(old_list))

print("New list:", new_list)
print('ID of new List:', id(new_list))