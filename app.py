import storage
from password_generator import Password
from utils import (
    get_length,
    print_infos,
    find_website,
    info_to_memo,
    delete_row,
    bool_find,
)
from os import path

message = "Please Enter to continue...\n"


def run_app():
    if not path.exists("key.key"):
        storage.write_key()
        print("This is your master password: " + str(storage.load_key().decode()))

    run = App()
    run.main_section()


class App:
    def __init__(self):
        self.my_storage = storage.Storage()
        self.my_password = Password()
        self.key = storage.load_key()
        self.key_str = str(storage.load_key().decode())
        self.csv_name = "password.csv"

    def main_section(self):
        if self.check_section():
            while True:
                argument = int(
                    input(
                        "Choose an option: \n"
                        + "1. Get & add password for website.\n"
                        + "2. Find password for website.\n"
                        + "3. Reset key.\n"
                        + "4. Print Database.\n"
                        + "5. Delete website's password.\n"
                        + "6. Exit.\n"
                    )
                )
                if argument == 1:
                    self.add_section()
                    input(message)
                elif argument == 2:
                    self.find_section()
                    input(message)
                elif argument == 3:
                    self.reset_section()
                    input(message)
                elif argument == 4:
                    self.print_section()
                    input(message)
                elif argument == 5:
                    website = input("What is the website? ")
                    find_website(website)
                    argument = input("Are you sure to delete this info (Enter Yes & No):\n").lower()
                    if argument == "yes":
                        self.delete_section(website)
                        input(message)
                    elif argument == "no":
                        input(message)
                    else:
                        print("Invalid argument")
                        input(message)
                elif argument == 6:
                    self.exit()
                    break

    def check_section(self):
        key = str(input("Write your master key:\n"))

        if key == self.key_str:
            return True
        elif key != self.key_str:
            print("Sorry you can not enter... Program will close.")
            return False

    def add_section(self):
        website = str(input("What is website's url?\n"))

        if get_length() != 0 and (website == find_website(website)[0]):
            print("You have already password for this website:")
            print(find_website(website))
            return False
        length = input("Please enter desired length of the password.\n")

        while True:
            password = self.my_password.generate_password(int(length))
            print(password)
            prompt = input("Did you like it or try again?\n")

            if prompt.lower() == "yes":
                username = input("What is username or email?\n")
                data = Password.encrypt(self.my_password, website, username, password)
                self.my_storage.save(data)
                break

    @staticmethod
    def find_section():
        print(find_website(input("What is the website:\n")))

    def reset_section(self):
        data = info_to_memo()
        length = len(data)

        for i in range(length):
            self.my_storage.rewrite(data[i])

        storage.reset_key()
        self.key = storage.load_key()
        print("New key: " + str(storage.load_key().decode()))

    def delete_section(self, website):
        if bool_find(website):
            new = delete_row(website)
            new.to_csv(self.csv_name, mode="w")
        else:
            print("There is no such a website " + website + "...")

    @staticmethod
    def print_section():
        for i in range(0, get_length()):
            print_infos(i)

    @staticmethod
    def exit():
        print("See you later...")
