list_array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print(set(list_array))
list_array_upt = list_array.copy()
for i in range (0, 3):
    print(max(list_array_upt))
    list_array_upt.remove(max(list_array_upt))

print(min(list_array))
print(list_array.index(min(list_array)))
print(list_array[::-1])

