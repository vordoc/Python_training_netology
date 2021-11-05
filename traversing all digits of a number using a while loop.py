# обход всех цифр числа с помощью цикла while
# traversing all digits of a number using a while loop

x = int(input("Enter a number: "))
count = 0
count_even = 0
summ = 0
pr = 1
maxim = 0
minim = 9

while x > 0:
    last = x % 10
    count = count + 1

    if last % 2 == 0:
        count_even += 1
    summ = summ + last
    pr = pr * last

    if last > maxim:
        maxim = last

    if last < minim:
        minim = last

    x = x // 10

print(f'Total digits count in the number: {count}')
print(f'Total even digits count in the number: {count_even}')
print(f'The sum of all the digits in the number: {summ}')
print(f'The product of all the digits in the number: {pr}')
print(f'Maximum digit in the number: {maxim}')
print(f'Minimum digit in the number: {minim}')
