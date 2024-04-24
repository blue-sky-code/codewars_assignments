def solution(s):
    d=[]

    for chr in s:
        if chr.isupper():
            d.append(" ")
            
        d.append(chr)
        print (d)
        # #asc=ord(s[i])
        # #print(asc)
        # if 65<ord(s[i])<90:
        #     #for s[i] in enumerate(s):
        #     d.append(s[i])
        #     if d in s:




                

        


    return "".join(d)
        #return 0
        

print(solution("WeEllld"))
