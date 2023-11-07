#Complex Calculator using python 
print ("Press 1 for Sum")
print ("Press 2 for Minus")
print ("Press 3 for Multiplication")
print ("Print 4 for Division")
a=int(input("Enter your option="))
if (a==1):
     b=int(input("Enter your no.="))
     c=int(input("Enter your no.="))
     d=b+c
     print("sum=",d)
elif (a==2):
     b=int(input("Enter your no.="))
     c=int(input("Enter your no.="))
     d=b-c
     print("Minus=",d)
elif (a==3):
     b=int(input("Enter your no.="))
     c=int(input("Enter your no.="))
     d=b*c
     print("Multiplication=",d)
elif (a==4):
     b=int(input("Enter your no.="))
     c=int(input("Enter your no.="))
     d=b/c
     print("Division=",d)
else:
     print ("Enter correct option")