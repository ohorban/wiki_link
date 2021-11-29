from pyvis.network import Network
import networkx as nx

net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')
net.barnes_hut()
node1 = '1n'
net.add_node(node1)

node2 = '2n'
net.add_node(node2)
node3 = '3n'
net.add_node(node3)
node4 = '4n'
net.add_node(node4)

net.add_edge(node1, node2, color='red')
net.add_edge(node1, node2)
#net.add_edge(node2, node3)
#net.add_edge(node1, node2, color="red")


net.show_buttons(filter_=['physics'])
net.show('try.html')

#https://towardsdatascience.com/visualizing-networks-in-python-d70f4cbeb259

#https://pyvis.readthedocs.io/en/latest/tutorial.html