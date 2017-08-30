from createDB import *
import sqlite3

conn = sqlite3.connect('exercises.db')
conn2 = sqlite3.connect('exercises_2.db')

c = conn.cursor()
c2 = conn2.cursor()

legs_exercise = random_select('legs')
chest_exercise = random_select('chest')
back_exercise = random_select('back')
abdominals_exercise = random_select('abdominals')
misc_exercise = random_select('misc')
arms_exercise = random_select('arms')

print (legs_exercise,chest_exercise,back_exercise,abdominals_exercise,misc_exercise,arms_exercise)


