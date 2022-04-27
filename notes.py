#DAY 6: FUNCTIONS, CODE BLOCKS AND WHILE LOOPS

#FUNCTIONS
#Examples of Built in Functions
# print("Hello")
# num_char = len("Hello")
# print(num_char)

#Make your own fun
# #define the function
# def my_function():
#   print("Hello")
#   print("Bye")
# #Call the function
# my_function()

#INDENTATION
# Spaces are the preferred indentation method. Tabs should be used solely to remain consistent with code that is already indented with tabs. Python disallows mixing tabs and spaces for indentation.

# #FOR LOOPS - When you want to iterate over something and do something with each thing
# for item in list_of_items:
#     #Do something to each item

# for number in range(a,b):
#     print(number)

#WHILE LOOP - Simply want to carry out functionality until a condition is met that you set
while something_is_true:
    #Do something repeatedly. Only when this something because "False" does the loop stop

#INFINITE LOOP
while 5 > 3:
    #Do this
    #Then do this
    #Then do this


    
# EXERCISE: Reeborg's World Challenge - Hurdle 3
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# EXERCISE: Reeborg's World Challenge - Hurdle 4
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


