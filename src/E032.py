# Sum of pandigital products
# OPTIMAL(<0.15s)
# 
# APPROACH:
#   The product must be between 1234 and 9876, so, since 5 digits remain for the
#   multiplying numbers, the only two possible combinations are one digit number times a four digits one,
#   or two digits times a three digits. We create one factor and the other is produced with permutations, and
#   then we check if the product has the remaining digits.

from itertools import permutations, chain

DUMMY_RESULT = 7254

def generate_products():
    pan_products = set()
    digits = frozenset('123456789')
    one_digit = map(str, range(2, 9)) # 1 and 9 do not produce pandigital combinations.
    two_digit = (''.join(per) for per in permutations(digits, 2)) 
    product_max = 9877

    for i in chain(one_digit, two_digit):
        multiplicand_digits = frozenset(i)
        remaining_digits = digits - multiplicand_digits
        
        multiplicand = int(i)
        multiplier_max_length = 5 - len(i)

        for multiplier in (int(''.join(per)) for per in permutations(remaining_digits, multiplier_max_length)):
            product = multiplicand * multiplier

            if product > product_max:
                continue

            product_digits = frozenset(str(product))
            if len(product_digits) == 4 and '0' not in product_digits and product_digits.isdisjoint(frozenset(str(multiplier)) | multiplicand_digits):
                pan_products.add(product)

    return pan_products

pan_products = generate_products()

assert DUMMY_RESULT in pan_products 
result = sum(pan_products)