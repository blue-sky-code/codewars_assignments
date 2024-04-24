def descending_order(num):
    num=str(num)
    d=[]
    for i in list(num):
        d.append(i)
        d.sort(reverse=True)
    return int("".join(d))
    




print(descending_order(15))