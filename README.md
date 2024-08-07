Contact Management System
This is a Python-based Contact Management System that provides a simple command-line interface to manage your contacts. The system allows you to add, search, update, delete, and list contacts, with all data stored in a contacts.json file for persistence.

Features
Add Contact: Enter a name, phone number, and email to add a new contact.
Search Contact: Find a contact by name and display their details.
Update Contact: Update the phone number and email of an existing contact.
Delete Contact: Remove a contact from the list by searching for their name.
List Contacts: Display all contacts currently stored in the system.
Requirements
Python 3.x
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
Run the script:

bash
Copy code
python contact.py
Usage
Follow the on-screen menu to choose an option:

1: Add a new contact.
2: Search for a contact by name.
3: Update an existing contact.
4: Delete a contact.
5: List all contacts.
6: Exit the program.
The system requires all fields (name, phone, email) when adding a contact. Updates require you to re-enter all information for the contact.

File Structure
contact.py: The main script containing the contact management logic.
contacts.json: A JSON file used to store contact data persistently.
Future Enhancements
Add more advanced search capabilities (e.g., search by phone or email).
Implement error handling for invalid input and file operations.
Enhance data validation for phone numbers and email addresses.
Add a graphical user interface (GUI) for easier interaction.
License
This project is open-source and available under the MIT License.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

