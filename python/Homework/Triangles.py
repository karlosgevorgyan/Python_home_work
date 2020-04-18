def triangle(x):
    for i in range(x,0,-1):
        for y in range(0,i):
            print('*', end=' ')
        print()
triangle(5)


def top_right_triangle_while(age_length):
    x = age_length
    while x > 0:
        y = 0
        while y < x:
            print('*', end=' ')
            y += 1
        print()
        x -= 1

top_right_triangle_while(5)

print('----------------------------------')

def triangle_right(x):
    for i in range(0,x + 1):
        for y in range(0, i):
            print('*', end=' ')
        print()
triangle_right(5)

print('----------------------------------')

def bottom__triangle(x):
    for i in range(0,x):
        for y in range(x - i - 1, 0, -1):
            print(' ',end=' ')
        for t in range(0, i + 1):
            print('*',end=' ')
        print()
bottom__triangle(5)

print('----------------------------------')

def right_top_triangle(x):
    for i in range(0,x):
        for y in range(0,i):
            print(' ',end=' ')
        for c in range(x  - i,0, -1):
            print('*', end=' ')
        print()
right_top_triangle(5)

def right_top_triangle_while(x):
    i = 0
    while (i < x):
        y = 0
        while (y < i):
            print(' ', end=' ')
            y = y + 1
        z = x - i
        while (z > 0):
            print('*', end=' ')
            z = z - 1
        print()
        i = i + 1

right_top_triangle_while(5)