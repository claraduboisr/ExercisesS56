num1 = int(input("input the first number"))
num2 = int (input ("input the times its gonna be multiplied "))
result = num1**num2
num = num1


while num <= result:
    print (num)
    num = num + num1
    if num>result:
        break