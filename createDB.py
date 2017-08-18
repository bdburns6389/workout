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

def populate_db():
    c.execute("INSERT INTO exercises VALUES('Squats', 'Barbell Bench Press', 'Dumbbell Row', 'Roman Chair', 'Barbell Curl', "
              "'Calf Raises (Squat Machine)')")
    c.execute("INSERT INTO exercises VALUES('Deadlift', 'Dumbbell Bench Press', 'Cable Row', 'Ab Roller', 'Chinups', "
              "'Calf Raises (Sit Down Machine)')")
    c.execute("INSERT INTO exercises VALUES('Romanian Deadlift', 'Barbell Incline Bench Press', 'Wide-Grip Pullups', 'Russian Twists', 'Dips', "
              "'Farmer Carry')")
    c.execute("INSERT INTO exercises VALUES('Hack Squats', 'Dumbbell Incline Bench Press', 'Bent Over Barbell Row', 'Cable Twists', 'Dumbbell Curls', "
              "'Wrist Curls')")
    c.execute("INSERT INTO exercises VALUES('Front Squats', 'Dips', 'Cable Pulldown', 'Toes-to-Bar', 'Tricep Cable Pushdown', "
              "'Zottman Curls')")
    c.execute("INSERT INTO exercises VALUES('Clean Pull', 'Cable Flyes', 'Dips', 'Windshield Wipers', 'Tricep Cable Extension', "
              "'Calf Raises (Leg Press Machine)')")
    
    conn.commit()

def random_select(exercise):
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data = c.fetchone()
    data = data[0]
    return (data)

def random_select2(exercise):
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data2 = c.fetchone()
    data2 = data2[0]
    return data2

def db2_length():
    '''Returns no exercises, fix then write function that determine if more than 4 exercises, delete if so.'''
    c2.execute('SELECT * FROM exercises_2')
    data = c2.fetchall()
    data = len(data)
    return data

def random_into_db2():
    legs = random_exercise("legs")
    chest = random_exercise("chest")
    back = random_exercise("back")
    abdominals = random_exercise("abdominals")
    arms = random_exercise("arms")
    misc = random_exercise("misc")
    c2.execute('INSERT INTO exercises_2 VALUES(?, ?, ?, ?, ?, ?);', (legs, chest, back, abdominals, arms, misc))
    conn2.commit()

def db_length():
    c.execute('SELECT * FROM exercises')
    data = c.fetchall()
    data = len(data)
    return data

def compare_random(exercise1, exercise2):
    #Works but needs changing to be functional.
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
    data = c.fetchone()
    data = data[0]
    return (data)

def delete_db():
    """Deletes entire exercises database"""
    c.execute('DELETE FROM exercises')
    conn.commit()
    
def delete_db2():
    """Deletes entire exercises_2 database"""
    c2.execute('DELETE FROM exercises_2')
    conn2.commit()

def reset_db2():
    #Doesn't need to be a function.
    random_into_db2()
    bad = db2_length()
    if bad >= 4:
        delete_db2()


def populate_initialization:
    #Doesn't need to be a function.
    create_table()
    data = db_length()
    if data < 6:
        populate_db()


