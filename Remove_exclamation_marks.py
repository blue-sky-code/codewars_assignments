def remove_exclamation_marks(s):
    a=[]
    for i in range(len(s)):
        if s[i]=="!":
            s3 =s[i].replace("!","")
            a.append(s3)
        else:
            a.append(s[i])
    return "".join(a)
    


   
    

print(remove_exclamation_marks("!Hello! Wo!rld!!"))