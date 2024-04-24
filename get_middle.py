def get_middle(s):
    if len(s)%2==0:
        a=len(s)//2

        return s[a-1:a+1]
    return s[len(s)//2]
print (get_middle("abcde"))
        