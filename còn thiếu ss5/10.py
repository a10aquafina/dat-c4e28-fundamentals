from random import*
def even_list():
    # even_list=[]
    for i in range(3):
        a=choice(even_list)
        even_list.append(a)
        get_even_list([1, 2, 5, 9, -10, 6])
    return get_even_list



even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")