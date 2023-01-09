prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "  
 
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
 
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

#The programme determines if a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
#This loop asks the user their age, and then tell them the cost of their movie ticket