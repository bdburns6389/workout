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
    c.execute("INSERT INTO exercises VALUES('Squats', 'Bench Press', 'Dumbbell Row', 'Roman Chair', 'Barbell Curl', "
              "'Calf Raises')")
    conn.commit()
    c.close()
    conn.close()

def random_select(exercise):
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data = c.fetchone()
    data = data[0]
    return (data)
    #conn.commit()

def random_select2(exercise):
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data2 = c.fetchone()  #fetchone can be used as well
    data2 = data2[0]
    return data2
    #conn.commit()

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
    data = c.fetchone()  #fetchone can be used as well
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









compare_random("legs", "legs")








'''bad = db_length()
if bad <= 1:
    delete_db()'''


