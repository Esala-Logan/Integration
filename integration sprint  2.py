# Logan_Esala
# I want to make a program that asks the user what dish they want to make in a menu and based on their selection the program maps out the cooking process with ingreedients listed and as they are added it basically "shows" them what is made,
# For example mixing together flour and egg thorouly creates dough, I also want it to be like the user is taking the actions to create the dish like input mix to mix ingredients together
def Goodbye():
    print("Thanks for cooking with me today see you next time.")
from time import sleep
print("Welcome to the kitchen!", end = " ")
# I think it ended the first lines' output and put the space there I just wanted to try the end= although it wasn't necessary 
print("Ready to cook?")
print("What we can cook today:")
#setting up the menu and routes the user can take in terms of recipes
print("""
1. Fettucine Alfredo.
2. Sticky Buns.
3. Glaised Braised Short Ribs
4. Exit
""")
#Here I want to add a RESTART button that allows to start back at the menu would that be too difficult?
selection = input("Do you want to make option 1, 2, or 3? ")

#Fettucine Alfredo
if selection == '1':
    print("Nice choice...")
#Im using sleep() here to slow the output so it is easier for the user to read along with
    sleep(2)
    print("First start with 1 cup of flour, or")
    sleep(2)
    print(0.59 * 236.588236 * 1 // 1, "grams")
    sleep(0.5)

#converting the amount of flour in cups to grams eq - density of flour X 236.588 I also wanted the grams to be a rounded to be less confusing hence the floor division by 1 added to the end of the equation
    crack_egg = input("Now form a well with the flour and crack 2 eggs inside (crack them by entering the word crack): ")
    print("Ok now mix into a cohesive dough, let rest for 15 minutes and then proceed to buy dry pasta because this is taking too long")

#question: should I go into deeper detail or would it be a little to much for the amount of lines we're supposed to have? Also would it seem too boring? - solution add the ability to skip.
    sleep(2)
    print("Now onto the sauce part...")
    sleep(2)
    print("For the sauce itself we will need half a cup or 115g of softend butter added to a bowl, a large amount of grated parmesan cheese on standby", sep = "&")

#I used sep here to put an and where the comma was
    sleep(3)
    print("After your pasta has boiled for the amount of time on the package your going to want to...")
    sleep(3)
    Alfredo_finish = input("Dump the hot pasta in the bowl with the parmesan and butter and mix quick! (enter the word stir): ")
    print("mixing, emulsifing...")
    sleep(3)
    print("Congratulations! Heres your pasta:")
    print("     ~--- ~~-  -~- ")
    print("   ~~~~~~~~~~~~~~~~~ ")
    print(" /____________________\ ")
    print("(                      ) ")
    print(" \____________________/")
    Goodbye()

#Cinnamon sticky buns 
elif selection == '2':
#I am starting building the recipe for the second choice and others around the time of sprint 2 so im going to include more math and stuff.
    print("Dessert sounds good...")
    sleep(1)
    print("So, this one involves alot of measurements because baking is goofy...")
    Number_Buns = (int(float(input("How many buns would you like to make? (Type in 1 for 10 and 2 for other): "))))
    while Number_Buns != 1 and Number_Buns != 2:
        Number_Buns = (int(float(input("Sorry thats out of the range, please type 1, or 2: "))))
    if Number_Buns == 2:
        print("Ok you want another amount, sounds good.")
        New_Numbuns = int(input("How many would you like to make?: "))
        print("Ok", New_Numbuns, "is a nice number lets' get cooking")
        Ingredient_Calculation = 10 / New_Numbuns 
        sleep(0.5)

#im going to take the New bun number input and use it to calculate the new ingredient amount as 10 was the default for the recipe.
        print("First you need to prep a yeast mixture with:")
        print(9 / Ingredient_Calculation, "grams of yeast")
        print(120 / Ingredient_Calculation, "milliliters of 98*F milk")
        sleep(2)
        print(" ")
        print("With the yeast out of the way you're going to want to create a Tangzhong which sounds weird, but is just a mix of flour and milk that will make the dough more lofty,")
        sleep(3)
        print("Combine", 15 / Ingredient_Calculation, "grams of all-purpose flour")
        print(20 / Ingredient_Calculation, " millileters of milk and water in a pot of medium heat while stirring until it gelatinizes.") 
        sleep(3)
        print(" ")
        print("For the dough combine the ingredients listed:")
        print(443/Ingredient_Calculation, "grams of ap flour")
        print(2 / Ingredient_Calculation, "grams of fine salt")
        print(44 / Ingredient_Calculation, "grams of granulated sugar, the yeast mixture")
        print(55 / Ingredient_Calculation, "mL of water")
        print(2 / Ingredient_Calculation, "ROOM TEMPERATURE eggs, ")
        print("Add in the tangzhong that you made and after mixing into a cohesive dough add")
        sleep(2)
        print(50 / Ingredient_Calculation, "grams of butter that as been softened while mixing (mix for 5 minutes).")
        sleep(5)
        print("Good lord that was alot of stuff")
        sleep(2)
        Skip = int(input("would you like to keep going or skip to the buns? (Type 1 to stay or 2 to skip to the end) "))
        while Skip != 1 and Skip != 2:
            Skip = int(float(input("Sorry thats out of range please type 1, or 2: ")))
#If it is getting boring just looking at the ingredients then you can just skip to the finished producted here.
        if Skip == 1:
            print(" ")
            print("Ok then, now that you've made your dough shape it into a ball and place it in an oiled covered container for about 1 and a half hours.")
            print(" ")
            sleep(2)
            print("And we can't for get about the glaze In small pot, combine butter, sugar, and honey. Place in stove over medium heat, stir until thoroughly combined, place to the side to cool down.")
            print(" ")
            punch = input("Deflate the dough by punching it (press enter key): ")
            print("woah calm down")
            print(" ")
            print("Roll out your dough on a floured surface until it is about 1/2in thick Sprinkle cinnamon sugar on dough from edge to edge, leaving a quarter inch around the borders.")
            sleep(4)
            print(" ")
            print("Trim 1/2 in off sides of the log, cut dough using a nice, serrated knife, 2 in rolls to total 9 equal buns.")
            print(" ")
            print("In a 9x9 baking pan, add the caramel glaze at the bottom, sprinkle in 1 1/4 cup (140 g) of toasted, crushed pecan, arrange dough equally spaced apart In 3.")
            print("Place in oven at 350 degrees at 30-35 minutes. ")
            sleep(3)
            print(" ")
            print("DING")
            print("I cant find a cinnamon roll so heres a picture of a pretzel: 🥨")
        elif Skip == 2:
            print("DING")
            print("I cant find a cinnamon roll so heres a picture of a pretzel: 🥨")
        elif Number_Buns == 1:
            print("Ok you want, 10, sounds good lets' get cooking.") #will continue later but this is just default measurments which are gonna be a bunch of print statements.
        Goodbye()
#So at this point im happy with the calculations and im using the sleep and blank print("") statments to make the output look prettier and less jarring.
#I need to sort out the if statement at the beginning if you pick 10 and the if user wants skip -> update, did it. 
#create rolling dough icon when kneading steamy oven on pasta and steaming pot for meatfkf
#Glaised Braised Short Ribs
elif selection == '3':
    print("Tasty stuff...")
    skip_or_not = int(float(input("Would you like to go through the steps for prep or go straight to cooking?(Type in 1 to stay or 2 to skip): ")))
    while skip_or_not != 1 and skip_or_not != 2:
        skip_or_not = int(float(input("Sorry thats out of range please type 1, or 2: ")))
    if skip_or_not == 1:
        print("First,")
    elif skip_or_not == 2:
        Prep_Skip = input("Press enter to prep your recipe and worksation")
        for x in range(1, 18, 2):
            print(x, "ingredients prepped")
        print("Ok that was easier than listing everything out.")
elif selection == '4':
    print("Ok, bye")
#dont make let it just end reloop it with new message and menu again--how would I do that?
#As you can see i want to go a similar route for the other recipes as I did with 1, trying to walk the user through them while letting them participate while calculating whatever measurments are needed in the recipe, I just dont know if this is seeming like im on the right track in terms of the project though 
#** exponential multiplication, * multiplication, / division/ % modulus shows remainder, // floor division rounds to whole number, + addition, - subtraction, 
