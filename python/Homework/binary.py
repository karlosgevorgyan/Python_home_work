def to_binary(value):
    result = []
    for i in range(31,-1,-1):
        curent = (value >> i) & 1
        result.append(curent)
    return result
print(to_binary(7))


def to_decimal(array):
    is_negative = (array[0] == 1)
    result = 0
    for i in range(0, len(array)):
        if is_negative:
            if array[i] == 0:
                result += (1 << (31 - i))
        else:
            if array[i] == 1:
                result += (1 << (31 - i))
    if is_negative:
        result = (result + 1) * -1
    return result




def and_op(a, b):
    array_a = to_binary(a)
    array_a_b = to_binary(b)
    result = []
    for i in range(0, len(a)):
        result.append(a[i] & b[i])
    return to_decimal(result)
and_op(10,8)

def or_op(a,b):
    array_a = to_binary(a)
    array_a_b = to_binary(b)
    result = []
    for i in range(0,len(a)):
        result.append(a[i] | b[i])
    return to_decimal(result)


def xor_op(a,b):
    array_a = to_binary(a)
    array_a_b = to_binary(b)
    result = []
    for i in range(0,len(a)):
        result.append(a[i] ^ b[i])
    return to_decimal(result)



def add_op(a, b):
    array_a = to_binary(a)
    array_y = to_binary(b)
    result = []

    tmp = 0
    for i in range(len(array_y) - 1, -1, -1):
        result_value = array_a[i] + array_y[i] + tmp
        if result_value >= 2:
            result.insert(0, result_value % 2)
            tmp = 1
        else:
            result.insert(0, result_value)
            tmp = 0
    return to_decimal(result)

print(add_op(10,5))