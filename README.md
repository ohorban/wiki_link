# wiki_link
##### project in progress

## PyVis:
So far I implemented an algorithm that uses stacks and queues to find the shortest path from one link to another. 
![example1](pics/stacks_queues.png)
For example we can go from [Shrek](https://en.wikipedia.org/wiki/Shrek_(character)) to [Trump](https://en.wikipedia.org/wiki/Donald_Trump) in just two links:
```
['https://en.wikipedia.org/wiki/Shrek_(character)', 'https://en.wikipedia.org/wiki/Hollywood_Walk_of_Fame', 'https://en.wikipedia.org/wiki/Donald_Trump']
you can reach your final destionation in 2 link(s)
```
The interactive visual repersentation of the graph is output to `pyvis.html`
![graph](pics/pyvis.jpg)

[See graph here](https://ohorban.github.io/wiki_link/pyvis.html) (it will take some time to load)