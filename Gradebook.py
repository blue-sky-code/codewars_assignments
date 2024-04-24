def get_grade(s1, s2, s3):
    # Code here
    scores=s1+s2+s3
    average=scores/3
    if average>=90 and average<=100:
        return "A"
    elif average>=80 and average<90:
        return "B"
    elif average>=70 and average<80:
        return "C"
    elif average>=60 and average<70:
        return "D"
    elif average>=0 and average<60:
        return "F"
    


print(get_grade(70, 70, 70))