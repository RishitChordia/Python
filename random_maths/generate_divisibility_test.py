def check_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


def find_multiplier(prime):
    for i in range(10):
        if (i*prime)%10 == 1:
            return (i*prime-1)//10
    return 0


def find_b_coefficient(multiplier, prime):
    b_coefficient = (10*prime - multiplier)%prime
    if abs(b_coefficient - prime) < b_coefficient:
        return b_coefficient - prime
    return b_coefficient


def main():
    input_num = int(input('Enter a prime number: '))
    if not check_prime(input_num):
        print('Learn about prime numbers.')
        return
    multiplier = find_multiplier(input_num)
    b_coefficient = find_b_coefficient(multiplier, input_num)
    if b_coefficient > 0:
        print(f'The formula is A + {b_coefficient}B.')
    else:
        print(f'The formula is A - {abs(b_coefficient)}B.')



if __name__ == "__main__":
    main()


# I have no idea why I'm doing this
    