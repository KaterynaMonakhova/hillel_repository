import random

list_num = []

def random_list(list_num):
    for i in range(0, random.randint(1, 20)):
        x = random.randint(0, 255)
        list_num.append(x)
    print(list_num)
    return (list_num)

def array_el(list_num):
    random_list(list_num)
    n = random.randint(1, 20)
    len_arr = len(list_num)
    print(f"The array length is {len_arr}. The range is {n}")
    for i in list_num:
        if n == list_num.index(i):
            list_num[n] = int(list_num[n] ** n)
            print(f"list_num[{n}]**{n}= {list_num[n]}")
        elif n > len_arr:
            print("The list index out of range")
            return (-1)

    return (list_num[n])

array_el(list_num)
