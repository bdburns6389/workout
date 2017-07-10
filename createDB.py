import sqlite3
import random

conn = sqlite3.connect('exercises.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS exercises(legs TEXT, chest TEXT, back TEXT, abdominals TEXT, arms TEXT, misc TEXT)')

def data_entry():
    c.execute("INSERT INTO exercises VALUES('Squats', 'Bench Press', 'Dumbbell Row', 'Roman Chair', 'Barbell Curl', 'Calf Raises')")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    legs = str(input("Please input a leg exercise: "))
    chest = str(input("Please input a chest exercise: "))
    back = str(input("Please input a back exercise: "))
    abdominals = str(input("Please input an abdominal exercise: "))
    arms = str(input('Please input an arm exercise: '))
    misc = str(input("Please input a miscellaneous exercise: "))
    c.execute("INSERT INTO exercises (legs, chest, back, abdominals, arms, misc) VALUES (?, ?, ?, ?, ?, ?)", (legs, chest, back, abdominals, arms, misc))
    conn.commit()

dynamic_data_entry()



