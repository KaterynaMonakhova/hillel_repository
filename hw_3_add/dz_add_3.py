base_str = input("Enter the string that have to be checked: ")
check_str = tuple(base_str.split())

def count_words(check_str):
    counter_items = 0
    flag = True
    result = []

    for item in check_str:
        if counter_items == 3:
            print(f"There are 3 words in a row: {result}")
            break
        for symbol in item:
            if symbol.isdigit():
                flag = False
                counter_items = 0
                break
            else:
                flag = True
        if flag:
            counter_items += 1
            result.append(item)
        else:
            if len(result) != 0:
                result.clear()
    return (counter_items)

count_words(check_str)
