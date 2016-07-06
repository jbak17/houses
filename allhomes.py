import urllib2
import re
import string
from bs4 import BeautifulSoup

#give progam path to property
class Property(object):
    def __init__(self, path):
        #variables
        self.URL = path #string to URL
        self.price = [] #array of strings
        self.postcode = None #int
        self.address = None #string
        self.listingDate = None #date
        self.pageViews = None #int
        self.saleDate = None #date if current == False
        self.current = True
        self.utilities = Utilities()
        
        #initialise
        self.soup = self.utilities.makeSoup(path)
        self.price.append(self.setPrice(self.soup))
        self.postcode = self.getPostcode(self.soup)
        self.address = self.getAddress(self.soup)
        self.listingDate = self.getListingDate(self.soup)
            
    def setPrice(self, soup):
        price = soup.find_all('h2')  #gets all html h2 tags
        price = self.utilities.stripDigits(str(price[0]))    #selects first h2 tag and strips to price
        return price[1:-1]
    
    def getPostcode(self, soup):
        postcode = soup.find_all('span', {"itemprop": "postalCode"})
        return self.utilities.stripDigits(str(postcode[0]))
        
    def getAddress(self, soup):
        place = soup.find_all('title')
        address = str(place[0])
        index = address.index(',')
        street = address[7:(index)]
        return street
        
    def getListingDate(self, soup):
        date = soup.find_all('span', {"class": "boldFont"})
        for i in date:
            print str(i) + '\n'
        return date
        
        
    def getPageViews(self, soup):
        pass
        
    def __str__(self):
        return 'URL: {}\nPrice: {}\nPostcode: {}\nAddress: {}\nListing date: {}\n'.format(self.URL, self.price, self.postcode, self.address, self.listingDate)

    def __repr__(self):
        return 'Property({})'.format(self.URL)

class Utilities(object):
    '''
    Class to hold helper functions for program
    '''
    def __init(self):
        pass
        
    def makeSoup(self, path):
        '''
        Takes a URL path and returns an HTML soup
        '''
        response = urllib2.urlopen(path)
        html = response.read()
        soup = BeautifulSoup(html)
        return soup
    
    def stripDigits(self, inString):
        '''
        Takes a string with digits and returns only the digits
        Returns a string of digits
        '''
        trans = string.maketrans("","")
        nodigs = trans.translate(trans, string.digits)
        outString = inString.translate(trans, nodigs)
        return outString
        

#create property object

#add object to file
if __name__ == '__main()__':
    path = 'http://www.allhomes.com.au/ah/act/sale-residential/21-bettie-mcnee-street-watson-canberra/1317194347811'
    test_prop = Property(path)
    print test_prop

path = 'http://www.allhomes.com.au/ah/act/sale-residential/21-bettie-mcnee-street-watson-canberra/1317194347811'
test_prop = Property(path)
print test_prop
