def dir_reduc(arr):
    #b={"N":"NORTH","S":"SOUTH","W":"WEST","E":"EAST"}
    d=[]
    for i in arr:
        if len(d)>0:
            if (i=="NORTH" and d[-1]=="SOUTH") or (i=="WEST" and d[-1]=="EAST") or (i=="SOUTH" and d[-1]=="NORTH") or(i=="EAST" and d[-1]=="WEST"):
                d.pop()
            else:
                d=d+[i]
        else:
            d=d+[i]
    return d




print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
            

