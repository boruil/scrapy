# # # import requests
# # # import mechanize
# # # from lxml import html
# # # import sys
# # # import urlparse
# # # import time

# # # def scrape_pic(link):

# # # 	response = requests.get(link)
# # # 	body = html.fromstring(response.txt)

# # # 	images = parsed_body.xpath('//img/@src')
# # # 	print 'Found %s images' % len(images)

# # # 	for url in images[0:len(images)]:
# # # 		r = requests.get(url)
# # # 		f = open('pics2/%s' % url.split('/')[-1], 'w')
# # # 		f.write(r.content)
# # # 		f.close()

# # # br = mechanize.Browser()
# # # br.set_handle_robots(False)
# # # # response = br.open("http://jandan.net/ooxx/page-1588")
# # # scrape_pic("http://jandan.net/ooxx/page-1588")

# # import urllib2
# # # opener = urlopen.FancyURLopener({})
# # url = "http://stackoverflow.com/"
# # f = urllib2.urlopen(url)
# # # f = opener.open(url)
# # content = f.read()
# # w = open('pic/file.html','w')
# # w.write(content)
# # w.close

# import urllib

# urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")

from BeautifulSoup import BeautifulSoup
import urllib2
import urllib

# use this image scraper from the location that 
#you want to save scraped images to

def make_soup(url):
	req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
	con = urllib2.urlopen( req )
	html = con.read()
	return BeautifulSoup(html)

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "images found.")
    print 'Downloading images to current working directory.'

    image_links = [each.get('src') for each in images]
    count = 0
    for each in image_links:
    	print url + each
        filename=each.split('/')[-1]
        urllib.urlretrieve(url + each, 'pic/' + filename)
        count = count+1
    return image_links

url = 'http://www.boruili.com/'
get_images(url)

