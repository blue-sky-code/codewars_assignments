def is_isogram(string):
    m=[]
    for i in string:
        m.append(i)
        if i in m:
            return False
        return True
    return m

    
    

print (is_isogram("alia"))
