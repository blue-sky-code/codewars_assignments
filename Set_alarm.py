def set_alarm(employed, vacation):
    if employed and not vacation:
        return True
    else:
        return False
    

print(set_alarm(True,True))