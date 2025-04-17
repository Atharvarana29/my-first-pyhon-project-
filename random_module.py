
# basic structure of random module and use cases

# basic structure

# import random
# options =['r' , 'p' ,'s']
# computer_choice = random.choice(options)
# print("computer chose: " , computer_choice)

# use  cases

# avoid repeating the last move
# import random
# options = ['r','p', 's']
# last_move= None
# for round in range(5):
# below is the list comprehnsion

#     available_choice = [opt for opt in options if opt! = last_move]
# computer_choice = random.choice(options)
# last_move = computer_choice
# print(f"round{n+1} - computer chose: {computer_choice}")



# no repeated moves at all
# import random 
# options = [ 'r' , 'p', 's']
# random.shuffle(options)

# for round in range(len(options)):
#     computer_choice = options[round]
#     print(f"round{round+1} - computer chose: {computer_choice}")



# tracking all the moves played
# import random
# options = [ 'r' , 'p', 's']
# history = [] # just an empty list

# for round in range(5): #running the loop 5 times 
#     computer_choice = random.choice(options)
#     history.append(computer_choice)
#     print(f"round {round + 1} - computer chose: {computer_choice}")

# print("all computer moves : " , history )
 