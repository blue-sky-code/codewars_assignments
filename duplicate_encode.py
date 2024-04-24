def duplicate_encode(word):
    m=[]
    for i in range(len(word)):
        if word.lower().count(word[i].lower())>=2:# or word[i].capitalize() in word :
            m.append(")")
        else:
            m.append("(")
    return "".join(m)


print(duplicate_encode("(( @"))
print(duplicate_encode("Success"))
