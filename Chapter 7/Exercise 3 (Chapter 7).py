def make_shirt(size, message):#This code contains a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
    """Summarize the shirt that's going to be made.""" #The function prints a sentence summarizing the size of the shirt and the message printed on it. 

    print(f"\nI'm going to make a {size} t-shirt.") #This code calls the function once using positional arguments to make a shirt. 
    print(f'It will say, "{message}"')
 
make_shirt('large', 'I love BTS!')
make_shirt(message="Readability counts.", size='medium')
#Then, it calls the function a second time using keyword arguments.