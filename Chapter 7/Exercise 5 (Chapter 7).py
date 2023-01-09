def describe_city(city, country = 'the United Arab Emirates'): #I wrote a function called describe_city() that accepts the name of a city and its country. 
    """Describe a city.""" #The function should print a simple sentence, such as Reykjavik is in Iceland. 
    msg = f"{city.title()} is in {country.title()}." #I gave the parameter for the country a default value.
    print(msg)
 
describe_city('Dubai')
describe_city('Tokyo', 'Japan')
describe_city('Abu Dhabi')
#Lastly, I called the function for three different cities.