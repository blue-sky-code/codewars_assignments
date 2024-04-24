def rot13(message):
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    result = []
    for c in message:
        try:
            c_index = alphabets.index(c.lower())        
            rot_index = c_index+13
            if rot_index > 25:
                target_index = rot_index - 26
            else:
                target_index = rot_index
            
            result.append(alphabets[target_index] if c.islower() else alphabets[target_index].upper())
        except:
            result.append(c)
        

    return ''.join(result)


print(rot13('Test'))
print(rot13('aA bB zZ 1234 *!?%'))