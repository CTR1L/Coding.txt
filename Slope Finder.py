##########################
#this prints what the code does
print("hello! I am a slope finder, please give me two points and I will print the slope.")
#these label the different points as variables
a = int(input("X1: "))
b = int(input("Y1: "))
c = int(input("X2: "))
d = int(input("Y2: "))
#these are the equations to find either the denominator or the numerator
numerator = d - b
denominator = c - a
#this prints the slope which is just the numerator on top and the denominator at the bottom
print("your slope is: " + str(numerator)+ "/" + (str(denominator))) 
###########################

