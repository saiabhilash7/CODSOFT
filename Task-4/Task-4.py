import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Contact added!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contacts():
    query = input("Enter name or phone number to search: ")
    contacts = load_contacts()
    found_contacts = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("No contacts found.")

def update_contact():
    view_contacts()
    contacts = load_contacts()
    index = int(input("Enter the contact number to update: ")) - 1
    if 0 <= index < len(contacts):
        print("Leave blank to keep current value.")
        name = input(f"Enter new name ({contacts[index]['name']}): ") or contacts[index]['name']
        phone = input(f"Enter new phone number ({contacts[index]['phone']}): ") or contacts[index]['phone']
        email = input(f"Enter new email ({contacts[index]['email']}): ") or contacts[index]['email']
        address = input(f"Enter new address ({contacts[index]['address']}): ") or contacts[index]['address']
        
        contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
        save_contacts(contacts)
        print("Contact updated!")
    else:
        print("Invalid contact number.")

def delete_contact():
    view_contacts()
    contacts = load_contacts()
    index = int(input("Enter the contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted!")
    else:
        print("Invalid contact number.")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
