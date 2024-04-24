def DNA_strand(dna):
    x=dna.upper()
    m=[]
    for i in x:
        if i=="A":
            m.append(i.replace("A","T"))
        elif i=="T":
            m.append(i.replace("T","A"))
        #     dna=
        elif i=="C":
            m.append(i.replace("C","G"))
        elif i=="G":
            m.append(i.replace("G","C"))
    return "".join(m)
    

print(DNA_strand("ATTgc"))

