# Jude and Harry
# Take a sentence and type the words out by letter

def myFunc(word): 
    a = word.split() # Splits the sentence into words
    for a in word:
        b = a.split() # Splits the words into letters
        for b in a:
            print(b) # Prints the letters
c = input(print("Enter a short sentence: "))
print("\n" * 51)
c = c.replace(" ", "-") # replaces spaces with "-"
(myFunc(c))

