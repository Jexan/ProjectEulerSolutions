# Sum of multiples of 3 and 5

def sum_multiples():
    return sum(i for i in range(1, 1000) if not i % 3 or not i % 5)


result = sum_multiples()
if __name__ == '__main__':
    print(result)