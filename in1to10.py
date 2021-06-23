# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True

out_side = input("Enter OutSide Value True 'T' False 'F' : ")
num = int(input("Enter Number : "))
out_side.lower()

if ((out_side == "t") and (num <= 1 or num >= 10)):
    print("True")
elif((out_side == "t") and (num >= 1 or num <= 10)):
    print("False")
elif ((out_side == "f") and (num <= 1 or num >= 10)):
    print("False")
elif ((out_side == "f") and (num >= 1 or num <= 10)):
    print("True")
else:
    print("invalid")