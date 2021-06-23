# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

inp_temp = int(input("Enter Temperature: "))
is_summer = input("Enter Yes for summer and No for other Season ")
is_summer = is_summer.lower()
if(inp_temp>=60 and inp_temp<=90 and is_summer == "no"):
 print("You are allowed to Play")
elif(inp_temp>=60 and inp_temp<=100 and is_summer == "yes"):
 print("You are allowed to Play ")
else:
 print("Not Allowed to Play")
