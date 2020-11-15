
## print first 100 even digits




def is_even(a):

    is_even = False

    b = a / 2

    if (b == int(b)):

        is_even = True

    return is_even


elements = []
i = 0

while len(elements) < 100:

    if(is_even(i)):
        elements.append(i)

    i = i + 1

print(elements)



