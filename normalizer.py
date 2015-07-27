from bs4 import BeautifulSoup
import urllib
import re
import time

masterHash = {}
letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
letterArray = letters.split()

def scrapeSlangPage(letter):
	r = urllib.urlopen('http://www.noslang.com/dictionary/' + letter)
	soup = BeautifulSoup(r)
	terms = soup.find_all('dt')
	for i in terms:
		try:
			abbrString = str(i.find('abbr'))
			meaning = re.findall('"(.*?)"', abbrString)[0]
			slang = i.find('abbr').text
			masterHash[slang] = meaning
		except:
			print 'error' 

	print masterHash

for letter in letterArray:
	print letter
	time.sleep(2)
	scrapeSlangPage(letter)


outputFile = open('slang-dictionary.py', 'w')
outputFile.write(str(masterHash))