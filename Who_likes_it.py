def likes(names):
    # your code here
    d=[]
    if len(names)==0:
        return "no one likes this"
    else:
        if len(names)==1:
            for i in range(len(names)):
                d.append(names[i])
                a=" and ".join(d)
            return f"{a} likes this"
        if len(names)==2:
            for i in range(len(names)):
                d.append(names[i])
                a=" and ".join(d)
            return f"{a} like this"
        
        elif len(names)==3:
            for i in range(len(names)):
                d.append(names[i])
            b=d[0:2]
            #y=len(names)-2
            y=d[2:3]
            a=", ".join(b)
            v="".join(y)
            return f"{a} and {v} like this"
        elif len(names)>3:
            for i in range(len(names)):
                d.append(names[i])
                #print (d[1])
            b=d[0:2]
            y=len(names)-2
            a=", ".join(b)
            return f"{a} and {y} others like this"


        

print(likes(['Jacob', 'Alex']))
