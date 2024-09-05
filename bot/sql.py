import sqlite3

con = sqlite3.connect("Baza.db")
sql = con.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS Users(ism TEXT, nomer TEXT)")
sql.execute("CREATE TABLE IF NOT EXISTS Shikoyatlar(id TEXT, location TEXT, tashkilot TEXT, shikoyat TEXT, holat TEXT)")
con.commit()


def user(ism, nomer):
    sql.execute(f"""INSERT INTO Users(ism, nomer) VALUES('{ism}', '{nomer}');""")
    con.commit()
    return "Ro'yhatdan o'tdingiz."

def shikoyatlar(id, location, tashkilot, shikoyat, holat):
    sql.execute(f"""INSERT INTO Shikoyatlar(id, location, tashkilot, shikoyat, holat) VALUES('{id}', '{location}', '{tashkilot}', '{shikoyat}', '{holat}');""")
    con.commit()
    return "trdyjgku"


def get_shikoyat(id):
    s = sql.execute(f"SELECT * FROM Shikoyatlar WHERE id = {id};")
    all = s.fetchall()
    return all

def get_one_shikoyat(tashkilot, id):
    d = sql.execute(f'SELECT * FROM Shikoyatlar WHERE id = {id}, tashkilot = {tashkilot}')
    s = d.fetchall()
    return s