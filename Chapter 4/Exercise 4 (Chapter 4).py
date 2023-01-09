#This programme contains an if-elif-else chain that determines a person’s stage of life. 
age = input(int("What is your age? ")) #This code asks the user to set a value for the variable age

if age < 2: #If the person is less than 2 years old, the code prints a string that says that the person is a baby.
    print("You're a baby!")
elif age < 4: #If the person is at least 2 years old but less than 4, it prints a message saying that the person is a toddler.
    print("You're a toddler!")
elif age < 13: #If the person is at least 4 years old but less than 13, it prints a message saying that the person is a kid.
    print("You're a kid!")
elif age < 20: #If the person is at least 13 years old but less than 20, it prints a message saying that the person is a teenager.
    print("You're a teenager!")
elif age < 65:#If the person is at least 20 years old but less than 65, it prints a message saying that the person is an adult.
    print("You're an adult!")
else:#If the person is age 65 or older, the code prints a message saying that the person is an elder.
    print("You're an elder!")