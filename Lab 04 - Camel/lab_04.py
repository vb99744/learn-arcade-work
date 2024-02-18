import random


def menu():
    print("""
    A. Drink from your canteen.
    B. Ahead moderate speed
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check.
    Q. Quit.
    """)

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    """miles traveled, the drinks in the canteen, and how far the natives are behind you."""
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    canteen_drinks = 3

    done = False
    while not done :
        menu()
        user_choice = input("What is your choice? ").upper()



        if user_choice == 'Q': # Q. Quit.
            print("You have quit the game.")
            done = True
        elif user_choice == 'E': # E. Status check.
            print("Miles traveled:", miles_traveled)
            print("Drinks in canteen:", canteen_drinks)
            print("The natives are", miles_traveled - natives_distance, "miles behind you.")
        elif user_choice == 'D': # D. Stop for the night.
            camel_tiredness = 0
            print("You have stopped to rest for the night.")
            print("The camel is happy.")
            natives_distance = natives_distance + random.randrange(7, 15)
            pass
        elif user_choice == 'C': # C. Ahead full speed.
            traveled = random.randrange(10, 21)
            miles_traveled = miles_traveled + traveled
            print("You have traveled", traveled, "miles.")
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + random.randrange(1, 4)
            natives_distance = natives_distance + random.randrange(7, 15)
            if random.randrange(1, 21) == 5:
                print("You found an oasis!")
                thirst = 0
                camel_tiredness = 0
                canteen_drinks = 3
            pass
        elif user_choice == 'B': # B. Ahead moderate speed.
            traveled = random.randrange(5, 13)
            miles_traveled = miles_traveled + traveled
            print("You have", traveled, "miles.")
            thirst = thirst + 1
            camel_tiredness = camel_tiredness + 1
            natives_distance = natives_distance + random.randrange(7, 15)
            if random.randrange(20) == 5:
                print("You found an oasis!")
                thirst = 0
                camel_tiredness = 0
                canteen_drinks = 3
            pass
        elif user_choice == 'A': # A. Drink from canteen.
            if canteen_drinks > 0:
                thirst = 0
                canteen_drinks = canteen_drinks - 1
                print("You have", canteen_drinks, "drinks left in your canteen.")
            else:
                print("You have no drinks left in your canteen.")
            pass



        if thirst > 6:
            print("You died of thirst!")
            done = True
        elif thirst > 4:
            print("You are thirsty.")

        if camel_tiredness > 8:
            print("Your camel is dead.")
            done = True
        elif camel_tiredness > 5:
            print("Your camel is getting tired.")

        distance_between = miles_traveled - natives_distance

        if distance_between <= 0:
            print("The natives have caught you.")
            done = True
        elif distance_between < 15:
            print("The natives are getting close!")

        if miles_traveled >= 300 and not done:
            print("You win! You have escaped the Mobi desert.")
            done = True


# call the main
main()