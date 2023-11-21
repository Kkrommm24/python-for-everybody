def computepay(hours, rate):
    pay = float(hours) * float(rate) 
    if float(hours) > 40:
        xh_over = float(hours) - 40
        pay_over = xh_over * 1.5 * float(rate) + 40 * float(rate)
        return pay_over
    else :
        return pay

xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
print("Pay: ", computepay(xh,xr))