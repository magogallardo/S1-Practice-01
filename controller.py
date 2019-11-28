

class Controller(object):


	def __init__(self, model, view):
		self.model = model
		self.view = view


	def login(self):
		self.view.show_login()

	def principal(self, username):
		self.view.show_principal_logged(username)
		self.username = username

	def principal_not_logged(self):
		self.view.show_principal_not_logged()

	def sing_up(self):
		users = self.model.get_users()
		emails = self.model.get_emails()

		username, password, name, last_name, email = self.view.show_sing_up(users, emails)
		self.model.register_user(username, password, name, last_name, email)

		self.view.show_successful_register(username)
		self.username = username
		return True

	def show_movies(self):

		movies = self.model.read_Movies()
		self.view.show_movies(movies)

	def show_my_tickets(self, username):
		tickets = self.model.read_my_tickets(username)
		self.view.show_my_tickets(tickets)

	def login(self):
		user, password = self.view.show_login()
		access = self.model.get_access(user, password)
		# If access is 1 is correct
		# If access is 2 password isn't correct
		# If access is 3 user doesn't exists
		return access, user

	def buy_a_ticket(self, username):
		
		if self.view.ask_something("Do you want to buy a ticket?"):
			schedule_id = self.view.show_choose_schedule()
			self.view_schedule(schedule_id)

	def view_schedule(self, sch_id):


		sch = self.model.read_schedule(sch_id)
		used_seats = self.model.get_used_seats(sch_id)

		required_tickets = self.view.show_schedule(sch)

		self.buy_seats(required_tickets, sch_id, used_seats)

	def buy_seats(self, required_tickets, sch_id, used_seats):


		seats_number_per_sala = self.model.get_sala_seats_number(sch_id)


		seats_to_buy = self.view.show_buy_seats(required_tickets, used_seats, seats_number_per_sala)
		
		if seats_to_buy != False:
			self.model.buy_seats(sch_id, seats_to_buy, self.username)
			self.view.show_successful_purchase()








	def error_handler(self, error_code):


#    1.- Invalid password
#
#
#
#
#
#

		if error_code == 1:
			self.view.show_invalid_password()
		if error_code == 2:
			self.view.show_user_not_registered()