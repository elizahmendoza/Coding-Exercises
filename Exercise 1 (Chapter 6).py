prompt = "\nWhat topping would you like on your pizza?" #This code contains a loop that asks the user to enter a series of pizza toppings until they enter a 'quit' value. 
prompt += "\nEnter 'quit' when you are finished: "
 
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break

#As they enter each topping, it prints a message saying i'll add that topping to their pizza.

   