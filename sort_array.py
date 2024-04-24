def sort_array(source_array):
    odd_list=[]
    ordered_list=[]
    c=0
    for i in range(len(source_array)):
        if source_array[i]%2!=0:
            odd_list.append(source_array[i])
            sorted_odd_list=sorted(odd_list)
    for j in range(len(source_array)):
        if source_array[j]%2==0:
            ordered_list.append(source_array[j])
        else:
            ordered_list.append(sorted_odd_list[c])
            c=c+1
    return ordered_list



        # if source_array[i]%2!=0:
        #     m.append(source_array[i])
        #     a=sorted(m)
        # elif m.append(source_array[i]%2==0):
        #     m.append(source_array[i])
            #a=sorted(m)
    #return a


    #     if source_array[i]%2!=0:
    #         m.append(source_array[i])
    #         a=sorted(m)
    #     else:
    #         a.insert(i,source_array[i])
    # return a
                   
        
        
        


    #return(sorted(source_array%2!==0))

print(sort_array([2,7,4,5,6]))