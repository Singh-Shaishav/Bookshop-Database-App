import sqlite3

def connect():
    conn=sqlite3.connect("Database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS List (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISNB INTEGER)")
    conn.commit()
    conn.close

def insert(Title, Author, Year, ISNB):
    conn=sqlite3.connect("Database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO List VALUES (NULL,?,?,?,?)",(Title, Author, Year, ISNB))
    conn.commit()
    conn.close

def view():
    conn=sqlite3.connect("Database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM List ")
    row=cur.fetchall()
    conn.close
    return row

def Search(Title="", Author="", Year=""):
    conn=sqlite3.connect("Database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM List WHERE Title=? OR Author=? OR Year=?",(Title, Author, Year))
    row=cur.fetchall()
    conn.close  
    return row

def Delete(id):
    conn=sqlite3.connect("Database.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM List WHERE ID=?", (id,) )
    conn.commit()
    conn.close

def update(id,Title,Author,Year,ISNB):
    conn=sqlite3.connect("Database.db")
    cur=conn.cursor()
    cur.execute("UPDATE List SET Title=? , Author=?, Year=?, ISNB=? WHERE id=?",(Title,Author,Year,ISNB,id))
    conn.commit()
    conn.close

