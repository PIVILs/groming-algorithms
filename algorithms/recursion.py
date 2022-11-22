l = [5, 3, 6, 2, 10, -1, 100]

def sum_list(L):
    """ Sum of list elements using recursion."""
    if L == []:
        return 0
    return L[0] + sum_list(L[1:])

print(sum_list(l))


def largest_number(L):
    """ Largest List Number Using Recursion."""
    if len(L) == 2:
        if L[0] > L[1]:
            return L[0]
        else:
            return L[1]
    else:
        sub_max = largest_number(L[1:])
        if L[0] > sub_max:
            return L[0]
        else:
            return sub_max

print(largest_number(l))