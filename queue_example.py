def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    tills_dict= {}
    for i in range(0, n):
        if len(customers) > i:
            tills_dict[i] = customers[i]  
    
    customers_in_queue = customers[i+1:]
    checkout_time = 0
    if len(customers_in_queue) == 0:
        return max(customers)
    while max(tills_dict.values()) > 0:
        for key in tills_dict:
            tills_dict[key] -= 1
        
        for key in tills_dict:
            if tills_dict[key] == 0 and len(customers_in_queue) > 0:
                tills_dict[key] = customers_in_queue[0]
                customers_in_queue.remove(customers_in_queue[0])
        checkout_time += 1
    
    return checkout_time


print(queue_time([], 1))
print(queue_time([5,1,3], 2))
print(queue_time([2,2,3,3,4,4], 2))