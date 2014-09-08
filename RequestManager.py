import json   #exposes an API
import urllib   
import urllib2

class RequestManager:

	def __init__(self):
		pass                      #just a placeholder, why?

	def login(self, username, password):
		
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  #so that browser identifies itself as a version of Internet Explorer

		url = 'https://www.okcupid.com/login'

		values = {'username' : username,
		'password' : password,
		'okc_api' : '1' }
		headers = { 'User-Agent' : user_agent }

		data = urllib.urlencode(values)            # Data encoding, why did we encode with "urllib" and not "urllib2"
		req = urllib2.Request(url, data, headers)  # Python module for fetching URLs(represents HTTP request you're making)
		response = urllib2.urlopen(req)            # returns a response object for the URL requested
		the_page = response.read()                 # reads response object
		print the_page

		jsonValue = json.loads(the_page) #takes a JSON string and returns it as a Python data structure

		userIdValue = jsonValue['userid']

requestAPI = RequestManager()
requestAPI.login("romeus99","password348127")







