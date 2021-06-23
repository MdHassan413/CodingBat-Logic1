# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

inp_cig = int(input("Enter the number of cigars: "))
inp_day = input("Enter 'wd' for Weekday or 'we' for Weekend ")
inp_day.lower()
if(inp_day == 'wd' and inp_cig>=40 and inp_cig<=60):
 print("party successful")
elif(inp_day == "we" and inp_cig >=40):
 print("party successful")
else:
 print("party unsuccessful")