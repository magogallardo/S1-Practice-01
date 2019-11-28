import MySQLdb

connection = MySQLdb.connect (host = "localhost", user =  "root", passwd = "123", db = "cinema")
cursor = connection.cursor()

username = "emmanuelgallardomago"

cursor.execute("SELECT * FROM User WHERE username = \'{}\'".format(username))

results = cursor.fetchall()

print results[0][1]



cursor.execute("INSERT INTO Ticket VALUES (%s, %s, %s, %s)", (0, "emmanuelgallardomago", 1, 3))
connection.commit()

listtest = [1, 2, 3]
print listtest


