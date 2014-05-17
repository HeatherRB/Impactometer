from bs4 import BeautifulSoup
from urllib2 import urlopen, URLError

BASE_URL = 'http://www.qmul.ac.uk'
pages = [BASE_URL]
i = 0
impactCount = 0

def validUrl(url):
	if url is None:
		return False
	elif (url.find('@') >= 0):
		return False
	elif (url.find('qmul.ac.uk') >= 0):
		if (url.find('.html') >= 0) or (url[-1:0]=='/'):
			return True
	else:
		return False

def cleanUrl(url):
	return url.replace(' ','%20')

def urlError(url):
	try:
		urlopen(url)
		return False
	except URLError as e:
		print('URLError')
		return True
	except:
		print('Something else went wrong')
		return True

while (i < len(pages)) and (i <= 500): 
	print(pages[i])
	page = pages[i]
	i += 1
	if urlError(page): continue
	soup = BeautifulSoup(urlopen(page).read(), "lxml")
	text = soup.get_text()
	impactCount += text.count('impact')
	for link in soup.find_all('a'):
		url = link.get('href')
		for oldUrl in pages:
			if url == oldUrl:
				break
		else:
			if validUrl(url):
				pages = pages + [cleanUrl(url)]
print(impactCount)
