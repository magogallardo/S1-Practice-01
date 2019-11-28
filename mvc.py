import basic_backend
import mvc_exceptions as mvc_exc
import os

class Model(object):

	def __init__(self, app_items):
		pass

class View(object):

	def show_login(isconnected):
		if isconnected == True:
			pass
		else:
			print "Welcome! sing in!"


	def show_principal(username = "emmanuelgallardomago", name = "Emmanuel"):
		os.system("clear")
		print "///////////////// Cinema //////////////////"
		print "//////////////Welcome, {}! ///////////".format(name)


class Controller(object):

	def __init__(self, model, view):
		self.model = model
		self.view = view


	def login(self):
		self.view.show_login()

	def principal(self):
		self.view.show_principal()
	


def main():

	c = Controller(Model(0), View())

	op = 0
	while op == 0:
		c.principal()
		op = input()







if __name__ == '__main__':
	main()