# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.


# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True

inp_a = int(input("Enter Value Of 'A' : "))
inp_b = int(input("Enter Value Of 'B' : "))
c = inp_a + inp_b 
if ((inp_a == 6 or inp_b == 6)):
    print('True') 
elif (c == 6 ):
    print("True")
else :
    print(c)