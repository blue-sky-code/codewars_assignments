def square_digits(num):
    list_of_nums=[]
    for i in str(num):
        list_of_nums.append(int(i))

    # for j in range(len(list_of_nums)):
    #     s=list_of_nums[j]*list_of_nums[j]
        
    #     list_of_nums.append(s)
    for j in range (len(list_of_nums)):
        list_of_nums[j]=list_of_nums[j]*list_of_nums[j]
        a="".join(str(j) for j in list_of_nums)
        
        
    return a

print (square_digits(9119))