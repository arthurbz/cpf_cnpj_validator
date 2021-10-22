import sys


def split_str(string):
    return [int(s) for s in string]


def calculate_sum(array, iteration, weight):
    sum = 0

    for i in range(iteration):
        print(weight, ' * ', array[i], ' = ', weight * array[i])
        sum += weight * array[i]
        weight -= 1
    print('Sum: ', sum)

    return sum


def get_digit(sum):
    digit = 11 - (sum % 11)

    if digit > 9:
        digit = 0
    print('Digit: ', digit)
    return digit


def cnpj_validator(cnpj):
    sum = calculate_sum(cnpj, 4, 5)
    sum += calculate_sum(cnpj[4: ], 8, 9)
    digit1 = get_digit(sum)

    cnpj_with_digit = cnpj[: len(cnpj) - 2]
    cnpj_with_digit.append(digit1)

    sum = calculate_sum(cnpj_with_digit, 5, 6)
    sum += calculate_sum(cnpj_with_digit[5: ], 8, 9)
    digit2 = get_digit(sum)
    
    return digit1 == cnpj[12] and digit2 == cnpj[13]


def cpf_validator(cpf):
    digit1 = get_digit(calculate_sum(cpf, 9, 10))

    cpf_with_digit = cpf[: len(cpf) - 2]
    cpf_with_digit.append(digit1)

    digit2 = get_digit(calculate_sum(cpf_with_digit, 10, 11))
 
    return digit1 == cpf[9] and digit2 == cpf[10]


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        array = split_str(sys.argv[1])
        if len(array) == 11:
            cpf_validator(array)
        if len(array) == 14:
            cnpj_validator(array)


