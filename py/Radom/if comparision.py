#print(max(3,4,5))

def max_num(num1,num2,num3,num4,num5):
    if(num1>=num2 and num1>=num3 and num1 >= num4  and num1>=num5 ):
        return num1
    elif(num2>=num1 and  num2>=num3 and  num2 >= num4 and num2 >=num5):
        return num2
    elif(num3>=num1 and num3 >=num2 and num3 >=num4 and num3 >=num5):
        return num3
    elif(num4 >=num1 and num4 >= num2 and num4 >= num3 and num4 >= num5):
        return num4
    else:
        return num5


print(max_num(3,4,6,7,8,))