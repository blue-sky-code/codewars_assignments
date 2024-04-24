# def solution(n):
#     m = list(str(n))
#     m.reverse()
#     for i in range(len(m)):
#         m[i] = int(m[i])
#     return m


# print(solution(32145))

def abbrev_name(name):
    #if len(name.split(" "))==2:
    for i in name:
        if " " in name:
            #x=i.split(" ",1)
            return i[0:1].capitalize()
        else:
            return 0
        
print(abbrev_name("mina jafari"))
        
