def my_func(num_1, num_2, num_3):
    result = sum([num_1, num_2, num_3]) - min([num_1, num_2, num_3])
    print(result)
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
my_func(num_1, num_2, num_3)