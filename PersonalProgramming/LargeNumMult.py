
def getdigits(num):
    digits = {}
    number = str(num)[::-1]
    for i in range(len(str(num))):
        digits.setdefault(i, []).append(number[i])
    for i, j in digits.items():
        digits[i] = int(j[0])
    print(digits)
    return digits


def multiply(digits1, digits2):
    result = {}
    carry = 0
    for i, l in digits2.items():
        for j, k in digits1.items():
            product = l * k + carry
            if product > 9 and j+1 < len(digits1):
                carry = product // 10
                product = product % 10
            else:
                carry = 0
            result.setdefault(i, []).append(product)

            '''
            123
            456
            s1: 1 & 4 => 4
            s2: 1 & 5 => ???          
            '''
    print(result)
    for i, j in result.items():
        result[i] = j[::-1]
    for i, j in result.items():
        result[i] = ''.join(map(str, j)) + '0' * i
    return result


def display(result):
    total = 0
    for j in result.values():
        total += int(j)
    print(total)


if __name__ == "__main__":
    num1 = 435903485298340840328905890438534353
    num2 = 293485082937459789302850983049285092
    digits1 = getdigits(num1)
    digits2 = getdigits(num2)
    result = multiply(digits1, digits2)
    print(result)
    print(num1 * num2)
    display(result)
