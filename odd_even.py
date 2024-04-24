def odd_or_even(arr):
    s=0
    for i in arr:
        s=i+s
    if s%2==0:
            return "even"
    return "odd"
    #return s

print(odd_or_even([-4,2,1]))
