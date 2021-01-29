# import random
# import string
import leancloud
# from os import walk

# class database:
	# def __init__(self):
	# 	self._user = [
	# 		{
	# 			'ID': '8ZZS9XQI0B',
	# 			'username':'positino',
	# 			'password':'680822dd'
	# 		},
	# 		{
	# 			'ID': 'BCPU6Y99NU',
	# 			'username':'proveigar',
	# 			'password':'qq562966969'
	# 		},
	# 		{
	# 			'ID': '9HKELFRM9A',
	# 			'username':'jiao1',
	# 			'password':'123123ss'
	# 		}
	# 	]

	# 	f = []
	# 	for (dirpath, dirnames, filenames) in walk('assets/'):
	# 		f.extend(filenames)
	# 		break

	# 	self.champions = [
	# 		{
	# 			'ID':''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
	# 			'name':filename[:-4],
	# 			'profile':'assets/' + filename
	# 		} for filename in f
	# 	]


	# 	self.ownership = [
	# 		{
	# 			'user_id': '8ZZS9XQI0B',
	# 			'champion_id': self.champions[137]['ID']	# vladimir
	# 		},
	# 		{
	# 			'user_id': '8ZZS9XQI0B',
	# 			'champion_id': self.champions[30]['ID']		# fizz
	# 		},
	# 		{
	# 			'user_id': '8ZZS9XQI0B',
	# 			'champion_id': self.champions[45]['ID']		# jayce
	# 		},
	# 		{
	# 			'user_id': 'BCPU6Y99NU',
	# 			'champion_id': self.champions[132]['ID']	# veigar
	# 		},
	# 		{
	# 			'user_id': 'BCPU6Y99NU',
	# 			'champion_id': self.champions[86]['ID']		# pantheon
	# 		},
	# 		{
	# 			'user_id': '9HKELFRM9A',
	# 			'champion_id': self.champions[68]['ID']		# lux
	# 		},
	# 	]


class database:
	def __init__(self):
		leancloud.init("aAiiV2Rde8ou80vX6YMnCvAx-9Nh9j0Va", "DW9TsPU1DjBd6TLEKXJEAe6x")


	def current_user(self):
		# return not leancloud.User().get_current() == None
		return leancloud.User().get_current()


	def register(self, username, password):
		new_user = leancloud.User()
		new_user.set_username(username)
		new_user.set_password(password)
		new_user.sign_up()


	def login(self, username, password):
		user = leancloud.User()
		user.login(username=username, password=password)


	def logout(self):
		pass


	def own_champion(self, champion_name):
		pass


	def delete_champion():
		pass


	def get_owned_champion(self):
		pass


	def get_all_champion(self):
		pass


# db = database()
# db.login('niubility','123')
# print(db.current_user())
# db.register('positino', '123')

# try:
# 	db.login('eddy','123')
# except:
# 	print('Incorrect username or password!')
