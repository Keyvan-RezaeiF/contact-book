from person import Person


class Book:

    def __init__(self):
        self.people = dict()


    def check_email(self):
        while True:
            has_email = input("\n\tDoes contact have any e-mail ? (y/n) : ")
            if has_email == "y" or has_email == "Y":
                while True:
                    email = input("\n\tEnter contact's email : ")
                    if "@" in email:
                        return email
                    else:
                        print("\n\tSomething went wrong! Try again!")
            elif has_email == "n" or has_email == "N":
                return None
            else:
                print("\n\tSomething went wrong! Try again!")


    def add_contact(self):
        first_name = input("\n\tEnter contact's first name : ").title()
        last_name = input("\n\tEnter contact's last name : ").title()
        email = self.check_email()
        contact = Person(first_name, last_name, email)
        contact.add_numbers()
        full_name = contact.get_first_name() + " " + contact.get_last_name()
        info = [contact.get_email(), contact.get_numbers()]
        self.people[full_name] = info


    def edit_contact(self):
        pass

    
    def search_by_first_name(self):
        first_name = input("\n\tEnter first name : ")
        found = False
        for key in self.people.keys():
            if key.split()[0] == first_name.title():
                found = True
                print(f"\n\tE-mail : {self.people[key][0]}  numbers : {self.people[key][1]}\n")

        if found == False:
            print("\n\tNot found!")


    def search_by_last_name(self):
        last_name = input("\n\tEnter last name : ")
        found = False
        for key in self.people.keys():
            if key.split()[1] == last_name.title():
                found = True
                print(f"\n\tE-mail : {self.people[key][0]} , numbers : {self.people[key][1]}\n")
    
        if found == False:
            print("\n\tNot found!")


    def search_by_whole_name(self):
        whole_name = input("\n\tEnter whole name : ")
        found = False
        for key in self.people.keys():
            if key == whole_name.title():
                found = True
                print(f"\n\tE-mail : {self.people[key][0]} , numbers : {self.people[key][1]}\n")
    
        if found == False:
            print("\n\tNot found!")


    def search_by_email(self):
        email = input("\n\tEnter email : ")
        found = False
        for key, value in self.people.items():
            if value[0] == email:
                found = True
                print(f"\n\tname : {key} , numbers : {self.people[key][1]}\n")
    
        if found == False:
            print("\n\tNot found!")


    def search_by_number(self):
        phone_number = input("\n\tEnter email : ")
        found = False
        for key, value in self.people.items():
            for number in value[1]:
                if number == phone_number:
                    found = True
                    print(f"\n\tname : {key} , E-mail : {self.people[key][0]}")
    
        if found == False:
            print("\n\tNot found!")


    def search_in_book(self):
        print("\n\t*** Search menu ***")
        print("---------------------------------------")
        print("\t*** 1. Search by first name")
        print("\t*** 2. Search by last name")
        print("\t*** 3. Search by whole name")
        print("\t*** 4. Search by email")
        print("\t*** 5. Search by number")
        print("\t*** 6. Back")
        print("\t*** 7. Exit")
        choice = input("\n\tEnter your choice : ")

        if choice == "1":
            self.search_by_first_name()
        elif choice == "2":
            self.search_by_last_name()
        elif choice == "3":
            self.search_by_whole_name()
        elif choice == "4":
            self.search_by_email()
        elif choice == "5":
            self.search_by_number()
        elif choice == "6":
            return
        elif choice == "7":
            print("\n\tSee you later!\n")
            exit()
        else:
            print("\n\tWrong input! Try again!\n")
        
        self.search_in_book()


    def sort_by_sth(self):
        pass

    
    def delete_contact(self):
        pass        

    
    def show_contact_book(self):
        if self.people:
            print()
            for key, value in self.people.items():
                print(f"\n\t{key} --> E-mail : {value[0]} , numbers : {value[1]}")
        else:
            print("\n\tContact book is empty!")

    
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
        choice = input("\n\tEnter your choice : ")

        if choice == "1":
            self.add_contact()
        elif choice == "2":
            self.edit_contact()
        elif choice == "3":
            self.search_in_book()
        elif choice == "4":
            self.sort_by_sth()
        elif choice == "5":
            self.delete_contact()
        elif choice == "6":
            self.show_contact_book()
        elif choice == "7":
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