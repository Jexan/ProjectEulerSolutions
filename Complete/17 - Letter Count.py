def wordize(n):
    if 1 <= n <= 19:
        return one_ten[n-1]
    if 20 <= n <= 99:
        return tens[n//10-2] + (one_ten[n%10-1] if n%10 != 0 else '')
    if 100 <= n <= 999:
        return one_ten[n//100-1] + "hundred" + ("And" + wordize(n%100) if n%100 != 0 else '')
    else:
    	return "oneThousand"

one_ten = ['one',
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
 'nineteen']

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']

letter_repr = [wordize(i) for i in range(1, 1001)]

result = sum(map(len, letter_repr))
if __name__ == '__main__':
    print(result)