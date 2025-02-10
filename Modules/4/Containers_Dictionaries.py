#Dictionaries are a data type used to store information in a key-value manner. 
#Dictionaries are defined by the use of curly braces, yet use square brackets to access the values.
#Think of dictionaries as an address book where names act as a key to retrieve an address (the value). 
#Dictionaries are unordered, changeable, and indexed.
#Dictionaries can contain any type of data, including other dictionaries.
#Dictionaries, like lists, do not care what data type values are; we can even use a list as the value of a key!

languages = {
    'Canada' : 'French',
    'United States' : 'English',
    'Mexico' : 'Spanish',
    'Brazil' : 'Portuguese'
}
languages['Haiti'] = 'French'
suriname = 'Suriname'
languages[suriname] = 'Dutch'
# Can also be written
# languages = { 'Canada': 'French', 'United States' : 'English', 'Mexico' : 'Spanish', 'Brazil' : 'Portuguese' }

# print(languages[1]) # This causes Python to throw a 'KeyError' exception
print(languages['Brazil']) # This prints Portuguese
print(languages['Suriname']) # This prints Dutch
print(languages) # This prints {'Canada': 'French', 'United States': 'English', 'Mexico': 'Spanish', 'Brazil': 'Portuguese', 'Haiti': 'French', 'Suriname': 'Dutch'}
print(languages.keys()) # This prints dict_keys(['Canada', 'United States', 'Mexico', 'Brazil', 'Haiti', 'Suriname'])
print(languages.values()) # This prints dict_values(['French', 'English', 'Spanish', 'Portuguese', 'French', 'Dutch'])
print(languages.items()) # This prints dict_items([('Canada', 'French'), ('United States', 'English'), ('Mexico', 'Spanish'), ('Brazil', 'Portuguese'), ('Haiti', 'French'), ('Suriname', 'Dutch')])
print(languages.get('Canada')) # This prints French
print(languages.get('United States')) # This prints English
print(languages.get('Mexico')) # This prints Spanish
print(languages.get('Brazil')) # This prints Portuguese
print(languages.get('Haiti')) # This prints French
print(languages.get('Suriname')) # This prints Dutch
print(languages.get('Argentina')) # This prints None
print(languages.get('Argentina', 'Not Found')) # This prints Not Found
