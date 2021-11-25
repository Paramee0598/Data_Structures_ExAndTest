h,w = input("Enter your High and Weight : ").split()
h=float(h)
w=float(w)
BMI = (w)/(h*h)
if BMI < 18.5 :
    print('Less Weight')
    pass
if 18.50 <= BMI  < 23 :
    print('Normal Weight')
    pass
if 23 <= BMI  < 25 :
    print('More than Normal Weight')
    pass
if 25 <= BMI  < 30 :
    print('Getting Fat')
    pass
if BMI  >= 30 :
    print('Fat')
    pass





