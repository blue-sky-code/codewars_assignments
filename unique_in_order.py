def unique_in_order(sequence):
    sequence1=[]
    
    for i in range (len(sequence)-1):
        if sequence[i]!=sequence[i+1]:
            sequence1.append(sequence[i])
    if (len(sequence)>0):
        sequence1.append(sequence[-1])
    return sequence1
    
        
    
        

print(unique_in_order([]))