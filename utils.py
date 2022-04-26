import pandas as pd

from password_generator import Password
from storage import Storage


def add_password_to_csv(website, username, password):
    my_password_gen = Password()
    data = my_password_gen.encrypt(website, username, password)

    my_storage = Storage()
    my_storage.save(data)


def get_infos(position_x, position_y):
    my_password = Password()
    return my_password.decrypt(position_x, position_y)


def info_to_memo():
    info = []
    for i in range(0, get_length()):
        temp = [get_infos(0, i), get_infos(1, i), get_infos(2, i)]
        info.append(temp)
    return info


def print_infos(row):
    print(
        "| website: "
        + get_infos(0, row)
        + " | username: "
        + get_infos(1, row)
        + " | password: "
        + get_infos(2, row)
        + " | "
    )


def get_length():
    df = pd.read_csv("password.csv")
    return len(df)


def find_website(website, arg=True):
    info = info_to_memo()
    for i in range(get_length()):
        if arg:
            if str(info[i][0]) == str(website):
                return info[i]
            else:
                return "False"
        else:
            if str(info[i][0]) == str(website):
                return i


def delete_row(website):
    df = pd.read_csv("password.csv")
    index = find_website(website, arg=False)
    return df.drop([index])


def bool_find(website):
    info = info_to_memo()
    for i in range(get_length()):
        if str(info[i][0]) == str(website):
            return True
        else:
            return False
