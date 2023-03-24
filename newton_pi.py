from decimal import Decimal, getcontext
from os import system

# set the precision of decimal arithmetic.
precision = 5000
getcontext().prec = precision

# set the size of the cmd window.
system("mode con cols=200 lines=30")

print('Larger term would have a more accurate result.')
print(f'Current precision: {precision} digit(s)')

terms = int(input("Input the terms: "))

n = Decimal('1') / Decimal('2')
content = Decimal('0')
tri_area = Decimal('3') ** Decimal('0.5') / Decimal('8')
arrg = Decimal('2') / Decimal('3')
fct = Decimal('1')

for term in range(0, terms):

    # n*(n-1)*(n-2)...
    arrg = arrg * (n - term + 1)
    result = arrg

    # factorial
    if term != 0:
        fct *= term

    result /= fct

    if result == 1:
        result = result
    elif result > 0:
        result = -result

    odd = 2 * (term + 1) - 1

    result /= odd
    result /= 2**odd

    content += result

    print(term, ' ', Decimal('12') * (content - tri_area))

system('pause')
