def sum_num():
    sum = 0
    while True:
        list_numbers = input()
        numbers = list_numbers.split(' ')
        for i in numbers:
            if i == 'exit':
                print(sum)
                print('Exit')
                return
            else:
                sum += int(i)
        print(sum)
        print('Enter number or exit')
sum_num()