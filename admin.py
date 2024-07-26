import pandas as pd
import os
from users import dfToDict, RFID0Corrector

df = pd.read_csv('csv/admin.csv', encoding='latin1')
password_to_admin = dfToDict(df)


def reload_admin_csv():
    df = pd.read_csv('csv/admin.csv', encoding='latin1')
    password_to_admin = dfToDict(df)
    RFID0Corrector(password_to_admin)
