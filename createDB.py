import sqlite3
import random
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


def populate_db2():
    """Only for testing"""
    c2.execute("INSERT INTO exercises_2 VALUES('Squats', 'Barbell Bench Press', 'Dumbbell Row', 'Roman Chair', 'Barbell Curl', "
              "'Calf Raises (Squat Machine)')")
    c2.execute("INSERT INTO exercises_2 VALUES('Deadlift', 'Dumbbell Bench Press', 'Cable Row', 'Ab Roller', 'Chinups', "
              "'Calf Raises (Sit Down Machine)')")
    c2.execute("INSERT INTO exercises_2 VALUES('Romanian Deadlift', 'Barbell Incline Bench Press', 'Wide-Grip Pullups', 'Russian Twists', 'Dips', "
              "'Farmer Carry')")
    conn2.commit()


def db_length():
    """Returns number of rows in database."""
    c.execute('SELECT * FROM exercises')
    data = c.fetchall()
    data = len(data)
    return data


def db2_length():
    """Determines number of rows in second database."""
    c2.execute('SELECT * FROM exercises_2')
    data = c2.fetchall()
    data = len(data)
    return data


def random_exercise(exercise):
    """Chooses random exercise using parameter."""
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data = c.fetchone()
    data = data[0]
    return data


def delete_db():
    """Deletes entire exercises database"""
    c.execute('DELETE FROM exercises')
    conn.commit()


def delete_db2():
    """Deletes entire exercises_2 database"""
    c2.execute('DELETE FROM exercises_2')
    conn2.commit()


def db2_list(exercise_column):
    c2.execute('SELECT %s FROM exercises_2' % (exercise_column))
    data = c2.fetchall()
    new = []
    for i in data:
        a = (i[0])
        new.append(a)
    return new
    
        
def unique_exercises(*args):
    """Returns List of exercises from each body part that are unique from each other."""
    unique_exercises_list = []
    for exercise_type in [*args]:
        temp = random_exercise(exercise_type)
        while temp in unique_exercises_list:
            temp = random_exercise(exercise_type)
        unique_exercises_list.append(temp)
    return unique_exercises_list

def brian_unique_exercises(*args):
    unique_list = []
    for i in [*args]:
        temp = random_exercise(i)
        db2_column = db2_list(i)
        while temp in unique_list or temp in db2_column:
            temp = random_exercise(i)
        unique_list.append(temp)
    return unique_list
    


def compare_to_db2(db1_exercise, db2_exercise_list, exercise_type):
    """Compares exercises from unique_exercises to second database to eliminate repeats."""
    while db1_exercise in db2_exercise_list:
        db1_exercise = random_exercise(exercise_type)
    return (db1_exercise)
    

def add_to_db2(leg, back, chest, abdominals, arms, misc):
    """Adds final list of exercises to second database."""
    c2.execute("INSERT INTO exercises_2 (legs, back, chest, abdominals, arms, misc) VALUES (?, ?, ?, ?, ?, ?)", (leg, back, chest, abdominals, arms, misc))
    conn2.commit()


def main():
    create_table()
    create_table2()
    data = db_length()
    if data < 6:
        populate_db()
    data2 = db2_length()
    if data2 >= 4:
        delete_db2()
    db1_exercise_list = (brian_unique_exercises("legs","back","chest","abdominals","arms","misc"))
    print(db1_exercise_list)
    add_to_db2(db1_exercise_list[0], db1_exercise_list[1], db1_exercise_list[2], db1_exercise_list[3], db1_exercise_list[4], db1_exercise_list[5]) #Don't delete anything above this.
   

if __name__ == '__main__':
     main()
