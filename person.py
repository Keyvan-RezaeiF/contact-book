class Person():

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.numbers = list()

    
    def add_numbers(self):
        count = int(input("\n\tHow many numbers do you want to add ? "))
        while count > 0:
            self.numbers.append(input("\n\tEnter the number : "))
            count -= 1


    def get_first_name(self):
        return self.first_name

    
    def get_last_name(self):
        return self.last_name

    
    def get_email(self):
        return self.email


    def get_numbers(self):
        return self.numbers