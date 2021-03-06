# Jude and Harry
# Plays a 2 player Hangman Game

wrong = 0 # Sets counter for wrong


answer = list(input("Enter a word to be guessed? ")) #prompts a word to be guessed
print("\n" * 51) #clears the screen

list1 = [] #array

for i in range(0, len(answer)): #for letters in answer prints underscores
    list1.append("_")

print(list1) #prints the underscores

while list1 != answer and wrong < 10:
    correct = False
    contains = False
    guess = str(input("\nPlayer 2, guess a letter: ")) #prompts the user for a letter

    for t in list1: 
        if guess == t:
            correct = True
           
    for i in answer:
        if i == guess and correct == False:
            contains = True
    
    if contains == True:
        let = [i for i, x in enumerate(answer) if x == guess]

        for j in range(0, len(let)):
            list1.insert(let[j], guess)
            list1.pop(let[j] + 1)
        
        for x in range(0, len(list1)):
            print(list1[x], end = " ")


    # This part builds the Hangman by determining the number of wrong answers
            
    elif correct == False:
        print("try again!")
        wrong = wrong + 1
        # Builds Head
        if wrong == 1:
          print("  0" + "\n")
        #Builds Body
        if wrong == 2:
          print("  0" + "\n")
          print("  |" + "\n")
        #Builds Left Arm
        if wrong == 3:
          print("  0" + "\n")
          print("- |")
        # Bulds Right Arm
        if wrong == 4:
          print("  0" + "\n")
          print("- | -")  
        # Builds Left Leg
        if wrong == 5:
          print("  0")
          print("- | -")
          print(" /")
        # Builds Right Leg  
        if wrong == 6:
          print("   0")
          print(" - | -")
          print("  / \ ")
        # Builds Left Hand
        if wrong == 7:
          print("   0")
          print("\- | -")
          print("  / \ ")
        # Builds Right Hand
        if wrong == 8:
          print("   0")
          print("\- | -/")
          print("  / \ ")
        # Builds Hat
        if wrong == 9:
          print("   ^")
          print("   0")
          print("\- | -/")
          print("  / \ ")
        # Game ends due to too many wrong answers
        if (wrong == 9):
          print("You failed, try again next time!")
          break
    
