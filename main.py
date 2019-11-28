import mvc_exceptions as mvc_exc
from getpass import getpass
from model import Model
from view import View
from controller import Controller

	
def main():

	c = Controller(Model(0), View())

	


# ////////////// DEBUGGGG//////////////
	isLogged = False

	username = ""
	


	op = 10

	# Bucle para mostrar menu

	while op != 0:
		
		#Menu si esta registrado

		if isLogged:
			c.principal(username)

			
			op = input()

			if op == 1:
				c.show_movies()
				c.buy_a_ticket(username)

			if op == 2:
				c.show_my_tickets(username)


			if op == 9:
				isLogged = False

		else:

		#Menu si no esta registrado

			c.principal_not_logged()
			op = input()
			

			#Show movies

			if op == 1:
				c.show_movies()
			
			#Login

			if op == 2:

				# Login Attempt

				while isLogged == False:

					logged, username = c.login()
					if logged == 1:
						isLogged = True
					if logged == 2:
						c.error_handler(1)
					if logged == 3:
						c.error_handler(2)

			if op == 3:

				if c.sing_up():
					isLogged = True


	








if __name__ == '__main__':
	main()