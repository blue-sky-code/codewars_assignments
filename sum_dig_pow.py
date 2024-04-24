def sum_dig_pow(a, b):
    d=[]
    s=0
    for i in range(a,b+1):
        s=0
        if i<10:
            d.append(i)
        elif i>=10:
            x=list(str(i))
            for j in range(len(x)):
                s=s+((int(x[j]))**(j+1))
            if s==i:
                d.append(i)
    return d
print(sum_dig_pow(7,135))