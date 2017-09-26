import sqlite3
#Fetchall from db2, put in list, see if exercise (variable) from
#first db is in list
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
    ran_select = c.fetchone()
    ran_select = ran_select[0]
    return (ran_select)

# def random_select2(exercise):
#     c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
#     data2 = c.fetchone()
#     data2 = data2[0]
#     return data2

def db2_length():
    '''Returns no exercises, fix then write function that determine if more than 4 exercises, delete if so.'''
    c2.execute('SELECT * FROM exercises_2')
    data = c2.fetchall()
    data = len(data)
    return data

def random_into_db2():
    #Add body groups as parameters to function, maybe convert to str()?
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
    #Works but needs changing to be functional.  Should make random function rerun if the same.
    """Put two parameters in compare, to correspond to one in random select and one in random select2"""
    exer1 = random_select(exercise1)
    exer2 = random_select2(exercise2)
    print (exer1)
    print (exer2)
    if exer1 == exer2:
        random_select(exercise1)

# def match_random_to_db2():
#     c.execute('SELECT (legs) FROM exercises')
#     data = c.fetchall()
#     return data


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

# def reset_db2():
#     #Doesn't need to be a function.
#     random_into_db2()
#     bad = db2_length()
#     if bad >= 4:
#         delete_db2()

# def populate_initialization():
#     #Doesn't need to be a function.
#     create_table()
#     data = db_length()
#     if data < 6:
#         populate_db()


def check_if_clash(exercise, exer1, exer2):
    if exer1 == exer2:
        while exer1 == exer2:
            exer1 = random_exercise(exercise)
    return (exer1,exer2)
    

#make work
def randExercise(ex):
  return random ''

  exercises = []

    for exerciseType in ['legs','chest','back']:
      tmp = randExercise(exerciseType)
      while(tmp in exercises):
        tmp = randExercise(exerciseType)
      exercises.append(tmp)
 

    





def main():
    create_table()
    create_table2()
    data = db_length()
    if data < 6:
        populate_db()
    data2 = db2_length()
    if data2 >= 4:
        delete_db2()
    legs_exer = random_exercise("legs")
    chest_exer = random_exercise("chest")
    back_exer = random_exercise("back")
    abdominals_exer = random_exercise("abdominals")
    arms_exer = random_exercise("arms")
    misc_exer = random_exercise("misc")
    #Makes sure exercises don't repeat
    legs_exer,back_exer = check_if_clash("legs", legs_exer, back_exer)
    arms_exer,back_exer = check_if_clash("arms", arms_exer, back_exer)
    chest_exer,back_exer = check_if_clash("chest", chest_exer, back_exer)
    back_exer,chest_exer = check_if_clash("back", back_exer, chest_exer)
    print (legs_exer,back_exer,chest_exer,abdominals_exer,arms_exer,misc_exer)
    
    #Pull exercise list from db2, make sure they don't match chosen exercise(use list and ask if exercise from db1 is in list of db2)
    
    
    
    
    #Put exercises into db2 using random_into_db2() function.

if __name__ == '__main__':
    main()
