import random
s = {
    1: 'stone',
    2: 'paper',
    3: 'scissor'
}
# This is actually the game logic which is going on refreshing the input of the number everytime and then getting the input
print("choose your options among these 1)scissor ,2)stone ,3)paper ,press 'quit' to end the game") 
while True:
    n = random.randint(1, 3)
    result = s.get(n)
    b = input("enter your choice !! ").lower()
    if b == result:
        print("the match has a been a draw match :)")
        print("the computer's choice was", result),
    elif b == "scissor" and result == "stone":
        print("the computer's choice was", result)
        print("sorry the computer has won the game !!")
    elif b == "scissor" and result == "paper":
        print("the computer's choice was", result)
        print("you have won the game !!")
    elif b == "stone" and result == "paper":
        print("the computer's choice was", result)
        print("sorry the computer has won the game !!")
    elif b == "stone" and result == "scissor":
        print("the computer's choice was", result)
        print("sorry the computer has won the game !!")
    elif b == "paper" and result == "scissor":
        print("the computer's choice was", result)
        print("the computer has won the game !!")
    elif b == "paper" and result == "stone":
        print("the computer's choice was", result)
        print("you have won the game !!")
    elif b=="quit":
        break
    else:
        print("can't understand plz repeat")
