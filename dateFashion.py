# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).


# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

judge_me=int(input("Plese judge my stylishness in the range of 0 to 10 : "))
judge_mydates=int(input("Please judge my date in the range of 0 to 10 : "))
if ((judge_me>=8) or (judge_mydates>=8)):
        print("Your table selected")
elif((judge_me<=2) or (judge_mydates<=2)):
    print("Sorry try for next time")
else:
    print("you may be selected")