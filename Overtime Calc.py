def computepay(hours, rate):
    if hours > 40 :
        nhrs = hours * rate
        overtime = (hours - 40) * (rate * 0.5)
        pay = nhrs + overtime
    else: 
        pay = hours * rate
    return pay
 
hours = input("Enter Hours:")
rate = input("Enter Rate:")
hours = float(hours)
rate = float(rate)

gross = computepay(hours, rate)
print("Pay", gross)