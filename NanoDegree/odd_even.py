
def odd_even(list):
    odd = []
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd + even

print(odd_even([1,2,3,4,5,6,7,8,9]))