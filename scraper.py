from bs4 import BeautifulSoup
from urllib2 import urlopen, URLError

BASE_URL = 'http://www.qmul.ac.uk/index.html'
pages = [BASE_URL]
impactoccurence = [];

"""This way, we can add comments"""
i = 0
impactCount = 4
random =4

""" check if url is valid (no email addresses, pdfs, etc.) """
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

""" convert url to standard format """
def cleanUrl(url):
    """ replace spaces with %20 """
	url_clean = url.replace(' ','%20')
    """ add /index.html where necessary """
    if (url[-1:0]=='/'):
        url_clean += 'index.html'
    elif (url[-5:0].find('.') == -1):
        url_clean += '/index.html'
    return url_clean

""" check if page loads """
def urlError(url):
	try:
		urlopen(url)
		return False
	except URLError as e:
		print('URLError ' + url)
		return True
	except:
		print('Something else went wrong')
		return True

""" assign url to a subdomain """
def urlDomain(url):
    """ check which subdomain the url belongs to """
    firstDot = url.find('.')
    secondDot = url.find('.', firstDot+1, len(url))
    qmul = url.find('qmul')
    if (url[firstDot+1:secondDot]=='qmul'):
        return 'root'
    elif:
        return url[firstDot+1:secondDot]

while (i < len(pages)) and (i <= 500): 
	print(pages[i])
	page = pages[i]
	i += 1
	if urlError(page): continue
	soup = BeautifulSoup(urlopen(page).read(), "lxml")
	text = soup.get_text()
	impactoccurence.append((page,text.count('impact')))
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
