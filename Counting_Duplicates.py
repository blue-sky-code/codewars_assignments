def duplicate_count(text):
    d=[]
    s={}
    text=text.lower()
    d=[]
    text=text.lower()
    s={}
    for i in text:
        if text.count(i)>1:
            d.append(i)
            s=set(d)
    return (len(s))
    
        
    
        
    
    
        
      


print(duplicate_count("aabbbbcdbbbcce"))

