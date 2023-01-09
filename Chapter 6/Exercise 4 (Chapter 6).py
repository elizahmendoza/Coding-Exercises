sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef'] #I made a list called 'sandwich_orders' and filled it with the names of various sandwiches. 
finished_sandwiches = [] #Then, I made an empty list called 'finished_sandwiches'.
 
while sandwich_orders:#This code loops through the list of sandwich orders and print a message for each order, such as 'I made your tuna sandwich'. 
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)#As each sandwich is made, it moves to the list of finished sandwiches. 
  
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
#After all the sandwiches have been made, it prints a message listing each sandwich that was made.