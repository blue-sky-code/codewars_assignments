def rot13(message):
    



    # a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # b=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    ch1={"A":"N","B":"O","C":"P","D":"Q","E":"R","F":"S","G":"T","H":"U","I":"V","J":"W","K":"X","L":"Y","M":"Z","N":"A","O":"B","P":"C","Q":"D","R":"E","S":"F","T":"G","U":"H","V":"I","W":"J","X":"K","Y":"L","Z":"M"}
    ch2={"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z","n":"a","o":"b","p":"c","q":"d","r":"e","s":"f","t":"g","u":"h","v":"i","w":"j","x":"k","y":"l","z":"m"}
    d1=[]
    for item in message:
        if item in ch1.keys():
             #a1= message.replace(i,ch1.values())
             #a1=i
            #  i=ch1.values()
            ziba=ch1[item]


            d1.append(ziba)
        elif item in ch2.keys():
            #a1=message.replace(i,ch2.values())
            #  s1=ch2.values()
            #  d1.append(s1)
            
             #d1.append(a1)
             ziba=ch2[item]
             d1.append(ziba)
        else:
             d1.append(item)
    return("".join(d1))



print(rot13('WVvxwt0u8lkXyNp'))


            
