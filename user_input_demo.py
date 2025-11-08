name = (input("Enter your name:",))
print ("Hello,"+name+"!")

age = int(input("Enter your age:"))
print("You will be",age+1,"next year")

price = float(input("Enter the price"))
discount = price * 0.1
print ("Discount is:",discount)

answer=input("are you a student? YES or NO:")
is_student= answer == "yes"
if is_student:
    print("hello student")
else:
    print("hello guest")
