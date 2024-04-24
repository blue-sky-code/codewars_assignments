import operator

def queue_time(customers, num):
    # def queue_time(customers, num):
    # total=0
    # for i in range(len(customers)):
    #     if num==1:
    #         total=total+customers[i]
    #     elif num>1 and max(customers)>((total+customers[i])*2)-(max(customers)) and customers.count(i)==1:
    #             total=max(customers)
    #     elif len(customers)<num:
    #             total=max(customers)
    #     elif customers.count(i)==1:
    #             c=max(customers)
    #             f=min(customers)
    #             total=c+f
        
    #     elif customers.count(i)>1:
    #         w=list(set(customers))
    #         total=sum(w)
                
            
    # return total



    # total=0
    # for i in range(len(customers)):
    #     for j in range(num):
    #         if num==1:
    #             total=total+customers[i]
    #         elif num>1:
    #             while customers[i]==0:
    #                 customers[i]=customers[i]-1
                    
    #                 a=customers.pop(customers[i])
    #                 total=total+a
    # return total

                
                


    # total=0
    # for i in range(len(customers)):
    #     if num==1:
    #         total=total+customers[i]
    #     elif num>1 and max(customers)>((total+customers[i])*2)-(max(customers)) and customers.count(i)==1:
    #             total=max(customers)
    #     elif len(customers)<num:
    #             total=max(customers)
    #     elif customers.count(i)==1:
    #             c=max(customers)
    #             f=min(customers)
    #             total=c+f
        
    #     elif customers.count(i)>1:
    #         w=list(set(customers))
    #         total=sum(w)
                
            
    # return total
        

    if num == 1:
        return sum(customers)
    elif num >= len(customers):
        return max(customers)
    else:
        tills = [0] * num  # ایجاد یک لیست تیل با تعداد تیل‌های موجود و مقدار ابتدایی صفر
        for customer in customers:  # حلقه برای هر مشتری در لیست مشتریان
            min_till = min(tills)  # پیدا کردن تیل با کمترین زمان مشتری
            min_till_index = tills.index(min_till)  # پیدا کردن اندیس تیل با کمترین زمان مشتری
            tills[min_till_index] += customer  # افزودن زمان مشتری به تیل مربوطه
        return max(tills)
        


print(queue_time([46, 30, 50, 27, 41, 25, 22, 29, 6, 20, 15, 34], 4))


# total=0
#     for i in range(len(customers)):
#         if num==1:
#             total=total+customers[i]
#         elif num>1 and customers[i]==max(customers):
#             total=customers[i]
            
#     return total