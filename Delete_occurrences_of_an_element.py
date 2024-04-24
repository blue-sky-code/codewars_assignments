def delete_nth(order,max_e):
    d=[]
    for i in range(len(order)):
        x=d.count(order[i])
        if x<max_e:
            d.append(order[i])
    return d
    

    
        
        
    
        


print(delete_nth([1,1,3,3,7,2,2,2,2,4],3))