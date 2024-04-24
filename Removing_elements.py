def remove_every_other(my_list):
        # del my_list[1::2]
        # return my_list

    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r
    


print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))



    
