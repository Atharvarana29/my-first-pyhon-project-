import random
options = [ 'r' , 'p' , 's']

print("Welcome to the game of ROCK PAPER SCISSOR !!! ✅")

wish = input(f"enter your wish(r = ROCK , p = PAPER, s = SCISSOR) : " )

Mywish = random.choice(options)  #here we need to remember that we donot have to use 
# random.shuffle as it will just shuffle and return nothig 
# while random.choice randomly picks a choice and if we are storing
# it in some variable then the returned value gets stored in that 

print(f"ok fine! now it's my turn and my wish is :  {Mywish}")
# now according to rules
if ( Mywish == wish ):
    print("Since we both have the same wish . so plese enter a new wish")
elif ( Mywish == 'r' and wish == 's'):
    print("i won!")
elif(Mywish == 'p' and wish == 'r'):
    print("i won!")
elif(Mywish == 's' and wish == 'p'):
    print("i won!")
else:
    print("you are the winner ")

