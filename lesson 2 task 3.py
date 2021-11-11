winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
n = int(input("введите номер месяца:"))
if n in winter:
    print('winter')
elif n in spring:
    print('spring')
elif n in summer:
    print('summer')
else:
    print('autumn')


my_dict = {int(1): 'winter', int(2): 'winter', int(3): 'spring', int(4): 'spring', int(5): 'spring', int(6): 'summer', int(7): 'summer', int(8): 'summer', int(9): 'autumn', int(10): 'autumn', int(11): 'autumn', int(12): 'winter'}
n = int(input("введите номер месяца:"))

print(my_dict.get(n))


