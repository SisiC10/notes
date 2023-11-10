name = input("Enter your name: ")

print(name + ", welcome to your adventure...")
print("You will be given two choices, please write one of the capitalized options in lowercase to make a choice. Goodluck!")

answer = input("You opened your mailbox this morning to find a letter made out to you. In it, is coordinates to a remote location where the letter explains you will find great treasure. You immediately free your plans and take off with only your map. Soon, you find yourself walking down a long road, which is just about to come to an end. You can turn either KEEP GOING or GO HOME. Which do you choose? ")

if answer == "keep going":
    answer = input("You continue walking and soon reach a river. You can either WALK around or SWIM across it. WHICH DO YOU CHOOSE? "). lower()
    if answer == "walk":
        print("The walk is too long, the sun has gone down and you are about to be eaten by a pack of coyotes. Game over.")
    elif answer == "swim":
        answer = input("You have made it across the river. You are very close to your treasure. You can either RUN and get your treasure before someone else finds it, or REST and assume the coordinates were given just to you. WHICH DO YOU CHOOSE? ")
        if answer == "run":
            answer = input("You begin running at full speed and soon see your treasure in the distance. What you have endured has been worth it! Then, just as you are coming up to it, someone appears out of nowhere, grabs your treasure, and disappears.. like magic. It is gone. GAME OVER.")
        elif answer == "rest":
            answer = input("You take a long breather and then continue on your journey, you walk and walk and see nothing. You walk past your coordinates, and then back to them. You try digging for it and find nothing. Luckily, you recieved enough rest that you can swim back and hopefully make it off the long road before sunset... GAME OVER.")
    else:
        print("This answer is invalid. Thanks for playing " + name + "!")

elif answer == "go home":
    answer = input("You turn around, but the road is no longer there. Instead, there are two doors, one RED and one BLUE. WHICH DO YOU CHOOSE? "). lower()
    if answer == "red":
        print("You walk through the door and are immediately englufed by the flames of hell. Never fuck with the color of Satan. GAME OVER.")
    elif answer == "blue":
        print("You open the blue door and see your treasure. It is everything you dreamed it would be. You grab your treasure and go home. Sometimes giving in to your laziness is just easier. YOU WON.")
    else:
        print("This answer is invalid. Thanks for playing " + name + "!")