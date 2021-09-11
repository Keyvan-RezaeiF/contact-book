class Book:

    def __init__(self):
        self.people = dict()


    def display_main_menu(self):
        print("\t*** My contact book ***")
        print("---------------------------------------")
        print("\t*** 1. Add contact")
        print("\t*** 2. Edit contact")
        print("\t*** 3. Search")
        print("\t*** 4. Sort")
        print("\t*** 5. Delete contact")
        print("\t*** 6. Exit")
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