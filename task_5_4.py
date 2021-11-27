from functools import reduce
list = [i for i in range(100, 1001) if i % 2 == 0]
print(list)
def my_number(prev_el, el):
    return prev_el * el
print(reduce(my_number, list))