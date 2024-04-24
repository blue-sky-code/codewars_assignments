import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    a= sq%(sq**(1/2))
    #print(int(a))
    d=[]
    
    if int(a)==0:
        b=math.sqrt(sq)
        c=b+1
        d=b+c+sq
        return d
        

        return"yes"
    return -1
   




print(find_next_square(342786627))


# d=[]
#     if sq%(sq**(1/2))==0:
#             b=math.sqrt(sq)
#             c=b+1
#             d=b+c+sq
#             return d
#     return -1