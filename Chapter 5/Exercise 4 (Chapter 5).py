rivers = {
    'Nile': 'Egypt',
    'Mississippi': 'United States',
    'Krishna': 'India',
    'Amazon': 'South America',
    'Rio Grande': 'North America',
    }
 
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")
 
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")
 
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")

#This programme contains a dictionary containing three major rivers and the country each river runs through.
#I used a loop to print the name of each river the name of each country included in the dictionary and it prints a sentence about each river.