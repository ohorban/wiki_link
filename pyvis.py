import sys
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
from collections import deque
import copy

from pyvis.network import Network
import networkx as nx

start = 'https://en.wikipedia.org/wiki/Shrek_(character)' #Shrek
finish = 'https://en.wikipedia.org/wiki/Donald_Trump'  #Trump

graph = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')
graph.barnes_hut()
source_node = start

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

def get_title(link):
    return link[30:]

def show():
    graph.show_buttons(filter_=['physics'])
    graph.show('try.html')


stack = []
stack.append(start)
q = deque([])
q.append(stack)

while len(q) > 0:
    current_stack = q.popleft()
    current_link = current_stack[-1]
    all_links = get_all_links(current_link)
    graph.add_node(get_title(current_link), title=current_link)

    for link in all_links:
        graph.add_node(get_title(link), title=link)
        graph.add_edge(get_title(current_link), get_title(link))
        if link == finish:
            current_stack.append(link)
            print(current_stack)
            print("you can reach your final destionation in " + str(len(current_stack) - 1) + " link(s)")
            show()
            sys.exit()
        new_stack = copy.copy(current_stack)
        new_stack.append(link)
        q.append(new_stack)
print("path not found")