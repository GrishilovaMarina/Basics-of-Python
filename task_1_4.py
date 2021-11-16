from sys import argv

def count(tax, hours, prem):
    return tax * hours + prem
if len(argv) < 4:
    print('Недостаточно параметров')
else:
    print(count(int(argv[1]),int(argv[2]),int(argv[3])))