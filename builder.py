from bs4 import BeautifulSoup, SoupStrainer
import httplib2

start = 'https://en.wikipedia.org/wiki/Ukraine'  # Ukraine
finish = 'https://en.wikipedia.org/wiki/Gay'     # Gay

http = httplib2.Http()
status, response = http.request(start)
all_links = []

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'): #exctract only href links
        if '/wiki' in link['href']: #exctract only Wiki links
            if link['href'][0:5] == '/wiki':
                link['href'] = '//en.wikipedia.org' + link['href']
            if link['href'][0:6] != 'https:':
                link['href'] = 'https:' + link['href']
            if 'en.wikipedia' in link['href']:
                all_links.append(link['href'])
                print(link['href'])
                

#print(all_links)
print("number of links:", len(all_links))
