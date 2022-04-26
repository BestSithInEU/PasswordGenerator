import os.path
from os import path

import pandas as pd
from cryptography.fernet import Fernet

key_name = "key.key"


def write_key():
    key = Fernet.generate_key()

    with open(key_name, "wb") as key_file:
        key_file.write(key)


def load_key():
    return open(key_name, "rb").read()


def reset_key():
    os.remove(key_name)
    write_key()


class Storage:
    def __init__(self):
        self.headers = ["Website", "Username/Email", "Password"]
        self.csv_name = "password.csv"
        self.key_name = "key.key"
        self.enc_list = []

        if not path.exists(self.key_name):
            write_key()

        self.key = load_key()

        if not path.exists(self.csv_name):
            df_obj = pd.DataFrame(columns=self.headers)
            df_obj.to_csv(self.csv_name, mode="w")

    def save(self, data):
        df = pd.DataFrame(data, columns=self.headers)
        df.to_csv(self.csv_name, mode="a", header=False)

    def rewrite(self, data):
        df = pd.DataFrame(data, columns=self.headers)
        df.to_csv(self.csv_name, mode="w")
