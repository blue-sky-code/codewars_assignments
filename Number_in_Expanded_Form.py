import math
def expanded_form(num):
    num=str(num)
    b=[]
    #c=1
    for i in range(len(num)):
        a=int(num[i])*(pow(10,(len((num))-(i+1))))
        # b.append(a)
        #a=num[i]*(1**(i+2))
        #c+=1
        b.append(str(a))
    return " + ".join(b)
    # num1=len(str(num))
    # for i in range(num1):
    #     a=num1[i]*(pow(10,(int(math.log10(num1)))+1))
    #     b.append(a)
    #     return b
    


   

print(expanded_form(46))




        

