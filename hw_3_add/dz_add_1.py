n = input("Enter integer: ")

def product_num(n):
    pr_numbers = 1
    for i in n:
        if int(i) != 0:
            pr_numbers *= int(i)

    print(pr_numbers)
    return pr_numbers

product_num(n)


