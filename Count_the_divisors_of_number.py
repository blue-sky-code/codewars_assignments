def divisors(n):
    #y=[]
    # for i in range(n):
    #     d=i%2
    #     if d==0:
    #         y.append(i)
    # return y
    d=[]

    for i in range(1,n+1):
        if n%i==0:
            d.append(i)
    return len(d)
    

print(divisors(4096))

