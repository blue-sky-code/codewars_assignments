import re
def validate_pin(pin):
    # y=re.match("^\d*$",pin)
    # if y and (len(pin)==6 or len(pin)==4):
    #     return True
    # return False
    if len(pin) != 4 and len(pin) != 6:
        return False
    
    try:
        int_val = int(pin)
        return True
    except:
        return False

print(validate_pin('a123'))