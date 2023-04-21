import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='chaurasiya',
    port='3306',
    database='pycharm_app',
)


# ..................................Insert Data..........................................................................


mycursor = mydb.cursor()
mysql = "INSERT INTO users(id, username, password) VALUES({}, '{}', '{}')".format(5, 'shiv', 'vihs')
mycursor.execute(mysql)
mydb.commit()
print(mysql)
print("user saved to db")


# ............................................Fetch data ...............................................................


mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM users');

users = mycursor.fetchall()

for user in users:
    # print(users)
    print('user_id', "=", user[0])
    print('username', "=", " "  + user[1])
    print('password', "=", " " + user[2])



# .......................................................Delete data.....................................................


mycursor = mydb.cursor()
mysql = "DELETE FROM users WHERE username = ('{}')".format('Nisha')
mycursor.execute(mysql)
mydb.commit()
print(mysql)
print("user Delete to db")




# .......................................................Update data.....................................................


mycursor = mydb.cursor()
mysql = "UPDATE users SET username='{}', password='{}' WHERE id={}".format('Actor', 'rotcA', 4)
mycursor.execute(mysql)
mydb.commit()
print(mysql)
print("user updated to db")



