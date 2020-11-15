



### first 100 primal digits

def is_prim(a):

    l = []

    for i in range(2, a):

        calc = a / i

        if (calc == int(calc)):

            l.append(i)

    is_prim = (len(l) < 1)

    return is_prim

while len(p_elements) < 100:

    if(is_prim(i)):
        p_elements.append(i)

    i = i + 1

print(p_elements)



