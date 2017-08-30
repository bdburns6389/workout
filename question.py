def db2_random_insert(exercise):
    #Not Working correctly
    """Returns exercise randomly, then puts it into second database."""
    data = random_exercise(exercise)
    c.execute("INSERT INTO exercises_2 (legs) VALUES %s" % (data)) 

def random_exercise(exercise):
    """Chooses random exercise using parameter."""
    c.execute('SELECT %s FROM exercises ORDER BY Random() LIMIT 1' % (exercise))
    data = c.fetchone()
    data = data[0]
    return (data)

db2_random_insert("legs")