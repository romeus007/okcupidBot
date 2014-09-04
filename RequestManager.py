import json
import urllib
import urllib2

class RequestManager:

	def __init__(self):
		pass

	def login(self, username, password):
		
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

		url = 'https://www.okcupid.com/login'

		values = {'username' : username,
		'password' : password,
		'okc_api' : '1' }
		headers = { 'User-Agent' : user_agent }

		data = urllib.urlencode(values)
		req = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(req)
		the_page = response.read()
		print the_page

		jsonValue = json.loads(the_page)

		userIdValue = jsonValue['userid']

		if userIdValue == 10:
			print 'userid is 10'
		else:
			print 'userid is ' + str(userIdValue)

			if userIdValue:
				print 'success'
			else:
				print 'error'







