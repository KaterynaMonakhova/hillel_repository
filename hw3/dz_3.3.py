s = str(input("Enter list of elements: "))
list_str = list(s.split())
print(list_str)

def most_frequent(list_str, most_frequent_value=None):
    n_most_common = 0
    for item in list_str:
        n = list_str.count(item)
        if n > n_most_common:
            n_most_common = n
            most_frequent_value = item
    print(most_frequent_value, n_most_common)
    return (most_frequent_value, n_most_common)
most_frequent(list_str)
