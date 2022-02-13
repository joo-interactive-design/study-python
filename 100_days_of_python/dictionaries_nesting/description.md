# Day 9 - Dictionaries, Nesting and the Secret Auction

## Python dictionary has two parts : Key and Value 
### {Key: Value}
programming_dictionary = {"Bug": " An error in a program that ..."}

### Retrieving items from dictionary
print(programming_dictionary["Bug"])
###### *When retrieving items, make sure the key is actual data type, and spell right 

### Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"<br>
print(programming_dictionary)

### Create an empty dictionary
empty_dictionary = {}

### Wipe an existing dictionary
programming_dictionary = {}

### Edit an item in a dictionary
Programming_dictionary["Bug"] = "new definition here"

### Loop through a dictionary
for key in programming_dictionary:<br>
  print(key)<br>
  print(programming_dictionary[key])<br>
##### *It's printing out key and value

## Nesting
{ <br>
  key: [List]<br>
  key2: {Dict},<br>
 }
 
 ### Nesting a List in a Dictionary
 travel_log = { <br>
  "France": {"cities_visited" : ["Paris", "lille", "Dijon"], "total_visits = 12},
  "Germany": {"cities_visited" : ["Berlin"], "total_visits : 5}<br>
 }<br>
 
 ### Nesting a List in a List
 travel_log = [ <br>
  {
    "country": "France", <br>
    "cities_visited" : ["Paris", "lille", "Dijon"], <br>
    "total_visits : 12<br>
  },<br>
  {
    "country": "Germany", <br>
    "cities_visited" : ["Berlin"],<br>
    "total_visits : 5<br>
  },<br>
 ]<br>
 
 
 
 
 ##### *Value can be list, dictionary
