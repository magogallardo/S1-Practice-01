import os
import sys
from getpass import getpass


class View(object):


	def show_principal_logged(self, username):
		os.system("clear")
		print "///////////////// Cinema //////////////////"
		print "//////////////Welcome, {}! ///////////\n\n".format(username)
		print "1.- View Movies"
		print "2.- View my tickets"


		print "9.- Log Out"
		print "0.- Exit"

	def show_principal_not_logged(self):
		os.system("clear")
		print "//////////////// Cinema //////////////////\n\n"
		print "Choose your option:"
		print "1.- View Movies"
		print "2.- Log In"
		print "3.- Sing up"
		print "0.- Exit"

	def show_sing_up(self, users, emails):
		
		username = ""
		password = ""
		name = ""
		last_name = ""
		email = ""

		users_list = []
		emails_list = []

		for i in users:
			users_list.append(i[0])
		for i in emails:
			emails_list.append(i[0])

		op = False
		while op == False:

			os.system("clear")
			username_input = raw_input("Type a Username: ")
			if username_input in users_list:
				raw_input("User already exists, choose another username.")
			else:
				username = username_input
				op = True

			
		password = getpass("Type a password: ")
		name = raw_input("Type your name: ")
		last_name = raw_input("Type your last name: ")

			
		op = False
		while op == False:
			email_input = raw_input("Enter your email: ")
			if email_input in emails_list:
				raw_input("Email already used. Please use another one")
			else:
				email = email_input
				op = True

		return username, password, name, last_name, email

	def show_successful_register(self, username):
		os.system("clear")
		print "Welcome, {}! You\'re already registered and ready to purchase.".format(username)
		raw_input("Press enter to continue...")

	def show_movies(self, movies):
		os.system("clear")


		print "////////////////////////////// Next ///////////////////////////////////\n\n"
		print "|| Id\t || Title \t || Duration \t || Day || Hour\t\t || Sala "
		

		for r in movies:
			print ("|| %s\t || %s\t || %s\t\t || %s || %s " % (r[0], r[1], r[2], r[3], r[4]))
			

		raw_input("\nPress enter to continue")

	def show_my_tickets(self, tickets):

		os.system("clear")

		print "//////////////////////////// My Tickets ////////////////////////////\n\n"
		print "|| Movie\t || Day / Hour\t\t || Sala || Seat number\t||"
		for r in tickets:
			print ("|| %s\t || %s\t || %s\t || %s\t\t ||" % (r[0], r[1], r[2], r[3]))

		raw_input("\nPress enter to continue")

	def ask_something(self, question):
		response = raw_input(question + " Y/N").upper()
		if response == "Y":
			return True
		else:
			return False

	def show_choose_schedule(self):
		 return raw_input("Choose a schedule (Id) you want to see: ")

	def show_schedule(self, sch):
		os.system("clear")

		print "////////////////////////////// Buy a ticket ///////////////////////////////////"
		print "////////////////////////You're about to tickets to {} ////////////////////".format(sch[0][1])
		return raw_input("\n\n\t\tHow many tickets do you want?: ")

	def show_buy_seats(self, required_seats_string, used_seats, number_of_seats):
		
		required_seats = int(required_seats_string)
		seats_numbers = []
		used_seats_list = []
		counter = 0
		counter2 = 0

		while counter < required_seats:
			

			os.system("clear")
			print "////////////////////// Select your seat number {} ////////////////////\n".format(counter2 + 1 )

			for i in used_seats:
				used_seats_list.append(i[0])

			for x in range((int(number_of_seats[0][0])/10)):

				sys.stdout.write(" ")
				
				for y in range(10):


					eval = str((x*10)+y+1)

					sys.stdout.write("[")
					if int(eval) in used_seats_list or eval in seats_numbers:
						sys.stdout.write("USED")
					else:
						sys.stdout.write(eval)

					sys.stdout.write("]")
					sys.stdout.write(" ")

				sys.stdout.write("\n")



			new_seat = raw_input("\nSelect the number of seat you want to buy: ")
			if int(new_seat) in used_seats_list or new_seat in seats_numbers:
				raw_input("Seat already in use, choose another one")
			else:
				seats_numbers.append(new_seat)
				counter= counter+1

			os.system("clear")
			print "\n"

			for x in range((int(number_of_seats[0][0])/10)):
				
				sys.stdout.write(" ")
				
				for y in range(10):


					eval = str((x*10)+y+1)

					sys.stdout.write("[")
					if eval in seats_numbers:
						sys.stdout.write("YOURS")
					else:
						sys.stdout.write(eval)

					sys.stdout.write("]")
					sys.stdout.write(" ")

				sys.stdout.write("\n")



		if self.ask_something("\n\nYou\'re about to buy these {} seats. Are you sure?".format(required_seats)):	
			return seats_numbers
		else:
			return False

	def show_successful_purchase(self):
		raw_input("Successful purchase! items added to your tickets")
		

	def show_login(self):
		os.system("clear")
		user = raw_input("User: ")
		password = getpass("Password: ")
		return user, password



# //////////////////////// ERROR VIEWS /////////////////////////////


	def show_invalid_password(self):
		print "\n"
		raw_input("Your password is invalid! Try Again")

	def show_user_not_registered(self):
		print "\n"
		raw_input("User not registered")
