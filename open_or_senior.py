def open_or_senior(data):
    data1=[]
    for i in data:
        if i[0]>=55 and i[1]>7:
            data1.append("Senior")
        else:
            data1.append("Open")
    return data1
    
        
    
           
           



    #return m[0][1]

print((open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])))