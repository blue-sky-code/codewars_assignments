def zero(expression=None):
    if expression is None:
        return 0
    else:
        whole_expression=f"0{expression}"
        return eval(whole_expression)
    
    pass #your code here
def one(expression=None): 
    if expression is None:
        return 1
    else:
        whole_expression=f"1{expression}"
        return eval(whole_expression)
    pass #your code here

    
def two(expression=None): 
    if expression is None:
        return 2
    else:
        whole_expression=f"2{expression}"
        return eval(whole_expression)
    pass #your code here
def three(expression=None): 
    if expression is None:
        return 3
    else:
        whole_expression=f"3{expression}"
        return eval(whole_expression)
    pass #your code here
def four(expression=None):
    if expression is None:
        return 4
    else:
        whole_expression=f"4{expression}"
        return eval(whole_expression)
    pass #your code here
def five(expression=None): 
    if expression is None:
        return 5
    else:
        whole_expression=f"5{expression}"
        return eval(whole_expression)
    pass #your code here
def six(expression=None): 
    if expression is None:
        return 6
    else:
        whole_expression=f"6{expression}"
        return eval(whole_expression)
    pass #your code here
def seven(expression=None): 
    if expression is None:
        return 7
    else:
        whole_expression=f"7{expression}"
        return eval(whole_expression)
    pass #your code here
def eight(expression=None): 
    if expression is None:
        return 8
    else:
        whole_expression=f"8{expression}"
        return eval(whole_expression)
    pass #your code here
def nine(expression = None):
    if expression is None:
        return 9
    else:
        whole_expression = f"9{expression}"
        return eval(whole_expression)

def plus(d: int):
    return f"+{d}" 
    
    pass #your code here
def minus(d: int): 
    return f"-{d}"
    #your code here
def times(d: int): 
    return f"*{d}"
    pass #your code here
def divided_by(d: int): 
    #your code here
    return f"/{d}"



print((seven(times(four()))))