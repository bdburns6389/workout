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


def random_select(exercise):
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    rand_select = c.fetchone()
    rand_select = rand_select[0]
    return rand_select


def db_length():
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


def check_if_clash(exercise, exer1, exer2):
    if exer1 == exer2:
        while exer1 == exer2:
            exer1 = random_exercise(exercise)
    return exer1, exer2

def db2_list(exercise_column):
    c2.execute('SELECT %s FROM exercises' % (exercise_column))
    data = c2.fetchall()
    new = []
    for i in data:
        a = (i[0])
        new.append(a)
    return new
    
        
def unique_exercises(*args):
    """Returns List of exercises from each body part that are unique from each other."""
    #Is using *args valid? (If not, use string for arguments, e.g. "legs")
    unique_exercises_list = []
    for exercise_type in [*args]:
        temp = random_exercise(exercise_type)
        while temp in unique_exercises_list:
            temp = random_exercise(exercise_type)
        unique_exercises_list.append(temp)
    return unique_exercises_list


def main():
    create_table()
    create_table2()
    data = db_length()
    if data < 6:
        populate_db()
    data2 = db2_length()
    if data2 >= 4:
        delete_db2()
    print(unique_exercises("legs","back","chest","abdominals","arms","misc"))

    #Pull exercise list from db2, make sure they don't match chosen exercise(use list and ask if exercise from db1 is in list of db2)
    #Possibly pull list from db2 to compare, then use unique_exercise function, to avoid more code.
    #Put exercises into db2 using random_into_db2() function.


if __name__ == '__main__':
     main()


    #if similar, rerun exercise.


#Now that I have a list, I need to compare unique_exercises list to the db2_list.