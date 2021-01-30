import leancloud
import json

class database:
	def __init__(self):
		leancloud.init("aAiiV2Rde8ou80vX6YMnCvAx-9Nh9j0Va", "DW9TsPU1DjBd6TLEKXJEAe6x")

	def current_user(self):
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
		user.logout()


	def get_champion_by_name(self, champion_name):
		query = leancloud.Query('Champion')
		query.equal_to('name', champion_name)
		return query.find()[0]


	def own_champion(self, champion_name):
		if self.current_user == None:
			return
		else:
			Ownership = leancloud.Object.extend('Ownership')
			new_ownership = Ownership()
			new_ownership.set('user', self.current_user())
			new_ownership.set('champion', self.get_champion_by_name(champion_name))
			new_ownership.save()


	def disown_champion(self, champion_name):
		champion_query = leancloud.Query('Champion')
		champion_query.equal_to('name', champion_name)
		ownership_query = leancloud.Query('Ownership')
		ownership_query.equal_to('user', self.current_user())
		ownership_query.matches_query('champion', champion_query)
		result = ownership_query.find()
		result[0].destroy()


	def get_owned_champion(self):
		query = leancloud.Query('Ownership')
		query.equal_to('user', self.current_user())
		result = query.find()
		champion_query = leancloud.Query('Champion')
		return [{
			'name': champion_query.get(entry.get('champion').id).get('name'),
			'thumbnail': champion_query.get(entry.get('champion').id).get('thumbnail').url
		} for entry in result]


	def get_unowned_champion(self):
		if self.current_user == None:
			return self.get_all_champion()
		else:
			ownership_query = leancloud.Query('Ownership')
			ownership_query.limit(154)
			champion_query = leancloud.Query('Champion')
			champion_query.limit(154)
			ownership_query.equal_to('user', self.current_user())
			owned_champion_names = [champion_query.get(entry.get('champion').id).get('name') for entry in ownership_query.find()]
			champion_query.not_contained_in('name', owned_champion_names)
			result = champion_query.find()
			return [{
				'name': entry.get('name'),
				'thumbnail': entry.get('thumbnail').url
			} for entry in result]


	def get_all_champion(self):
		champion_query = leancloud.Query('Champion')
		champion_query.limit(154)
		result = champion_query.find()
		return [{
			'name': entry.get('name'),
			'thumbnail': entry.get('thumbnail').url
		} for entry in result]


# db = database()
# db.get_champion_by_name('Fizz')
# db.login('positino','680822dd')
# print(db.get_owned_champion())
# print(len(db.get_all_champion()))


# try:
# 	db.login('eddy','123')
# except:
# 	print('Incorrect username or password!')
