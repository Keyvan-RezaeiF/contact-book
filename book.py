from person import Person
from collections import OrderedDict
from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')


class Book:

    def __init__(self):
        self.people = dict()


    def save_in_file(self):
        with open("contactBook.txt", "w") as file:
            for key, value in self.people.items():
                file.write(f"\n\t*** {key} --> E-mail : {value[0]} , numbers : {value[1]}")

    
    def check_email(self):
        while True:
            has_email = input("\n\tDoes contact have any e-mail ? (y/n) : ")
            if has_email == "y" or has_email == "Y":
                while True:
                    email = input("\n\tEnter contact's email : ")
                    if "@" in email:
                        return email
                    else:
                        print("\n\tYour e-mail is not valid! Try again!")
            elif has_email == "n" or has_email == "N":
                return None
            else:
                print("\n\tSomething went wrong! Try again!")


    def add_contact(self):
        self.show_contact_book()
        print("\n\t*** Add menu ***")
        print("---------------------------------------")
        print("\t*** 1. Add from terminal")
        print("\t*** 2. Add from text file")
        print("\t*** 3. Back")
        print("\t*** 4. Exit")
        choice = input("\n\tEnter your choice : ")

        if choice == "1":
            first_name = input("\n\tEnter contact's first name : ").title()
            last_name = input("\n\tEnter contact's last name : ").title()
            email = self.check_email()
        elif choice == "2":
            pass # add from txt file
        elif choice == "3":
            clear()
            return
        elif choice == "4":
            print("\n\tSee you later!\n")
            clear()
            exit()
        else:
            print("\n\tWrong input! Try again!\n")
        
        contact = Person(first_name, last_name, email)
        contact.add_numbers()
        full_name = contact.get_first_name() + " " + contact.get_last_name()
        info = [contact.get_email(), contact.get_numbers()]
        self.people[full_name] = info
        print("\n\tAdded successfully!")
        self.sort_based_on_first_name()
        self.save_in_file()
        clear()
        self.add_contact()


    def edit_first_name(self):
        choice = input("\n\tWhich one do you want to edit? Enter the number : ")
        i = 0
        for key, value in self.people.items():
            i += 1
            if i == int(choice):
                new_first_name = input("\n\tEnter contact's new first name : ")
                last_name = key[key.find(" ") + 1:]
                self.people.pop(key)
                new_key = (new_first_name + " " + last_name).title()
                self.people[new_key] = value
                print("\n\tEdited successfully!")
                self.sort_based_on_first_name()
                self.save_in_file()
                return
        print("\n\tNot found!")


    def edit_last_name(self):
        choice = input("\n\tWhich one do you want to edit? Enter the number : ")
        i = 0
        for key, value in self.people.items():
            i += 1
            if i == int(choice):
                new_last_name = input("\n\tEnter contact's new last name : ")
                first_name = key[:key.find(" ")]
                self.people.pop(key)
                new_key = (first_name + " " + new_last_name).title()
                self.people[new_key] = value
                print("\n\tEdited successfully!")
                self.save_in_file()
                return
        print("\n\tNot found!")
    

    def edit_whole_name(self):
        choice = input("\n\tWhich one do you want to edit? Enter the number : ")
        i = 0
        for key, value in self.people.items():
            i += 1
            if i == int(choice):
                new_name = input("\n\tEnter contact's new name : ")
                self.people.pop(key)
                new_key = new_name.title()
                self.people[new_key] = value
                print("\n\tEdited successfully!")
                self.sort_based_on_first_name()
                self.save_in_file()
                return
        print("\n\tNot found!")

    
    def edit_email(self):
        choice = input("\n\tWhich one do you want to edit? Enter the number : ")
        i = 0
        for key, value in self.people.items():
            i += 1
            if i == int(choice):
                while True:
                    new_email = input("\n\tEnter contact's new email : ")
                    if "@" in new_email:
                        self.people.pop(key)
                        value[0] = new_email
                        self.people[key] = value
                        print("\n\tEdited successfully!")
                        self.save_in_file()
                        return
                    else:
                        print("\n\tNot found!")


    def show_numbers(self, name):
        numbers = self.people[name][1]
        if numbers:
            i = 0
            for number in numbers:
                i += 1
                print(f"\n\t{i}. {number}")
            return True
        else:
            print("\n\tThere is no number for this contact!")
            return False


    def edit_numbers(self):
        choice1 = input("\n\tWhich contact do you want to edit? Enter the number : ")
        i = 0
        for key, value in self.people.items():
            i += 1
            if i == int(choice1):
                if self.show_numbers(key):
                    choice2 = input("\n\tWhich phone number do you want to edit? Enter the number : ")
                    j = 0
                    for number in value[1]:
                        j += 1
                        if j == int(choice2):
                            while True:
                                new_number = input("\n\tEnter contact's new number : ")
                                if len(new_number) == 11 and new_number.isnumeric():
                                    self.people.pop(key)
                                    value[1][int(choice2) - 1] = new_number
                                    self.people[key] = value
                                    print("\n\tEdited successfully!")
                                    self.save_in_file()
                                    return
                                else:
                                    print("\n\tNot found!")
                else:
                    while True:
                        want_to_add = input("\n\tDo you want to add any number for this contact ? (y/n) : ")
                        if want_to_add.lower() == "y":
                            count = int(input("\n\tHow many numbers do you want to add ? "))
                            while count > 0:
                                while True:
                                    number = input("\n\tEnter the number : ")
                                    if len(number) == 11 and number.isnumeric():
                                        value[1].append(number)
                                        break
                                    else:
                                        print("\n\tNumber is not valid! Try again!")
                                count -= 1
                            print("\n\tAdded successfully!")
                            self.save_in_file()
                            break    
                        elif want_to_add.lower() == "n":
                            break
                        else:
                            print("\n\tSomething went wrong! Try again!")
            else:
                print("\n\tSomething went wrong! Try again!")

            print("\n\tNot found!")

    
    def edit_contact(self): 
        clear()
        self.show_contact_book()
        print("\n\t*** Edit menu ***")
        print("---------------------------------------")
        print("\t*** 1. Edit first name")
        print("\t*** 2. Edit last name")
        print("\t*** 3. Edit whole name")
        print("\t*** 4. Edit email")
        print("\t*** 5. Edit numbers")
        print("\t*** 6. Back")
        print("\t*** 7. Exit")
        choice = input("\n\tEnter your choice : ")

        if choice == "1":
            self.edit_first_name()
        elif choice == "2":
            self.edit_last_name()
        elif choice == "3":
            self.edit_whole_name()
        elif choice == "4":
            self.edit_email()
        elif choice == "5":
            self.edit_numbers()
        elif choice == "6":
            clear()
            return
        elif choice == "7":
            print("\n\tSee you later!\n")
            clear()
            exit()
        else:
            print("\n\tWrong input! Try again!\n")
        
        clear()
        self.edit_contact()

    
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
        print("\t*** 5. Search by numbers")
        print("\t*** 6. Back")
        print("\t*** 7. Exit")
        choice = input("\n\tEnter your choice : ")
        clear()

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
            clear()
            return
        elif choice == "7":
            print("\n\tSee you later!\n")
            clear()
            exit()
        else:
            print("\n\tWrong input! Try again!\n")
        
        self.search_in_book()


    def sort_based_on_first_name(self):
        self.people = OrderedDict(sorted(self.people.items()))


    def delete_contact(self):
        if self.people:
            while True:
                self.show_contact_book()
                choice = input("\n\tWhich one do you want to delete? Enter the number (for back, Enter 0): ")
                clear()
                if choice == "0":
                    return
                elif int(choice) <= len(self.people):
                    i = 0
                    for key, value in self.people.items():
                        i += 1
                        if i == int(choice):
                            to_be_deleted_key = key
                            break
                    
                    self.people.pop(to_be_deleted_key)
                    self.save_in_file()
                else:
                    print("\n\tWrong input! Try again!\n")
        else:
            print("\n\tContact book is empty!")
        
    
    def show_contact_book(self):
        if self.people:
            print()
            i = 0
            for key, value in self.people.items():
                i += 1
                print(f"\n\t{i}. {key} --> E-mail : {value[0]} , numbers : {value[1]}")
        else:
            print("\n\tContact book is empty!")

    
    def display_main_menu(self):
        print("\n\t*** My contact book ***")
        print("---------------------------------------")
        print("\t*** 1. Add contact")
        print("\t*** 2. Edit contact")
        print("\t*** 3. Search")
        print("\t*** 4. Delete contact")
        print("\t*** 5. Show contact book")
        print("\t*** 6. Exit")
        choice = input("\n\tEnter your choice : ")

        clear()
        if choice == "1":
            self.add_contact()
        elif choice == "2":
            self.edit_contact()
        elif choice == "3":
            clear()
            self.search_in_book()
        elif choice == "4":
            self.delete_contact()
        elif choice == "5":
            self.show_contact_book()
        elif choice == "6":
            print("\n\tSee you later!\n")
            exit()
        else:
            print("\n\tWrong input! Try again!\n")
        
        self.display_main_menu()


def main():
    my_contact_book = Book()
    clear()
    my_contact_book.display_main_menu()


if __name__ == "__main__":
    main()