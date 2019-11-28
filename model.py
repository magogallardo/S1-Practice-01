import MySQLdb
import mvc_exceptions as mvc_exc



class Model(object):

	def __init__(self, app_items):
		self.connection = MySQLdb.connect (host = "localhost", user =  "root", passwd = "123", db = "cinema")
		self.cursor = self.connection.cursor()

	def get_users(self):
		self.cursor.execute("SELECT username FROM User")
		return self.cursor.fetchall()

	def get_emails(self):
		self.cursor.execute("SELECT email FROM User")
		return self.cursor.fetchall()
	
	def read_Movies(self):
		self.cursor.execute("SELECT * from Movies")
		return self.cursor.fetchall()


	def read_schedule(self, sch_id):
		self.cursor.execute("SELECT * from Schedule_View WHERE schedule_id = \'{}\'".format(sch_id))
		return self.cursor.fetchall()

	def get_used_seats(self, sch_id):
		self.cursor.execute("SELECT tkt.seat_number from Schedule sch, Ticket tkt WHERE sch.schedule_id = tkt.schedule_id AND sch.schedule_id = \'{}\'".format(sch_id))
		return self.cursor.fetchall()		

	def get_sala_seats_number(self, sch_id):
		self.cursor.execute("SELECT sa.number_of_seats FROM Sala sa, Schedule sch WHERE sch.sala_id = sa.sala_id AND sch.schedule_id = \'{}\'".format(sch_id))
		return self.cursor.fetchall()


	def buy_seats(self, sch_id, used_seats, username):
		for x in used_seats:
			self.cursor.execute("INSERT INTO Ticket VALUES (%s, %s, %s, %s)", (0, username, sch_id, x))
			self.connection.commit()

	def read_my_tickets(self, username):
		self.cursor.execute("SELECT mv.title, sch.datentime, sa.sala_number, tkt.seat_number FROM Movie mv, Schedule sch, Sala sa, Ticket tkt WHERE mv.movie_id = sch.movie_id AND sch.sala_id = sa.sala_id AND tkt.schedule_id = sch.schedule_id AND tkt.username = \'{}\'".format(username))
		return self.cursor.fetchall()

	def register_user(self, username, password, name, last_name, email):
		self.cursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s, %s)", (username, password, name, last_name, email))
		self.connection.commit()



	def get_access(self, username, password):
	



		self.cursor.execute("SELECT * FROM User WHERE username = \'{}\'".format(username))
		results = self.cursor.fetchall()
		if(results):
			if results[0][1] == password:
				return 1
			else:
				#raise mvc_exc.InvalidPassword("Invalid Password!")
				return 2

		else:
			#raise mvc_exc.UserNotRegistered("User \"{}\" is not registered yet!".format(username))
			return 3