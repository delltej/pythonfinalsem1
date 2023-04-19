#  an empty dictionary
phoneDirectory = {}
print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
option = 0
while (option != 5):
  print("1.Add a record")
  print("2.Search a record")
  print("3.Update a record")
  print("4.Delete a record")
  print("5.Quit")
  #for selecting option
  option = int(input("enter option "))
  if option == 5:
    print("Thank you\n")
    # for adding
  if option == 1:
    x = input("Enter name: ")
    #for enter alphabate not number
    if x.isalpha():
      y = input("Enter your 10-digit phone number: ")
      #for enter number and limit 10 
      if y.isdigit() and len(y) == 10:
        phoneDirectory.update({x: y})
        print("Record added")
      else:
        print("Invalid phone number. Please enter a 10-digit number.")
    else:
      print("Invalid name. Please enter only alphabets.")
    # for updating the changes
  elif (option == 3):
    x = input("Enter your name ")
    y = input("Enter new 10-digit phone number:  ")
    phoneDirectory.update({x: y})
    print("Record updated")
    #for search option
  elif (option == 2):
    x = input("Enter name to search:")
    z = 0
    for t in phoneDirectory.keys():
      if t == x:
        print(t, ":", phoneDirectory[t])
        z = 1
      else:
        pass

    if (z == 0):
      print("not found")
      #for deleting option
  elif (option == 4):
    x = input("Enter name")
    del phoneDirectory[x]
    print("Record deleted")
    # print the final phone directory
print(phoneDirectory)
