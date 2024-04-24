def first_non_consecutive(arr):
    #d=[]
    
    
    for i in range(len(arr)-1):
        diff=arr[i+1]-(arr[i])
        if diff!=1:
            return arr[i+1]
            #d.append(arr[i+1])
            
    #return int(d)
            

            
        
            
            

    
        

print((first_non_consecutive([1,2,3,4,5,6,7,8])))