def enough(cap, on, wait):
    # if on==cap:
    #     return wait
    # elif on<cap:
    #     diff=on-wait
    #     return diff
    # if cap-on>0:
    #     d=wait-(cap-on)
    #     return d
    # elif cap==on:
    #     return wait
    d=on+wait
    if d<=cap:
        return 0
    elif d>cap:
        diff= d-cap
        return diff

print(enough(10, 5, 5))