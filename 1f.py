print("Enter Numerator Value : ")
num1 = int(input())
print("Enter Denominator value : ")
num2 = int(input())
try:
    result = num1/num2
    print("The Division of Given Numbers is : ", result)
except ZeroDivisionError:
    print("Divide By zero Error. The Denominator should not be Zero")