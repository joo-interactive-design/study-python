#exercise 1 - capitalize the first letter of words
def format_name(f_name, l_name):
  first_name = f_name.title()
  last_name = l_name.title()
  return f"{first_name} {last_name}"

print(format_name("mina", "kim"))
#result will be Mina Kim

#multiple return values
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs"
  first_name = f_name.title()
  last_name = l_name.title()
  return f"{first_name} {last_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))

#exercise 2 - Days in Month( Leap Year challenge )
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    if is_leap(year) and month == 2:
      return 29
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    return month_days[month-1]
  # is_leap(year) is either true or false 
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












