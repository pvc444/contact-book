import json

try:
  with open("contacts.json", "r") as file:
    contacts = json.load(file)

except FileNotFoundError:
  contacts = []


while True:
  print("======= contact Book =======")
  print("1.Add contact")
  print("2.Show contacts")
  print("3.Search contact")
  print("4.Delete contact")
  print("5.Exit")

  choice = input("choose an option:")


  if choice == "1":
   
     name = input("please enter your name:")
     number = input("please enter your phone_number:")
     email = input("please enter your email:")


     contact = {
       "name": name,
       "number": number,
       "email": email
}

     contacts.append(contact)

     with open("contacts.json", "w") as file:
       json.dump(contact,file ,indent=4)

     print("contact saved!")


  elif choice == "2":
     print("all contacts")

     for contact in contacts:
        print(contact)

  elif choice == "3":
    search_name = input("Enter the name to search:")
    found = True

    for contact in contacts:
      if contact["name"] == search_name:
        print(contact)
        found =True

    if not found:
      print("contact not found.")


  elif choice == "4":

     delete_name = input("enter the name to delete:")
     found = False

     for contact in contacts:
       if contact["name"] == delete_name:
          contacts.remove(contact)
          print("contact deleted")
          found = True
          break




     if not found:
        print("contact not found")

     with open("contacts.json", "w") as file:
       json.dump(contacts,file,indent=4)


  elif choice == "5":
     print("Goodbye")
     break


  else:
    print("invalid choice") 

