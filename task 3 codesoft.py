import sys

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        print("Name\t\tPhone\t\tEmail\t\tAddress")
        for contact in self.contacts:
            print(f"{contact.name}\t{contact.phone}\t{contact.email}\t{contact.address}")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts.pop(i)
                break

    def search_contacts(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, name, contact):
        for i, c in enumerate(self.contacts):
            if c.name == name:
                self.contacts[i] = contact
                break

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Update Contact")
        print("6. Quit")

        option = input("Enter your choice: ")

        if option == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif option == "2":
            contact_book.view_contacts()
        elif option == "3":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif option == "4":
            search_term = input("Enter the name or phone number to search: ")
            results = contact_book.search_contacts(search_term)
            for contact in results:
                print(f"{contact.name}\t{contact.phone}")
        elif option == "5":
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter the new name: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email: ")
            new_address = input("Enter the new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_book.update_contact(name, new_contact)
        elif option == "6":
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
