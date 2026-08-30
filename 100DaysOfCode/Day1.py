#Brand Name Generator
print("Welcome to the Brand Name Generator.")

#initialize the variables as empty strings
city = " "
pet_name = " "

#check user enetered smth' or not
while True:
  print("What's the name of the city you grew up in?")
  city = input("> ")
  #if there's no input, ask again
  if city== "":
    print("YOu haven't enetered anything yet. Please try again.")
  #if there's any input, break out the loop
  else:
    break

#same for the pet name 
while True:
  print("what's your pet name?")
  pet_name = input("> ")
  if pet_name== "":
    print("You haven't entered anything. Please try again.")
  else:
    break

#output using f-string to make it more readable
print(f"Your brand name could be {city} {pet_name}.")