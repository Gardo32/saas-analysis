import pandas as pd
import os

def RFID0Corrector(dct):
    keys_to_update = list(dct.keys())
    for key in keys_to_update:
        new_key = key
        while len(new_key) < 10:
            new_key = '0' + new_key
        if new_key != key:
            dct[new_key] = dct.pop(key)

def dfToDict(df):
    return {str(row[1]): row[0] for _, row in df.iterrows()}


df = pd.read_csv('csv/Users.csv', encoding='latin1')

password_to_user = dfToDict(df)

def addUser(username, password):
    usersfile = 'csv/Users.csv'
    users_df = pd.read_csv(usersfile)
    newUser = pd.DataFrame({'username': [username], 'password': [password]})
    users_df = pd.concat([users_df, newUser], ignore_index=True)
    users_df.to_csv(usersfile, index=False)

def reload_users_csv():
    df = pd.read_csv('csv/Users.csv', encoding='latin1')
    password_to_user = dfToDict(df)
    RFID0Corrector(password_to_user)
    return password_to_user


