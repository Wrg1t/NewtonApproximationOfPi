from decimal import Decimal, getcontext
from os import system

# set the size of the cmd window.
system("mode con cols=200 lines=20")

print('Larger term would have a more accurate result.')
term = int(input("Input the terms: "))
# set the precision of decimal arithmetic.
getcontext().prec = 1000

n = Decimal('1') / Decimal('2')
content = Decimal('0')

for i in range(0, term):
    result = Decimal('1')
    fct = Decimal('1')

    # n*(n-1)*(n-2)...
    for j in range(0, i):
        result *= n - j

    # factorial
    if result != 0:
        for k in range(1, i + 1):
            fct *= k

    result /= fct

    if result == 1:
        result = result
    elif result > 0:
        result = -result

    odd = 2 * (i + 1) - 1

    result /= odd
    result /= 2**odd


    content += result

    tri_area = Decimal('3') ** Decimal('0.5') / Decimal('8')
    print(i, ' ', Decimal('12') * (content - tri_area))

input("Press any key to exit...")