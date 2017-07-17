import sqlite3
import random

conn = sqlite3.connect('exercises.db')
conn2 = sqlite3.connect('exercises_2.db')

c = conn.cursor()
c2 = conn2.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS exercises(legs TEXT, chest TEXT, back TEXT, abdominals TEXT, arms TEXT, '
              'misc TEXT)')
    c2.execute('CREATE TABLE IF NOT EXISTS exercises_2(legs TEXT, chest TEXT, back TEXT, abdominals TEXT, arms TEXT, '
               'misc TEXT)')
def data_entry():
    c.execute("INSERT INTO exercises VALUES('Squats', 'Bench Press', 'Dumbbell Row', 'Roman Chair', 'Barbell Curl', "
              "'Calf Raises')")
    c2.execute("INSERT INTO exercises_2 VALUES('Squats', 'Bench Press', 'Dumbbell Row', 'Roman Chair', 'Barbell "
               "Curl', 'Calf Raises')")

    conn.commit()
    conn2.commit()
    c.close()
    c2.close()
    conn.close()
    conn2.close()

def dynamic_data_entry():
    legs = str(input("Please input a leg exercise: "))
    chest = str(input("Please input a chest exercise: "))
    back = str(input("Please input a back exercise: "))
    abdominals = str(input("Please input an abdominal exercise: "))
    arms = str(input('Please input an arm exercise: '))
    misc = str(input("Please input a miscellaneous exercise: "))
    c.execute("INSERT INTO exercises_2 (legs, chest, back, abdominals, arms, misc) VALUES (?, ?, ?, ?, ?, ?)", (legs, chest, back, abdominals, arms, misc))
    conn.commit()


def update_database():
    pass
def random_select():
    pass
# c.execute('SELECT * FROM exercises_2) then data=(len(c.fetchall))  to find if data is more than 4 columns.
#Make if statement (if more than 4 columns, delete table to start over.)
def delete_database():
    c.execute('DELETE FROM exercises')
    conn.commit() 

#create_table()
#data_entry()
#delete_database()
#dynamic_data_entry()




