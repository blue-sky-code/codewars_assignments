def count_smileys(arr):
    eyes=[":",";"]
    nose=["-","~"]
    mouth=[")","D"]
    d=[]
    for i in arr:
        if len(i)==2 and i[0] in eyes and i[-1] in mouth:
            d.append(i)
            
        elif len(i)>2 and i[0] in eyes and i[1] in nose and i[-1] in mouth:
            d.append(i)
        
            
    return len(d)
   



print(count_smileys([';]', ':[', ';*', ':$', ';-D']))