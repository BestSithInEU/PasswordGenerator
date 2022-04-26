import string
import random
import pandas as pd
from cryptography.fernet import Fernet
from storage import load_key


class Password:
    def __init__(self):
        self.enc_list = None
        self.length = int
        self.characters = list(
            string.ascii_letters + string.digits + string.punctuation + ""
        )
        self.key_name = "key.key"
        self.key = load_key()

    def generate_password(self, length):
        self.length = length

        random.shuffle(self.characters)
        password = []

        for _ in range(length):
            password.append(random.choice(self.characters))

        random.shuffle(password)

        return "".join(password)

    def encrypt(self, website, username, password):
        website = str(website)
        password = str(password)
        username = str(username)
        fernet = Fernet(self.key)
        self.enc_list = [
            [
                fernet.encrypt(website.encode()).decode(),
                fernet.encrypt(username.encode()).decode(),
                fernet.encrypt(password.encode()).decode(),
            ]
        ]
        return self.enc_list

    def decrypt(self, position_x, position_y):
        header_dict = {0: "Website", 1: "Username/Email", 2: "Password"}
        df = pd.read_csv("password.csv")
        data = df[header_dict[position_x]][position_y]

        fernet = Fernet(self.key)
        raw_data = fernet.decrypt(data.encode())
        return raw_data.decode()
