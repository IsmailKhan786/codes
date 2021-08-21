import string
a = input(" Enter first word: ")
b = input(" enter Second Word : ")
flag = 0
for char in a.lowr():
    if(char.isalpha):
        if(char in s2.lower()):         
            flag = 1
            continue
else:
    flag=0
      break
if(flag == 1):
    print(" YES ")
else:
    print(" NO")