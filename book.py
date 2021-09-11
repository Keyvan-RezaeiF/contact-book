from person import Person


class Book:

    def __init__(self):
        self.people = dict()


    def add_contact(self):
        first_name = input("\n\tEnter contact's fisrt name : ").title()
        last_name = input("\n\tEnter contact's last name : ").title()
        email = input("\n\tEnter contact's email : ")
        contact = Person(first_name, last_name, email)
        contact.add_numbers()
        key = contact.get_first_name() + " " + contact.get_last_name()
        value = [contact.get_email(), contact.get_numbers()]
        self.people[key] = value


    def edit_contact(self):
        pass

    def search_in_book(self):
        pass

    def sort_by_sth(self):
        pass

    def delete_contact(self):
        pass

    def show_contact_book(self):
        print()
        print(self.people)


    def display_main_menu(self):
        print("\n\t*** My contact book ***")
        print("---------------------------------------")
        print("\t*** 1. Add contact")
        print("\t*** 2. Edit contact")
        print("\t*** 3. Search")
        print("\t*** 4. Sort")
        print("\t*** 5. Delete contact")
        print("\t*** 6. Show contact book")
        print("\t*** 7. Exit")
        choice = int(input("\n\tEnter your choice : "))

        if choice == 1:
            self.add_contact()
        elif choice == 2:
            self.edit_contact()
        elif choice == 3:
            self.search_in_book()
        elif choice == 4:
            self.sort_by_sth()
        elif choice == 5:
            self.delete_contact()
        elif choice == 6:
            self.show_contact_book()
        elif choice == 7:
            print("\n\tSee you later!\n")
            exit()
        else:
            print("\n\tWrong input! Try again!\n")
        
        self.display_main_menu()


def main():
    my_contact_book = Book()
    my_contact_book.display_main_menu()


if __name__ == "__main__":
    main()