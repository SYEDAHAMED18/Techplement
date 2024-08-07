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
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    # Simple data validation
    if not name or not phone or not email:
        print("All fields are required!")
        return

    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print(f"Contact {name} added.")

def search_contact(contacts):
    search_name = input("Enter name to search: ").strip()
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"Found: {contact}")
            return
    print("Contact not found.")

def update_contact(contacts):
    search_name = input("Enter name to update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            contact['phone'] = input("Enter new phone number: ").strip()
            contact['email'] = input("Enter new email: ").strip()
            save_contacts(contacts)
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_name = input("Enter name to delete: ").strip()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == search_name.lower():
            del contacts[i]
            save_contacts(contacts)
            print("Contact deleted.")
            return
    print("Contact not found.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(contact)

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            list_contacts(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
