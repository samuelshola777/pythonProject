if __name__ == '__main__':

 print("entre two integer, and i will tell you the relationship the satisfy.")

num1 = int(input("enter first integer"))
num2 = int(input("enter second intger"))

if num1 == num2:
 print("num1 is equal to number2")
elif num1 > num2:
 print("num1 is great num2")
elif num2 > num1:
 print("num2 is greater than number 1")
elif num1 < num2:
  print("num1 is less than num2")
elif num2 < num1:
 print("num2 is lesser than num1")
else:
     print("not a valid number")
