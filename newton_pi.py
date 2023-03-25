from decimal import Decimal, getcontext
import os

# Set the precision of decimal arithmetic.
PRECISION = 10000
getcontext().prec = PRECISION

# Set the size of the cmd window.
if os.name == 'nt':
    os.system("mode con cols=200 lines=53")

print(f'Current precision: {PRECISION} digit(s)')
print('More terms would have a more accurate result.')

num_terms = int(input("Input the number of terms to use in the approximation: "))

exponent = Decimal('1') / Decimal('2')
approximation = Decimal('0')  # Initial approximation.
triangle_area = Decimal('3') ** Decimal('0.5') / Decimal('8')  # Area of a 30-60-90 triangle in the unit circle.
binomial_coeff = Decimal('2') / Decimal('3')  # Initial value for binomial coefficient.
factorial = Decimal('1')  # Initial value for factorial.
prev_pi = Decimal('0')

for term_index in range(num_terms):
    # Calculate the next term in the approximation using the binomial theorem.
    binomial_coeff *= exponent - term_index + 1 

    # Update the factorial for the term.
    if term_index != 0:
        factorial *= term_index

    # Determine the sign of the term.
    if term_index % 2 == 0:
        term_sign = 1
    else:
        term_sign = -1

    # Calculate the denominator of the term, which is an odd number.
    term_denominator = 2 * term_index + 1

    # Calculate the final value of the term and add it to the approximation.
    term_value = term_sign * binomial_coeff / (factorial * term_denominator * 2 ** term_denominator)
    approximation += term_value

    # Print the current approximation to pi.
    pi = Decimal('12') * (approximation - triangle_area)

    if pi == prev_pi:
        print('\nReached same value of pi as previous iteration. Terminating loop.')
        break
    
    print(f'\r{term_index}  {pi}', end='', flush=True)
    
    prev_pi = pi


# Pause the program before exiting.
input('Press Enter to exit...')
