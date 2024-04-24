def disemvowel(string_):
    vowels=["A","E","I","O","U","a","e","i","o","u"]
    #vow=["a","e","i","o","u"]
    d=[]
    #string_=string_.lower()
    # print(string_)
    # for i in range(len(string_)):
    #     if not string_[i] in vow:
    #         d.append(string_[i])
            
    # return ''.join(d)

    for chr in vowels:
        string_ = string_.replace(chr, "")
        
    return string_
    
        
print(disemvowel("This weEbsite is for losers LOL and liiooO!"))