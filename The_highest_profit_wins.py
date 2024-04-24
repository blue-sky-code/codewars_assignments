def min_max(lst):
    d=[]
    min_val=min(lst)
    d.append(min_val)
    max_val=max(lst)
    d.append(max_val)
    
    
    return d
print(min_max([1,2,6,3,4,5]))