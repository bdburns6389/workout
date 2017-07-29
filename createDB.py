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


def random_select(exercise):
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data = c.fetchone()  #fetchone can be used as well
    data = data[0]
    return data
    #conn.commit()

def random_select2(exercise):
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data2 = c.fetchone()  #fetchone can be used as well
    data2 = data2[0]
    return data2
    #conn.commit()
#"""def delete_database():
#   c.execute('DELETE * FROM exercises_2')
#  conn.commit()""" """Not needed, but might be good to test stuff with."""
def db2_length():
    '''Returns no exercises, fix then write function that determine if more than 4 exercises, delete if so.'''
    c2.execute('SELECT * FROM exercises_2')
    data = c2.fetchall()
    data = len(data)
    print (data)

def db_length():
    c.execute('SELECT * FROM exercises')
    data = c.fetchall()
    data = len(data)
    print (data)

def db2_random_insert(exercise):
    #Not Working correctly
    """Returns exercise randomly, then puts it into second database."""
    data = random_exercise(exercise)
    c.execute("INSERT INTO exercises_2 (legs) VALUES %s" % (data)) 

def compare_random(exercise1, exercise2):
    """Put two parameters in compare, to correspond to one in random select and one in random select2"""
    data = random_select(exercise1)
    data2 = random_select2(exercise2)
    print (data)
    print (data2)
    if data == data2:
        print("same")
    else:
        print("different")

def random_exercise(exercise):
    """Chooses random exercise using parameter."""
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data = c.fetchone()  #fetchone can be used as well
    data = data[0]
    return (data)

def delete_db():
    c.execute('DELETE FROM exercises')
    conn.commit()
    
def delete_db2():
    c2.execute('DELETE FROM exercises_2')
    conn2.commit()

create_table()
#data_entry()
#dynamic_data_entry()
#random_select("arms")
#compare_random("legs","legs")
#db_length()
#db2_random_insert("legs")
delete_db2()
#c.close()
#conn.close()

