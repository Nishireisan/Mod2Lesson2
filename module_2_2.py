first = int(input('First: '))
second = int(input('Second: '))
third = int(input('Third: '))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
