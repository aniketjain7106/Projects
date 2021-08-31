import mysql.connector as connector
db= connector.connect(
  host="localhost",
  user="root",
  password="password",
  port='3306',
  database='splitwise'
)
cur=db.cursor()
s1="update aniket set aniket=0"
cur.execute(s1)
db.commit()
s1="update aniket set aish=0"
cur.execute(s1)
db.commit()
s1="update aniket set adi=0"
cur.execute(s1)
db.commit()
s1="update aniket set sinha=0"
cur.execute(s1)
db.commit()