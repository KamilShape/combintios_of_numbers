work = True
# ask_to_continue = True
# proper_numbers_amount = False

while work:
    ask_to_continue = True
    proper_numbers_amount = False
    number1 = int(input('Input 1 number: '))
    number2 = int(input('Input 2 number: '))

    if number1 > number2:
        print('Number 1 must be higher than number 2')
        continue

    while not proper_numbers_amount:
        numbers_amount = int(input(f'How many number would you like to take from range {number1, number2}: '))
        if numbers_amount > number2:
            print('Numbers amount must be lower than number 2')
            proper_numbers_amount = False
        else:
            proper_numbers_amount = True

    n = number2 - number1 + 1
    k = numbers_amount
    n_factorial = 1
    k_factorial = 1
    n_k_factorial = 1

    for i in range(1, n + 1):
        n_factorial *= i

    for j in range(1, k + 1):
        k_factorial *= j

    for m in range(1, n - k + 1):
        n_k_factorial *= m

    comb = n_factorial / (k_factorial * n_k_factorial)

    print(f'There is {comb} combinations.')

    while ask_to_continue:
        con = input('Would you like to continue! (y/n): ')
        if con == 'y':
            ask_to_continue = False
            work = True
        elif con == 'n':
            ask_to_continue = False
            work = False
        else:
            print('Wrong letter.')
            ask_to_continue = True