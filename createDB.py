import sqlite3

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


def random_select():
    c.execute('SELECT legs FROM exercises ORDER BY Random() LIMIT 1')
    data = c.fetchone()  #fetchone can be used as well
    data = data[0]
    return data
    #conn.commit()

def random_select2():
    c.execute('SELECT legs FROM exercises ORDER BY Random() LIMIT 1')
    data2 = c.fetchone()  #fetchone can be used as well
    data2 = data2[0]
    return data2
    #conn.commit()
# c.execute('SELECT * FROM exercises_2) then data=(len(c.fetchall))  to find if data is more than 4 columns.
#Make if statement (if more than 4 columns, delete table to start over.)
def delete_database():
    c.execute('DELETE FROM exercises')
    conn.commit() 


def compare_random():
    data = random_select()
    data2 = random_select2()
    print (data)
    print (data2)
    if data == data2:
        print("same")
    else:
        print("different")

def random_exercise(exer):
    """Chooses random exercise using parameter."""
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exer))
    data = c.fetchone()  #fetchone can be used as well
    data = data[0]
    print (data)

#create_table()
#dynamic_data_entry()
insert_exercise("chest")
c.close()
conn.close()

