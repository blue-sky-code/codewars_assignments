def find_it(seq):
    for i in range(len(seq)):
        x=seq.count(seq[i])
        if x%2!=0:
            return seq[i]
            
            
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
