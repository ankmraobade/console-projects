# PHONE BOOK APP

"""
Using Dictionary and Functions to create a Phone Book App that has the following abilities:
1. View the Phone Book
2. Add a Contact
3. Edit a Contact
4. Delete a Contact
5. Search a Contact
6. Exit
Implement the CRUD Functionality.
"""

from sys import *

phone_book = {}
draft_phone_book = {}

# Checking whether the phone book is empty or not
def is_empty(phone_book):
    if phone_book:
        return False
    else:
        return True

# Function: View Phone Book
def view(phone_book):
    print("Contact List: ", phone_book)

# Function: Add Contact in Phone Book
def add(phone_book):
    name = input("Enter Contact Name: ")
    phone = input("Enter Contact Phone: ")
    phone_book[name] = phone
    print("New Contact Added: ", phone_book)

# Function: Edit an Existing Contact in Phone Book
def edit_name(phone_book):
    name = input("Enter the name of the contact you want to edit: ")
    new_replacable_name = input("Enter the new replacable name: ")
    phone_book[new_replacable_name] = phone_book.pop(name)
    print("Name changed from", name, "to", new_replacable_name)
    print("Updated Phone Book: ", phone_book)

# Function: Edit an Existing Contact Phone in Phone Book
def edit_phone(phone_book):
    name_search = input("Enter the name of the contact whose phone number you would like to edit in the Phone Book: ")
    phone_edit = input("Enter the new phone number: ")
    draft_phone_book[name_search] = phone_edit
    phone_book.update(draft_phone_book)
    print("Phone Number Successfully Changed!")
    print("Updated Phone Book: ", phone_book)

# Function: Deleting an Existing Contact
def delete(phone_book):
    name = input("Enter the name of the contact you want to delete: ")
    phone_book.pop(name)
    print("Contact", name, "has been deleted successfully!")
    print("New Phone Book: ", phone_book)

# Function: Search a Contact
def search(phone_book):
    search_name = input("Enter the name of the contact you want to search: ")
    if search_name in phone_book:
        print("Name: ", search_name)
        print("Contact Phone: ", phone_book.get(search_name, 0)
    else:
        print("Contact: ", search_name, "Not Found! No such contact is available")

print("--------------")
print("PHONE BOOK APP")
print("--------------")

while True:
    choice = int(input("Enter Your Choice: 1. View Phone Book 2. Add New Contact 3. Edit Existing Contact 4. Delete A Contact 5. Search A Contact 6. Exit: "))

    # Main Program
    def main(choice):
        
        # Viewing Phone Book
        if choice == 1:
            if is_empty(phone_book) == False:
                view(phone_book)
            else:
                print("No Contacts Yet.")
                print("Thank you for using the PHONE BOOK APP")

        # Adding New Contact in Phone Book
        elif choice == 2:
            add(phone_book)

        # Editing an existing Contact in Phone Book
        elif choice == 3:
            edit_choice = input("Do you want to edit the name of the contact or phone number of the contact? Press (n/N) for editing the name of the contact OR Press (p/P) for editing the phone number of the contact: ")
            if edit_choice == 'n' or edit_choice == 'N':
                edit_name(phone_book)
            elif edit_choice == 'p' or edit_choice == 'P':
                edit_phone(phone_book)
            else:
                print("Invalid entry. Please enter either n or p")

        # Deleting an existing Contact in Phone Book
        elif choice == 4:
            delete(phone_book)
        
        # Searching a Contact in Phone Book
        elif choice == 5:
            search(phone_book)

        # Exiting the Phone Book Application
        elif choice == 6:
            print("Thank you for using the Phone Book Application.")
            exit()
            
    main(choice)
