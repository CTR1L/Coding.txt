import random
# imports the package random

#Making a custom function that is one trial for a singular dice roll
def trial():
    #this puts a random number 1-6 into a variable called randomdicenumb
    randomdicenumb = random.randint(1,6)
    #this makes the variable "counter" global so I can access it outside of the custom function
    global counter
    #this sets the counter to 0 so I can update it later while the loop begins
    counter = 0 
    #this is the starting value for the "stopgo" variable, I will set it to 0 later in the code so I know when to end the loop
    stopgo = 10
    # this starts the loop so it'll end once stopgo reaches the value 0
    while stopgo != 0:
        #this addes 1 to the counter so I can know how many times the code takes to roll a 6
        counter = counter + 1
        #this gives me another random dice number so I can change it each time
        randomdicenumb = random.randint(1,6)
        #this sets it so that if the random dice number ever rolls a 6 the code ends
        if randomdicenumb == 6: 
            stopgo = 0
trial()
#this gives the varaiable num an input so that the player can set the roll number to find the average of how many times they roll
num = int(input("How many times will you roll? "))
#this gives num another variable because it will change later, this saves the previous value of num
number_of_trials = num
#this sets the value of "average" to 0 so that I may change it later. I save each number of times it takes to get a 6 into this variable
average = 0
#this begins the loop so it may end once the number of times the user has selected.
while num != 0:
    #this is the custom function I made for the dice roll
    trial()
    #this updates the value of num each time it does the trial
    num = num - 1 
    #this adds the number of times it took to get 6 to the counter to the average
    
    average = average + counter
    #this lets the code know when to end the loop
    if num == 0:
        #this prints the average
        print("your average roll number that it takes you to get to is: " + str(average/number_of_trials))
