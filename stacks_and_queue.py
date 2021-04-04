import sys
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
from collections import deque
import copy

start = 'https://en.wikipedia.org/wiki/Shrek_(character)' #Shrek
finish = 'https://en.wikipedia.org/wiki/Donald_Trump'  #Trump

def get_all_links(link):
    http = httplib2.Http()
    status, response = http.request(link)

    all_links = []
    for link in BeautifulSoup(response, features="html.parser", parse_only=SoupStrainer('a')):
        if link.has_attr('href'): #exctract only href links
            if '/wiki' in link['href']: #exctract only Wiki links
                if link['href'][0:5] == '/wiki':
                    link['href'] = '//en.wikipedia.org' + link['href']
                if link['href'][0:6] != 'https:':
                    link['href'] = 'https:' + link['href']
                if 'en.wikipedia' in link['href']:
                    all_links.append(link['href'])
    return all_links


stack = []
stack.append(start)
q = deque([])
q.append(stack)

while len(q) > 0:
    current_stack = q.popleft()
    current_link = current_stack[-1]
    all_links = get_all_links(current_link)
    all_links_copy = copy.copy(all_links) #in order not to skip links since we're deleting them from all_links

    for link in all_links_copy:
        if link == finish:
            current_stack.append(link)
            print(current_stack)
            print("you can reach your final destionation in " + str(len(current_stack) - 1) + " link(s)")
            sys.exit()
        new_stack = copy.copy(current_stack)
        new_stack.append(link)
        q.append(new_stack)
        #all_links.remove(link)
print("path not found")

