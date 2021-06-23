# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

a = int(input("Enter First Number For Sum"))
b = int(input("Enter Second Numbre For Sum"))
c = a + b
d = 20

if (c < 10 or c > 20):
    print(c)
else:
    print(d)
