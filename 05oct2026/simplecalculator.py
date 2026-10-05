num1 = 10
num2 = 5
operator = '+'

if operator =='+':
    result = num1 + num2
elif operator =='-':
    result = num1 - num2
elif operator =='*':
    result = num1 * num2
elif operator =='/':
    if num2 !=0:
        result = num1 / num2
    else:
        result = "error division by zero"
else:
    result = "invalid operator"
print(f"result:{result}")