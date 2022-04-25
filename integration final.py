"""Integration project as a whole"""
__author__ = "Logan Esala"
# Logan_Esala
# This a program that asks the user what dish they want to make
# given a menu and based on their selection the program maps out the
# cooking process based on how much of the dish the user wants to
# make with ingredients listed and as they are added it
# basically "shows" them what is made, for example mixing together
# flour and egg thoroughly creates dough, I also want it to be like
# the user is taking the actions to create the dish like input mix
# to mix ingredients together
from time import sleep


def main():
    """This is the whole program im using this to make the restart button
    work, so it runs again, also if there are errors"""

    def goodbye():
        """Using this to make an easy ending statement after each
        recipe. It just prints a predetermined statement
        """
        print("Thanks for cooking with me today see you next time.")

    def menu():
        """Using this, so I don't have to redo the menu for the times it'll
        get called when someone wants to restart this
        function prints the menu input"""
        print("Welcome to the kitchen!", end=" ")
        # Wanted to try the end= although it wasn't necessary
        print("Ready to cook?")
        print("What we can cook today:")
        # Setting up the menu and routes the user can take in terms of recipes
        print("""
        1. Fettuccine Alfredo. 🍝
        2. Sticky Buns. 🍩
        3. Glazed Braised Short Ribs. 🍖
        4. Exit
        """)

    menu()
    # Here I want to add a RESTART button that allows to
    # start back at the menu would that be too difficult?
    selection = input("Do you want to make option 1, 2, or 3? (Type here): ")
    while selection != '1' and selection != '2' and \
            selection != '3' and selection != '4':
        print("Sorry that isn't an option please try again")
        sleep(2)
        menu()
        selection = input("Do you want to make option 1, 2, or 3? ")
    # Fettuccine Alfredo
    if selection == '1':
        print("Nice choice...")
        # I'm using sleep() here to slow the output, so
        # it is easier for the user to read along with
        sleep(2)
        print("First start with 1 cup of flour, "
              "or:", 0.59 * 236.588236 * 1 // 1, "grams")
        sleep(0.5)
        # Converting the amount of flour, in cups to grams =
        # density of flour X 236.588, I also
        # want the grams to be rounded to be less confusing
        #  hence the floor division by 1 added to the end of the equation.
        print("")
        # These print("") statements print blank lines to make the output more
        # organized
        print("Now form a well with the flour and crack 2 eggs inside")
        crack_egg = input("(crack them by entering anything): ")
        # These show an error, but I am only using them as an interactive
        # message to break up the monotony and nothing more.
        print("Ok now mix into a cohesive dough, let rest for 15 minutes ")
        print("and then proceed to buy dry pasta"
              " because this is taking too long")
        # Should I go into deeper detail or would is seemed
        # too boring? - solution add the ability to skip.
        print("")
        sleep(2)
        print("Now onto the sauce part...")
        sleep(2)
        print("")
        print("For the sauce itself we will need to add half a cup or 115g of")
        print("softened butter to a bowl, a large amount of grated "
              "parmesan cheese on standby", sep="&")
        # I used sep here to put an and (&) where the comma was
        sleep(3)
        print("After your pasta has boiled for the amount of "
              "time on the package your going to want to...")
        sleep(3)
        alfredo_finish = input("Dump the hot pasta in the bowl "
                               "with the parmesan butter and "
                               "mix quick! (enter the word mix): ")
        while alfredo_finish != "mix":
            alfredo_finish = input("Don't set it on fire... Type mix: ")
        print("mixing, emulsifying", end='')
        print(".", end='')
        sleep(0.8)
        print(".", end='')
        sleep(0.8)
        print(". Congratulations! ")
        sleep(0.8)
        print("")
        print("Here's your pasta:")
        print("     ~--- ~~-  -~- ")
        print("   ~~~~~~~~~~~~~~~~~ ")
        print("  ____________________ ")
        print("(                      ) ")
        print(" \____________________/")
        goodbye()

    # Cinnamon sticky buns
    elif selection == '2':
        # Note to self: I am starting building the recipe for the
        # second choice and others around the time of sprint 2
        # so im going to include more math and stuff.
        print("Dessert sounds good...")
        sleep(1)
        print("So, this one involves alot of "
              "measurements because baking is goofy")
        input_validation = True
        while input_validation:
            try:
                number_buns = (int(float(input("How many buns would you like"
                                               " to make? (Type in 1 for 10"
                                               " and 2 for other): "))))
                if number_buns == 1 or number_buns == 2:
                    input_validation = False
            except ValueError:
                print("Please enter a number Error #1")
        # Stops program from breaking when the wrong value is input
        print("")
        if number_buns == 2:
            print("Ok you want another amount, sounds good.")
            validating_input = True
            while validating_input:
                try:
                    new_num_buns = int(float(input("How many buns would "
                                                   "you like to make?: ")))
                    validating_input = False
                except ValueError:
                    print("Please enter a number Error #2")
            print("Ok", new_num_buns, "is a nice number lets' get cooking")
            ingredient_calculation = 10 / new_num_buns
            # I'm going to take the new bun input and use it to calculate
            # the new ingredient amount as 10 was the default for the recipe.
            sleep(0.5)
            print("First you need to prep a yeast mixture with:")
            print("")
            print(9 / ingredient_calculation, "grams of yeast")
            print(120 / ingredient_calculation, "milliliters of 98*F milk")
            sleep(2)
            print(" ")
            print("With the yeast out of the way you're going to want to")
            print("create a Tangzhong which sounds weird, but it's just a mix"
                  " of flour, and milk that will make the dough more lofty,")
            sleep(3)
            print("Combine", 15 / ingredient_calculation,
                  "grams of all-purpose flour")
            print(20 / ingredient_calculation, " millimeters of milk and water"
                                               " in a pot of medium heat while"
                                               " stirring until it gelatinizes"
                                               " (turns into a doughy ball).")
            sleep(3)
            print(" ")
            print("For the dough combine the ingredients listed:")
            print(443 / ingredient_calculation, "grams of ap flour")
            print(2 / ingredient_calculation, "grams of fine salt")
            print(44 / ingredient_calculation,
                  "grams of granulated sugar, the yeast mixture")
            print(55 / ingredient_calculation, "mL of water")
            print(2 / ingredient_calculation, "ROOM TEMPERATURE eggs, ")
            print("Add in the Tangzhong that you made and "
                  "after mixing into a cohesive dough add")
            sleep(2)
            print(50 / ingredient_calculation, "grams of butter that "
                                               "has been softened while "
                                               "mixing (mix for 5 minutes).")
            sleep(5)
            print("Good lord that was alot of stuff")
            sleep(2)
            please_input_no_break = True
            while please_input_no_break:
                try:
                    skip = int(input("Would you like to keep going or skip to"
                                     " the buns? (Type 1 to stay or 2 to skip"
                                     " to the end) "))
                    if skip == 1 or skip == 2:
                        please_input_no_break = False
                except ValueError:
                    print("Please enter a number Error #3")
                # Stops program from breaking when the wrong value is input
            if skip == 1:
                # If it is getting boring just looking at the ingredients
                # then you can just skip to the finished product here.
                print(" ")
                print("Ok then, 7 decades later now that we've made our dough"
                      "shape it into a ball and place it in an oiled covered ")
                print("container for about 1 and a half hours.")
                print(" ")
                sleep(2)
                print("And we can't for get about the glaze, In a small pot,")
                print("combine butter, sugar, and honey. Place on stove over")
                print("medium heat, stir until thoroughly combined, place to")
                print("the side to cool down.")
                print(" ")
                punch = input("Deflate the dough by"
                              " punching it (press enter key): ")
                # These show a "value not used" error, but I am only using
                # them as an interactive message to break up the monotony
                # and nothing more.
                print("woah calm down")
                print(" ")
                print("Roll out your dough on a floured surface until it is ")
                print("about 1/2in thick, Sprinkle cinnamon sugar on dough ")
                print("from edge to edge, leaving a quarter inch around the"
                      " borders.")
                sleep(4)
                print(" ")
                print("Trim 1/2 in off sides of the log, cut dough using a")
                print(" nice, serrated knife, 2 inch rolls to total 10 equal"
                      " buns.")
                print(" ")
                print("In a 9x9 baking pan, add the caramel glaze")
                print(" at the bottom, sprinkle in 1 1/4 cup (140 g)"
                      " of toasted, crushed pecan,")
                print("arrange dough equally spaced apart In 3.")
                print("Place in oven at 350 degrees at 30-35 minutes. ")
                sleep(3)
                print(" ")
                print("DING")
                sleep(0.5)
                print(" ")
                print("Can't find a cinnamon roll "
                      "emoji so here's your pretzel: 🥨")
            elif skip == 2:
                prep_skip = input("Press enter to prep your"
                                  " recipe and chef it up")
                # These show a "value not used" error, but I am only using
                # them as an interactive message to break up the monotony
                # and nothing more.
                for i in range(1, 8, 2):
                    print(i, "Rolls rolled")
                sleep(1)
                for i in range(1, 6, 2):
                    print(i, "Eggs cracked")
                sleep(1)
                print("1 fishes fished")
                print("")
                sleep(0.5)
                print("DING")
                sleep(0.5)
                print("I cant find a cinnamon roll so here's a picture of a")
                print("pretzel: 🥨")

        elif number_buns == 1:
            # This is the original recipe amount so there are like no
            # calculations this is what I used as a reference to calculate
            # what the user inputs in type #2
            print("Ok you want, 10, sounds good lets' get cooking.")
            print("First you need to prep a yeast mixture with:")
            print("9 grams of yeast")
            print("120 milliliters of 98*F milk")
            sleep(2)
            print(" ")
            print("With the yeast out of the way you're going to want to "
                  "create a Tangzhong which sounds weird, but is just a mix "
                  " of flour, and milk that will make the dough more lofty,")
            sleep(3)
            print("Combine 15 grams of all-purpose flour")
            print("20 millimeters of milk and water in "
                  "a pot of medium heat while stirring until it gelatinizes.")
            sleep(3)
            print(" ")
            print("For the dough combine the ingredients listed:")
            sleep(0.5)
            print("")
            print("443 grams of ap flour")
            print("2 grams of fine salt")
            print("44 grams of granulated sugar, the yeast mixture")
            print("55 mL of water")
            print("2 ROOM TEMPERATURE eggs, ")
            sleep(0.5)
            print("Also add in the Tangzhong that you made and"
                  " after mixing into a cohesive dough add")
            sleep(2)
            print("50 grams of butter that has been previously"
                  " softened while mixing (mix for 5 minutes).")
            sleep(5)
            print("Good lord that was alot of stuff")
            sleep(2)
            validation_station = True
            while validation_station:
                try:
                    skip = int(input("Would you like to keep going or skip to"
                                     " the buns? (Type 1 to stay or 2 to skip"
                                     " to the end) "))
                    if skip == 1 or skip == 2:
                        validation_station = False
                except ValueError:
                    print("Please enter a number Error #4")
                # Stops program from breaking when the wrong value is input
            if skip == 1:
                # If it is getting boring just looking at the ingredients
                # then you can just skip to the finished product here.
                print(" ")
                print("Ok then, 7 decades later now that we've made our dough"
                      "shape it into a ball and place it in an oiled covered ")
                print("container for about 1 and a half hours.")
                print(" ")
                sleep(2)
                print("And we can't for get about the glaze, In a small pot,")
                print("combine butter, sugar, and honey. Place on stove over")
                print("medium heat, stir until thoroughly combined, place to")
                print("the side to cool down.")
                print(" ")
                punch = input("Deflate the dough by "
                              "punching it (press enter key): ")
                # These show a "value not used" error, but I am only using
                # them as an interactive message to break up the monotony
                # and nothing more.
                print("woah calm down")
                print(" ")
                print("Roll out your dough on a floured"
                      " surface until it is about 1/2 of an"
                      " inch thick, and sprinkle cinnamon sugar"
                      " on the dough from edge to edge")
                sleep(1)
                print("leaving a quarter inch around the borders.")
                sleep(1)
                print(" ")
                print("Trim 1/2 in off sides of the"
                      " log, cut dough using a nice,")
                print("serrated knife, 2 in rolls to total 10 equal buns.")
                sleep(0.5)
                print(" ")
                print("In a 9x9 baking pan, add the"
                      " caramel glaze at the bottom,")
                print("sprinkle in 1 1/4 cup (140 g)"
                      " of toasted, crushed pecan,")
                print("arrange dough equally spaced apart In 3.")
                print("Place in oven at 350 degrees at 30-35 minutes. ")
                sleep(3)
                print(" ")
                sleep(0.5)
                print("DING")
                sleep(0.5)
                print("I can't find a cinnamon roll "
                      "emoji so here's a picture of a")
                print("pancake: 🥞")
            elif skip == 2:
                prep_skip = input("Press enter to prep your"
                                  " recipe and chef it up")
                # These show a "value not used" error, but I am only using
                # them as an interactive message to break up the monotony
                # and nothing more.
                for i in range(1, 8, 2):
                    print(i, "Mixes mixed")
                sleep(1)
                for i in range(1, 6, 2):
                    print(i, "Eggs cracked")
                sleep(1)
                print("1 flip flop lost")
                print("")
                sleep(0.5)
                print("DING")
                sleep(0.5)
                print("I can't find a cinnamon roll "
                      "emoji so here's a picture of a")
                print("pancake: 🥞")
        goodbye()
    # Glazed Braised Short Ribs
    elif selection == '3':
        # I'm going to create a function that does the
        # division seen in the cinnamon bun recipe
        def divide_food(x, y):
            """This divides the original recipe amount with a new user
               determined amount of food, should make it more convenient
               to calculate
            """
            result = x / y
            return result

        print("Tasty stuff...")
        sleep(0.5)
        print("For this recipe I advise you cook the ribs and prep the "
              "sauce ahead of time like the night before a family dinner")
        sleep(0.5)
        print("First, you're going to want to get short ribs")
        print("that are a specific cut called an english cut")
        print("One serving should be enough for one person, so")
        # Stops program from breaking when the wrong value is input
        validating_input = True
        while validating_input:
            try:
                new_dish = int(float(input("How many servings do you want to"
                                           " make? "
                                           "(4 is standard but go crazy): ")))
                validating_input = False
            except ValueError:
                print("Please enter a number Error #5")
        print("")
        print("Ok", new_dish, "servings it is.")
        print("")
        serving_calculation = 4 / new_dish
        # Takes desired servings and divides
        # them by original recipe servings
        # this will be used to calculate
        # ingredient amounts based on user input.
        print("So, to start you're going to want to brown ", end='')
        print(".", end='')
        sleep(0.8)
        print(".", end='')
        sleep(0.8)
        print(". ", end='')
        sleep(0.8)
        rib_meat_round = (divide_food(3.5, serving_calculation))
        format_meat = "{:.2f}".format(rib_meat_round)
        # Takes original amount of meat and
        # divides by calculated serving size
        # and rounds the decimal to 2 places
        # so the number looks better
        print(format_meat, "pounds")
        sleep(0.5)
        print("of short ribs in a large pot, "
              "just be sure to lay them in and brown "
              "them slowly, because if you burn the fond "
              "then the sauce will be doomed to a fate of "
              "'this tastes gross'")
        sleep(3)
        print("When the ribs are browned throw in: ")
        print(divide_food(1, serving_calculation), "Red onion(s)")
        print(divide_food(3, serving_calculation), "Carrots")
        print(divide_food(1, serving_calculation), "Celery stalk(s)")
        sleep(3)
        print("They only need to be rough chopped nothing crazy")
        print("After a minute add in a squeeze of tomato paste for"
              " its' added umami.")
        sleep(1)
        print("")
        print("Now before anything burns quick de glaze the pot with",
              divide_food(1, serving_calculation), "bottle(s) of cheap white"
              " wine.")
        print("(You can use about", divide_food(3, serving_calculation),
              " cups of stock too, but you may have to add vinegar near the"
              " end to add some acidity adjust according to what tastes good)")
        print("")
        sleep(2)
        print("Now you can experiment with spices and flavors, this sauce "
              "is very versatile, dried chili's")
        sleep(2)
        print("Orange peel, lemon zest, star anise, coriander,"
              " pepper and anything you think you might like")
        sleep(2)
        print("")
        print("Start with a big pinch of salt though, and add the meat back "
              "in with the vegetables seasonings and liquid ")
        print("")
        sleep(2)
        print("Bring down to a bare simmer and cover and cook low and slow "
              "for a long time, like 8 hours or whenever the bones start "
              "to pull off the meat easily")
        sleep(3)
        print("Be careful as you pull them out onto a plate and begin to prep"
              " the sauce")
        sleep(2)
        print("Since we are going to reduce this to a glaze were going to"
              " need to remove the fat from the liquid, this can")
        sleep(2)
        print("be done by putting it in the fridge and waiting for it to"
              " solidify on top overnight or by using a gravy separator")
        print("")
        sleep(3)
        print("When the fat is removed from the liquid put it in a pan "
              "and begin to simmer it it should take about a half hour")
        sleep(2)
        print("to boil down, when you can make trails that collapse in on "
              "themselves slowly when you stir, the sauce is done.")
        sleep(3)
        print("")
        print("All you have to do now is add the meat to the"
              " pan and delicately coat them in sauce")
        print("Sizzle Sizzle", end='')
        print(".", end='')
        sleep(0.8)
        print(".", end='')
        sleep(0.8)
        print(". ", end='')
        sleep(0.8)
        print("♨")
        goodbye()
    elif selection == '4':
        print("Ok, bye")


main()
ended_restart_thing = True
while ended_restart_thing:
    print("")
    sleep(5.5)
    print("Restarting...")
    sleep(1)
    print("")
    print("Handing out the menus...")
    sleep(2)
    print("")
    main()
# Here I am setting up a while loop to restart the program after one of the 4
# choices is finished running for however many times th user wants
# ** exponential multiplication, * multiplication, / division/ % modulus shows
# remainder, // floor division rounds to whole number, + addition, -subtraction
