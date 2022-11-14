
import time as t


def getdigits(num):
    digits = []
    number = str(num)[::-1]
    for i in range(len(str(num))):
        digits.append(number[i])
    for i in range(len(digits)):
        digits[i] = int(digits[i])
    print(digits)
    return digits


def multiply2(digits1, digits2):
    result = []
    for i in range(len(digits2)):
        for j in range(len(digits1)):
            product = digits2[i] * digits1[j]
            if j >= len(result):
                result.append(product)
            else:
                result[j] += product
            # print(result)
            for num in result:
                if num > 9:
                    if result.index(num) < len(result) - 1:
                        result[result.index(num) + 1] += (num // 10)
                        result[result.index(num)] = num % 10
                    else:
                        result.append(num // 10)
                        result[result.index(num)] = num % 10
                else:
                    result[result.index(num)] = num

            # print("pos", i, j, " product: ", product, " result: ", result)

    return result


def display(result):
    result = result[::-1]
    for j in result:
        print(j, end='')
    print()


def fill_in_prod(num, index, result):
    while index >= len(result):
        result.append(0)
    result[index] += num
    while result[index] > 9:
        carry = result[index] // 10
        result[index] %= 10
        if index + 1 >= len(result):
            result.append(0)
        result[index + 1] += carry
        index += 1
    return result


def multiply(digits1, digits2):
    result = []
    for i in range(len(digits1)):
        for j in range(len(digits2)):
            # calculate
            result = fill_in_prod(digits1[i] * digits2[j], i + j, result)
    return result


if __name__ == "__main__":
    num1 = 100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000
    num2 = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

    digits1 = getdigits(num1)
    digits2 = getdigits(num2)
    time1 = t.time()
    result = multiply2(digits1, digits2)
    print(t.time() - time1)
    time2 = t.time()
    result = multiply(digits1, digits2)
    print(t.time() - time2)

    # print(result)
    time3 = t.time()
    print(num1 * num2, " <-is the correct answer")
    print(t.time() - time3)
    # display(result)
