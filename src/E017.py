# letters used by numbers from 1 to 1000
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   Write the numbers in english and then finally sum their lenghts.

LIMIT = 1000

DUMMY_LIMIT = 5
DUMMY_RESULT = 19

def wordize(n):
    if 1 <= n <= 19:
        return one_ten[n-1]
    if 20 <= n <= 99:
        return tens[n//10-2] + (one_ten[n%10-1] if n%10 != 0 else '')
    if 100 <= n <= 999:
        return one_ten[n//100-1] + "hundred" + ("And" + wordize(n%100) if n%100 != 0 else '')
    else:
    	return "oneThousand"

one_ten = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']

def number_letters_to_write_until(limit):
    letter_repr = [wordize(i) for i in range(1, limit + 1)]
    return sum(map(len, letter_repr))

assert number_letters_to_write_until(DUMMY_LIMIT) == DUMMY_RESULT
result = number_letters_to_write_until(LIMIT)