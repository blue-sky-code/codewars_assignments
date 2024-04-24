def persistence(n):
    d=[]
    n=str(n)
    c=1
    counter=0
    if int(n)<10:
        return 0
    else:
        while int(n)>=10:
            counter+=1
            for i in n:
                c=c*int(i)
            n=str(c)
            c=1

            
        
    return counter

print(persistence(25))