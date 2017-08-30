import sqlite3

conn = sqlite3.connect('exercises.db')
conn2 = sqlite3.connect('exercises_2.db')

c = conn.cursor()
c2 = conn2.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS exercises(legs TEXT, chest TEXT, back TEXT, abdominals TEXT, arms TEXT, '
              'misc TEXT)')
    
def create_table2():
    c2.execute('CREATE TABLE IF NOT EXISTS exercises_2(legs TEXT, chest TEXT, back TEXT, abdominals TEXT, arms TEXT, '
               'misc TEXT)')

def random_select(exercise):
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data = c.fetchone()
    data = data[0]
    return (data)

def dynamic_data_entry():
    #Turn this into function that puts it in category selected by user.
    legs = str(input("Please input a leg exercise: "))
    chest = str(input("Please input a chest exercise: "))
    back = str(input("Please input a back exercise: "))
    abdominals = str(input("Please input an abdominal exercise: "))
    arms = str(input('Please input an arm exercise: '))
    misc = str(input("Please input a miscellaneous exercise: "))
    c.execute("INSERT INTO exercises_2 (legs, chest, back, abdominals, arms, misc) VALUES (?, ?, ?, ?, ?, ?)", (legs, chest, back, abdominals, arms, misc))
    conn.commit()