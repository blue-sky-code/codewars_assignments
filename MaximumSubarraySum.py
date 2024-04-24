def max_sequence(arr):
    d=[]
    max_now=arr[0]
    max_end=0
    for i in range(0,len(arr)):
        max_end+=max_end+arr[i]
        if max_end<0:
            max_end=0
        elif max_now<max_end:
            max_now=max_end
    return max_now


    # for i in arr:
    #     d.append(i)
    #     for j in range(i+1,len(arr)):
    #         i+=arr[j]
    #         d.append(i)
    #     if j<0 or len(arr)==0:
    #         return 0
    #     else:
    #         max_sum=max(d)
    #         return max_sum
    
        

    # curr_sum=0
    # x=len(arr)
    # if x==1:
    #     return arr[0]
    # max_sum=arr[0]
    # for i in range(x-1):
    #     curr_sum=arr[i]
    #     for j in range(i+1, x):
    #         curr_sum+=arr[j]
    #         max_sum=max(max_sum,curr_sum,arr[j])
    # return max_sum

    # len_n = len(arr)
 
    # if len_n == 1:
    #   return arr[0]
    # sums = []
    # sums.append(arr[0])
    # max_sum = arr[0]
    # for i in range(1, len_n):
    #    sums.append(max(sums[i-1] + arr[i], arr[i]))
    #    max_sum = max(max_sum, sums[i])
    # return max_sum



    

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
            
        
