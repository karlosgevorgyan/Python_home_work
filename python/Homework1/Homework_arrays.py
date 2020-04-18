array = [3,5,7,9,11,13,15,17]
def max(array):
    max = array[0]
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
    return max
print(max(array))

print('----------------------------------------------')

def min(array):
    min = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
    return min
print(min(array))

print('----------------------------------------------')

def sum(array):
    sum = 0.0
    for i in range(len(array)):
        sum += array[i]
    return sum
print(sum(array))

print('----------------------------------------------')

def average(array):
    sum = 0.0
    for i in range(len(array)):
        sum += array[i]
    return sum / len(array)
print(sum(array))

print('----------------------------------------------')

def mult(array):
    sum = 1.0
    for i in range(len(array)):
        sum *= array[i]
    return sum
print(mult(array))

print('----------------------------------------------')

array = [3,5,6,2,4,7,1,8,10,9]
# sort the array using bubble sort
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
bubble_sort(array)
print(array)

print('----------------------------------------------')

# sort the array using selection sort
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if i != min_index:
            array[min_index], array[i] = array[i], array[min_index]
selection_sort(array)
print(array)

print('----------------------------------------------')

# sort the array using insertion sort
def insertion_sort(array):
    for i in range(len(array)):
        value = array[i]
        j = i - 1
        while j > -1 and array[j] > value:
            array[j + 1] = array[j]
            j = j - 1
        if array[j + 1] != value:
            array[j + 1] = value
insertion_sort(array)
print(array)

print('----------------------------------------------')


#binaryy_search():
array =  int(input('please enter your number: '))
list = []
for i in (34,56,32,76,8,7,43,21):
    if array >= i:
        list.append(1)
        array = array-i
    else:
        list.append(0)
print(list)

print('----------------------------------------------')


